import json

class Doacao:
    def __init__(self, doador, valor, data):
        if not doador or valor <= 0 or not data:
            raise ValueError("Dados da doação inválidos.")
        self.doador = doador
        self.valor = valor
        self.data = data

    def __str__(self):
        return f'Doador: {self.doador}, Valor: R${self.valor:.2f}, Data: {self.data}'

class Voluntario:
    def __init__(self, nome, contato):
        if not nome or not contato:
            raise ValueError("Dados do voluntário inválidos.")
        self.nome = nome
        self.contato = contato

    def __str__(self):
        return f'Nome: {self.nome}, Contato: {self.contato}'

class CasaDaEsperanca:
    def __init__(self):
        self.doacoes = []
        self.voluntarios = []

    def adicionar_doacao(self, doacao):
        self.doacoes.append(doacao)
        print("Doação registrada com sucesso!")

    def adicionar_voluntario(self, voluntario):
        self.voluntarios.append(voluntario)
        print("Voluntário cadastrado com sucesso!")

    def listar_doacoes(self):
        if not self.doacoes:
            print("Nenhuma doação registrada.")
        else:
            print("Lista de Doações:")
            for i, doacao in enumerate(self.doacoes, start=1):
                print(f"{i}. {doacao}")

    def listar_voluntarios(self):
        if not self.voluntarios:
            print("Nenhum voluntário cadastrado.")
        else:
            print("Lista de Voluntários:")
            for i, voluntario in enumerate(self.voluntarios, start=1):
                print(f"{i}. {voluntario}")

    def remover_doacao(self, index):
        try:
            removed = self.doacoes.pop(index)
            print(f"Doação removida: {removed}")
        except IndexError:
            print("Índice de doação inválido.")

    def remover_voluntario(self, index):
        try:
            removed = self.voluntarios.pop(index)
            print(f"Voluntário removido: {removed}")
        except IndexError:
            print("Índice de voluntário inválido.")

    def salvar_dados(self, arquivo='dados.json'):
        with open(arquivo, 'w') as f:
            json.dump({
                'doacoes': [doacao.__dict__ for doacao in self.doacoes],
                'voluntarios': [voluntario.__dict__ for voluntario in self.voluntarios]
            }, f, indent=4)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, arquivo='dados.json'):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                self.doacoes = [Doacao(**doacao) for doacao in dados['doacoes']]
                self.voluntarios = [Voluntario(**voluntario) for voluntario in dados['voluntarios']]
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Dados iniciais foram criados.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os dados: {e}")

def main():
    ong = CasaDaEsperanca()
    ong.carregar_dados()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Doação")
        print("2. Adicionar Voluntário")
        print("3. Listar Doações")
        print("4. Listar Voluntários")
        print("5. Remover Doação")
        print("6. Remover Voluntário")
        print("7. Salvar Dados")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            doador = input("Nome do doador: ")
            valor = float(input("Valor da doação: "))
            data = input("Data da doação (YYYY-MM-DD): ")
            try:
                ong.adicionar_doacao(Doacao(doador, valor, data))
            except ValueError as e:
                print(e)

        elif escolha == "2":
            nome = input("Nome do voluntário: ")
            contato = input("Contato do voluntário: ")
            try:
                ong.adicionar_voluntario(Voluntario(nome, contato))
            except ValueError as e:
                print(e)

        elif escolha == "3":
            ong.listar_doacoes()

        elif escolha == "4":
            ong.listar_voluntarios()

        elif escolha == "5":
            ong.listar_doacoes()
            index = int(input("Informe o índice da doação a ser removida: ")) - 1
            ong.remover_doacao(index)

        elif escolha == "6":
            ong.listar_voluntarios()
            index = int(input("Informe o índice do voluntário a ser removido: ")) - 1
            ong.remover_voluntario(index)

        elif escolha == "7":
            ong.salvar_dados()

        elif escolha == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
