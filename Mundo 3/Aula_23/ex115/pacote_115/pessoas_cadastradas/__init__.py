
cadastro_pessoas_list = [{'nome': 'Efraim', 'idade': 28}, {'nome': 'Eloah', 'idade': 26}]

def cadastros():
    
    print("-"*30)
    print(f"{"PESSOAS CADASTRADAS":^30}")
    print("-"*30)

    for i in cadastro_pessoas_list:
        print(f"{i['nome']} {i['idade']}")
 

def novo_cadastro():

    pessoa = {}

    print("-"*30)
    print(f"{"NOVO CADASTRO":^30}")
    print("-"*30)

    pessoa['nome'] = str(input("Nome: ")).capitalize()
    pessoa['idade'] = int(input("Idade: "))

    cadastro_pessoas_list.append(pessoa.copy())


