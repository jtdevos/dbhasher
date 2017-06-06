import pytest
from dbhasher import metadata

CON_STRING = "dbname='ezproxyconfig_jim' user='ezproxy_test' host='localhost'"

def test_build():
    meta = metadata.buld_metadata(CON_STRING)
    assert meta is not None
    assert meta.name == 'ezproxyconfig_jim'


