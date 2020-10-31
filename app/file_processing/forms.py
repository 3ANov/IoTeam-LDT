from django.forms import ModelForm
from file_processing.models import FileModel


class FileUploadForm(ModelForm):
    class Meta:
        model = FileModel
        fields = ['created_date', 'content', 'content_type']
        labels = {
            'content': 'Файл',
        }
