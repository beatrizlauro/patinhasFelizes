# model.py
import sqlite3

def conectar():
    return sqlite3.connect('petshop.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_pet TEXT NOT NULL,
            especie TEXT NOT NULL,
            tutor TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_animal(nome_pet, especie, tutor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO animais (nome_pet, especie, tutor) VALUES (?, ?, ?)', (nome_pet, especie, tutor))
    conn.commit()
    conn.close()

def listar_animais():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animais')
    animais = cursor.fetchall()
    conn.close()
    return animais

def buscar_animal_por_nome(nome_pet):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animais WHERE nome = ?', (nome_pet,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_animal(id, nome_pet, especie, tutor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE animais SET nome_pet = ?, especie = ?, tutor = ? WHERE id = ?', (nome_pet, especie, tutor, id))
    conn.commit()
    conn.close()

def deletar_animal(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM animais WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# test_model.py
from .model import *

criar_tabela()
adicionar_animal("Bem", "Cachorro", "Maria")
adicionar_animal("Mingal", "Gato", "Augusto")

print("Todos os animais:")
for a in listar_animais():
    print(a)

print("Busca por nome:")
print(buscar_animal_por_nome("Bem"))