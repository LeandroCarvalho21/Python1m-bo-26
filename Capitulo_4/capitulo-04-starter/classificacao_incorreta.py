idade = 22
tem_cnh= True
vascaino = True

if(idade>=18 and tem_cnh and vascaino) :
    print("Pode dirigir, cuidado com a Balisa ")
else:
    print("infelismente não pode dirigir")

estudante = True
renda_mensal = 2500
pcd = False
idade_cinema = 40

if(estudante or renda_mensal<=1600 or pcd or idade>=65) :
    print("="*30)
    print("paga meia no cinema, vai assistir minions ")
else:
    print("paga tudo, 💵")

# Instituto Eurofarma 
# Criterios parar os cursos

altura = input("Digite a sua altura: ")

if (not altura):
    print(f"Você não digitou a altura {altura}")
else:
    peso = float(input("Digite o peso"))


