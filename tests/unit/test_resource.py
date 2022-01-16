from src.sonolus_core import compress, hash


class TestResource:
    def test_hash_match(self) -> None:
        text = "sonolus"
        hashed_text = hash(bytes(text, "utf-8"))
        assert hashed_text == "f0260ceecb08ad5060fc664b24a9f18b6698f541"

    def test_compress_match(self) -> None:
        text = "sonolus_core"
        compressed_bytes = compress(bytes(text, "utf-8"), 1642333227.8384304)
        hashed_text = hash(compressed_bytes)
        assert hashed_text == "a5ffba2b9ab4163b60d4a9fdc57098ce233d961b"
