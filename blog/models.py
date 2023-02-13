from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from hitcount.models import HitCount

from users.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.CharField(max_length=400, verbose_name='content')
    preview = models.ImageField(upload_to='blog/', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    status = models.BooleanField(default=True, verbose_name='Allow publish')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')




