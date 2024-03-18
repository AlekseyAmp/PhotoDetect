from dataclasses import dataclass
from datetime import datetime


@dataclass
class SaveImageReturn:
    id: int
    dt: datetime


@dataclass
class BoundingBox:
    x1: int
    y1: int
    x2: int
    y2: int


@dataclass
class DetectedObject:
    label: str
    bounding_box: BoundingBox
