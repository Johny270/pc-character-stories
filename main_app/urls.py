from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.character_index, name='character-index'),
    path('characters/<int:character_id>/', views.character_detail, name="character-detail"),
    path('characters/create/', views.CharacterCreate.as_view(), name='character-create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character-update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
