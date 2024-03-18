from sqlalchemy.orm import Session

from fastapi import Depends

from src.adapters.database.repositories import ImageRepository
from src.adapters.database.sa_session import get_session
from src.adapters.detect import ObjectDetector
from src.application.services import ImageService


def get_image_repo(
    session: Session = Depends(get_session)
) -> ImageRepository:
    return ImageRepository(session)


def get_object_detector() -> ObjectDetector:
    return ObjectDetector()


def get_image_service(
    image_repo: ImageRepository = Depends(get_image_repo),
    object_detector: ObjectDetector = Depends(get_object_detector)
) -> ImageService:
    return ImageService(
        image_repo,
        object_detector
    )
