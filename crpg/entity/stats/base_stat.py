from abc import ABCMeta


class BaseStat(metaclass=ABCMeta):

    # The numeric value of the current stat
    _val = None

    # What the stat originated as
    _origin_val = None

    # Half-value thresholds
    _partial_val = None

    def __init__(self):
        pass




