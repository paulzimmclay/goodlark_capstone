from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from applications.forms import ApplicationUserForm


@login_required
def regular_application(request):
    # u = User.objects.get(id=request.user.id)

    application_user_form = ApplicationUserForm(initial={
        'first_name': request.user.first_name, 
        'last_name': request.user.last_name,
        'email': request.user.email},
        )
    return render(request, 'regular_application.html', {'application_user_form': application_user_form})