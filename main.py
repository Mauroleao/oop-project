from cachorro import Cachorro
from gato import Gato   
from dono import Dono

lista_cachorros = list()
lista_gatos = list()

while True:

    print(20*"-")
    print("1. Cadastrar usuario")
    print("2. Cadastrar cachorro")
    print("3. Cadastrar gato")
    print("4. Listar cachorros")
    print("5. Listar gatos")
    print("6. Brincar com cachorro")
    print("7. Brincar com gato")
    print("8. Sair")
    print(20*"-")
    opcao = int(input("Escolha a Opcao desejada: "))
    global dono
    if opcao == 1:
        nome_usuario = input("Digite o nome do Usuário: ")
        dono = Dono(nome_usuario)
    elif opcao == 2:
        nome_cachorro = input("Digite o nome do Cachorro: ")
        idade_cachorro = input("Digite a idade do Cachorro: ")
        cor_cachorro = input("Digite a cor do Cachorro: ")
        qtd_brinquedos = input("Digite a quantidade de brinquedos do Cachorro: ")
        cachorro = Cachorro(nome_cachorro, idade_cachorro, cor_cachorro, qtd_brinquedos, dono=dono)
        lista_cachorros.append(cachorro[0])
        print(cachorro.nome)
    elif opcao == 3:
        nome_gato = input("Digite o nome do Gato: ")
        idade_gato = input("Digite a idade do Gato: ")
        cor_gato = input("Digite a cor do Gato: ")
        qtd_bolinhas = input("Digite a quantidade de bolinhas do Gato: ")
        gato = Gato(nome_gato, idade_gato, cor_gato, qtd_bolinhas, dono=dono)
        lista_gatos.append(gato)
    elif opcao == 4:
        for cachorro in lista_cachorros:
            print(cachorro)    
    elif opcao == 5:
        for gato in lista_gatos:
            print(gato) 
    elif opcao == 6:
        for cachorro in lista_cachorros:
            print(cachorro.brincar())
            if cachorro.felicidade >= 6:
                print(cachorro.fazer_barulho())
    elif opcao == 7:
        for gato in lista_gatos:
            print(gato.brincar())  
            if gato.felicidade >= 5:
                print(gato.fazer_barulho())                      
    else: 
        break    