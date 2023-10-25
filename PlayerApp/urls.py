from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('logouts/', views.logout_views, name='logouts'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),

    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('add_songs_to_playlist/<int:playlist_id>/', views.add_songs_to_playlist, name='add_songs_to_playlist'),
    path('delete_playlist/<int:playlist_id>/', views.delete_playlist, name='delete_playlist'),


]

from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 