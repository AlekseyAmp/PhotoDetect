from datetime import datetime

import pytz


# Утилиты для работы со временем
def get_current_dt(timezone: str = None) -> datetime:
    """
    Возвращает текущую дату и время без миллисекунд в указанном часовом поясе.

    :param timezone: Строка с идентификатором часового пояса.
    Если не указан, будет использован часовой пояс по умолчанию.

    :return: Текущая дата и время без миллисекунд.
    """
    current_dt = datetime.now(pytz.timezone(timezone))
    current_dt = current_dt.replace(microsecond=0)
    return current_dt


def datetime_to_json(dt: datetime) -> str:
    """
    Преобразует объект даты и времени в строку в формате JSON.

    :param dt: Объект даты и времени.

    :return: Строка в формате JSON.
    """
    return dt.strftime('%d.%m.%Y %H:%M:%S')
