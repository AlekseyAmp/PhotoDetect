import imghdr
from dataclasses import asdict, dataclass

from src.adapters.api.schemas import ImageResponse
from src.application import exceptions, interfaces
from src.application.constants import FileConstants


@dataclass
class ImageService:
    """
    Сервис для работы с изображениям.
    """

    object_detector: interfaces.IObjectDetector

    def _check_file_size(self, contents: bytes) -> None:
        """
        Проверяет размер файла.

        :param contents: Байтовое представление входного файла.

        :raises: FileLargeException, если размер файла превышает 10 МБ.
        """

        # Получаем размер файла в байтах
        image_size_bytes = len(contents)

        # Проверяем, превышает ли размер файла 10 МБ
        if image_size_bytes > FileConstants.MAX_IMAGE_SIZE * 1024 * 1024:
            raise exceptions.FileLargeException

    def _check_file_format(self, contents: bytes) -> None:
        """
        Проверяет формат файла.

        :param contents: Байтовое представление входного файла.

        :raises: InvalidFileFormatException,
        если формат файла не допустим.
        """

        # Получаем формат файла
        file_format = imghdr.what(None, h=contents)

        # Проверяем, является ли формат файла допустимым
        if file_format not in FileConstants.ALLOWED_FILE_FORMATS:
            raise exceptions.InvalidFileFormatException

    async def process_image(
        self,
        contents: bytes
    ) -> ImageResponse:
        """
        Обрабатывает изображение.

        :param contents: Байтовое представление входного файла.

        :return: ImageResponse.
        """

        # Проверяем формат и размер входного файла.
        self._check_file_format(contents)
        self._check_file_size(contents)

        # Получаем информацию об обнаружнных объектах на фотографии
        detected_objects_data = self.object_detector.detect_objects_on_image(
            contents
        )
        detected_objects = [
            asdict(detect_object)
            for detect_object in detected_objects_data
        ]

        return ImageResponse(
            detected_objects=detected_objects
        )
