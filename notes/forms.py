from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    ModelForm to handle note creation and updates.
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
