from django.contrib import admin
from .models import Note, Comment

# @admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on', 'status')
    list_filter = ('status',)
    search_fields = ['status', 'content']
    prepopulated_fields = {"slug": ("title",)}

# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'body', 'note', 'created_on', 'active',)
    list_filter = ('active', 'created_on',)
    search_fields = ('username', 'email',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)
