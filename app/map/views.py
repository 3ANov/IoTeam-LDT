from django.core.serializers import serialize
from django.views.generic import TemplateView

from map.models import OdhRecord


class MapTemplateView(TemplateView):
    template_name = "map/map.html"
    context = serialize('geojson', OdhRecord.objects.all())
