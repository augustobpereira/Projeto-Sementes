class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []

    def adicionarContato(self, contato):
        for c in self.contatos:
            if c.nome == contato.nome:
                print("Contato já existe na agenda.")
                return
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def removerContato(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                self.contatos.remove(c)
                print(f"Contato {nome} removido com sucesso!")
                return
        print("Contato não encontrado.")

    def buscarContato(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                return c
        print("Contato não encontrado.")
        return None

    def atualizarContato(self, nome, novoContato):
        for i, c in enumerate(self.contatos):
            if c.nome == nome:
                self.contatos[i] = novoContato
                print(f"Contato {nome} atualizado com sucesso!")
                return
        print("Contato não encontrado.")

    def listarContatos(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
            return
        for contato in self.contatos:
            print(contato)