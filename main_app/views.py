from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Dancer

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
            context["dancers"] = Dancer.objects.filter(name_icontains=name)
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