from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session

from settings import DatabaseSettings

class weatherDBConn():
    _db_url = URL.create(
        "mysql+pymysql",
        username=DatabaseSettings.user,
        password=DatabaseSettings.password,
        host=DatabaseSettings.url,
        port=DatabaseSettings.port,
        database=DatabaseSettings.dbname
    )
    
    _engine = create_engine(
        _db_url
    )
    
    def __enter__(self):
        print(self._engine.url.render_as_string(hide_password=False))
        self.session = Session(self._engine)
        return self.session
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
