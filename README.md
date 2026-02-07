# Django---Sticky-Notes
Application Part 1 & 2

## Setup Instructions

python -m venv venv
source venv/bin/activate #Windows: venv\Scripts\activate
pip install -r requirements
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Diagrams (Use Case + Sequence)

Render these PlantUML sources (https://plantuml.com/ or VSCode PlantUML) — they map exactly to the app routes and views.

Use Case Diagram:
```plantuml
@startuml
left to right direction
actor User
rectangle "Sticky Notes App" {
  usecase "View Notes List" as VNL
  usecase "View Note Details" as VND
  usecase "Create Note" as CN
  usecase "Update Note" as UN
  usecase "Delete Note" as DN
}
User --> VNL
User --> VND
User --> CN
User --> UN
User --> DN
@enduml
```

Sequence Diagram (combined flows):
```plantuml
@startuml
actor User
participant "views.py" as Views
participant "models.py (DB)" as DB

== View Notes List ==
User -> Views: GET /
Views -> DB: Note.objects.all()
DB --> Views: notes
Views --> User: 200 HTML (note_list)

== View Note Details ==
User -> Views: GET /{id}/
Views -> DB: Note.objects.get(id)
DB --> Views: note
Views --> User: 200 HTML (note_detail)

== Create Note ==
User -> Views: GET /create/
Views --> User: 200 HTML (note_form)
User -> Views: POST /create/ (form data)
Views -> DB: Note.save()
DB --> Views: created note
Views --> User: Redirect to /

== Update Note ==
User -> Views: GET /update/{id}/
Views -> DB: Note.objects.get(id)
DB --> Views: note (form pre-filled)
Views --> User: 200 HTML (note_form)
User -> Views: POST /update/{id}/ (form data)
Views -> DB: instance.save()
DB --> Views: updated note
Views --> User: Redirect to /{id}/

== Delete Note ==
User -> Views: GET /delete/{id}/
Views --> User: 200 HTML (note_delete confirm)
User -> Views: POST /delete/{id}/
Views -> DB: instance.delete()
DB --> Views: deleted
Views --> User: Redirect to /
@enduml
```
