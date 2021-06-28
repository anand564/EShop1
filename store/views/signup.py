from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        # validation:
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        # Saving in db:

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif not customer.first_name.isalpha():
            error_message = "First Name Must Be Alphabet !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name Must Be Greater Than 4 Charcters !!"
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif not customer.last_name.isalpha():
            error_message = "Last Name Must Be Alphabet !!"
        elif len(customer.last_name) < 1:
            error_message = "Last Name Atleast Have 1 Letter"
        elif not customer.phone:
            error_message = "Phone Number Required !!"

        elif len(customer.phone) < 10:
            error_message = "Phone Number Must Be 10 Digits"
        elif not customer.password:
            error_message = "Password Required !!"
        elif len(customer.password) < 6:
            error_message = "The Password Must Be Greater Than 6 Digits or Letters Combination"
        elif customer.isExists():
            error_message = "Email Already Registered !!"
        return error_message
