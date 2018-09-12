from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def regular_application(request):
    
    return HttpResponse('<p>login successful</p>')
