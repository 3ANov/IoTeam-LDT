from django.views.generic import TemplateView


class MapTemplateView(TemplateView):
    template_name = "map/map.html"
