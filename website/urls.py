from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='home'),
    path('private/', views.PrivateNoteList.as_view(), name='pr_notes'),
    path('<slug:slug>/', views.note_detail, name='note_detail'),
    path('<slug:slug>/update/', views.NoteUpdateView.as_view(), name='note_update_view'),
    path('<slug:slug>/delete/', views.NoteDeleteView.as_view(), name='note_delete_view'),
    path('private/<slug:slug>/', views.pr_note_detail, name='pr_note_detail'),
    path('private/<slug:slug>/update/', views.NoteUpdateView.as_view(), name='pr_note_update_view'),
    path('private/<slug:slug>/delete/', views.NoteDeleteView.as_view(), name='pr_note_delete_view'),
]