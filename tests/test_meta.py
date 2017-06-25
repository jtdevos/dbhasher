import pytest
from pytest import fixture
from dbhasher import metadata
import os

CON_STRING = "dbname='dbhash_testdb' user='ezproxy_test' host='localhost'"

DB_TEMPLATE_NAME = 'dbhash_world_template'
DB_NAME = 'dbhash_world'

# @fixture
# def freshdb():
#     conn = psycopg2.connect(CON_STRING)
#     cur = conn.cursor()
#     cur.execute("select * from ezconfig_ezproxy_stanza ")
#     rows = cur.fetchall()


def test_build():
    meta = metadata.buld_metadata(CON_STRING)
    assert meta is not None
    assert meta.name == 'ezproxyconfig_jim'

    assert len(meta.tables) > 0 



