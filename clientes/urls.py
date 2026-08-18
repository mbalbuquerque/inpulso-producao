from django.urls import path

from . import views


app_name = "clientes"


urlpatterns = [
    path("", views.lista_clientes, name="lista"),

    path(
        "novo/",
        views.novo_cliente,
        name="novo",
    ),

    path(
        "<int:id>/editar/",
        views.editar_cliente,
        name="editar",
    ),

    path(
        "<int:id>/excluir/",
        views.excluir_cliente,
        name="excluir",
    ),
]