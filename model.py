# Camada Model: responsável pela persistência (SQLite).

import sqlite3

DB_PATH = 'petshop.db'

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            tutor TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_pet(nome, especie, tutor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO pets (nome, especie, tutor) VALUES (?, ?, ?)',
        (nome, especie, tutor)
    )
    conn.commit()
    conn.close()

def listar_pets():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, especie, tutor FROM pets')
    rows = cursor.fetchall()
    conn.close()
    return [
        {'id': r[0], 'nome': r[1], 'especie': r[2], 'tutor': r[3]}
        for r in rows
    ]

def buscar_pet_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, especie, tutor FROM pets WHERE nome = ?', (nome,))
    rows = cursor.fetchall()
    conn.close()
    return [
        {'id': r[0], 'nome': r[1], 'especie': r[2], 'tutor': r[3]}
        for r in rows
    ]

def atualizar_pet(pet_id, nome, especie, tutor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE pets SET nome = ?, especie = ?, tutor = ? WHERE id = ?',
        (nome, especie, tutor, pet_id)
    )
    conn.commit()
    conn.close()

def deletar_pet(pet_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pets WHERE id = ?', (pet_id,))
    conn.commit()
    conn.close()