from dataclasses import asdict, dataclass

import sqlalchemy as sqla
from sqlalchemy.orm import Session

from src.adapters.database import tables
from src.application import entities, interfaces


@dataclass
class SABaseRepository:
    """
    Базовый класс репозитория SQLAlchemy.

    :param session: Сессия SQLAlchemy для взаимодействия с базой данных.
    """
    session: Session


@dataclass
class ImageRepository(SABaseRepository, interfaces.IImageRepository):
    """
    Репозиторий для работы с данными об изображении
    и обнаруженными на них объектами.
    """

    def save_image(self, image_data: bytes) -> entities.SaveImageReturn:
        """
        Сохраняет данные об изображении.

        :param image_data: Байтовое представление входного изображения.

        :return: Идентификатор сохраненного изображения.
        """

        table: sqla.Table = tables.images

        query: sqla.Insert = (
            sqla.insert(
                table
            )
            .values(
                image_data=image_data
            )
            .returning(
                table.c.id,
                table.c.dt
            )
        )

        image = self.session.execute(query).mappings().one()
        self.session.commit()
        return entities.SaveImageReturn(**image)

    def save_detected_objects(
        self,
        image_id: int,
        detected_objects: list[entities.DetectedObject]
    ) -> None:
        """
        Сохраняет слоем данные об обнаруженных объектах на изображении.

        :param image_id: Идентификатор изображения.

        :param detected_objects: Информация об обнаружнных
        объектах на изображении.

        :return: None
        """

        table: sqla.Table = tables.detected_objects

        values = [
            {
                'image_id': image_id,
                'label': obj.label,
                'bounding_box': asdict(obj.bounding_box)
            }
            for obj in detected_objects
        ]

        query: sqla.Insert = (
            sqla.insert(
                table
            ).values(
                values
            )
        )

        self.session.execute(query)
        self.session.commit()
