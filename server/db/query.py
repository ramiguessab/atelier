from pyodbc import connect, Row


class Query:
    connection = connect(
        "DRIVER={PostgreSQL};SERVER=localhost;DATABASE=postgres;UID=postgres;PWD=admin;BoolsAsChar=0"
    )

    def __init__(self, query: str) -> None:
        self.cursor = Query.connection.cursor()
        self.result = self.cursor.execute(query)

    def commit(self):
        self.result.commit()

    def getAll(self):
        return self.__parse(self.result.fetchall())

    def __parse(self, rows: list[Row]):
        parsed_rows = list()
        if len(rows) > 0:
            columns = [column[0] for column in rows[0].cursor_description]

            for row in rows:
                parsed_rows.append(dict(zip(columns, row)))
        return parsed_rows
