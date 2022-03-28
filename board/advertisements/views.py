from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from advertisements.models import Advertisement
from django.http import HttpResponse


def advertisement_list():
    advert_list = Advertisement.objects.all()
    return advert_list


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
        context['description'] = '''
        Бесплатные объявления в вашем городе!0
        
        Бесплатные объявления в вашем городе!1
        Бесплатные объявления в вашем городе!2
        Бесплатные объявления в вашем городе!3
        '''
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


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisements_list'


class AdvertisementDetailView(DetailView):
    model = Advertisement
