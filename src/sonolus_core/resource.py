import gzip
import hashlib


def compress(data: bytes) -> bytes:
    return gzip.compress(data, 9)


def hash(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()
