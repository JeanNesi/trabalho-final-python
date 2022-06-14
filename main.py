import os
import time
from view import *

"""Função Menu"""


def menu():
    os.system('cls')
    print("1 - Cadastrar uma reserva. ")
    print("2 - Entrada do cliente (Check in).")
    print("3 - Saída do cliente (Check out).")
    print("4 - Alterar reserva.")
    print("5 - Relatórios. ")
    print("6 - Sair.")

    global option
    option = int(input("\nDigite a opção desejada: "))

    os.system('cls')

    """Verificação da opção"""
    while(option != 6):

        if(option == 1):
            Register()
            print("Registro concluído com sucesso!")
            time.sleep(3)
            menu()

        if(option == 2):
            CheckIn()
            print("Check In concluído com sucesso!")
            time.sleep(3)
            menu()

        if(option == 3):
            CheckOut()
            print("Check Out concluído com sucesso!")
            time.sleep(3)
            menu()

        if(option == 4):
            Update()
            print("Atualização concluída com sucesso!")
            time.sleep(3)
            menu()

        if(option == 5):
            ReportMenu()

        else:
            print("Opção inválida")
            time.sleep(3)
            menu()


"""Função menu relatório"""


def ReportMenu():
    os.system('cls')
    print("1 - Relatório de todas as reservas com status R. ")
    print("2 - Relatório de todas as reservas com status C.")
    print("3 - Relatório de todas as reservas com status A.")
    print("4 - Relatório de todas as reservas com status F.")
    print("5 - Relatório total recebido (somar valor de todas as reservas finalizadas)")
    print("6 - Relatório de Reserva por pessoa (Pesquisa por CPF)")
    print("7 - Sair. ")

    global optionReport
    optionReport = int(input("\nDigite a opção desejada: "))

    os.system('cls')

    """Verificação da opção relatório"""
    while(optionReport != 7):

        if(optionReport == 1):
            StatusR()
        if(optionReport == 2):
            StatusC()

        if(optionReport == 3):
            StatusA()

        if(optionReport == 4):
            StatusF()

        if(optionReport == 5):
            ReportValue()

        if(optionReport == 6):
            ReportCPF()

        else:
            print("Opção inválida")
            time.sleep(3)
            return
    menu()


"""Função Registrar"""


def Register():
    client = []

    name = Name()
    client.append(name)

    cpf = Cpf()
    client.append(int(cpf))

    hosted = Hosted()
    client.append(int(hosted))

    type_room = TypeRoom()
    client.append(type_room)

    days = Days()
    client.append(int(days))

    value = Value(type_room, int(hosted), int(days))
    client.append(value)

    status = "R"
    client.append(status)

    print(client)
    Insert(client)


def Name():
    """Registrar nome"""
    name = input("Digite o nome da pessoa titular: ")
    os.system('cls')
    while(name == ""):
        print("O nome é obrigatório")
        name = input("Digite o nome da pessoa titular: ")
        os.system('cls')
    return name


def Cpf():
    """Registrar CPF"""
    cpf = input("Digite o CPF: ")
    os.system('cls')
    while(cpf == ""):
        print("O CPF é obrigatório")
        cpf = input("Digite o CPF: ")
        os.system('cls')
    return cpf


def Hosted():
    """Registrar número de pessoas que vão se hospedar"""
    hosted = input("Digite a quantidade de pessoas que vão se hospedar: ")
    os.system('cls')
    while(hosted == ''):
        print("A quantidade de pessoas hospedadas é obrigatória!")
        hosted = input("Digite a quantidade de pessoas hospedadas:  ")
        os.system('cls')
    return hosted


def TypeRoom():
    """Registrar o tipo de quarto"""
    type_room = input(
        "Digite o tipo de quarto ( S – Standar, D – Deluxe, P – Premium): ")
    type_room = type_room.upper()
    os.system('cls')

    while(type_room == ''):
        print("O tipo de quarto é obrigatório!")
        type_room = input(
            "Digite o tipo de quarto ( S – Standar, D – Deluxe, P – Premium):")
        type_room = type_room.upper()
        os.system('cls')

    if(type_room == "S" or type_room == "D" or type_room == "P"):
        error = "valid"
    else:
        error = "invalid"

    while(error == "invalid"):
        print("Tipo de quarto inválido!")
        type_room = input(
            "Digite o tipo de quarto ( S – Standar, D – Deluxe, P – Premium):")
        type_room = type_room.upper()
        os.system('cls')
        if(type_room == "S" or type_room == "D" or type_room == "P"):
            error = "valid"
    return type_room


def Days():
    """Registrar número de dias de hospedagem"""
    days = input("Digite a quantidade de dias de hospedagem: ")
    os.system('cls')
    while(days == ''):
        print("A quantidade de dias de hospedagem é obrigatória!")
        days = input("Digite a quantidade de dias de hospedagem: ")
        os.system('cls')
    return days


