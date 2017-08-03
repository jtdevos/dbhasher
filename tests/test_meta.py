import pytest
from pytest import fixture
from dbhasher import metadata
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import os

CON_STRING = "dbname='dbhash_world' user='ezproxy_test' host='localhost'"

DB_TEMPLATE_NAME = 'world_template'
DB_NAME = 'dbhash_world'
DB_USER = 'dbhashuser'

# con = connect(dbname='postgres', user='nishant', host='localhost', password='everything')

@fixture
def freshdb():
    conn = psycopg2.connect(dbname='postgres', user='dbhashuser',
                            host='localhost', password='')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    print('about to create database')
    cur.execute("create database dbhash_world owner dbhashuser template world_template ")
    yield True

    print('about to drop database')
    cur.execute("drop database dbhash_world")
    conn.close()




def test_build(freshdb):
    meta = metadata.build_metadata(CON_STRING)
    assert meta is not None
    assert meta.name == DB_NAME
    assert len(meta.tables) > 0



