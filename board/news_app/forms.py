from django import forms
from news_app.models import News


# class NewsForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     # created_at = forms.DateTimeField() само заполняется
#     # updated_at = forms.DateTimeField()

class NewsForm(forms.ModelForm):  # вариант

    class Meta:
        model = News
        fields = ['title', 'description']  # '__all__'
