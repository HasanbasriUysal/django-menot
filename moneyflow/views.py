from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .models import Account, Document


@login_required
def frontpage(request):       
        return render (request, "moneyflow/index.html")


class OwnerFilteredMixin(LoginRequiredMixin):
     def get_queryset(self):
        super_vastaus = super().get_queryset()
        
        return super_vastaus.filter(owner=self.request.user)


class AccontsList(OwnerFilteredMixin, ListView):
    model = Account
    

class AccountDetail(OwnerFilteredMixin, DetailView):
    model = Account

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)   
         context["transaction"] = self.object.transactions.all()
         return context
    

class DocumentList(OwnerFilteredMixin,ListView):
     model = Document

    