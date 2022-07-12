from django.urls import path

from .views import HomeView, NoteCreateView, NoteDeleteView, NoteDetailView, NoteListView, NoteUpdateView, TripDeleteView, TripDetailView, TripUpdateView, trips_list, TripCreateView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', trips_list, name="trip-list"),
    path('dashboard/trip/create/', TripCreateView.as_view(), name="trip-create"),
    path('dashboard/trip/<int:pk>/', TripDetailView.as_view(), name="trip-detail"),
    path('dashboard/trip/<int:pk>/update/', TripUpdateView.as_view(), name="trip-update"),
    path('dashboard/trip/<int:pk>/delete/', TripDeleteView.as_view(), name="trip-delete"),
    path('dashboard/note/', NoteListView.as_view(), name="note-list"),
    path('dashboard/note/<int:pk>/', NoteDetailView.as_view(), name="note-detail"),
    path('dashboard/note/<int:pk>/update/', NoteUpdateView.as_view(), name="note-update"),
    path('dashboard/note/<int:pk>/delete/', NoteDeleteView.as_view(), name="note-delete"),
    path('dashboard/note/create/', NoteCreateView.as_view(), name="note-create"),
]
