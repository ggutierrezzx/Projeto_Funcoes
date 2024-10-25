
tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False 
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar():
    if not tarefas:
        print('Nenhuma tarefa encontrada.')
        return
    
    for index, tarefa in enumerate(tarefas):
        status = 'Feito' if tarefa['concluida'] else "Não foi feita!"
        print(f"{index + 1}. {tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}) - Status: {status}")

def aprioridade(prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada.")
        return
    
    for tarefa in tarefas_filtradas:
        status = "✔️" if tarefa['concluida'] else "❌"
        print(f"{tarefa['nome']} - {tarefa['descricao']} - Status: {status}")

def acategoria(categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa na categoria '{categoria}' encontrada.")
        return
    
    for tarefa in tarefas_filtradas:
        status = "✔️" if tarefa['concluida'] else "❌"
        print(f"{tarefa['nome']} - {tarefa['descricao']} - Status: {status}")

def menu():
    while True:
        print("Gerenciador de Tarefas".center(50))
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")       
        print("3. Exibir Tarefas por Prioridade")
        print("4. Exibir Tarefas por Categoria")
        print("5. Sair")

        opc = input('Escolha uma opção: ')

        if opc == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa: ")
            categoria = input("Categoria da tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)

        elif opc == '2':
            listar()

        elif opc == '3':
            prioridade = input("Prioridade a ser exibida: ")
            aprioridade(prioridade)

        elif opc == '4':
            categoria = input("Categoria a ser exibida: ")
            acategoria(categoria)

        elif opc == '5':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
