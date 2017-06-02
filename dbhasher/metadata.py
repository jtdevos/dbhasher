"""builds metadata for database"""



class DatabaseMetadata:
    """DB-level Metadata"""

    def __init__(self, name):
        print('in init')
        self.tables = []
        self.name = name

class TableMetadata:
    pass



class Builder:

    def __init__(self, connstring):
        pass
        