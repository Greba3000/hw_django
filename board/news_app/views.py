from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView

from news_app.models import News
from news_app.forms import NewsForm


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(View):

    def get(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        latest_comments = news.comment.all()[0:5]
        return render(request, 'news_app/news_detail.html', context={'news': news, 'comments': latest_comments})


# class AddNews(CreateView):
#     model = News
#     create_form = NewsForm
class AddNews(View):

    def get(self, request):
        add_news = NewsForm()
        return render(request, 'news_app/add_news.html', context={'add_news': add_news})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news')  # если все ОК перекинет нас на начальную страницу
        return render(request, 'news_app/add_news.html', context={'add_news': news_form})


# class UpdNews(UpdateView):
#     template_name = 'news_app/upd_news.html'
class UpdNews(View):
    def get(self, request, profile_id):  # profile_id менять нельзя
        news = News.objects.get(id=profile_id)
        news_form = NewsForm(instance=news)  # работает только если NewsForm отнаследован от ModelForm
        return render(request, 'news_app/upd_news.html', context={'news_form': news_form, 'news_id': profile_id})

    def post(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return HttpResponseRedirect(f'/news/{profile_id}')
        return render(request, 'news_app/upd_news.html', context={'news_form': news_form, 'news_id': profile_id})


class LeaveComment(View):

    def post(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        news.comment.create(author=request.POST['author'], text=request.POST['text'])  # news.comment.all()
        return HttpResponseRedirect(f'/news/{profile_id}')
