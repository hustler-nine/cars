from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView
from .forms import  UserCreateForm, ProfileUpdateForm
from driveclub.models import ProfileUser


# Create your views here.


def redirect_to_user(request):
    url = '/accounts/profile/' + str(request.user.user.id) + '/'
    return HttpResponseRedirect(redirect_to=url)


class UserProfile(DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = '/accounts/login/'


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        extra_form = ProfileUpdateForm(request.POST)
        url = '/accounts/login/'
        if (form.is_valid()) and (extra_form.is_valid()):
            # create a new user first
            new_user = form.save()
            # create an object in memory but not save it
            new_extended_obj = extra_form.save(commit=False)
            # assign the user to the extended obj
            new_extended_obj.user = new_user
            # write to database
            new_extended_obj.save()
        return HttpResponseRedirect(redirect_to=url)

    else:
        form = UserCreateForm()
        extra_form = ProfileUpdateForm()
        context = {
            'form': form,
            'extra_form': extra_form,
        }
        return render(request, 'register.html', context)


