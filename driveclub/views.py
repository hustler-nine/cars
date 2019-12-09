from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Vehicle, ProfileUser
from django.core.serializers import serialize
from .forms import VehicleForm, VehicleFormA
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.


def serialized_data(data):
    try:
        return serialize('json', data)
    except:
        return serialize('json', [data])


def intropage(request):
    return render(request, 'intro.html')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


# forbids the url
def has_user_access_to_modify(current_user, current_object):
    profile_user = ProfileUser.objects.all().filter(user__pk=current_user.id)[0]

    if current_object.user == profile_user or current_user.is_superuser:
        return True
    return False


def admin_access_only(current_user):
    if current_user.is_superuser:
        return True
    return False


def create_vehicle(request):
    if request.method == 'GET':
        form = VehicleForm()
        context = {'form': form}
        return render(request, 'vehicle_create.html', context)

    elif request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('created')
        else:
            return HttpResponse('not created')


class VehicleCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'vehicle_create.html'
    form_class = VehicleForm
    success_url = '/driveclub/homepage/vehicles/'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return VehicleForm
        else:
            return VehicleFormA

    # Attach content to the current user
    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = 'vehicle_create.html'
    form_class = VehicleForm
    success_url = '/driveclub/homepage/vehicles/'

    def get(self, request, pk):
        if has_user_access_to_modify(self.request.user, self.get_object()):
            instance = Vehicle.objects.get(pk=pk)
            if self.request.user.is_superuser:
                form = VehicleForm(request.POST or None, instance=instance)
                return render(request, 'vehicle_create.html', {'form': form})
            else:
                form = VehicleFormA(request.POST or None, instance=instance)
                return render(request, 'vehicle_create.html', {'form': form})
        return render(request, 'permission_denied.html')


class VehicleDelete(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = '/driveclub/homepage/vehicles/'

    # allows the user to delete only his content
    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request, 'vehicle_delete.html', {'vehicles': self.get_object()})
        return render(request, 'permission_denied.html')


class VehicleList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'


class VehicleDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicles'


class UserVehicles(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

    # Get all vehicles tied to the user
    def get_queryset(self):
        owner_id = self.request.user.id
        try:
            owner = ProfileUser.objects.all().filter(user__pk=owner_id)[0]
            vehicles = Vehicle.objects.all().filter(user=owner.pk)
            return vehicles
        except:
            return []


class GetAllUsers(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'get_all_users.html'

    def get_queryset(self,):
        if admin_access_only(self.request.user):
            users = User.objects.all()
            return users[1:]
        return f'nope'


class UserVehicles2(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

    # Admin gets all vehicles tied to the user
    def get_queryset(self):
        try:
            vehicles = Vehicle.objects.filter(user=self.kwargs['pk'])
            return vehicles
        except:
            return []








