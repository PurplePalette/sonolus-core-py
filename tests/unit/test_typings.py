from dataclasses import asdict
import src.sonolus_core.typings as typings

LATEST_VERSION = "0.5.9"


class TestBackgroundTypings(object):
    def test_background_from_dict(self) -> None:
        json = {
            "name": "darkblue",
            "version": 3,
            "title": "Dark Blue",
            "subtitle": "Sonolus",
            "author": "Sonolus",
            "thumbnail": {
                "type": "BackgroundThumbnail",
                "hash": "c9360af9be48adc37758060cdb3901e12ab0be3e",
                "url": "/repository/BackgroundThumbnail/c",
            },
            "data": {
                "type": "BackgroundData",
                "hash": "92369babe7837afa849337ecd928832c3b94bd8a",
                "url": "/repository/BackgroundData/1",
            },
            "image": {
                "type": "BackgroundImage",
                "hash": "17bb17c86fe270da637693ee36e26c40e947bd12",
                "url": "/repository/BackgroundImage/1",
            },
            "configuration": {
                "type": "BackgroundConfiguration",
                "hash": "d4367d5b719299e702ca26a2923ce5ef3235c1c7",
                "url": "/repository/BackgroundConfiguration/d",
            },
        }
        bg = typings.BackgroundItem(**json)
        assert bg.name == "darkblue"

    def test_background_to_dict(self) -> None:
        bg = typings.BackgroundItem(
            name="darkblue",
            version=3,
            title="Dark Blue",
            subtitle="Sonolus",
            author="Sonolus",
            thumbnail=typings.SRL(
                type="BackgroundThumbnail",
                hash="c9360af9be48adc37758060cdb3901e12ab0be3e",
                url="/repository/BackgroundThumbnail/c",
            ),
            data=typings.SRL(
                type="BackgroundData",
                hash="92369babe7837afa849337ecd928832c3b94bd8a",
                url="/repository/BackgroundData/1",
            ),
            image=typings.SRL(
                type="BackgroundImage",
                hash="17bb17c86fe270da637693ee36e26c40e947bd12",
                url="/repository/BackgroundImage/1",
            ),
            configuration=typings.SRL(
                type="BackgroundConfiguration",
                hash="d4367d5b719299e702ca26a2923ce5ef3235c1c7",
                url="/repository/BackgroundConfiguration/d",
            ),
        )
        resp = asdict(bg)
        example = {
            "name": "darkblue",
            "version": 3,
            "title": "Dark Blue",
            "subtitle": "Sonolus",
            "author": "Sonolus",
            "thumbnail": {
                "type": "BackgroundThumbnail",
                "hash": "c9360af9be48adc37758060cdb3901e12ab0be3e",
                "url": "/repository/BackgroundThumbnail/c",
            },
            "data": {
                "type": "BackgroundData",
                "hash": "92369babe7837afa849337ecd928832c3b94bd8a",
                "url": "/repository/BackgroundData/1",
            },
            "image": {
                "type": "BackgroundImage",
                "hash": "17bb17c86fe270da637693ee36e26c40e947bd12",
                "url": "/repository/BackgroundImage/1",
            },
            "configuration": {
                "type": "BackgroundConfiguration",
                "hash": "d4367d5b719299e702ca26a2923ce5ef3235c1c7",
                "url": "/repository/BackgroundConfiguration/d",
            },
        }
        assert resp == example
