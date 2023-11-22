from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Account

def frontpage(request):    
    if request.user.is_anonymous:
        return redirect(reverse("admin:login"), kwargs={"next":"/"})
    context = {
        "accounts": Account.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/index.html", context)
