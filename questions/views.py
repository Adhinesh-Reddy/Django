from django.http import HttpResponse


def login_view(request):
    return HttpResponse("<h1>My first Django App!  yey</h1>")
   
