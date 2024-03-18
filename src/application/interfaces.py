
from abc import ABC, abstractmethod

from src.application import entities


class IObjectDetector(ABC):

    @abstractmethod
    def detect_objects_on_image(
        self,
        contents: bytes
    ) -> list[entities.DetectedObject]:
        pass
