from PyQt5.QtCore import QSettings

idol_list = list(range(1, 29)) + [90]
idol_default = [1, 2, 3, 90]


def save_settings(slot, idol_id):
    settings = QSettings("settings.ini", QSettings.IniFormat)

    settings.beginGroup("Idols")
    settings.setValue(f"idol_{slot}", idol_id)
    settings.endGroup()


def load_settings():
    settings = QSettings("settings.ini", QSettings.IniFormat)

    settings.beginGroup("Idols")
    try:
        idols = [int(settings.value(f"idol_{idx + 1}", idol_default[idx])) for idx in range(4)]
    except ValueError:
        idols = idol_default
    for idol_idx, idol in enumerate(idols):
        if idol not in idol_list:
            idols[idol_idx] = idol_default[idol_idx]
    settings.endGroup()

    return idols
