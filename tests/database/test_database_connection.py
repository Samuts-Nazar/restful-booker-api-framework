def test_database_connection(db_cursor):
    db_cursor.execute("SELECT 1")
    result = db_cursor.fetchone()
    assert result[0] == 1