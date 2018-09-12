from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from applications.forms import ApplicationUserForm, ApplicationForm
from applications.models import ApplicationForm


@login_required
def regular_application(request):
    if request.method == 'POST':
        u = User.objects.get(id=request.user.id)
        application = ApplicationForm
        application_user_form = ApplicationUserForm(request.POST, instance=request.user)
        application_form = ApplicationForm(request.POST, instance=u.id)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
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
        'mailing_address': 'checka',
    })

    print(application_form.as_p())


    return render(request, 'regular_application.html', {
        'application_user_form': application_user_form,
        'application_form': application_form,
        })