import sqlite3 as lite

"""Conectar com o banco de dados"""
connection = lite.connect("database.db")


"""Inserir informações no banco de dados"""


def Insert(data):
    with connection:
        cursor = connection.cursor()
        query = "INSERT INTO clientes (name, cpf, hosted, type_room, days, value, status) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(query, data)


"""Buscando informações no banco"""


def View(info, infoType):
    lista = []
    information = ["Id", 'Nome', 'CPF', 'N° de pessoas',
                   'Tipo de quarto', 'Número de dias', 'Valor', 'Status']
    search = [info]
    with connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM clientes WHERE {infoType}=?"
        cursor.execute(query, search)
        info = cursor.fetchall()

        for i in info:
            lista.append(i)

        for v in lista:
            seeInfos = {information[i]: v[i] for i in range(len(information))}
            seeInfos = str(seeInfos).strip('{}')
            print(f"\n {seeInfos}")
            print(
                "-----------------------------------------------------------------------------------------------------------------------------------------")

        return


""" Buscar por CPF e STATUS"""


def ViewStatusCPF(a, b):
    lista = []

    information = ["Id", 'Nome', 'CPF', 'N° de pessoas',
                   'Tipo de quarto', 'Número de dias', 'Valor', 'Status']
    search = []
    search.append(a)
    search.append(b)
    with connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM clientes WHERE cpf=? AND status=?"
        cursor.execute(query, search)
        info = cursor.fetchall()

        if(info != []):
            for i in info:
                lista.append(i)

            for v in lista:
                seeInfos = {information[i]: v[i]
                            for i in range(len(information))}
                seeInfos = str(seeInfos).strip('{}')
                print(f"\n {seeInfos}")
                print(
                    "-----------------------------------------------------------------------------------------------------------------------------------------")
        else:
            return "invalid"


""" Atualização de informações """


def Upadated(infos):
    lista = infos
    with connection:
        cursor = connection.cursor()
        query = "UPDATE clientes SET hosted=?, type_room=?, days=?, value=?, status=? WHERE id=?"
        cursor.execute(query, lista)


""" Atualização de Status """


def UpadatedStatus(status):
    lista = status
    with connection:
        cursor = connection.cursor()
        query = "UPDATE clientes SET status=? WHERE id=?"
        cursor.execute(query, lista)


""" Verificação e soma de todos os valores """


def TotalValue():
    lista = []
    tvalue = 0
    with connection:
        cursor = connection.cursor()
        query = "SELECT value FROM clientes"
        cursor.execute(query)
        info = cursor.fetchall()

        for i in info:
            lista.append(i)
        for v in lista:
            tvalue += v[0]
        return print(f"Valor Total: R${tvalue}")
