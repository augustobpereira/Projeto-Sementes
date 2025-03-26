class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # O livro começa disponível

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' de {self.autor} - {status}"


class Biblioteca:
    def __init__(self):
        self.livros = {}

    def adicionar_livro(self, titulo, autor):
        if titulo in self.livros:
            raise ValueError(f"Erro: O livro '{titulo}' já está cadastrado na biblioteca.")

        self.livros[titulo] = Livro(titulo, autor)

    def emprestar_livro(self, titulo):
        if titulo not in self.livros:
            raise ValueError(f"Erro: O livro '{titulo}' não existe no cadastro da biblioteca.")
        if not self.livros[titulo].disponivel:
            raise ValueError(f"Erro: O livro '{titulo}' já está emprestado.")

        self.livros[titulo].disponivel = False

    def devolver_livro(self, titulo):
        if titulo not in self.livros:
            raise ValueError(f"Erro: O livro '{titulo}' não existe no cadastro da biblioteca.")
        if self.livros[titulo].disponivel:
            raise ValueError(f"Erro: O livro '{titulo}' não está emprestado.")

        self.livros[titulo].disponivel = True

    def listar_livros(self):
        return [str(livro) for livro in self.livros.values()]