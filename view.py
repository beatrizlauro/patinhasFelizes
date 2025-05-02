# controller.py
# Para utilizar a biblioteca customtkinter é necessário executar o comando abaixo no cmd
#       pip install customtkinter

import customtkinter as ctk

class PetsView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        # Configuração aparencia
        ctk.set_appearance_mode('dark')

        # Criação da Janela Principal
        self.title('Patinhas Felizes')
        self.geometry('300x300')

        # Botão para abrir a janela de cadastro
        btn_janela_cadastro = ctk.CTkButton(master=self, text='Cadastro', command=self.janela_cadastro).place(x=90, y=100)

        # Botão para consultar os pets cadastrados
        btn_janela_consulta = ctk.CTkButton(master=self, text='Consultar', command=self.janela_consulta).place(x=90, y=150)

    # Criação da Janela de Cadastro
    def janela_cadastro(self):
        janela_cadastro = ctk.CTkToplevel(self)
        janela_cadastro.grab_set()
        janela_cadastro.title('Cadastro')
        janela_cadastro.geometry('650x300')

        # Criação dos campos da Janela de Cadastro
        label_pet = ctk.CTkLabel(janela_cadastro, text='Nome do Pet')
        label_pet.pack(pady=5)
        self.nome_pet = ctk.CTkEntry(janela_cadastro, placeholder_text='Digite o nome do pet')
        self.nome_pet.pack(pady=5)

        label_especie = ctk.CTkLabel(janela_cadastro, text='Espécie')
        label_especie.pack(pady=5)
        self.especie = ctk.CTkEntry(janela_cadastro, placeholder_text='Digite a espécie do pet')
        self.especie.pack(pady=5)

        label_tutor = ctk.CTkLabel(janela_cadastro, text='Tutor')
        label_tutor.pack(pady=5)
        self.tutor = ctk.CTkEntry(janela_cadastro, placeholder_text= 'Digite o nome do Tutor')
        self.tutor.pack(pady=5)

        # Criação de um frame para conter os botões
        frame_janela_cadastro = ctk.CTkFrame(janela_cadastro, width=280, height=50)
        frame_janela_cadastro.pack(padx=10, pady=10)

        # Botão para adicionar pet na lista
        btn_adicionar_animal = ctk.CTkButton(frame_janela_cadastro, text='Cadastrar', command=lambda: self.controller.adicionar_pet(
                                            self.nome_pet.get(),
                                            self.especie.get(),
                                            self.tutor.get()
        ))

        # Botão para deletar o pet da lista
        btn_deletar_animal = ctk.CTkButton(frame_janela_cadastro, text='Deletar', command=lambda: self.controller.deletar_animal(self.nome_pet.get()))

        # Botão para buscar animal
        btn_buscar_animal_por_nome = ctk.CTkButton(frame_janela_cadastro, text='Buscar', command=lambda: self.controller.buscar_animal_por_nome(self.nome_pet.get()))
        
        # Botão para atualizar os dados do pet
        btn_atualizar_animal = ctk.CTkButton(frame_janela_cadastro, text='Atualizar', command=lambda: self.controller.atualizar_animal(
                                            self.nome_pet.get(),
                                            self.especie.get(),
                                            self.tutor.get()
        ))
        
        # Posicionamento dos botões dentro do frame
        btn_adicionar_animal.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        btn_buscar_animal_por_nome.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        btn_deletar_animal.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        btn_atualizar_animal.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
            
    # Criação da Janela de Consulta
    def janela_consulta(self):
        janela_consulta = ctk.CTkToplevel(self)
        janela_consulta.grab_set()
        janela_consulta.title('Consulta')
        janela_consulta.geometry('650x300')

        label_lista = ctk.CTkLabel(janela_consulta, text="Lista de Pets Cadastrados")
        label_lista.pack(pady=10)

        # Botão para listar os animais (chama o controller)
        btn_listar_animais = ctk.CTkButton(
            janela_consulta,
            text='Listar',
            command=self.listar_animais
            )
        btn_listar_animais.pack(pady=10)

        # Textbox para exibir os dados
        self.textbox_pets = ctk.CTkTextbox(janela_consulta, width=600, height=250)
        self.textbox_pets.pack(pady=10)
    
    def listar_animais(self):
    # Solicita os dados do controller
        dados = self.controller.listar_animais()  # <- Precisa retornar uma lista de dicionários

        # Libera edição do textbox para escrever
        self.textbox_pets.configure(state="normal")
        self.textbox_pets.delete("1.0", "end")  # Limpa conteúdo anterior

        # Verifica se há dados
        if not dados:
            self.textbox_pets.insert("end", "Nenhum pet cadastrado.\n")
        else:
            for pet in dados:
                linha = f"Nome: {pet['nome']} | Espécie: {pet['especie']} | Tutor: {pet['tutor']}\n"
                self.textbox_pets.insert("end", linha)

        # Bloqueia a edição novamente
        self.textbox_pets.configure(state="disabled")
        
# Iniciar a aplicação
if __name__ == "__main__":
    app = PetsView(controller=None)
    app.mainloop()
    