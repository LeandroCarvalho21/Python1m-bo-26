#Variavel aluno do tipo str guarda os dados informado pelo usúario.  
aluno = input("Digite seu nome: ")
anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = 2026
#saida de dados com f-string, consigo jutar texto e outras variaveis na mesma linha 
print(f'Olá {aluno}!!! Você nasceu {anoNascimento} e tem {anoAtual-anoNascimento}')
