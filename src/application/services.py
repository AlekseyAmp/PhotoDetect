from dataclasses import asdict, dataclass

from src.adapters.api.schemas import ImageResponse
from src.application import interfaces


@dataclass
class ImageService:
    """
    Сервис для работы с изображениям.
    """

    object_detector: interfaces.IObjectDetector

    async def process_image(
        self,
        contents: bytes
    ) -> ImageResponse:
        """
        Обрабатывает изображение.

        :param contents: Байтовое представление входного изображения.

        :return: ImageResponse.
        """

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
