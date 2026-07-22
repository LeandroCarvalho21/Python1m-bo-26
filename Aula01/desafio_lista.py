#um Um deerminado time pode ter no maximo 5 jogadores titulares.
#1. criar uma lista com 4 jogadores (str)
#2. Perguntar para usuário o nome de im jogador e incluir na lista (input e appeed)
#3. não permitir que o time passe de 5 jogadores 
#3.1 para descobrir quantos jogadores ja então na lista, use a função len()
#3.2 montar um if, verifique se o time ja possui 5 jogadores, caso verdade exibir a mensagem:
# "time completo ", caso contrario, exibir a mesagem "time está incompleto" 
#4. Subtituir o primeiro jogador da lista po um novo nome digitado pelo usuario 
#5. Pesquisar se o jogador está no time, caso sim, mostrar o nome dele ex: "O jogador está no time"

jogadores_titulares= ["Leandro","Bernardo", "Leonid","Deusdette"]
novo_jogador=str(input("Digite o nome do novo jogador\n"))
jogadores_titulares.append(novo_jogador)
print(f"O novo jogador escalado é: {novo_jogador}")
if (len(jogadores_titulares)>=5):
    print(f"Time está completo")
    print(f"Seleção formada por: {[jogadores_titulares]}")
else:
    print("Time está incompleto")

altera_jogador= str(input("Digite o nome do novo jogador para substituir pelo indice 0: "))
jogadores_titulares[0]= altera_jogador
print(f"o jogador do indice 0 foi substituido por {jogadores_titulares[0]}")
print(f"Seleção atual formada por: {[jogadores_titulares]}")

pesquisa= str(input("Pesquise um jogador\n"))
if(pesquisa in jogadores_titulares):
    print(f"O jogador {pesquisa} está na lista oficial!")
else:
    print(f"O jogador não está na lista")