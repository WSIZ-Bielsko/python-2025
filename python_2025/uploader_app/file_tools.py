import json
import os
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


UPLOAD_DIR = "uploads"


def get_meta_by_file_id(file_id: UUID, upload_dir=UPLOAD_DIR) -> FileMeta:
    meta_file_name = str(file_id) + '.meta'
    meta_file_path = os.path.join(UPLOAD_DIR, meta_file_name)

    with open(meta_file_path, 'r') as f:
        meta = json.load(f)
        mf = FileMeta.model_validate(meta)
        return mf


def test_load_meta():
    meta = get_meta_by_file_id(UUID('f787896c-bcbe-411c-a909-68936c31bcdb'))
    print(meta)


def get_files_by_name(files: list[FileMeta], file_name: str) -> list[FileMeta]:
    """

    :param file_name:
    :param files:
    :return: files with original file name =  file_name
    """
    return [f for f in files if f.original_file_name == file_name]


def get_all_files(upload_dir=UPLOAD_DIR) -> list[FileMeta]:
    files = [f for f in os.listdir(upload_dir) if f.endswith('.meta')]
    for f in files:
        print(f)
    # todo: now convert all these to a list[FIleMeta], sort by original_file_name, and return...

def test_getting_all_files():
    get_all_files()


if __name__ == '__main__':
    x = FileMeta(file_id=uuid4(), original_file_name='test.txt', user_id=1, category_id=2, size_mb=1000,
                 upload_date=datetime.now())
    y = FileMeta(file_id=uuid4(), original_file_name='test2.txt', user_id=1, category_id=3, size_mb=1000,
                 upload_date=datetime.now())
    z = FileMeta(file_id=uuid4(), original_file_name='test2.txt', user_id=2, category_id=3, size_mb=1000,
                 upload_date=datetime.now())

    for f in get_files_by_name([x, y, z], 'test2.txt'):
        print(f)
