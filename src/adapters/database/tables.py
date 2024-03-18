from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    MetaData,
    String,
    Table,
)
from sqlalchemy.dialects.postgresql import JSONB

from src.application.constants import TimeConstants
from src.application.utils import get_current_dt

metadata = MetaData()

images = Table(
    'images',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True,
        comment='Уникальный идентификатор изображения',
    ),
    Column(
        'dt',
        DateTime,
        nullable=False,
        default=get_current_dt(TimeConstants.DEFAULT_TIMEZONE),
        comment='Дата загрузки изображения',
    ),
    Column(
        'image_data',
        LargeBinary,
        nullable=False,
        comment='Байтовое представление изображения',
    ),
    comment='Таблица, содержащая информацию об изображениях',
)

detected_objects = Table(
    'detected_objects',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True,
        comment='Уникальный идентификатор обнаруженного объекта',
    ),
    Column(
        'image_id',
        Integer,
        ForeignKey(
            'images.id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        nullable=False,
        comment='Идентификатор изображения',
    ),
    Column(
        'label',
        String,
        nullable=False,
        comment='Метка объекта на изображении',
    ),
    Column(
        'bounding_box',
        JSONB,
        nullable=False,
        comment='Информация о прямоугольнике объекта на изображении',
    ),
    comment=(
        'Таблица, '
        'содержащая информацию об обнаруженных объектах на изображении'
    ),
)
