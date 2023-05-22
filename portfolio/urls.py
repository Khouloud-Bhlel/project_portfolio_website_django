from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('project', views.project, name='project'),
    path('project/creer', views.creer_projet, name='creer_projet'),
    path('project/modifier/<int:pk>', views.modifier_projet, name='modifier_projet'),
    path('project/supprimer/<int:pk>', views.supprimer_projet, name='supprimer_projet'),
    path('service', views.handleblog, name='handleblog'),
    path('service/creer', views.creer_service, name='creer_service'),
    path('service/modifier/<int:pk>', views.modifier_service, name='modifier_service'),
    path('service/supprimer/<int:pk>', views.supprimer_service, name='supprimer_service'),
    path('personnel', views.personnel, name='personnel'),
    path('personnel/ajouter', views.AjouterPersonnelView.as_view(), name='ajouter_personnel'),
    path('personnel/supprimer/<int:pk>', views.SupprimerPersonnelView.as_view(), name='supprimer_personnel'),
    path('equipe', views.equipe, name='equipe'),
    path('ajouter_equipe', views.CreerEquipeView.as_view(), name='ajouter_equipe'),
    path('equipe/modifier_equipe/<int:pk>/', views.ModifierEquipeView.as_view(), name='modifier_equipe'),
    path('supprimer_equipe/<int:id>', views.SupprimerEquipeView.as_view(), name='supprimer_equipe'),
]
