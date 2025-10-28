class GarantiaEstendida:
    def __init__(self, id_garantia_estendida, id_garantia, beneficios, custo):
        self.id_garantia_estendida = id_garantia_estendida
        self.id_garantia = id_garantia
        self.beneficios = beneficios
        self.custo = custo

    def __str__(self):
        return f"Garantia Estendida {self.id_garantia_estendida}: Benefícios - {self.beneficios}, Custo - R${self.custo:.2f}"
# Exemplo de uso
#garantia_estendida1 = GarantiaEstendida(1, 1, 1, "2024-03-10", "2026-03-10", "Ativa", ["Suporte técnico", "Reparo gratuito"], 500.0)

#print(garantia_estendida1)  # Saída: Garantia Estendida 1: 2024-03-10 - 2026-03-10 (Ativa, Benefícios: ['Suporte técnico', 'Reparo gratuito'], Custo: R$500.00)