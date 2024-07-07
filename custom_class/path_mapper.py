from urllib.parse import urljoin


class PathMapper:
    _HTTP_BASE:str
    _path:str

    def __init__(self, _path:str) -> None:
        self._path = _path
        self._HTTP_BASE = 'https://exmaple.com/'

    def to_url(self, image:str):
        return urljoin(self._HTTP_BASE, (self._path + image))