from fastapi import APIRouter, Depends, File, UploadFile

from src.adapters.api.dependencies import get_image_service
from src.adapters.api.schemas import ImageResponse
from src.application.services import ImageService

router = APIRouter()


@router.post(path="/detect", response_model=ImageResponse)
async def upload_and_detect_objects_on_image(
    image: UploadFile = File(...),
    image_service: ImageService = Depends(
        get_image_service
    )
) -> ImageResponse:
    contents = await image.read()

    return await image_service.process_image(contents)
