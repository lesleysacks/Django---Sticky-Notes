"""Views for the sticky_notes app: list, create, detail, update, delete.

These simple function-based views render templates and handle form
submission for the `Note` model.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    """Render the list of notes ordered by newest first.

    Returns an HTML response containing the `note_list` template with
    a `notes` context variable.
    """
    notes = Note.objects.all().order_by("-id")
    return render(request, "note_list.html", {"notes": notes})


def note_create(request):
    """Handle creation of a new `Note`.

    On GET: render an empty `NoteForm`.
    On POST: validate and save the form, then redirect to the list.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
        # If invalid, fall through to re-render the form with errors (status 200)
    else:
        form = NoteForm()

    return render(request, "note_form.html", {"form": form})


def note_detail(request, id):
    """Render a single note identified by `id`.

    Returns 404 if the note does not exist.
    """
    note = get_object_or_404(Note, id=id)
    return render(request, "note_detail.html", {"note": note})


def note_update(request, id):
    """Update an existing note.

    On GET: render a pre-filled form.
    On POST: validate and save changes, then redirect to the detail view.
    """
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, "note_form.html", {"form": form, "note": note})


def note_delete(request, id):
    """Delete a note after confirmation.

    On GET: render a confirmation page.
    On POST: delete the instance and redirect to the list.
    """
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "note_delete.html", {"note": note})