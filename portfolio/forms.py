from django import forms
from .models import Projet, Service, Personnel,Equipe
    


from django import forms
from .models import Projet

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['libellee', 'descriptionn', 'date_debut', 'date_fin', 'acheve', 'progression']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'libellee': 'Libellé',
            'descriptionn': 'Description',
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin',
            'acheve': 'Terminé',
            'progression': 'Progression',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class AjouterPersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'fichier_cv': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'fichier_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'lien_linkedin': forms.URLInput(attrs={'class': 'form-control'}),
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = "__all__"  
