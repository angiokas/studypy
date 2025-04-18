from functools import wraps

from .models import Base, Difficulty, Flashcard, Studyset
from .session_management import get_session

"""class BaseRepository:

    
    def __init__(self, **kwargs):
        columns = {c.name for c in self.__table__.columns}
        for key in kwargs:
            if key in columns:
                setattr(self, key, kwargs[key])
        kwargs.pop('id', None)
    
    @property
    def __table__(self)
        raise NotImplementedError

    def session_method(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session = get_session()
            try:
                return func(*args, session=session, **kwargs)
            except Exception as e:
                print(f"Error occurred: {e}")
                session.rollback()
            finally:
                session.close()

        return wrapper

    def create(self, **kwargs):
        session = get_session()
        try:
            obj = self.model(**kwargs)
            session.add(obj)
            session.commit()
            print(f"{self.model} added to the database!")
        except Exception as e:
            print(f"Error occured: {e}")
            session.rollback()
        finally:
            session.close()
        
    
    def get_all(self):
        session = get_session()
    
        try:
            objects = session.query(self.model).all()
            if not objects:
                return "There are no flashcards in the database yet."
            
            objects_arr = []
            for object in objects:
                objects_arr.append(objects)
            print(objects_arr)
            return objects_arr

        except Exception as e:
            print(f"Error occurred: {e}")
            session.rollback()
        finally:
            session.close()
"""


def create_flashcard(
    f_question: str,
    f_answer: str,
):
    """Creates a Flashcard object and saves it to the database"""
    session = get_session()

    try:
        flashcard = Flashcard(question=f_question, answer=f_answer)
        session.add(flashcard)
        session.commit()
        print("Flashcard added to database!")

    except Exception as e:
        print(f"Error occured: {e}")
        session.rollback()
    finally:
        session.close()


def create_studyset(name: str):
    """Creates a Flashcard object and saves it to the database"""
    session = get_session()

    try:
        studyset = Studyset(name=name)
        session.add(studyset)
        session.commit()
        print("Studyset added to database!")

    except Exception as e:
        print(f"Error occured: {e}")
        session.rollback()
    finally:
        session.close()


def add_flashcard_to_studyset(flashcard_id: int, studyset_id: int):
    session = get_session()
    flashcard = session.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    studyset = session.query(Studyset).filter(Studyset.id == studyset_id).first()
    if not flashcard:
        raise ValueError(
            f"There is no flashcard with id= {flashcard_id} in the database."
        )
    if not studyset:
        raise ValueError(
            f"There is no studyset with id= {studyset_id} in the database."
        )
    try:
        studyset.flashcards.append(flashcard)
        # print(f"{flashcard_id} flashcard added to {studyset_id} studyset")

    except Exception as e:
        print(f"Error occured: {e}")
        session.rollback()
    finally:
        session.close()


def get_all_flashcards():
    """Returns a list of all Flashcards from the database."""
    session = get_session()

    try:
        flashcards = session.query(Flashcard).all()
        if not flashcards:
            return "There are no flashcards in the database yet."

        flashcards_arr = []
        for flashcard in flashcards:
            flashcards_arr.append(flashcard)
        return flashcards_arr

    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()


def get_all_studysets():
    """Returns a list of all Flashcards from the database."""
    session = get_session()

    try:
        studysets = session.query(Studyset).all()
        if not studysets:
            return "There are no flashcards in the database yet."

        studysets_arr = []
        for studyset in studysets:
            studysets_arr.append(studyset)
        return studysets_arr

    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()
