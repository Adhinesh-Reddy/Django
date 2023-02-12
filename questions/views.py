from cmath import log
from django.shortcuts import redirect, render

from questions.models import Answers, Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.http import HttpResponse


from django.contrib import messages
def login_view(request):
    return HttpResponse("<h1>My first Django App!  yey</h1>")
   
