import pytest
from dbhasher import metadata

@pytest.fixture
def builder():
    return metadata.Builder('hello')

def test_build(builder):
    b = builder
    assert b is not None


