from django.shortcuts import render
from .forms import NewsletterForm   

# Create your views here.
def retornar_home(request):
    return render(request,'home.html')

def retornar_cadastro(request):
    
    return render(request,'cadastro.html', {'form': NewsletterForm})

