from typing import Any

from pydantic import BaseModel


class ImageResponse(BaseModel):
    id: int
    dt: str
    detected_objects: list[dict[str, Any]] | None
