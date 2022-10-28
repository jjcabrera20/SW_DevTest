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


def beneficiary_edit(request, beneficiaries_id):
    beneficiary = get_object_or_404(Beneficiaries, id=beneficiaries_id)
    if request.method == 'POST':
        form = BeneficiariesForm(request.POST, instance=beneficiary)
        if form.is_valid():
            p1 = form.save()
            return redirect('beneficiaries_app:beneficiary_list')
        else:
            messages.error(request, form.errors)
    else:
        form = BeneficiariesForm(instance=beneficiary)
    context = {'form': form}
    return render(request, 'beneficiary_edit.html', context)


def beneficiary_delete(request, beneficiaries_id):
    beneficiary = get_object_or_404(Beneficiaries, id=beneficiaries_id)
    context = {
        "beneficiary": beneficiary
    }
    if request.method == 'POST':
        beneficiary.delete()
        return redirect('beneficiaries_app:beneficiary_list')
    else:
        return render(request, "beneficiary_delete.html", context)


def beneficiary_list(request):
    beneficiaries = Beneficiaries.objects.all()
    context = {'beneficiaries': beneficiaries}
    return render(request, "beneficiary_list.html", context)
