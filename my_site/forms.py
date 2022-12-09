from django import forms

class ContactForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, verbose_name="На что")
    content = forms.FloatField(label='content', verbose_name="Сколько")