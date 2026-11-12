from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel # JS 카멜 -> Snake로 변경해서 받기
from datetime import datetime
from app.enums.s3_enum import S3Folder

class ImageUploadResponseDTO(BaseModel):
    original_key: str | None = None
    thumb_key: str | None = None
    original_url: str | None = None
    thumb_url: str | None = None

    # ORM -> Pydantic
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, from_attributes=True)

class FileUploadResponseDTO(BaseModel):
    file_key: str | None = None
    file_url: str | None = None
    original_filename: str | None = None

    # ORM -> Pydantic
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, from_attributes=True)