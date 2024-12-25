from cars.models import Car
from cars.forms import NewCarForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars

def is_superuser(user):
    return user.is_superuser

@method_decorator(user_passes_test(is_superuser), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = NewCarForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'details.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = NewCarForm
    template_name = 'car_update.html'
    success_url = '/cars/'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'