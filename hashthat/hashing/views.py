from django.shortcuts import render
from .forms import HashForm
# Create your views here.
def homepage(request):
    return render(request, 'home.html', {'HashForm':HashForm()})