"""builds metadata for database"""

import psycopg2



class DatabaseMetadata:
    """DB-level Metadata"""

    def __init__(self, name):
        print('in init')
        self.tables = []
        self.name = name

class TableMetadata:
    """table-level metadata"""

    def __init__(self, name):
        self.name = name
        self.columns = []

class Builder:
    """connects to db and builds metadata"""

    def __init__(self, connstring):
        self.connstring = connstring
        with self._connect() as conn:
            self._dsn_params = conn.get_dsn_parameters()

    def _connect(self):
        return psycopg2.connect(self.connstring)

    def _query(self, sql):
        with psycopg2.connect(self.connstring) as con:
            with con.cursor() as cur:
                rows = cur.execute(sql).fetchall()
        return rows

    def build(self):
        with self._connect() as con:
            pass






def buld_metadata(connstring):
    builder = Builder(connstring)

    with psycopg2.connect(connstring) as conn:
        parms = conn.get_dsn_parameters()
        dbmeta = DatabaseMetadata(parms['dbname'])
    return dbmeta

