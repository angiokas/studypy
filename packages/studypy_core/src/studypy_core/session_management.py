from sqlalchemy.orm import sessionmaker

from studypy.configs import DatabaseEngineFactory

_engine = None
_session = None


def get_engine():
    global _engine

    if _engine is None:
        print("No engine detected, creating it now...")
        factory = DatabaseEngineFactory()
        _engine = factory.create_engine()
    print(_engine.url)
    return _engine


def get_session():
    global _session

    if _session is None:
        print("No sessionmaker yet, creating it now...")
        _session = sessionmaker(bind=get_engine(), expire_on_commit=False)
    return _session()
