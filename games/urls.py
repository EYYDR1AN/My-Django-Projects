from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blimp-jump/', views.blimp_jump, name='blimp_jump'),
    path('automation-attack/', views.automation_attack, name='automation_attack'),
    path('whack-a-mole/', views.whack_mole, name='whack_mole'),
    path('memory-matching/', views.memory_matching, name='memory_matching'),
]