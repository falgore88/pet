from django.db.models import Manager

from core.querysets.base import BaseQuerySet

__all__ = ['BaseManager']


class BaseManager(Manager):
    queryset_class = BaseQuerySet

    def get_queryset(self):
        return self.queryset_class(self.model, using=self._db)
