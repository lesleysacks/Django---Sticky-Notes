"""Forms for the sticky_notes app.

Provides a `ModelForm` used to create and edit `Note` instances.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating `Note` instances."""
    class Meta:
        model = Note
        fields = ['title', 'content']
