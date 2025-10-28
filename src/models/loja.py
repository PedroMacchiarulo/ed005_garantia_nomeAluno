class Loja:
    """
    Representa uma loja com nome, CNPJ, telefone, cidade e estado.
    """
    def __init__(self, id_loja, nome_loja, cnpj, telefone, cidade, estado):
        self.id_loja = id_loja
        self.nome_loja = nome_loja
        self.cnpj = cnpj
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"Loja {self.id_loja}: {self.nome_loja} ({self.cidade}, {self.estado})"

# Exemplo de uso
#loja1 = Loja(4, "Tech Store São Gonçalo", "12345678000155", "(21) 99999-1122", "São Gonçalo", "RJ")
