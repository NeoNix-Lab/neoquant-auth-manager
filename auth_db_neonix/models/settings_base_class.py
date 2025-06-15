from abc import ABC, abstractmethod
from enum import Enum, auto
from ..dto.user_settings_dto import BaseSettingsDto


class SettingsTypeEnum(Enum):
    SOCKET = auto()
    PATH = auto()
    CLOUD = auto()
    DOCKER = auto()


class SettingsBaseClass(ABC):
    def __init__(self, setting_type: SettingsTypeEnum, is_default: bool, name: str, settings_id: int, settings=None):
        self._type = setting_type
        self.is_default: bool = is_default
        self._id = settings_id
        self._name = name
        if settings is not None:
            self._setting: dict = self._set_settings()
        else:
            self._settings = settings

    @property
    def get_type(self):
        return self._type

    @property
    def get_settings(self):
        return self._setting

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    @property
    def to_dict(self) -> BaseSettingsDto:
        return {"Id": self._id, "Type": str(self._type.value), "Settings": self._setting,
                "Name": self._name, "Is_Default": self.is_default}

    @abstractmethod
    def _set_settings(self) -> dict:
        ...

    @classmethod
    def from_dict(cls, record: dict):
        return cls(SettingsTypeEnum(record["Type"]), record["Is_Default"],
                   record["Name"], record["Id"], record["Settings"])
