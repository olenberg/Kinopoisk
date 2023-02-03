from app.dao.models.director import Director
from app.config import Config


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self, filters):
        page = filters.get("page")

        if page is not None:
            result = self.session.query(Director).paginate(page=int(page), per_page=Config.RECORDS_PER_PAGE,
                                                           error_out=False).items
            return result

        return self.session.query(Director).all()
