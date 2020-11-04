from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from file_processing.forms import FileUploadForm
from file_processing.models import FileModel
from file_processing.services import parsing_odh_file


class FileUploadView(LoginRequiredMixin, View):
    form_class = FileUploadForm
    success_url = reverse_lazy('home')
    template_name = 'file_processing/upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #parsing_odh_file()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


def file_view(request):
    file_to_read = FileModel.objects.filter(content_type='ODH_DATA').first()
    out_str = file_to_read.content.open('r').readlines()
    file_to_read.content.close()
    return render(request, 'file_processing/file_read.html', {'out_str': out_str})
