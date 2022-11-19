from django import forms

class ContactForm(forms.Form):
    title = forms.CharField(max_length=100, verbose_name="На что")
    content = forms.FloatField(verbose_name="Сколько")