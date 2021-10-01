from django.shortcuts import render
from django.views import View
from .forms import CustomerRegisterForm


class ShowCustomerRegisterForm(View):
    def get(self, request):
        form = CustomerRegisterForm()
        return render(request, 'customers/customer_register.html', context={
            'form': form
        })
