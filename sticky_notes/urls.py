from django.urls import path
from . import views 


urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('delete/<int:id>/', views.note_delete, name='note_delete'),
    path('update/<int:id>/', views.note_update, name='note_update'),
    path('<int:id>/', views.note_detail, name='note_detail'),
    
    #  NoteDeleteView.as_view(), name='note_delete'),  
]