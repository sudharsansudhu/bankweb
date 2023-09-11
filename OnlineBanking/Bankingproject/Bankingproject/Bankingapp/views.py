from django.shortcuts import render
from django.http import HttpResponse
from .models import plans
# Create your views here.
def home(request):
    obj=plans.objects.all()
    return render(request,'index.html', {'result':obj})
