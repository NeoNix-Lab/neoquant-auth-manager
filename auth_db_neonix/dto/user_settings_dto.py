from ..models.settings_base_class import SettingsBaseClass, SettingsTypeEnum as TypeEnum
from typing import TypedDict


class BaseSettingsDto(TypedDict):
    Id: int
    Type: str
    Settings: dict
    Name: str
    Is_Default: bool


# TODO : validate paths
class DbSetting(SettingsBaseClass):

    def __init__(self, item_db_path, data_db_path, ui_path, name: str, settings_id: int, is_default: bool, ):
        self.item_db_path = item_db_path
        self.data_db_path = data_db_path
        self.ui_path = ui_path
        super().__init__(TypeEnum.PATH, is_default, name, settings_id)

    def _set_settings(self) -> dict:
        return {"ITEM_DB_PATH": self.item_db_path, "DATA_DB_PATH": self.data_db_path, "UI_PPATH": self.ui_path}


class SocketSettings(SettingsBaseClass):

    def __init__(self, port, address, name: str, settings_id: int, is_default: bool, ):
        self.port = port
        self.address = address
        super().__init__(TypeEnum.PATH, is_default, name, settings_id)

    def _set_settings(self) -> dict:
        return {"PORT": self.port, "ADDRESS": self.address}
