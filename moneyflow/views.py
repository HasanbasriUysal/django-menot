from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView

from .models import Account, Document


@login_required
def frontpage(request):       
        return render (request, "moneyflow/index.html")


class AccontsList(LoginRequiredMixin, ListView):
     model = Account

     def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
    

@login_required
def documents(request):     
    context = {
        "documents": Document.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/documents.html", context)