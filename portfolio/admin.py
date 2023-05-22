from django.contrib import admin
from .models import Contact, Projet, Service, Personnel,Equipe

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'emailv', 'description')
    search_fields = ('name', 'email','emailv')
    list_filter = ('name', 'email','emailv')

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('libellee', 'descriptionn', 'date_debut', 'date_fin', 'acheve')
    search_fields = ('libelle',)
    list_filter = ('acheve',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('type','title', 'description')
    search_fields = ('type',)
    list_filter = ('type',)

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fichier_cv', 'fichier_photo', 'lien_linkedin')
    search_fields = ('nom',)
    list_filter = ('nom',)

class EquipeAdmin(admin.ModelAdmin):
    list_display = ('Nom',)
    search_fields = ('Nom',)
    list_filter = ('Nom',)
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Equipe, EquipeAdmin)