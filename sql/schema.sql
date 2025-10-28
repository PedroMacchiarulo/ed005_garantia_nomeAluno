-- Criação do banco de dados (opcional)
CREATE DATABASE garantia_notas;
\c garantia_notas;

-- ============================
-- TABELA: loja
-- ============================
CREATE TABLE loja (
    id_loja SERIAL PRIMARY KEY,
    nome_loja VARCHAR(100) NOT NULL UNIQUE,
    cnpj CHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(15),
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL CHECK (estado ~ '^[A-Z]{2}$')
);

-- ============================
-- TABELA: equipamento
-- ============================
CREATE TABLE equipamento (
    id_equipamento SERIAL PRIMARY KEY,
    id_loja INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    numero_serie VARCHAR(50) NOT NULL UNIQUE,
    data_compra DATE NOT NULL,
    
    CONSTRAINT fk_loja_equip FOREIGN KEY (id_loja)
        REFERENCES loja (id_loja)
        ON DELETE RESTRICT
);

-- ============================
-- TABELA: garantia
-- ============================
CREATE TABLE garantia (
    id_garantia SERIAL PRIMARY KEY,
    id_equipamento INT NOT NULL UNIQUE,
    id_loja INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL CHECK (data_fim > data_inicio),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Ativa', 'Expirada', 'Cancelada')),

    CONSTRAINT fk_equip_garantia FOREIGN KEY (id_equipamento)
        REFERENCES equipamento (id_equipamento)
        ON DELETE RESTRICT,

    CONSTRAINT fk_loja_garantia FOREIGN KEY (id_loja)
        REFERENCES loja (id_loja)
        ON DELETE RESTRICT
);