def Value(type_room, hosted, days):
    """Registrar valor"""
    if(type_room == "S"):
        value = 100 * int(hosted) * int(days)
    elif(type_room == "D"):
        value = 200 * int(hosted) * int(days)
    elif(type_room == "P"):
        value = 300 * int(hosted) * int(days)
    return value


def UpdatedStatus():
    status = input(
        "Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado) : ")
    status = status.upper()
    os.system('cls')

    while(status == ''):
        print("O status é obrigatório!")
        status = input(
            "Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado) : ")
        status = status.upper()
        os.system('cls')

    if(status == "R" or status == "C" or status == "A" or status == "F"):
        error = "valid"
    else:
        error = "invalid"

    while(error == "invalid"):
        print("Tipo de quarto inválido!")
        status = input(
            "Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado) : ")
        status = status.upper()
        os.system('cls')
        if(status == "R" or status == "C" or status == "A" or status == "F"):
            error = "valid"
    return status


"""Função Check In"""


def CheckIn():
    cpf = input("Digite o CPF para realizar a busca: ")

    while(cpf == ""):
        print("CPF não pode ser vazio!")
        cpf = input("Digite o CPF para realizar a busca: ")

    cpf = int(cpf)
    validation = ViewStatusCPF(cpf, "R")
    lista = []
    status = "A"
    lista.append(status)

    if(validation == 'invalid'):
        print("Reserva com status 'R' não encontrada no CPF digitado ")
        time.sleep(3)
        menu()

    ClientId = int(input("\nDigite o ID que deseja mudar o status: "))
    lista.append(ClientId)

    UpadatedStatus(lista)
    os.system('cls')


"""Função Check Out"""


def CheckOut():
    cpf = input("Digite o CPF para realizar a busca: ")

    while(cpf == ""):
        print("CPF não pode ser vazio!")
        cpf = input("Digite o CPF para realizar a busca: ")

    cpf = int(cpf)
    validation = ViewStatusCPF(cpf, "A")

    lista = []
    status = "F"
    lista.append(status)

    if(validation == 'invalid'):
        print("Reserva com status 'A' não encontrada no CPF digitado ")
        time.sleep(3)
        menu()

    ClientId = int(input("\nDigite o ID que deseja mudar o status: "))
    lista.append(ClientId)

    UpadatedStatus(lista)
    os.system('cls')


"""Função Update"""


def Update():
    cpf = input("Digite o CPF para realizar a busca: ")

    """Verificando se CPF não está vazio"""
    while(cpf == ""):
        print("CPF não pode ser vazio!")
        cpf = input("Digite o CPF para realizar a busca: ")

    """Passando cpf para função de buscar por CPF"""
    cpf = int(cpf)
    View(cpf, "cpf")

    lista = []
    ClientId = int(input("\nDigite o ID que deseja mudar o status: "))
    os.system('cls')

    """-----------Atualizar número de pessoas que vão se hospedar------------"""
    hosted = Hosted()
    lista.append(int(hosted))

    """-------------------Atualizar o tipo de quarto-------------------------"""
    type_room = TypeRoom()
    lista.append(type_room)

    """---------------Atualizar número de dias de hospedagem-----------------"""
    days = Days()
    lista.append(int(days))

    """---------------------------Atualizar valor----------------------------"""
    value = Value(type_room, hosted, days)
    lista.append(value)

    """Atualizar o tipo de quarto"""
    status = UpdatedStatus()
    lista.append(status)

    lista.append(ClientId)
    Upadated(lista)
    os.system('cls')


def StatusR():
    status = 'R'
    View(status, "status")

    exitMenu = input("\nPressione ENTER para voltar")
    if(exitMenu == "" or exitMenu != ""):
        ReportMenu()


def StatusC():
    status = 'C'
    View(status, "status")

    exitMenu = input("\nPressione ENTER para voltar")
    if(exitMenu == "" or exitMenu != ""):
        ReportMenu()


def StatusA():
    status = 'A'
    View(status, "status")

    exitMenu = input("\nPressione ENTER para voltar")
    if(exitMenu == "" or exitMenu != ""):
        ReportMenu()


def StatusF():
    status = 'F'
    View(status, "status")

    exitMenu = input("\nPressione ENTER para voltar")
    if(exitMenu == "" or exitMenu != ""):
        ReportMenu()


def ReportValue():
    TotalValue()
    exitMenu = input("\nPressione ENTER para voltar")
    if(exitMenu == "" or exitMenu != ""):
        ReportMenu()


def ReportCPF():
    cpf = input("Digite o CPF para realizar a busca: ")

    while(cpf == ""):
        print("CPF não pode ser vazio!")
        cpf = input("Digite o CPF para realizar a busca: ")

    cpf = int(cpf)
    View(cpf, "cpf")

    exitMenu = input("\nPressione ENTER para voltar")
    if(exitMenu == "" or exitMenu != ""):
        ReportMenu()


"""Chamando menu"""
menu()

print("Programa encerrado com sucesso!")
