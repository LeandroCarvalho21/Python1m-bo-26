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
