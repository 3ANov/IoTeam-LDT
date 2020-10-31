from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView

from map.models import OdhRecord


class MapTemplateView(TemplateView):
    template_name = "map/map.html"



def odh_record_dataset(request):
    data = serialize('json', OdhRecord.objects.all())
    return HttpResponse(data, content_type="json")