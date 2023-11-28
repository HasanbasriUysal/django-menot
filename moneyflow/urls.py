from django.urls import path

from . import views

urlpatterns = [
    path("", views.frontpage, name="index"),
    path("tilit/", views.AccontsList.as_view(), name="accounts"),
    path(
        "tilit/<int:pk>", 
        views.AccountDetail.as_view(),
        name="accounts-detail",
    ),
    path("dokumentit/", views.documents, name="documents"),
]
