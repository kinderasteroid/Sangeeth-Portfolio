from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('h1.html')
  return HttpResponse(template.render())
# Create your views here.

def reg(request):
  template = loader.get_template('xyz.html')
  return HttpResponse(template.render())
