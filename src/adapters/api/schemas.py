from typing import Any

from pydantic import BaseModel


class ImageResponse(BaseModel):
    detected_objects: list[dict[str, Any]]
