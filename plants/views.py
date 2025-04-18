from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Plant
from .forms import PlantForm
from .forms import CareLogForm


def home(request):
    return render(request, "home.html")


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    care_form = CareLogForm()

    if request.method == "POST":
        care_form = CareLogForm(request.POST)
        if care_form.is_valid():
            new_log = care_form.save(commit=False)
            new_log.plant = plant
            new_log.save()
            return redirect("detail", plant_id=plant.id)

    return render(
        request, "plants/detail.html", {"plant": plant, "care_form": care_form}
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class PlantCreate(CreateView):
    model = Plant
    form_class = PlantForm
    success_url = reverse_lazy("index")
    template_name = "plants/plant_form.html"


class PlantUpdate(UpdateView):
    model = Plant
    form_class = PlantForm
    success_url = reverse_lazy("index")
    template_name = "plants/plant_form.html"


class PlantDelete(DeleteView):
    model = Plant
    success_url = reverse_lazy("index")
    template_name = "plants/plant_confirm_delete.html"
