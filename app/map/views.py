from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView

from map.models import OdhRecord


class MapTemplateView(TemplateView):
    template_name = "map/map.html"


def odh_record_dataset(request):
    data = serialize('json', OdhRecord.objects.all()[:10],
                     fields=('root_id', 'name', 'coordinates', 'geometry_type'))
    return HttpResponse(data, content_type="json")
