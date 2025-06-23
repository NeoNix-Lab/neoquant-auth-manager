from auth_db_neonix.models.user_model import User
from auth_db_neonix.models.settings_base_class import SettingsBaseClass, SettingsTypeEnum
from auth_db_neonix.models.user_settings_models import DbSetting, SocketSettings
from auth_db_neonix.services.settings_factory import settings_from_dict
from auth_db_neonix.dto.user_dto import User_Dto_as_Dict

# TODO: automate this tests


def test_db_setting_serialization():
    db = DbSetting(
        item_db_path="item_path",
        data_db_path="data_path",
        ui_path="ui_path",
        name="TestSetting",
        settings_id=1,
        is_default=True
    )

    # Serializza
    dto = db.to_dict
    assert db.get_type == SettingsTypeEnum.PATH
    assert dto["Name"] == "TestSetting"
    assert dto["Settings"]["UI_PPATH"] == "ui_path"
    assert isinstance(dto["Type"], str)

    # Deserializza
    restored = settings_from_dict(dto)
    assert isinstance(restored, SettingsBaseClass)  # factory da migliorare
    assert restored.get_settings["ITEM_DB_PATH"] == "item_path"


def test_user_to_from_dto():
    user_dto: User_Dto_as_Dict = {
        "Username": "Nicola",
        "Email": "nicola@example.com",
        "UserId": "uid123",
        "Settings": [
            {
                "Id": 1,
                "Type": "path",
                "Settings": {
                    "ITEM_DB_PATH": "item.db",
                    "DATA_DB_PATH": "data.db",                 "UI_PPATH": "ui.json"
                },
                "Name": "Default",
                "Is_Default": True
            }
        ]
    }

    # Deserializza -> Oggetto
    user = User.from_dto(user_dto, jwt="abc.jwt.token")
    assert user.userId == "uid123"
    assert user.profile["Username"] == "Nicola"
    assert len(user.settings) == 1

    # Serializza -> DTO
    dto_back = user.to_dto()
    assert dto_back["Email"] == "nicola@example.com"
    assert dto_back["Settings"][0]["Settings"]["UI_PPATH"] == "ui.json"


def test_socket_setting_serialization():
    socket = SocketSettings(
        port=8080,
        address="127.0.0.1",
        name="SocketCfg",
        settings_id=2,
        is_default=False
    )

    dto = socket.to_dict
    assert dto["Settings"]["PORT"] == 8080

    restored = settings_from_dict(dto)
    assert isinstance(restored, SettingsBaseClass)
