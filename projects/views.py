from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Project


# Create your views here.

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def projects(request):
  myprojects = Project.objects.all()
  return render(request, 'all_projects.html', {'myprojects': myprojects})
 

def details(request, id):
  myproject = get_object_or_404(Project, id=id)
  return render(request, 'details.html', {'myproject': myproject})
