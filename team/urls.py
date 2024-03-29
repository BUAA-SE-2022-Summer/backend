# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_team', views.create_team),
    path('invite_member', views.invite_member),
    path('kick_member', views.kick_member),
    path('set_manager', views.set_manager),
    path('delete_manager', views.delete_manager),
    path('get_team_info', views.get_team_info),
    path('rename_team', views.rename_team),
    path('show_my_team_list', views.show_my_team_list),
    path('confirm_invitation', views.confirm_invitation),
    path('accept_invitation', views.accept_invitation)
]
