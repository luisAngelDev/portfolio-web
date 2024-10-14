from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Publication

# Create your views here.

def home_publication(request):
  mypublications = Publication.objects.all()
  return render(request, 'publication.html', {'mypublications': mypublications})

def details(request, id):
  mypublication = get_object_or_404(Publication, id=id)
  return render(request, 'publication_details.html', {'mypublication': mypublication})
