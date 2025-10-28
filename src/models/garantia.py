class Garantia:
    """
    Representa uma garantia com id do equipamento, id da loja, data de início, data de fim e status.
    """
    def __init__(self, id_garantia, id_equipamento, id_loja, data_inicio, data_fim, status):
        self.id_garantia = id_garantia
        self.id_equipamento = id_equipamento
        self.id_loja = id_loja
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status

    def __str__(self):
        return f"Garantia {self.id_garantia}: {self.data_inicio} - {self.data_fim} ({self.status})"

# Exemplo de uso
#garantia1 = Garantia(1, 1, 1, "2024-03-10", "2025-03-10", "Ativa")