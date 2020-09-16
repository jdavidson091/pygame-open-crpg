from abc import (
    ABCMeta,
    abstractmethod,
    abstractclassmethod,
    abstractproperty,
)

from .stats.stat_collection import StatCollection


class BaseEntityFactory(metaclass=ABCMeta):

    @abstract
    entity_class = None

    def __init__(self):
        self.entity_class = entity_class

    def create(self, jobclass=None, race=None, stats=None, *args, **kwargs):
        entity = self.entity_class()
        if jobclass:
            entity = entity.as_jobclass(jobclass)
        if race:
            entity = entity.as_race(race)
        for stat in stats:
            entity = entity.with_stat(stat)
        return entity


class BaseEntity(metaclass=ABCMeta):

    # jobclass - instance of a jobclass implementation.
    #   This is the Entity's notion of class/job, which determines abilities and spells.
    jobclass = None
    race = None
    _stat_collection = None

    def __init__(self):
        self._stat_collection = StatCollection()

    def as_jobclass(self, jobclass_instance):
        self.jobclass = jobclass_instance

    def as_race(self, race):
        self.race = race

    def with_stat(self, stat):
        self._stat_collection.append(stat)

    @abstractmethod
    def rest(self):
        raise NotImplementedError('Rest logic must be implemented in Entity subclass.')

    def adjust_stat(self, stat_name, val):
        self._stat_collection.adjust_stat()


