import imghdr
from dataclasses import asdict, dataclass

from src.adapters.api.schemas import ImageResponse
from src.application import exceptions, interfaces
from src.application.constants import FileConstants
from src.application.utils import datetime_to_json


@dataclass
class ImageService:
    """
    Сервис для работы с изображениям.
    """

    image_repo: interfaces.IImageRepository
    object_detector: interfaces.IObjectDetector

    def _check_file_size(self, file_data: bytes) -> None:
        """
        Проверяет размер файла.

        :param file_data: Байтовое представление входного файла.

        :raises: FileLargeException, если размер файла превышает 10 МБ.
        """

        # Получаем размер файла в байтах
        image_size_bytes = len(file_data)

        # Проверяем, превышает ли размер файла 10 МБ
        if image_size_bytes > FileConstants.MAX_IMAGE_SIZE * 1024 * 1024:
            raise exceptions.FileLargeException

    def _check_file_format(self, file_data: bytes) -> None:
        """
        Проверяет формат файла.

        :param file_data: Байтовое представление входного файла.

        :raises: InvalidFileFormatException,
        если формат файла не допустим.
        """

        # Получаем формат файла
        file_format = imghdr.what(None, h=file_data)

        # Проверяем, является ли формат файла допустимым
        if file_format not in FileConstants.ALLOWED_FILE_FORMATS:
            raise exceptions.InvalidFileFormatException

    async def process_image(
        self,
        file_data: bytes
    ) -> ImageResponse:
        """
        Обрабатывает изображение, находит объекты на нём.

        :param file_data: Байтовое представление входного файла.

        :return: ImageResponse.
        """

        # Проверяем формат и размер входного файла.
        self._check_file_format(file_data)
        self._check_file_size(file_data)

        # Сохраняем изображение в БД
        image = self.image_repo.save_image(file_data)

        # Получаем информацию об обнаружнных объектах на изображении
        detected_objects_data = self.object_detector.detect_objects_on_image(
            file_data
        )

        # Если нет информации, то возвращаем:
        if not detected_objects_data:
            return ImageResponse(
                id=image.id,
                dt=datetime_to_json(image.dt),
                detected_objects=None
            )

        detected_objects = [
            asdict(detect_object)
            for detect_object in detected_objects_data
        ]

        # Сохраняем информацию об обнаружнных объектах на изображении в БД
        self.image_repo.save_detected_objects(image.id, detected_objects_data)

        return ImageResponse(
            id=image.id,
            dt=datetime_to_json(image.dt),
            detected_objects=detected_objects
        )
