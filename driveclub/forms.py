from django import forms
from .models import Vehicle
from django.core.validators import RegexValidator


class VehicleForm(forms.ModelForm):

    name = forms.CharField(required=True, validators=[RegexValidator(
        r'^[A-Z]+', message='Name must start with a capital letter, sorry!'
    )], widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    speed = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }))
    weight = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }))
    image = forms.ImageField(required=True)
    video = forms.FileField(required=True)
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'speed', 'weight', 'image', 'video', 'description')


class VehicleFormA(forms.ModelForm):

    name = forms.CharField(required=True, validators=[RegexValidator(
        r'^[A-Z]+', message='Name must start with a capital letter, sorry!'
    )], widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    speed = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }))
    weight = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }))
    image = forms.ImageField(required=True)
    video = forms.FileField(required=True)

    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'speed', 'weight', 'image', 'video')







