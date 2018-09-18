from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


from applications.forms import ApplicationForm
from applications.models import ApplicationFormModel


@login_required
def regular_application(request):
    application = ApplicationFormModel.objects.get(user_id=request.user.id)
    
    if request.method == 'POST':

        application_form = ApplicationForm(request.POST, instance=application)

        if application_form.is_valid():
            application_form.save()
            return HttpResponseRedirect('/')
        else: 
            print('forms not valid')

    
    # dictionary of all user application fields
    application_dict = application.__dict__
    # fields to exclude from form:
    excluded_fields = {'id', 'user_id', '_state'}
    # dictionary of fields to include on form
    application_fields = {k:v for (k, v) in application_dict.items() if k not in excluded_fields}

    # generate dictionary that includes all needed keys and default values:
    default_dict = {}
    default_dict['user'] = request.user.id
    for k,v in application_fields.items():
        default_dict[k] = v

    application_form = ApplicationForm(initial=default_dict)


    return render(request, 'regular_application.html', {
        'application_form': application_form,
        })