from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CommentForm
from .models import Note
from django.urls import reverse

def note_detail(request, slug):
    template_name = 'html/note_detail.html'
    note = get_object_or_404(Note, slug=slug)
    comments = note.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current note to the comment
            new_comment.note = note
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'note_detail': note,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def pr_note_detail(request, slug):
    template_name = 'html/pr_note_detail.html'
    pr_note = get_object_or_404(Note, slug=slug)
    comments = pr_note.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current note to the comment
            new_comment.note = pr_note
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'pr_note_detail': pr_note,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class NoteList(generic.ListView):
    context_object_name = 'notes_list'
    queryset = Note.objects.filter(status=0).order_by('-created_on')
    template_name = 'html/index.html'

class PrivateNoteList(generic.ListView):
    context_object_name = 'private_notes_list'
    queryset = Note.objects.filter(status=1).order_by('-created_on')
    template_name = 'html/private.html'

class NoteUpdateView(generic.UpdateView):
    model = Note
    fields = ['title', 'content', 'status']
    template_name = "html/note_update_view.html"

class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = '/'
    template_name = "html/note_confirm_delete.html"

# class PrivateNoteDetail(generic.DetailView):
#     context_object_name = 'pr_note_detail'
#     model = Note
#     template_name = 'html/pr_note_detail.html'

# class NoteDetail(generic.DetailView):
#     context_object_name = 'note_detail'
#     model = Note
#     template_name = 'html/note_detail.html'
