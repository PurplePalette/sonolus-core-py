import gzip
import hashlib


def compress(data: bytes, mtime=None) -> bytes:
    return gzip.compress(data, 9, mtime=mtime)


def hash(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()
