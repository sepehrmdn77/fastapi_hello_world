from fastapi.testclient import TestClient

from core.database import Base, create_engine, sessionmaker, get_db

from sqlalchemy import StaticPool

from main import app

from h_w.models import HelloModel

import pytest


POSTGRES_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    POSTGRES_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  module
@pytest.fixture(scope="module")
def db_session():
    db = TestSessionLocal()

    try:
        yield db
    finally:
        db.close()


#  module
@pytest.fixture(scope="module", autouse=True)
def override_dependencies(db_session):

    app.dependency_overrides[get_db] = lambda: db_session
    yield
    app.dependency_overrides.pop(get_db,None)


#  session
@pytest.fixture(scope="session", autouse=True)
def tearup_and_down_db():
    '''for tests in local env export env variables in terminal:
        export POSTGRES_DATABASE_URL="sqlite:///:memory:"
        export JWT_SECRET_KEY="test"'''
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture(autouse=True)
def setup_test_data(db_session):
    db_session.add(HelloModel(text="Hello Test World"))
    db_session.commit()
