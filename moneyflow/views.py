from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .models import Account, Category, Document


@login_required
def frontpage(request):
    return render(request, "moneyflow/index.html")


class OwnerFilteredMixin(LoginRequiredMixin):
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class AccountList(OwnerFilteredMixin, ListView):
    model = Account


class AccountDetail(OwnerFilteredMixin, DetailView):
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transactions"] = self.object.transactions.all()
        return context


class DocumentList(OwnerFilteredMixin, ListView):
    model = Document


class DocumentDetail(OwnerFilteredMixin, DetailView):
    model = Document
    

class CategoryList(OwnerFilteredMixin, ListView):
    model = Category


class CategoryDetail(OwnerFilteredMixin, DetailView):
    model = Category    