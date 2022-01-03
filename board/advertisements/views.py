from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


class MainPage(TemplateView):
    template_name = 'advertisements/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = [
            'Куплю',
            'Продам',
            'Услуги',
        ]
        context['regions'] = [
            'Москва',
            'Московская область',
            'Республика Алтай',
            'Вологодская область',
        ]
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['name'] = 'Бесплатные объявления'
        context['description'] = 'Бесплатные объявления в вашем городе!'
        return context


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['address'] = 'г. Минск, ул. Петрова 15-15'
        context['tel'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'
        return context


class Advertisements(View):
    advertisements = [
        'куплю кота',
        'продам слона',
        'утюжу',
        'глажу',
        'муж на час',
        'на два',
        'на три',
    ]
    title = 'Объявления'
    request_counter = 0

    def get(self, request):
        return render(request, 'advertisements/advertisements.html',
                      {'title': Advertisements.title, 'advertisements': Advertisements.advertisements})

    def post(self, request):
        Advertisements.request_counter += 1
        message = 'Запрос на создание новой записи успешно выполнен.'
        return render(request, 'advertisements/advertisements.html',
                      {'request_counter': Advertisements.request_counter, 'message': message})
