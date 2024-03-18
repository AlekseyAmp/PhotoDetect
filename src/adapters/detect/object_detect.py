from dataclasses import dataclass
from io import BytesIO

from PIL import Image
from ultralytics import YOLO

from src.adapters.detect.settings import settings
from src.application import entities, interfaces


@dataclass
class ObjectDetector(interfaces.IObjectDetector):
    """
    Класс для обнаружения объектов на изображении
    с использованием модели YOLOv8.
    """

    model: YOLO = None

    def __post_init__(self) -> None:
        self._load_model()

    def _load_model(self) -> None:
        """
        Загрузка модели YOLOv8 с предварительно обученными весами
        """
        self.model = YOLO(settings.MODEL_PATH)

    def detect_objects_on_image(
        self,
        image_data: bytes
    ) -> list[entities.DetectedObject]:
        """
        Обнаружение объектов на изображении.

        :param image_data: Байтовое представление входного изображения.
        :return: Список объектов, обнаруженных на изображении.
        """

        # Открываем изображение из байтового представления
        image = Image.open(BytesIO(image_data))

        # Предсказываем объекты на изображении с помощью загруженной модели
        results = self.model.predict(image)
        result = results[0]

        detected_objects = []

        # Проходим по каждому обнаруженному объекту и его ограничивающей рамке
        for box in result.boxes:
            # Извлекаем координаты ограничивающей рамки
            x1, y1, x2, y2 = [
                round(coord)
                for coord in box.xyxy[0].tolist()
            ]

            # Извлекаем тип объекта
            class_id = box.cls[0].item()
            object_label = result.names[class_id]

            # Добавляем DetectedObject в список detected_objects
            detected_objects.append(
                entities.DetectedObject(
                    label=object_label,
                    bounding_box=entities.BoundingBox(
                        x1=x1,
                        x2=x2,
                        y1=y1,
                        y2=y2
                    )
                )
            )

        return detected_objects
