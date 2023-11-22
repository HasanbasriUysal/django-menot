from django.shortcuts import render


def frontpage(request):
    return render(request, "moneyflow/index.html")
