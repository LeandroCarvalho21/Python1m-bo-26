import requests
import os

url= "https://bakcend-fecaf-render.onrender.com/contatos"

def exibir_menu():
    print(30*"#")
    print("#- Contatos -#")
    print("1. Listar Contatos")
    print("2. Criar Contato")
    print("3. Atualizar Contato")
    print("4. Excluir Contato")
    print("0. Sair")
    print(30*"#")
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pause():
    input("Press Enter para continuar...")


def listar_contato():
    print(f"{'-----Listando contato-----':^64}")
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"{'ID':^4} | {'NOME':^17} | {'CELULAR':^15} | {'EMAIL':^20}")
        for contato in data:
            Num_id = contato['id']
            nome = contato.get('nome')
            numero_cel = contato.get('celular') or 'sem celular'
            email = contato.get('email') or 'sem email'
            print(f"{Num_id:^4} | {nome:<17} | {numero_cel:<15} | {email:<20}")
    else:
        print(f"Erro ao buscar os contatos código http: {response}")
    
def criar_contato():
    print(f"{'-----Criando contato-----':^50}")
    nome = input("Digite o nome: ").strip() 
    while nome == "":
        print("Erro!! Campo nome obrigatorio")
        nome = input("Digite o nome: ").strip()
         
        
    email = input("Digite o email: ")
    celular = input("Digite o celular: ")
    dados_contato={
        "nome": nome.strip(),
        "email": email.strip(),
        "celular": celular.strip()
    }
    response = requests.post(url, dados_contato)
    if response.status_code in [200, 201]:
        print("Contato cadastrado com sucesso")
        print(response.json())
        print(response)
    else:
        print(f"Erro ao criar contato: {response}")
        
    
    
    
def atualizar_contato():
    print("Atualizar contato")
    id_contato = input("Digite o ID do contato: ").strip()
    contato = buscar_contato_por_id(id_contato)
    if contato:
        nome_atualizado = input("Digite o novo nome: ").strip()
        email_atualizado = input("Digite o novo email: ").strip()
        contato_atualizado = input("Digite o novo contato: ").strip()
        
        dados_atualizados = {
            "nome" : nome_atualizado,
            "email" : email_atualizado,
            "contato" : contato_atualizado
            
        }
        
        response = requests.put(f"{url}/{id_contato}", json=dados_atualizados)
        if response.status_code == 200:
            print('atualizado com sucesso!!!')
            print(response.json())
        else:
            print(f'Falha na atualização do contato! Erro: {response}')
                
    else:
        print('Usuário não cadastrado!')
    
    
def buscar_contato_por_id(id):
    response = requests.get(f"{url}/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def excluir_contato():
    print("Excluindo contato")
    id_contato = input("Digite o ID contato: ")
    contato = buscar_contato_por_id(id_contato)
    if contato:
        response = requests.delete(f"{url}/{id_contato}")
        if response.status_code in [200, 204]:
            print("Contato excluido com sucesso!")
        else:
            print("Falha ao excluir contato!")
    else:
        print("Contato não cadastrado!")
        
    
def main():
    while True:
        exibir_menu()
        opcao = input("EScolha uma opção: ")
        
        if opcao == "1":
            limpar_tela()
            listar_contato()
            pause()        
        elif opcao == "2":
            limpar_tela()
            criar_contato()
            pause()        
        
        elif opcao == "3":
            limpar_tela()
            atualizar_contato()
            pause()        
        
        elif opcao == "4":
            limpar_tela()
            excluir_contato()
            pause()        
            
        elif opcao == "0":
            print("Saindo")
        else:
            print(f"a opção {opcao} está incorreta! Tente novamente!")
            
        
        

if __name__ == "__main__":
    main()