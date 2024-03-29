from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect
from .models import Dancer, Choreo, Team, Playlist
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.filter(user=self.request.user)
        return context

class About(TemplateView):
    template_name = "about.html"

class DancerList(TemplateView):
    template_name = "dancer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            # context["dancers"] = Dancer.objects.filter(name=name, user=self.request.user)
            context["dancers"] = Dancer.objects.filter(name=name)
            context["header"] = f"Searching for {name}"
        else:
            # context["dancers"] = Dancer.objects.filter(user=self.request.user)
            context["dancers"] = Dancer.objects.all()
            context["header"] = "Dancers"
        return context

class DancerDetail(DetailView):
    model = Dancer
    template_name = "dancer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context

class DancerCreate(CreateView):
    model = Dancer
    fields = ['name', 'img', 'bio']
    template_name = "dancer_create.html"
    # success_url = "/dancers/"
    def get_success_url(self):
        return reverse('dancer_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DancerCreate, self).form_valid(form)

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

class PlaylistChoreoAssoc(View):

    def get(self, request, pk, choreo_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given choreo_id
            Playlist.objects.get(pk=pk).choreos.remove(choreo_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given choreo_id
            Playlist.objects.get(pk=pk).choreos.add(choreo_pk)
        return redirect('home')


class TeamsList(TemplateView):
    template_name = "teams_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")

        if title != None:
            context["teams"] = Team.objects.filter(title=title)
            context["header"] = f"Searching for {title}"
        else:
            context["teams"] = Team.objects.all()
            context["header"] = "Teams"
        return context

class TeamDetail(DetailView):
    model = Team
    template_name = "team_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
