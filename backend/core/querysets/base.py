from operator import attrgetter

from django.db.models import QuerySet

__all__ = ['BaseQuerySet']


class BaseQuerySet(QuerySet):

    def map_by(self, attr_name):
        return {getattr(o, attr_name): o for o in self}

    def map_list_by(self, attr_name):
        res = {}
        for o in self:
            res.setdefault(getattr(o, attr_name), []).append(o)
        return res

    def get_ids(self):
        return set(map(attrgetter("pk"), self))
