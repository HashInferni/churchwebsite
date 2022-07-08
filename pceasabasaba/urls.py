from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('property-grid.html/', views.services, name='services'),
    path('blog-grid.html/', views.projects, name='projects'),
    path('property-single.html/', views.church_school, name='church school'),
    path('property-single.html/', views.brigade, name='brigade'),
    path('property-single.html/', views.youth_fellowship, name='youth fellowship'),
    path('property-single.html/', views.womans_guild, name='womans guild'),
    path('property-single.html/', views.pcmf, name='pcmf'),
    path('property-single.html/', views.choirs, name='choirs'),
    path('contact.html/', views.contact, name='contact')

]
