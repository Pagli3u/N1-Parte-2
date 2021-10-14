#dicionario de alunos
Alunos = {"marco": "email",
"paulo":"hotmail",
"matheus": "matheusemail",
"jean": "jeanemail",

 }
def mostralist():
    for aluno, email in Alunos.items():
        print(aluno,":" ,email)
    mostrarmenu() 
#Mostrandando em oredem alfabetica
def mostra_alf():
    for aluno, email in sorted(Alunos.items()):    
        print(aluno,":" ,email)
    mostrarmenu() 

#Excluindo um aluno
def excluiraluno():
    nome= str(input("Digite o nome do aluno que deseja excluir\n"))
    Alunos.pop(nome)
    print(Alunos)
    mostrarmenu()


#Criando um novo aluno 
def novoaluno():
    nome = input("Digite o nome\n")
    email = input("Digite o email\n")
    Alunos[nome] = email
    print(Alunos)
    mostrarmenu()


#funcao para mostra o menu    
def mostrarmenu():
    
    print("Digite 0 para sair")
    print("Digite 1 para criar alunos")
    print("Digite 2 para excluir alunos")
    print("Digite 3 para exibir alunos")
    print("Digite 4 para exibir alunos em oredem alfabetica ")
    print("Digite 5 para pesquisar aluno")
    print("Digite 6 alterar user aluno")
    escolha = int(input("Qual opcao deseja ?\n"))
    if escolha == 1 :
        novoaluno()
    elif escolha == 2:
        excluiraluno()
    elif escolha == 3:
        mostralist()
    elif escolha == 4:
        mostra_alf()
    elif escolha == 0:
          pass
        




mostrarmenu() 

