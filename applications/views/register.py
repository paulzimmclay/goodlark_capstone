from applications.forms import RegistrationForm
from django.shortcuts import render
from . import login_user

def register(request):

    registered = False
    
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        return login_user(request)
        
    
    registration_form = RegistrationForm()
    return render(request, 'register.html', {'registration_form': registration_form})