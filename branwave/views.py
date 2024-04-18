from django.shortcuts import render
from .models import clients
# Create your views here.
def index(request):
    cc=clients();
    cc.name='MadhuB';
    return render(request,"index.html",{'cc':cc});
