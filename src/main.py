from database import Database

def main():
    db = Database()
    query = """
    SELECT e.nome, e.marca, g.data_inicio, g.data_fim, g.status, ge.beneficios, ge.custo
    FROM equipamento e
    JOIN garantia g ON e.id_equipamento = g.id_equipamento
    LEFT JOIN garantia_estendida ge ON g.id_garantia = ge.id_garantia
"""
    resultados = db.consultar(query)

    print("Equipamentos e Garantias:")
    for resultado in resultados:
        print(f"Equipamento: {resultado[0]} ({resultado[1]})")
        print(f"Garantia: {resultado[2]} - {resultado[3]} ({resultado[4]})")
        if resultado[5] is not None:
            print(f"Garantia Estendida: Benefícios - {resultado[5]}, Custo - R${resultado[6]:.2f}")
        else:
            print("Garantia Estendida: Não disponível")
        print("------------------------")
        

if __name__ == "__main__":
    main()

import unittest
from database import Database

class TestDatabase(unittest.TestCase):
    def test_consulta_garantia_estendida(self):
        db = Database()
        query = """
            SELECT e.nome, e.marca, g.data_inicio, g.data_fim, g.status, ge.beneficios, ge.custo
            FROM equipamento e
            JOIN garantia g ON e.id_equipamento = g.id_equipamento
            LEFT JOIN garantia_estendida ge ON g.id_garantia = ge.id_garantia
        """
        resultados = db.consultar(query)
        self.assertGreater(len(resultados), 0, "A consulta não retornou resultados")
        print(resultados)
if __name__ == "__main__":
    unittest.main()