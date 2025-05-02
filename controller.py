# Camada Controller: lógica de negócio e mediação entre Model e View.

from model import criar_tabela, adicionar_pet, listar_pets, buscar_pet_por_nome, atualizar_pet, deletar_pet

class PetsController:
    def __init__(self):
        criar_tabela()

    def cadastrar(self, nome, especie, tutor):
        adicionar_pet(nome, especie, tutor)

    def listar(self):
        return listar_pets()

    def buscar_por_nome(self, nome):
        return buscar_pet_por_nome(nome)

    def atualizar(self, pet_id, nome, especie, tutor):
        atualizar_pet(pet_id, nome, especie, tutor)

    def deletar(self, pet_id):
        deletar_pet(pet_id)