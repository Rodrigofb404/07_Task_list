class Tarefas:
    def __init__(self):
        self.nome = ""
        self.descricao = ""
        self.prioridade = ""
        self.categoria = ""
        self.id = 1
        self.lista_tarefas = []

    def criar_tarefa(self, nome="", descricao="", prioridade="", categoria=""):
        tarefa = {
            'nome': nome,
            'descricao': descricao,
            'prioridade': prioridade,
            'categoria': categoria,
            'id': self.id
        }
        self.lista_tarefas.append(tarefa)
        self.id += 1

    def excluir_tarefa(self, id):
        for i, tarefa in enumerate(self.lista_tarefas):
            if tarefa["id"] == id:
                del self.lista_tarefas[i]
                print(f"A tarefa {tarefa['nome']} foi concluída e excluída")
                break
        
        for i in range(len(self.lista_tarefas)):
            if self.lista_tarefas[i]["id"] > id:
                self.lista_tarefas[i]["id"] -= 1
        
        self.id -= 1

    def exibir_lista(self):
        for tarefa in self.lista_tarefas:
            print(f"Tarefa {tarefa['id']} - Nome: {tarefa['nome']} | Descrição: {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']}")

    def devolver_lista(self):
        return self.lista_tarefas

if __name__ == "__main__":
    sair = False
    tarefas = Tarefas()
    lista_tarefas = tarefas.devolver_lista()
    while not sair:
        print("""\n---------- MENU ----------
1 - ADICIONAR TAREFA
2 - LISTAR TAREFAS
3 - CONCLUIR TAREFA
4 - SAIR""")
        opcao = int(input("O que você deseja fazer? "))
        print("")

        if opcao == 1:
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade: ")
            categoria = input("Categoria: ")
            tarefas.criar_tarefa(nome, descricao, prioridade, categoria)
        elif opcao == 2:
            tarefas.exibir_lista()
        elif opcao == 3:
            excluir = int(input("Qual o número da tarefa que você deseja excluir? "))
            tarefas.excluir_tarefa(excluir)
        elif opcao == 4:
            print("ENCERRANDO PROGRAMA")
            sair = True
