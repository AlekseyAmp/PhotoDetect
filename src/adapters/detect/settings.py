from pydantic import BaseModel


class Settings(BaseModel):
    MODEL_PATH: str = "src/adapters/detect/yolov8m.pt"


settings = Settings()
