from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def books(request):
	c = RequestContext(request, {}, [])
	return render_to_response('books.html', c)