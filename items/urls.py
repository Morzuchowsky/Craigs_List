from django.urls import path
from .views import (
    ItemListView,
    ItemUpdateView,
    ItemDetailView,
    ItemDeleteView,
    ItemCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name="item_edit"),
    path('<int:pk>/', ItemDetailView.as_view(), name="item_detail"),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name="item_delete"),
    path('', ItemListView.as_view(), name="item_list"),
    path('/new/', ItemCreateView.as_view(), name="item_new"),
]
