def tabela(lst):
    l = lst
    lis = l[:]
    
    print(f"""
    {"#"*60}
    #{"DOCE":^29}|{"SALGADO":^28}#
    #{"-"*29}+{"-"*28}#
    #{"QUENTE":^14}|{"FRIO":^14}|{"QUENTE":^13}|{"FRIO":^14}#
    #{"-"*14}+{"-"*14}+{"-"*13}+{"-"*14}#""")
    cont = 0

    for i in lis:
        cont += 1
        doce_quente = ""
        doce_frio = ""
        salgado_quente = ""
        salgado_frio = ""
        if i.doce_salgado == "A" and i.hot_cold == "A":
            if len(i.nome) >= 12:
                doce_quente = i.nome[0:12]
            else:
                doce_quente = i.nome

        elif i.doce_salgado == "A" and i.hot_cold == "B":
            if len(i.nome) >= 12:
                doce_frio = i.nome[0:12]
            else:
                doce_frio = i.nome

        elif i.doce_salgado == "B" and i.hot_cold == "A":
            if len(i.nome) >= 12:
                salgado_quente = i.nome[0:12]
            else:
                salgado_quente = i.nome

        elif i.doce_salgado == "B" and i.hot_cold == "B":
            if len(i.nome) >= 12:
                salgado_frio = i.nome[0:12]
            else:
                salgado_frio = i.nome
        
        print(f""" {cont:^3}#{doce_quente:^14}|{doce_frio:^14}|{salgado_quente:^13}|{salgado_frio:^14}#""")

    print(f"""    {"#"*60}""")


def parametros():
#nome
    nome = input("Nome da comida: ")


#tempo
    palavras_chave = []
    while 0>=len(palavras_chave) or 100>=len(palavras_chave) :
        palavra = input(f"""
        {"-="*30}
            Inserira a palavra chave

            caso queira sair digite 0
        {"-="*30}
            Resposta: """).upper()
        if palavra != '0':
            palavras_chave.append(palavra)
        elif palavra == '0':
            break
        else:
            print("Input inválido. ")

#doce ou salgado
    doce_salgado = ''
    while doce_salgado != "A" and doce_salgado != "B":
        doce_salgado = input(f"""
{"-="*30}
        O comida é:   
        
            A - Doce
            B - Salgado
{"-="*30}
        Resposta: """).upper()


#estrelas
    star = ''
    while star != "A" and star != "B":
        star = input(f"""
{"-="*30}
    AVALIAÇÕES da receita:
        A - ate 3 estrelas
        B - mais de 3 estrelas
{"-="*30}
    Resposta:""").upper()


#quente ou frio
    hot_cold = ''
    while hot_cold != "A" and hot_cold != "B":
        hot_cold = input(f"""
{"-="*30}
    A receita é:
        A - Quente
        B - Frio
{"-="*30}
    Resposta: """).upper()

#porcoes
    porc = ''
    while porc != "A" and porc != "B":
        porc = input(f"""
{"-="*30}
    Porção geradas:
    
        A - ate de 2 pessoas
        B - mais de 2 pessoas 
{"-="*30}
    Resposta: """).upper()

    print("-="*30)
    while True:
        try:
            n_ingredientes = int(input("Número de ingredientes: "))
            break
        except ValueError:
            print("ERRO. Você não digitou um número!")


    return nome,palavras_chave,doce_salgado,star,hot_cold,porc,n_ingredientes

def nomequant(n_ingredientes):
    lis = []

    for i in range(n_ingredientes):
        dic = {}                                                                      #dicionario
        dic[i] = input("Nome: "),input("Quantidade em gramas ou unidades: ")
        lis.append(dic)

    return lis