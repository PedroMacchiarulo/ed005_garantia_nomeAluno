-- ==============================================
-- Inserindo dados na tabela LOJA
-- ==============================================
INSERT INTO loja (nome_loja, cnpj, telefone, cidade, estado)
VALUES
('Tech Store Niterói', '12345678000199', '(21) 99999-1111', 'Niterói', 'RJ'),
('Eletrônicos Alpha', '98765432000122', '(11) 98888-2222', 'São Paulo', 'SP'),
('Casa Digital', '56473829000144', '(31) 97777-3333', 'Belo Horizonte', 'MG');

-- ==============================================
-- Inserindo dados na tabela EQUIPAMENTO
-- ==============================================
INSERT INTO equipamento (id_loja, nome, marca, numero_serie, data_compra)
VALUES
(1, 'Notebook Lenovo Ideapad 3', 'Lenovo', 'LEN12345', '2024-03-10'),
(1, 'Monitor LG 24"', 'LG', 'LG98765', '2024-05-22'),
(2, 'Impressora HP LaserJet', 'HP', 'HP54321', '2024-07-15');

-- ==============================================
-- Inserindo dados na tabela GARANTIA
-- ==============================================
INSERT INTO garantia (id_equipamento, id_loja, data_inicio, data_fim, status)
VALUES
(1, 1, '2024-03-10', '2025-03-10', 'Ativa'),
(2, 1, '2024-05-22', '2025-05-22', 'Ativa'),
(3, 2, '2024-07-15', '2025-07-15', 'Ativa');