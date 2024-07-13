class Doacao:
    def __init__(self, doador, valor, data):
        self.doador = doador
        self.valor = valor
        self.data = data

    def __str__(self):
        return f'Doador: {self.doador}, Valor: R${self.valor:.2f}, Data: {self.data}'

class Voluntario:
    def __init__(self, nome, contato):
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
            for doacao in self.doacoes:
                print(doacao)

    def listar_voluntarios(self):
        if not self.voluntarios:
            print("Nenhum voluntário cadastrado.")
        else:
            print("Lista de Voluntários:")
            for voluntario in self.voluntarios:
                print(voluntario)

# Exemplo de uso
if __name__ == "__main__":
    ong = CasaDaEsperanca()
    
    # Adicionando doações
    ong.adicionar_doacao(Doacao("João Silva", 100.0, "2024-07-13"))
    ong.adicionar_doacao(Doacao("Maria Souza", 50.0, "2024-07-14"))
    
    # Adicionando voluntários
    ong.adicionar_voluntario(Voluntario("Pedro Lima", "pedro@example.com"))
    ong.adicionar_voluntario(Voluntario("Ana Costa", "ana@example.com"))
    
    # Listando doações e voluntários
    ong.listar_doacoes()
    ong.listar_voluntarios()
