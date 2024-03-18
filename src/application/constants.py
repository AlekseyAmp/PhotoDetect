class TimeConstants:
    """
    Константы времени.
    """

    # Таймзона по умолчанию
    DEFAULT_TIMEZONE: str = "Asia/Yekaterinburg"


class FileConstants:
    """
    Константы для обработки файлов.
    """

    # Допустимые форматы файла
    ALLOWED_FILE_FORMATS: set[str] = {'jpeg', 'jpg', 'png'}

    # Максимальный допустимый размер файла
    MAX_IMAGE_SIZE: int = 10
