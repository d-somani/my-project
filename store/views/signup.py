from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )
        error_message = self.validateCustomer(customer)

        if not error_message:
            # Hash the password
            customer.password = make_password(customer.password)
            # Save the customer to the database
            customer.register()

            # Log the user in
            request.session['customer'] = customer.id
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
            error_message = "First Name is required!"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be at least 4 characters long."
        elif not customer.last_name:
            error_message = "Last Name is required!"
        elif len(customer.last_name) < 2:
            error_message = "Last Name must be at least 2 characters long."
        elif not customer.phone:
            error_message = "Phone number is required!"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be exactly 10 digits."
        elif len(customer.email) < 4:
            error_message = "Email must be at least 5 characters long!"
        elif not customer.password:
            error_message = "Password is required!"
        elif len(customer.password) < 6:
            error_message = "Password must be at least 6 characters long."
        elif customer.isExists():
            error_message = 'Email Address already registered'

        return error_message