from app.dao.models.genre import Genre
from app.config import Config


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self, filters):
        page = filters.get("page")

        if page is not None:
            result = self.session.query(Genre).paginate(int(page), Config.RECORDS_PER_PAGE,
                                                        max_per_page=Config.MAX_PAGE, error_out=False).items
            return result

        return self.session.query(Genre).all()
