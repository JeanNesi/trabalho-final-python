import sqlite3 as lite


"""Conectar com o banco de dados"""
connection = lite.connect("database.db")


"""Cria Tabela no banco de dados"""
with connection:
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, cpf NUMBER, hosted NUMBER, type_room TEXT, days NUMBER, value NUMBER, status TEXT)")
