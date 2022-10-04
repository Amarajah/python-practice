from django.shortcuts import render
from django.http import HttpResponse
from .models import Output

# Create your views here.
def index(request):
    output = Output.objects.all()
    return render(request, 'index.html', {'output': output})

def counter(request):
    textarea = request.POST['textarea']
    amount_of_text = len(textarea.split())
    return render(request,'counter.html',{'amount': amount_of_text})