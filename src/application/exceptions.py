from dataclasses import dataclass

from fastapi import HTTPException

from src.application.constants import FileConstants


# Ошибки, связанные с файлами
@dataclass
class FileLargeException(HTTPException):
    status_code: int = 403
    detail: str = (
        "Превышен максимальный размер файла. "
        f"Максимальный размер файла - {FileConstants.MAX_IMAGE_SIZE}"
    )


@dataclass
class InvalidFileFormatException(HTTPException):
    status_code: int = 422
    detail: str = (
        "Формат файла не допустим. "
        f"Допустимые форматы: {FileConstants.ALLOWED_FILE_FORMATS}"
    )
