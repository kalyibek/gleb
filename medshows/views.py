import os

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from . import models
from django.conf import settings


def redirect(request):
    return HttpResponseRedirect(reverse('medshow'))


class MedShowListView(generic.ListView):
    template_name = 'medshows.html'
    queryset = models.MedicalShows.objects.all()


class MedShowsDetailView(generic.DetailView):
    template_name = 'medshow_detail.html'
    queryset = models.MedicalShows.objects.all()

    def get_object(self, **kwargs):
        medshows_id = self.kwargs.get('id')
        return get_object_or_404(models.MedicalShows, id=medshows_id)


def create_medshow(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        images = request.FILES['images']
        medshow_type = request.POST['type']
        timeadd = request.POST['timeadd']

        new_medshow = models.MedicalShows.objects.create(
            title=title,
            description=description,
            images=images,
            type=medshow_type,
            timeadd=timeadd
        )
        new_medshow.save()
        return redirect('medshow')

    medshow_types = models.Type.objects.all()
    context = {
        'medshow_types': medshow_types
    }
    return render(request, 'medshow_create.html', context)


def update_medshow(request, id):
    medshow = get_object_or_404(models.MedicalShows, id=id)
    medshow_types = models.Type.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        images = request.FILES['images']
        medshow_type = request.POST['type']
        timeadd = request.POST['timeadd']

        medshow.title = title
        medshow.description = description
        medshow.images = images
        medshow.type = medshow_type
        medshow.timeadd = timeadd
        medshow.save()
        return redirect('medshow')

    context = {
        'medshow': medshow,
        'medshow_types': medshow_types,
    }
    return render(request, 'medshow_update.html', context)


def delete_medshow(request, id):
    medshow = get_object_or_404(models.MedicalShows, id=id)
    medshow.delete()
    return redirect('medshow')
