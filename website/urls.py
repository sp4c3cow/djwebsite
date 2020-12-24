from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='home'),
    path('private/', views.PrivateNoteList.as_view(), name='pr_notes'),
    path('<slug:slug>/', views.note_detail, name='note_detail'),
    path('private/<slug:slug>/', views.pr_note_detail, name='pr_note_detail')
]