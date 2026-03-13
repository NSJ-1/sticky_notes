from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display all notes.
    """
    notes = Note.objects.all().order_by("-created_at")

    context = {
        "notes": notes,
        "page_title": "All Notes",
    }
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """
    Showing note by primary key.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    Create a new note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    Edit an existing note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=pk)
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    Delete a note and redirect back to list.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
