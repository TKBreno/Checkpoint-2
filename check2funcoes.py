#cadastro  
def cadastroElemento(lista):
    resp = "S"
    while resp == "S":
        print("\n     .===================================================.")
        print("     |Para cadastrar digite: Email, nome completo e senha|")
        print("     :==================================================='")       
        tag = input("     |Email:").lower()
        lista[tag]=[input("     |Nome completo:"), input("     |Senha:")]
        resp = input("\n     Deseja cadastrar mais algum?:").upper()

#mostrar 
def mostrarElemento(lista):
    for tag, dados in lista.items():
        print("\n     .====================================.")
        print("     |Nome..........:", dados[0])
        print("     |Email.........:", tag)
        print("     |Senha.........:", dados[1])
        print("     '===================================='")
    tmp = input("")

#buscar
def buscarElemento(lista):
    busca = input("\n     Qual é o email para verificação?:").lower()
    leak = lista.get(busca)
    if leak != None:
        print("\n\033[1;31m     .==============================.")
        print("     |!!!SUAS INFORMAÇÕES VAZARAM!!!|")
        print("     :==============================;")
        print("     |Nome :", leak[0])
        print("     |Email:", busca)
        print("     |Senha:", leak[1])
        print("     '=============================='")
        question = input("\n\033[1;96m     Deseja Recuperar suas informações?(S/N):").upper()
        if question == "S":
            name = input("     Digite seu nome:")
            email = input("     Email:").lower()
            pwd = input("     Senha:")
            if lista.get(email) != None:
                if name == lista[email][0]:
                    if pwd == lista[email][1]:
                        del lista[email]
                        print("\n\033[1;92m     .===========================.")
                        print("     |!!!Informações excluidas!!!|")
                        print("     '==========================='")
                    else:
                        print("\n\033[1;31m     .===============.")
                        print("     |Senha incorreta|")
                        print("     '==============='")
                else:
                    print("\n\033[1;31m     .=========================.")
                    print("     |!!!Nome não encontrado!!!|")
                    print("     '========================='")
            else:
                print("\n\033[1;31m     .==========================.")
                print("     |!!!Email não encontrado!!!|")
                print("     '=========================='")
    else:
        print("\n\033[1;92m     .==================.")
        print("     |!!!Email Seguro!!!|")
        print("     '=================='")       
    tmp = input("")            


#excluir
def excluirElemento (lista):
    print("\n     .=================================================.")
    print("     |Para excluir digite: Nome completo, email e senha|")
    print("     :================================================='") 
    name = input("     |Digite seu nome:")
    email = input("     |Email:").lower()
    pwd = input("     |Senha:")
    if lista.get(email) != None:
        if name == lista[email][0]:
            if pwd == lista[email][1]:
                del lista[email]
                print("\n\033[1;92m     .===========================.")
                print("     |!!!Informações excluidas!!!|")
                print("     '==========================='")
            else:
                print("\n\033[1;31m     .===============.")
                print("     |Senha incorreta|")
                print("     '==============='")
        else:
            print("\n\033[1;31m     .=========================.")
            print("     |!!!Nome não encontrado!!!|")
            print("     '========================='")
    else:
        print("\n\033[1;31m     .==========================.")
        print("     |!!!Email não encontrado!!!|")
        print("     '=========================='")

    tmp = input("")





