from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Account, Document


@login_required
def frontpage(request):       
        return render (request, "moneyflow/index.html")


class AccountView:
     model = Account

     def get_queryset(self):
         return super().get_queryset().filter(owner=self.request.user)

class AccontsList(LoginRequiredMixin, AccountView, ListView):
    pass


class AccountDetail(LoginRequiredMixin, AccountView, DetailView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
         context = super().get_context_data(**kwargs)   
         context["transaction"] = self.object.transactions.all()
         return context
    
    transaction.account

@login_required
def documents(request):     
    context = {
        "documents": Document.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/documents.html", context)