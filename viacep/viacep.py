import requests
import re
import sys

def menu():
    print(30*"=")
    print("1 - Pesquisa por CEP")
    print("2 - Pesquisa por logradouro")
    print("0 - Sair\n")
    
    
def pause():
    input("Press enter para contiuar...")

def pesquisa_por_cep():
    cep = input("Digite seu cep: ").strip()
    cep_limpo = re.sub(r'[^0-9]', '', cep)
    URL = f'https://viacep.com.br/ws/{cep_limpo}/json/'

    response = requests.get(URL)
    print(response)

    if response.status_code == 200:
        print("ok")
        data = response.json()
        if 'erro' in data:
            print('erro: CEP não encontrado!')
        else:
            print(F"Logradouro: {data['logradouro']}")        
            print(F"Bairro: {data['bairro']}")        
            print(F"Cidade: {data['localidade']}")        
            print(F"UF: {data['uf']}")        
    else:
        print("erro: CEP Invalido!")
        
def logradouro():
    estado = input("Digite a sigla do estado: ")        
    Cidade = input("Digite o nome do cidade: ")        
    logradouro = input("Digite parte do logradouro: ")        
    
    url =  f"https://viacep.com.br/ws/{estado}/{Cidade}/{logradouro}/json/"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            print("erro, informação não encontrada..." )
        else:
            for info in data:
                print(info['cep'], info['bairro'], info['logradouro'])
    else:
        print("erro, informação incorreta..." )
def exit():
    input("Press enter para sair")
    sys.exit()

def main():
    opcao = ""
    while opcao != "0":
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            pesquisa_por_cep()
            pause()
        elif opcao == "2":
            logradouro()
            pause()
        elif opcao == "0":
            exit()
        else:
            print("Opção incorreta, tente novamente...")
            pause()
      
main()
            