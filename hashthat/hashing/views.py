from csv import excel
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Hash
from .forms import HashForm
import hashlib
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = HashForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(text=text)
            except Hash.DoesNotExist:
                hash = text_hash
                hash = Hash(text=text, hash=hash)
                hash.save()
            return redirect('hash', hash=text_hash)
    return render(request, 'home.html', {'HashForm':HashForm()})

def renderHash(request, hash):
    hash = Hash.objects.get(hash=hash)
    return render(request, 'hash.html', {'hash':hash})

def quickhash(request):
    text = request.GET['text']
    return JsonResponse({'hash': hashlib.sha256(text.encode('utf-8')).hexdigest()})
    