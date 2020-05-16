from check2funcoes import *
inventario = {"fulano@xxx.com":["Fulano", "p@sswd"], "alguem@yyy.com":["Alguem", "Try@gain"], "aluno@pridefiap.com":["Breno Toledo", "Cyberstorm"]}
resp = "N"
while resp == "N":
    print("\033[1;30m                        ,---.           ,---.")
    print("                       / /'`.\.--'''--./,''\ \ ")
    print("                       \ \    _       _    / /")
    print("                        `./  / __   __ \  \,'")
    print("                         /    /_O)_(_O\    \ ")
    print("                         |  .-'  ___  `-.  |")
    print("                      .--|       \_/       |--.")
    print("                    ,'    \   \   |   /   /    `.")
    print("                   /       `.  `--^--'  ,'       \ ")
    print("                  .'''''''.  `--.___.--'     .'''''''. ")
    print("\033[1;95m     .===========/         \================/         \==============.   #########   #####    ########    #########")
    print("     | .=========\         /================\         /============. |   #             #     #        #   #        #")
    print("     | |Entre com a opção correspondente                           | |   #             #     #        #   #        #")
    print("     | |Digite 1 para cadastrar um email vazado                    | |   #             #     #        #   #        #")
    print("     | |Digite 2 para mostrar todos os vazamentos                  | |   ########      #     #        #   # #######")
    print("     | |Digite 3 para verificar um email                           | |   #             #     # ###### #   #")
    print("     | |Digite 4 para remover um email da lista                    | |   #             #     # ###### #   #")
    print("     | |Digite 5 para sair                                         | |   #             #     #        #   #")
    print("     | |                                                           | |   #           #####   #        #   #")
    print("     | |RM85925...                                                 | |   ______________________________________________")
    print("     | '===========================================================' |")
    print("     '==============================================================='")
    print("\033[1;30m                     |____________||____________|")
    print("                       ),-----.(      ),-----.(")
    print("                     ,'   ==.   \    /  .==    `.")
    print("                    /            )  (            \ ")
    print("                    `-----------'    `-----------'\033[1;96m")
    opcao = int(input("\n     Qual a opção que deseja?:"))
    if opcao == 1:
        cadastroElemento(inventario)
    elif opcao ==2:
        mostrarElemento(inventario)
    elif opcao ==3:
        buscarElemento(inventario)
    elif opcao ==4:
        excluirElemento(inventario)
    elif opcao == 5:
        resp = input("\n     Tem certeza que deseja sair?").upper()

    else:
        print("\n     Opcao invalida. Tente novamente!")
