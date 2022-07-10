from random import choice
from time import sleep

nomes = ['Erick', 'Pedro', 'Flávia', 'Marcia', 'Eva', 'Wagner', 'Paulo']
emails = ['erick@gmail.com', 'pedro@gmail.com', 'flavia@gmail.com', 'marcia@gmail.com',
          'eva@gmail.com', 'wagner@gmail.com', 'paulo@gmail.com']
telefones = [19999999999, 18888888888, 17777777777, 16666666666, 15555555555, 14444444444]
cidades = ['Araras', 'Leme', 'São Paulo', 'Rio Claro', 'Limeira', 'Campinas', 'Jundiaí']
estados = ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Minas', 'Rio Grande do Norte', 'Amazonas', 'Ceará']

def linha():
    print('-'*75)

def opcao(respostas):
    lista = []
    for resposta in respostas:
        if resposta in '1':
            nome = choice(nomes)
            print(nome)
            lista.append(nome)
        if resposta in '2':
            email = choice(emails)
            print(email)
            lista.append(email)
        if resposta in '3':
            telefone = choice(telefones)
            print(telefone)
            lista.append(telefone)    
        if resposta in '4':
            cidade = choice(cidades)
            print(cidade)
            lista.append(cidade)
        if resposta in '5':
            estado = choice(estados)
            print(estado)
            lista.append(estado)
    return lista
    
def salvar_arquivo(save):
    with open('dados.txt', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{save}\n')
  
def menu():
    print('Bem-vindo ao Gerador de Dados Aleatórios - Para finalizar, digite "parar"')
    linha()
    print('Escolha uma ou mais opções abaixo a serem geradas aleatóriamente')
    print('[1] - Nome \n[2] - E-mail \n[3] - Telefone \n[4] - Cidade \n[5] - Estado')
    resposta = input('Digite uma(as) opções: ')
    linha()
    return resposta
  
while True:
    lista = []
    resposta = menu()
    if resposta in 'parar':
        print('Programa Finalizado')
        break
    else:
        resposta = resposta.replace(',', '')
        for posicao in range(len(resposta)):
            lista.append(resposta[posicao])
        salvar = input('Gostaria de salvar os dados em um arquivo de texto?(s/n): ')
        if salvar in 's':
            dados = opcao(lista)
            for dado in dados:
                salvar_arquivo(dado)
            print('Os dados foram salvos com sucesso!')
            linha()
            sleep(1)
        else:
            opcao(lista) 
            linha()
            sleep(1)
    