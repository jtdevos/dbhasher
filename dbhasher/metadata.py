"""builds metadata for database"""

import psycopg2



class DatabaseMetadata:
    """DB-level Metadata"""

    def __init__(self, name):
        print('in init')
        self.tables = []
        self.name = name

class TableMetadata:
    pass



def buld_metadata(connstring):
    with psycopg2.connect(connstring) as conn:
        parms = conn.get_dsn_parameters()
        dbmeta = DatabaseMetadata(parms['dbname'])
    return dbmeta