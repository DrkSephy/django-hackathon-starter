from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
	context = {'hello': 'world'}
	return render(request, 'hackathon/index.html', context)

def test(request):
	return HttpResponse('meow')
