from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Account


@login_required
def frontpage(request):       
        return render (request, "moneyflow/index.html")


@login_required
def accounts(request):    
    context = {
        "accounts": Account.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/accounts.html", context)


@login_required
def documents(request):     
    context = {
        "documents": Document.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/documents.html", context)