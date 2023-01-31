from app.dao.models.movie import Movie
from app.config import Config


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, filters):
        status = filters.get("status")
        page = filters.get("page")

        if status == "new" and page is not None:
            result = self.session.query(Movie).order_by(Movie.year.desc()).paginate(page=int(page),
                                                                                    per_page=Config.RECORDS_PER_PAGE,
                                                                                    error_out=False).items
            return result

        elif status == "new":
            return self.session.query(Movie).order_by(Movie.year.desc()).all()

        elif page is not None:
            result = self.session.query(Movie).paginate(page=int(page), per_page=Config.RECORDS_PER_PAGE,
                                                        error_out=False).items
            return result

        return self.session.query(Movie).all()
