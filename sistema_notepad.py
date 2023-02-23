opcao_do_menu = 0
def menu():
    print('1-Incluir nova tarefa')
    print('2-Ver lista de tarefa')
    print('3-Excluir tarefa salva')
    print('4-Sair')
 
menu()
lista_de_tarefas=[]
opcao_do_menu=int(input('Qual é sua opção: '))

while True :
    if opcao_do_menu == 1:
        print('Opção escolhida: 1-Incluir nova tarefa')
    opcao_do_menu = 0
    tarefa = input('Digite tarefa a ser adicionada: ')
    lista_de_tarefas.append(tarefa)
    print('Sua lista de tarefas')
    print(lista_de_tarefas)

    menu()
    opcao_do_menu= int(input('Digite o número da opção desejada: '))
    if opcao_do_menu == 2:
        print('Opção escolhida: 2- Ver lista de tarefas ')
        print('Sua lista de tarefas: ')
        print(lista_de_tarefas)
        opcao_do_menu = 0
        menu()
        opcao_do_menu= int(input('Digite o número da opção desejada: '))
    elif opcao_do_menu == 3:
        print('Opção escolhida: 3- Excluir tarefa salva ')
        print('Sua lista de tarefas: ')
        print(lista_de_tarefas)
        lista_a_ser_removida = input('Digite a tarefa a ser excluida ')
        lista_de_tarefas.remove(lista_a_ser_removida)
        print('Sua lista de tarefas: ')
        print(lista_de_tarefas) 
        opcao_do_menu = 0
        menu()
        opcao_do_menu = int(input('Digite o número da opção desejada:'))   
    elif opcao_do_menu == 4:
        print('Opção escolhida: 4- Sair')
        resposta_de_saida = input('Deseja mesmo sair? (S/N)').upper()
        if resposta_de_saida == 'S':
           break
        else:
            menu()
            opcao_do_menu = 0
            opcao_do_menu = int(input('Digite o número da opção desejada: '))  
   
    