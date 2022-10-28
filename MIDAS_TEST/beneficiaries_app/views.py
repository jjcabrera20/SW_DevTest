from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BeneficiariesForm
from .models import Beneficiaries


def index(request):
    return render(request, 'wellcome.html')


def beneficiary_new(request):
    if request.method == 'POST':
        form = BeneficiariesForm(request.POST)
        if form.is_valid():
            p1 = form.save()
            print(type(p1))
        return redirect('beneficiaries:beneficiary_list')
    else:
        form = BeneficiariesForm()

    return render(request, 'beneficiary_edit.html', {'form': form})


def beneficiary_list(request):
    beneficiaries = Beneficiaries.objects.all()
    context = {'beneficiaries': beneficiaries}
    return render(request, "beneficiary_list.html", context)
