from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from driveclub.models import ProfileUser


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('id', 'username',)


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = ProfileUser
        fields = ('age',)





