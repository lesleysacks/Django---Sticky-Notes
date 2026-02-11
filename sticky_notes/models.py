"""Data models for the sticky_notes application.

Defines the `Note` model used to store simple note data.
"""

from django.db import models


class Note(models.Model):
    """A short text note with a title and content.

    Fields:
        title: Short text title for the note.
        content: Body of the note.
        created_at: Timestamp when the note was created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
