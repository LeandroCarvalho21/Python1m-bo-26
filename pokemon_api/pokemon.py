import requests
import sys

def menu():
    print("-------Pesquisar pokemon-------")
    print("1 - Pesquisar pokemon")
    print("0 - Sair")

def pesquisa_pokemon():
    pokemon = input("Digite o ID ou nome do pokemon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    response = requests.get(url)
    print(response) 
    if response.status_code == 200:
        data = response.json()
        # print (data)
        print(f"ID: {data['id']}") 
        print(f"Nome: {data['name']}") 
        for habilidades in data['abilities']:
            print(habilidades)
        
       
    else:
        print("erro")
        
def pause():
    input("Press enter para continuar")

def exit():
    print("Saindo..")
    sys.exit()

def main():
    opcao = ""
    while opcao != "0":
        menu()
        opcao = input("Digite uma opção: ")
        if (opcao == "1"):
            pesquisa_pokemon()
            pause()
        elif (opcao == "0"):
            exit()
        else:
            print("Opção invalida")
main()
    