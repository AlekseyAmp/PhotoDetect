
from abc import ABC, abstractmethod

from src.application import entities


class IImageRepository(ABC):

    @abstractmethod
    def save_image(self, image_data: bytes) -> entities.SaveImageReturn:
        pass

    @abstractmethod
    def save_detected_objects(
        self,
        image_id: int,
        detected_objects: list[entities.DetectedObject]
    ) -> None:
        pass


class IObjectDetector(ABC):

    @abstractmethod
    def detect_objects_on_image(
        self,
        image_data: bytes
    ) -> list[entities.DetectedObject]:
        pass
