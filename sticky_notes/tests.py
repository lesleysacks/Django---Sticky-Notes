from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteTests(TestCase):
    def test_example(self):
        self.assertEqual(1, 1)

class NoteViewTests(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Sample Note",
            content="Sample Content"
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Note")

    def test_note_create_view_get(self):
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)

    def test_note_create_view_post(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_note_detail_view(self):
        response = self.client.get(
            reverse('note_detail', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_note_update_view(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.id]),
            {
                'title': 'Updated Title',
                'content': 'Updated Content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')

    def test_note_delete_view(self):
        response = self.client.post(
            reverse('note_delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)


class NoteFormValidationTests(TestCase):
    def test_empty_form_submission(self):
        response = self.client.post(reverse('note_create'), {
            'title': '',
            'content': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 0)
