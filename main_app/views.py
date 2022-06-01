from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect
from .models import Dancer, Choreo

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class DancerList(TemplateView):
    template_name = "dancer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["dancers"] = Dancer.objects.filter(name=name)
            context["header"] = f"Searching for {name}"
        else:
            context["dancers"] = Dancer.objects.all()
            context["header"] = "Dancers"
        return context

class DancerDetail(DetailView):
    model = Dancer
    template_name = "dancer_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["playlists"] = Playlist.objects.all()
    #     return context

class DancerCreate(CreateView):
    model = Dancer
    fields = ['name', 'img', 'bio']
    template_name = "dancer_create.html"
    # success_url = "/dancers/"
    def get_success_url(self):
        return reverse('dancer_detail', kwargs={'pk': self.object.pk})

class DancerUpdate(UpdateView):
    model = Dancer
    fields = ['name', 'img', 'bio']
    template_name = "dancer_update.html"
    # success_url = "/dancers/"
    def get_success_url(self):
        return reverse('dancer_detail', kwargs={'pk': self.object.pk})

class DancerDelete(DeleteView):
    model = Dancer
    template_name = "dancer_delete.html"
    success_url = "/dancers/"

class ChoreoCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        vid = request.POST.get("vid")
        embed = request.POST.get("embed")
        dancer = Dancer.objects.get(pk=pk)
        Choreo.objects.create(title=title, vid=vid, embed=embed, dancer=dancer)
        return redirect('dancer_detail', pk=pk)