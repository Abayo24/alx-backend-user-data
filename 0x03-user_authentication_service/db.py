#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database"""
        new_user: User = User(email=email, hashed_password=hashed_password)

        session = self._session
        session.add(new_user)
        session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by a given key and value pair"""
        try:
            user = self._session.query(User).filter_by(**kwargs).one()  # noqa
            return user
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Locate a user by user_id and update their attributes.
        """
        try:
            # Find the user by user_id
            user = self.find_user_by(id=user_id)

            # Update the user's attributes with the values provided in kwargs
            for key, value in kwargs.items():
                # Check if the user has the attribute to be updated
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"User has no attribute '{key}'")

            # Commit the changes to the database
            self._session.commit()

        except NoResultFound:
            print(f"No user found with id: {user_id}")
        except InvalidRequestError:
            print("Invalid request for user update")
        except Exception as e:
            print(f"An error occurred: {e}")
            self._session.rollback()
