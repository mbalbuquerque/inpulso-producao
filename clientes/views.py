from django.shortcuts import get_object_or_404, redirect, render

from .models import Cliente


def lista_clientes(request):
    clientes = Cliente.objects.all()

    busca = request.GET.get("busca", "").strip()

    if busca:
        clientes = clientes.filter(nome__icontains=busca)

    contexto = {
        "clientes": clientes,
        "busca": busca,
    }

    return render(request, "clientes/lista.html", contexto)


def novo_cliente(request):

    if request.method == "POST":

        nome = request.POST.get("nome", "").strip()
        telefone = request.POST.get("telefone", "").strip()
        email = request.POST.get("email", "").strip()
        endereco = request.POST.get("endereco", "").strip()

        if nome:
            Cliente.objects.create(
                nome=nome,
                telefone=telefone,
                email=email,
                endereco=endereco,
            )

            return redirect("clientes:lista")

    return render(request, "clientes/formulario.html")


def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":

        cliente.nome = request.POST.get("nome", "").strip()
        cliente.telefone = request.POST.get("telefone", "").strip()
        cliente.email = request.POST.get("email", "").strip()
        cliente.endereco = request.POST.get("endereco", "").strip()

        cliente.save()

        return redirect("clientes:lista")

    contexto = {
        "cliente": cliente,
    }

    return render(
        request,
        "clientes/formulario.html",
        contexto,
    )


def excluir_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()

        return redirect("clientes:lista")

    contexto = {
        "cliente": cliente,
    }

    return render(
        request,
        "clientes/confirmar_exclusao.html",
        contexto,
    )