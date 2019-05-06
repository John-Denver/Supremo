from django.urls import path
from . import views


app_name = 'STalk'


urlpatterns = [
    #path('iindex/', views.iindex, name='iindex'),

    path('logins', views.logins, name='logins'),
    path('registrations', views.registrations, name='registrations'),

    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('deejay', views.deejay, name='deejay'),
    path('(?<deejay_id>[0-9]+)/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('login_deejay/', views.login_deejay, name='login_deejay'),
    path('logout_deejay/', views.logout_deejay, name='logout_deejay'),
    path('(?<deejay_id>[0-9]+)/delete_deejay', views.delete_deejay, name='delete_deejay'),

    path('speaker_index', views.speaker_index, name='speaker_index'),
    path('(?<speaker_id>[0-9]+)/', views.detail2, name='detail2'),
    path('speaker_register/', views.speaker_register, name='speaker_register'),
    path('login_speaker/', views.login_speaker, name='login_speaker'),
    path('logout_speaker/', views.logout_speaker, name='logout_speaker'),
    path('speaker', views.speaker, name='speaker'),
    path('(?<speaker_id>[0-9]+)/delete_speaker', views.delete_speaker, name='delete_speaker'),

    path('mc_index', views.mc_index, name='mc_index'),
    path('mc', views.mc, name='mc'),
    path('mc_register/', views.mc_register, name='mc_register'),
    path('login_mc/', views.login_mc, name='login_mc'),
    path('logout_mc/', views.logout_mc, name='logout_mc'),
    path('(?P<m_id>[0-9]+)/', views.detailmc, name='detailmc'),
    path('(?<mc_id>[0-9]+)/delete_mc', views.delete_mc, name='delete_mc'),

    path('event_index', views.event_index, name='event_index'),
    path('event', views.event, name='event'),
    path('event_register/', views.event_register, name='event_register'),
    path('login_event/', views.login_event, name='login_event'),
    path('logout_event/', views.logout_event, name='logout_event'),
    path('(?P<event_id>[0-9]+)/', views.detailevent, name='detailevent'),
    path('(?<event_id>[0-9]+)/delete_event', views.delete_event, name='delete_event'),

    path('hype_index', views.hype_index, name='hype_index'),
    path('hype', views.hype, name='hype'),
    path('hyper_register/', views.hyper_register, name='hyper_register'),
    path('login_hyper/', views.login_hyper, name='login_hyper'),
    path('logout_hyper/', views.logout_hyper, name='logout_hyper'),
    path('(?P<hype_id>[0-9]+)/', views.detailhype, name='detailhype'),
    path('(?<hype_id>[0-9]+)/delete_hype', views.delete_hype, name='delete_hype'),
]








