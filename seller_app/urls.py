from django.urls import path

from seller_app import views


app_name = "seller"

urlpatterns = [
    path("", views.ItemListView.as_view(), name="item-list"),
    path("item-detail/<int:pk>/", views.ItemDetailView.as_view(), name="item-detail"),
    path("draft-list/", views.DraftListView.as_view(), name="draft-list"),
    path("draft-detail/<int:pk>/", views.DraftDetailView.as_view(), name="draft-detail"),
    path("draft-publish/<int:pk>/", views.DraftPublishView.as_view(), name="draft-publish"),
    path("item-delete/<int:pk>/", views.ItemDeleteView.as_view(), name="item-delete"),
    path("item-create/", views.ItemCreateView.as_view(), name="item-create"),
    path("item-update/<int:pk>/", views.ItemUpdateView.as_view(), name="item-update"), 
]
