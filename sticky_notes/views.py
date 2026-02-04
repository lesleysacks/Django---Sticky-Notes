from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all().order_by("-id")
    return render(request, "note_list.html", {"notes": notes})

def note_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if title and content:
            Note.objects.create(title=title, content=content)

        return redirect("note_list")

    return render(request, "note_create.html")   # ← show form on GET


def note_delete(request, id):
    note = get_object_or_404(Note, id=id )
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "note_delete.html", {"note": note})