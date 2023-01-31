from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = GenreDAO

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self, filters):
        return self.dao.get_all(filters)
