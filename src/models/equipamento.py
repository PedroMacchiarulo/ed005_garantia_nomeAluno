class Equipamento:
    """
    Representa um equipamento com id da loja, nome, marca, número de série e data de compra.
    """
    def __init__(self, id_equipamento, id_loja, nome, marca, numero_serie, data_compra):
        self.id_equipamento = id_equipamento
        self.id_loja = id_loja
        self.nome = nome
        self.marca = marca
        self.numero_serie = numero_serie
        self.data_compra = data_compra

    def __str__(self):
        return f"Equipamento {self.id_equipamento}: {self.nome} ({self.marca}, {self.numero_serie})"

# Exemplo de uso
#equipamento1 = Equipamento(1, 1, "Notebook Lenovo Ideapad 3", "Lenovo", "LEN12345", "2024-03-10")
