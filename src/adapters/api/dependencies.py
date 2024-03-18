from fastapi import Depends

from src.adapters.detect import ObjectDetector
from src.application.services import ImageService


def get_object_detector() -> ObjectDetector:
    return ObjectDetector()


def get_image_service(
    object_detector: ObjectDetector = Depends(get_object_detector)
) -> ImageService:
    return ImageService(
        object_detector
    )
