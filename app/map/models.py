from django.db import models


class OdhRecord(models.Model):
    """
    Объект - который хранит записи из odh geojson, но без большнства полей
        root_id - Идентификатор ОДХ
        name - Наименование объекта
        geometry - пространственные координаты объекта в виде строки
        geometry_type - тип пространственного объекта (Точка, полигон и т.д.)
    """
    root_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=300)
    geometry = models.TextField()
    geometry_type = models.CharField(max_length=20)
