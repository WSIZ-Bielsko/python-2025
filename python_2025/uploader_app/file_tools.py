from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel


class FileMeta(BaseModel):
    file_id: UUID
    original_file_name: str
    user_id: int
    category_id: int
    size_mb: int
    upload_date: datetime


if __name__ == '__main__':
    x = FileMeta(file_id=uuid4(), original_file_name='test.txt', user_id=1, category_id=2, size_mb=1000,
                 upload_date=datetime.now())
    y = FileMeta(file_id=uuid4(), original_file_name='test2.txt', user_id=1, category_id=3, size_mb=1000,
                 upload_date=datetime.now())
    z = FileMeta(file_id=uuid4(), original_file_name='test2.txt', user_id=2, category_id=3, size_mb=1000,
                 upload_date=datetime.now())

    for f in [x,y,z]:
        print(f)