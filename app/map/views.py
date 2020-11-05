from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView

from map.models import OdhRecord


class MapTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "map/map.html"


@login_required
def odh_record_dataset(request):
    data = serialize('json', OdhRecord.objects.all()[:1],
                     fields=('root_id', 'name', 'coordinates', 'geometry_type'))
    return HttpResponse(data, content_type="json")
