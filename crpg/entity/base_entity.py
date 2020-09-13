from abc import (
    ABCMeta,
    abstractmethod,
    abstractclassmethod,
    abstractproperty,
)


class BaseEntityFactory(metaclass=ABCMeta):

    def __init__(self):
        pass

    @classmethod
    def create(cls):
        pass


class BaseEntity(metaclass=ABCMeta):

    # jobclass - instance of a jobclass implementation.
    #   This is the Entity's notion of class/job, which determines abilities and spells.
    jobclass = None
    race = None

    def __init__(self):
        pass

    def as_jobclass(self, jobclass_instance):
        self.jobclass = jobclass_instance

    def as_race(self, race):
        self.race = race

    @abstractmethod
    def rest(self):
        raise NotImplementedError('Rest logic must be implemented in Entity subclass.')





