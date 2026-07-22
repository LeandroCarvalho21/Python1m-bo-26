# condicionais e tipo de dado booleano
idade = 18

#computador, verifique se a idade do usuário é maior ou igual a 18
if (idade>=18):
    #Essa instrução só execultada caso a condição acima seja verdadeira(TRUE)
    print("Bem vindo ao Senai Delivery")
else:
    print("Você não tem idade para usar o Senai Delivery")


#Aprovou , Exame, Reprovou 
#Se media >=7 => Aprovou direto 
#Caso contrário, SE a media <7 e media >=5, exame 
#por fim, se a media for <5 => reprovou direto  

media = 10
if (media >= 7):
    print(f"sua média é {media}: Aprovado")
#condicional intermediaria, abreviação de ELSE IF, podemos ter  N(Vários) ELIFS em um unico IF
elif (media>=5):
    print(f"sua média é {media}: Exame")
#ELSE fecha o bloco do if, so pode ter um
else:
    print(f"sua média é{media}: Reprovado")

#Time A
#Time B
#Criar um bloco de if para determinar qual time venceu, ou se houve um EMPATE

timeA = int(input("Quantos gols o time A fez?"))
timeB = int(input("Quantos gols o time B fez?"))

if (timeA>timeB):
    print(f"Time A venceu de: {timeA}x{timeB}")
elif(timeA<timeB):
    print(f"Time B venceu de: {timeB}x{timeA}")
else:
    print(f"Houve empate {timeB}x{timeA}")
