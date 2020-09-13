from abc import ABCMeta


class BaseJobclass(metaclass=ABCMeta):

    race = None
    spells_available = None
    spells_memorized = None

    # TODO: starting stats? Potential stat ceilings? Usable weapons/armor?

    def __init__(self):
        pass
