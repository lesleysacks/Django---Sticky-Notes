from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    notes = Note.objects.all().order_by("-id")
    return render(request, "note_list.html", {"notes": notes})


def note_create(request):
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
    note = get_object_or_404(Note, id=id)
    return render(request, "note_detail.html", {"note": note})


def note_update(request, id):
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
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "note_delete.html", {"note": note})