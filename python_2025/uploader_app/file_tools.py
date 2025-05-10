import json
import os
from datetime import datetime, timedelta
from uuid import UUID, uuid4

from pydantic import BaseModel


class FileMeta(BaseModel):
    file_id: UUID
    original_file_name: str
    user_id: int
    category_id: int
    size_mb: int
    upload_date: datetime
    is_frozen: bool = False


UPLOAD_DIR = "uploads"


def validate_file_name(file_name) -> str:
    """
    Validate `file_name` do discourage path traversal attacks.

    :param file_name:
    :return:
    """

    # Normalize the path to resolve any '..' or '.' references
    normalized = os.path.normpath(file_name).replace('\\', '/')

    # Check if the normalized path starts with '..' or contains '/'
    if normalized.startswith('..') or '/' in normalized or '\\' in normalized:
        raise ValueError("Invalid file name: Path traversal detected")

    # Ensure the file name is a simple basename (no directory components)
    if os.path.basename(file_name) != file_name:
        raise ValueError("Invalid file name: Must be a simple file name")

    return file_name


def get_meta_by_file_id(file_id: UUID, upload_dir=UPLOAD_DIR) -> FileMeta:
    meta_file_name = str(file_id) + '.meta'
    meta_file_path = os.path.join(upload_dir, meta_file_name)

    with open(meta_file_path, 'r') as f:
        meta = json.load(f)
        mf = FileMeta.model_validate(meta)
        return mf


def test_load_meta():
    meta = get_meta_by_file_id(UUID('f787896c-bcbe-411c-a909-68936c31bcdb'))
    print(meta)


def is_deletable(file: FileMeta) -> bool:
    """
    Check if file.is_frozen is true; if not --> return true (all not-frozen files can be deleted)
    if `true` (file is frozen) -- check if it was uploaded in the last 30 seconds; if yes --> return true (recent uploads
    can be deleted) else return false.
    :param file:
    :return:
    """


def test_deletable_frozen_recent_can_be_deleted():
    now = datetime.now() - timedelta(seconds=5)
    meta = FileMeta(file_id=uuid4(), original_file_name='x.pdf', user_id=1, category_id=1, size_mb=1024,
                    upload_date=now, is_frozen=True)
    assert is_deletable(meta) is True


def test_deletable_frozen_old_cannot_be_deleted():
    now = datetime.now() - timedelta(seconds=55)
    meta = FileMeta(file_id=uuid4(), original_file_name='x.pdf', user_id=1, category_id=1, size_mb=1024,
                    upload_date=now, is_frozen=True)
    assert is_deletable(meta) is False


def test_deletable_nonfrozen_old_can_be_deleted():
    now = datetime.now() - timedelta(seconds=55)
    meta = FileMeta(file_id=uuid4(), original_file_name='x.pdf', user_id=1, category_id=1, size_mb=1024,
                    upload_date=now, is_frozen=False)
    assert is_deletable(meta) is True


def get_files_by_name(files: list[FileMeta], file_name: str) -> list[FileMeta]:
    """

    :param file_name:
    :param files:
    :return: files with original file name =  file_name
    """
    return [f for f in files if f.original_file_name == file_name]


def get_all_files(upload_dir=UPLOAD_DIR) -> list[FileMeta]:
    files = [f for f in os.listdir(upload_dir) if f.endswith('.meta')]
    response = []
    for f in files:
        print(f'decoding {f}')
        with open(os.path.join(upload_dir, f), 'rb') as ff:
            meta = json.load(ff)
            mf = FileMeta.model_validate(meta)
            response.append(mf)

    response.sort(key=lambda x: x.original_file_name)
    return response


def test_getting_all_files():
    res = get_all_files()
    print(res)


if __name__ == '__main__':
    x = FileMeta(file_id=uuid4(), original_file_name='test.txt', user_id=1, category_id=2, size_mb=1000,
                 upload_date=datetime.now())
    y = FileMeta(file_id=uuid4(), original_file_name='test2.txt', user_id=1, category_id=3, size_mb=1000,
                 upload_date=datetime.now())
    z = FileMeta(file_id=uuid4(), original_file_name='test2.txt', user_id=2, category_id=3, size_mb=1000,
                 upload_date=datetime.now())

    for f in get_files_by_name([x, y, z], 'test2.txt'):
        print(f)
