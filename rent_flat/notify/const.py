from enum import Enum


class NotifyType(Enum):
    Add = 'Created'
    Del = 'Deleted'
    Mod = 'Modified'
    Mess = 'Message'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]