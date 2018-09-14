from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


from applications.forms import ApplicationUserForm, ApplicationForm
from applications.models import ApplicationFormModel


@login_required
def regular_application(request):
    application = ApplicationFormModel.objects.get(user_id=request.user.id)
    
    if request.method == 'POST':

        application_user_form = ApplicationUserForm(request.POST, instance=request.user)
        application_form = ApplicationForm(request.POST, instance=application)

        print('forms are valid?', application_form.is_valid(), application_user_form.is_valid())
        print(application_form.errors)

        if application_user_form.is_valid() and application_form.is_valid():
            application_user_form.save()
            application_form.save()
            return HttpResponseRedirect('/')
        else: 
            print('forms not valid')


    application_user_form = ApplicationUserForm(initial={
        'first_name': request.user.first_name, 
        'last_name': request.user.last_name,
        'email': request.user.email,
        })


    application_form = ApplicationForm(initial={
        'user': request.user.id,
        'mailing_address': application.mailing_address
    })


    return render(request, 'regular_application.html', {
        'application_user_form': application_user_form,
        'application_form': application_form,
        })