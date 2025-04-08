import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n ---- MENU CADASTROS ----" )
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastro")
    print("3 - Sair")
    print("-----------------------")

    salvar_cadastros("cadastros")
    with open (arquivo_cadastros, "w" ,encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivos, indent=4, ensure_ascii=False)

    def carregar_cadastros(): 
        try:
            with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
             return json.load(arquivo)
        except(FileNotFoundError, json.JSONDecodeError):
            return[]
        
        def cadastrar_pessoa(cadatros):
        nome = input("Nome: ")
        idade = input("idade: ")
        turma= input("turma: ")
        curso = input("curso: ")
        cadastrar.append({"Nome": nome, "idade": idade, "Turma": turma, "Curso": curso,})
        salvar_cadastros(cadastros)
        print(Cadastro realizado com sucesso!)
        def ver_cadastros (cadastros):
    if not cadastros:
    print("\nNenhum cadastro realizado.")
    else:
    print("\n== LISTA DE CADASTROS =====")
    for i, pessoa in enumerate (cadastros, 1):
    print (
    f"(i). Nome: (pessoa ['Nome']), Idade:
    (
    pessoa['Idade']), Turma: (pessoa ['Turma']], Curso: (pessoa ['Curso']")
    input("\nPressione Enter par
    voltar ao menu...")
