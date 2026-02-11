"""Admin registration for the sticky_notes app.

Registers models with the Django admin site.
"""

from django.contrib import admin
from .models import Note

admin.site.register(Note)
