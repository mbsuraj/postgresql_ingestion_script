class Loader:

    def __init__(self, curser=None, table=None, tablename=None, format='csv'):

        assert curser is not None, "No cursor created"
        assert table is not None, "Table variable needed"
        assert tablename is not None, "Table name is needed"
        self._curser = curser
        self._table = table
        self._tablename = tablename
        self._format = format


    def load(self):
        """
        load data into postgresql
        :return:
        """
        if self._format == 'csv':
            self._curser.copy_expert(f"""COPY {self._tablename} FROM STDIN WITH (FORMAT CSV)""", self._table)
        elif self._format == 'xlsx':
            raise Exception("Capability not yet ready. Coming soon.")
        else:
            pass
        return self._curser