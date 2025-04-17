from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Plant
from .forms import PlantForm


def home(request):
    return render(request, "home.html")


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, "plants/detail.html", {"plant": plant})

class PlantCreate(CreateView):
    model = Plant
    form_class = PlantForm
    success_url = reverse_lazy('index')
    template_name = 'plants/plant_form.html'

class PlantUpdate(UpdateView):
    model = Plant
    form_class = PlantForm
    success_url = reverse_lazy('index')
    template_name = 'plants/plant_form.html'

class PlantDelete(DeleteView):
    model = Plant
    success_url = reverse_lazy('index')
    template_name = 'plants/plant_confirm_delete.html'