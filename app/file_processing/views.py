from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from file_processing.forms import FileUploadForm


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})