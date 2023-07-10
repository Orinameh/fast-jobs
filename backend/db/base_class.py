from typing import Any

from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __table_args__ = {"extend_existing": True}


# The below command to create a database and user with the necessary permissions.
# sudo -u postgres psql

# \l  # means show all databases

# CREATE DATABASE dbName;
# CREATE USER username WITH ENCRYPTED PASSWORD 'password';
# GRANT ALL PRIVILEGES ON DATABASE dbName TO username;

# \c dbname : to connect to a database
# \dt : to see tables in the database
