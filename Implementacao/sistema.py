
from receita import Receita
from user import User
from user import Admin
from bd import BD
from interface import erro404, parametros
import interface
import pesquisa

def menu_cadastro(data):
    user_atual = 0
    while user_atual == 0 :
        comand = interface.menu_comando()
        if comand == "A":
            login,senha,email = interface.login_senha_email()
            if len(email) >= 1:
                aux = ""
                for i in data.lista_users:
                    if i.email == email:
                        aux = "S"
                if aux == "S":
                    print("Usuário já existente. ")
                else:
                    lista_receitas = []                        #CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                    x = User(login,senha,email,lista_receitas) 
                    data.lista_users.append(x)
            else:
                lista_receitas = []            #SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                x = User(login,senha,email,lista_receitas)  
                data.lista_users.append(x)
                     
            print("-="*30)
        

        elif comand == "B":
            email,senha = interface.email_senha()
            if len (email) >= 1:
                erro_pin = 0
                for i in data.lista_admin:
                    if i.email == email and i.senha == senha:
                        print("Bem vindo, administrador. Por segurança do sistema, favor insira seu pin de administração para prosseguir.")
                        pin = input("Pin: ")
                        if i.senha_admin == pin:
                            user_atual = i.login
                        else:
                            print("Pin incorreto")
                            erro_pin = 1
                            break
                    else:
                        user_atual = 0

                for i in data.lista_users:
                    if i.email == email and i.senha == senha:
                        user_atual = i.login
                    else:
                        user_atual = 0
                if user_atual == 0 and erro_pin == 0:
                    print("Senha ou email incorretos")

        elif comand == "C":
            return 'exit'
            break
                
        else:
            interface.invalid_input()

    return user_atual


## TODO: 
# A -> menu criar receitas (baseado nos comentados lá embaixo)      pronto
# B -> menu de pesquisa
# C -> menu de acesso às receitas, criando um novo menu no C, podendo ver as receitas e alterá-las/excluí-las
# D -> menu de acesso à conta do usuário, podendo acessar seus dados, podendo excluir conta e alterar dados(senha, login, email).

def menu_user(user_atual, j, data):
    print(f'Bem vindo, {user_atual}!')
    
    while user_atual == j.login:
        comand = input(f"""{"##"*30}    
    A - Criar Receita
    B - Pesquisa
    C - Minhas Receitas
    D - Pesquisar uma receita própria
    E - Minha Conta 
    
    F - Sair
{"-="*30}
Resposta: """).upper()

        if comand == "A":
            print(f"""
{"-="*30}
   ################
   # Nova Receita #
   ################
{"-="*30}
        """)
            #lista = [] 
            nome,palavras_chave,doce_salgado,gluten,porcoes,n_ingredientes, descricao, modo_preparo =parametros()     #funcao valores
            if len(j.lista_receitas) >= 1:
                aux = ""
                print(j.lista_receitas)
                for receita in j.lista_receitas:
                    print(receita)
                    if receita.nome == nome:
                        aux = "S"
                if aux == "S":
                    print("\n ~~ Nome já existente ~~ ")
                else:
                    ingre = interface.lista_ingredientes(n_ingredientes)           #funcao que retorna uma lista dos ingredientes que vai usar
                    food = Receita(nome,user_atual,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao, modo_preparo)
                    #lista.append(food)
                    j.lista_receitas.append(food)
            # else:
            #     ingre = defs.lista_ingredientes(n_ingredientes)
            #     food = Receita(nome,user_atual,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao, modo_preparo)
            #     j.lista_receitas.append(food)
            #     print


        elif comand == "B":
            pesquisa.pesquisar_receita(data)

        elif comand == "C":
                print("-="*30)
                i = 1
                if len(j.lista_receitas) >= 1:
                    print(f""" 
                        {'-'*30}
                        Minhas Receitas:
                        """)
                    for receita in j.lista_receitas:
                        print(f"""################\n# RECEITA {i} #\n################\n\nNome: {receita.nome} \n\nIngredientes: {receita.lista_ingredientes} \n\nModo de preparo: {receita.modo_preparo} \n\nDescricao: {receita.descricao} \n\nPalavras Chave: {receita.palavras_chave}
                            """)
                        i += 1
                    alterar = input(f'Deseja alterar alguma receita? \n1 - sim, 2 - não')
                    if alterar == 1:
                        receita = ('Qual receita deseja alterar? Insira o número referente à pesquisa.')
                    else:
                        pass
                else:
                    print("O usuário ainda não possui receitas cadastradas. ")

        #login senha, email, alterar e excluir
        elif comand == "E":
            while True:
                alteracao = interface.menu_alteracao(j)
                if alteracao == '1':
                    login,senha,novo_nome = interface.login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.login = novo_nome
                
                elif alteracao == '2':
                    login,senha,novo_senha = interface.login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.senha = novo_senha   
                
                elif alteracao == '3':
                    login,senha,novo_email = interface.login_senha_novo_nome() 
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.email = novo_email   
                
                elif alteracao == '4':

                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                data.lista_users.remove(usuarios)
                                user_atual = 0          # excluiu a conta entao sai     # quando deleta o user nao sai da conta mas deleta as coisas
                                break
                elif alteracao == '0':
                    break
                else:
                    interface.invalid_input()   

        elif comand == "F":
            user_atual = 0

        else:
            interface.invalid_input()


def menu_admin(user_atual, i, data):
    while user_atual == i.login:
        comand = interface.menu_comando_admin()
        if comand == "A":
            aux_user = 1
            aux_adm = 1
            for usuario in data.lista_users:
                interface.print_users(aux_user,usuario)
                aux_user += 1
            for admin in data.lista_admin:
                interface.print_amins(aux_adm,admin)
                aux_adm += 1

            alteracao = interface.menu_alteracao_admin()
            if alteracao == 'A':
                login = input(" Email do usuário: ")
                for usuario_pesquisa in data.lista_users:
                    if login == usuario_pesquisa.login:
                        data.lista_users.pop(usuario_pesquisa)
            elif alteracao == 'B':
                print("Alterar dados de uma conta.")
            elif alteracao == 'C':
                print("Adicionar uma conta admnistrativa.")
            elif alteracao == 'D':
                print("Sair")
            else:
                interface.invalid_input()

        elif comand == "B":
            interface.menu_pesquisa_receitas(data)

        elif comand == "C":
            interface.print_denuncias_recebidas()
            pesquisa.acessar_denuncias(data.lista_denuncia, data.lista_users)    # denuncias nao esta funcionando direito

        elif comand == "D":
            user_atual = 0

        else:
            interface.erro404()
