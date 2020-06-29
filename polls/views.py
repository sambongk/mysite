#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


def index(request):
	return HttpResponse("헬로우고 나발이고.")