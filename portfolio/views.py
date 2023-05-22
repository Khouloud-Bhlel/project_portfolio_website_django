from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from portfolio.models import Contact, Projet, Service, Personnel,Equipe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProjetForm, AjouterPersonnelForm, ServiceForm,EquipeForm
from django.db.models import Q
from django.db.models import Count, Q

from django.shortcuts import render
from django.db.models import Count
#home-----------------------------------------------------------------------------
def home(request):
    return render(request, 'home.html')

#about--------------------------------------------------------------------------------
def about(request):
    projets = Projet.objects.all()
    return render(request, 'portfolioo.html', {'projets': projets})

#contact--------------------------------------------------------------------------------
from django.core.mail import send_mail
def contact(request):
    template_name = 'contact.html'

    name = request.POST.get("name", "")
    from_email = request.POST.get("email", "")
    message = request.POST.get("message", "")
    
    if name and message and from_email:
       
        send_mail(
                name, 
                message, 
                from_email, 
                ["khouloudbenhelal24@gmail.com"],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us!')

    # Redirection vers la même page avec un ancrage
        return redirect(request.META.get('HTTP_REFERER', '/') + '#footer')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return render(request, 'contact.html')


from django.shortcuts import render
from .models import Projet,Equipe

# equipe ------------------------------------------------
def equipe(request):
    if not request.user.is_authenticated:
            messages.warning(request, "Please login to access this page")
            return redirect("/auth/login/")
    posts = Equipe.objects.all()
    context = {"posts": posts}
    return render(request, 'equipe.html', context)
class CreerEquipeView(CreateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'ajouter_equipe.html'
    success_url = reverse_lazy('equipe')
    
class ModifierEquipeView(UpdateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'modifier_equipe.html'
    success_url = reverse_lazy('equipe')


class SupprimerEquipeView(DeleteView):
    def __init__(self):
        self.model = Equipe
        self.template_name = 'supprimer_equipe.html'
        self.success_url = reverse_lazy('equipe')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Equipe, id=id)
  

#index-----------------------------------------------------
def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Projet
from .forms import ProjetForm

def project(request):
    projects = Projet.objects.all()
    context = {"projects": projects}
    return render(request, 'project.html', context)

def creer_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.progression = 0
            projet.save()
            return redirect('project')
    else:
        form = ProjetForm()

    context = {'form': form}
    return render(request, 'creer_projet.html', context)


def modifier_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)

    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            projet = form.save(commit=False)
            progression = int(request.POST.get('progression', 0))
            projet.progression = progression
            projet.save()
            return redirect('project')
    else:
        form = ProjetForm(instance=projet)

    return render(request, 'modifier_projet.html', {'form': form, 'object': projet})

def supprimer_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    projet.delete()
    return redirect('project')


# service :------------------------------------------------
def handleblog(request):
    if not request.user.is_authenticated:
            messages.warning(request, "Please login to access this page")
            return redirect("/auth/login/")
    posts=Service.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def creer_service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/service')
    context = {'form': form}
    return render(request, 'creer_service.html', context)

def modifier_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('/service')
    context = {'form': form}
    return render(request, 'modifier_service.html', context)

def supprimer_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('/service')
    context = {'service': service}
    return render(request, 'supprimer_service.html', context)

# view personnel : ------------------------------------------------------
def personnel(request):
    personnels = Personnel.objects.all()
    context = {"personnels": personnels}
    return render(request, 'personnel.html', context)

class AjouterPersonnelView(CreateView):
    model = Personnel
    form_class = AjouterPersonnelForm
    template_name = 'ajouter_personnel.html'
    success_url = reverse_lazy('personnel')

class SupprimerPersonnelView(DeleteView):
    model = Personnel
    template_name = 'supprimer_personnel.html'
    success_url = reverse_lazy('personnel')

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Personnel, id=id)
