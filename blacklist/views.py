from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from wsgiref.util import FileWrapper
from django.conf import settings

from .handle import handle_uploaded_file
from .forms import UploadFileForm
from .models import blacklist

import os

# Create your views here.


def index(request):
	if request.user.is_authenticated:
		bl = blacklist.objects.latest('pk')
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				handle_uploaded_file(request.FILES['blacklist'], request.user.username)
				return HttpResponseRedirect('/')
			return render(request, 'index.html', {'form': form, 'blacklist': bl})
		else:
			form = UploadFileForm()
		return render(request, 'index.html', {'form': form, 'blacklist': bl})
	else:
		return render(request, 'index_no_login.html')

def get_file(request):
	if request.user.is_authenticated:
		path = 'files/blacklist.ini'
		file_path = os.path.join(settings.MEDIA_ROOT, path)
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
		raise Http404
	else:
		return render(request, 'index_no_login.html')

def get_text(request):
	if request.user.is_authenticated:
		path = 'files/blacklist.ini'
		file_path = os.path.join(settings.MEDIA_ROOT, path)
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read())
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
		raise Http404
	else:
		return render(request, 'index_no_login.html')