# Camada View: interface gráfica (CustomTkinter).
# Comunica-se apenas com o Controller.

import customtkinter as ctk
from controller import PetsController

class PetsView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = PetsController()

        ctk.set_appearance_mode('dark')
        self.title('Patinhas Felizes')
        self.geometry('300x300')

        ctk.CTkButton(self, text='Cadastro', command=self.janela_cadastro).place(x=90, y=100)
        ctk.CTkButton(self, text='Consultar', command=self.janela_consulta).place(x=90, y=150)

    def janela_cadastro(self):
        win = ctk.CTkToplevel(self)
        win.grab_set()
        win.title('Cadastro')
        win.geometry('400x250')

        nome = ctk.CTkEntry(win, placeholder_text='Nome do Pet')
        nome.pack(pady=5)
        especie = ctk.CTkEntry(win, placeholder_text='Espécie')
        especie.pack(pady=5)
        tutor = ctk.CTkEntry(win, placeholder_text='Tutor')
        tutor.pack(pady=5)

        frame = ctk.CTkFrame(win)
        frame.pack(pady=10)
        ctk.CTkButton(frame, text='Cadastrar',
                      command=lambda: self.controller.cadastrar(
                          nome.get(), especie.get(), tutor.get()
                      )).grid(row=0, column=0, padx=5)
        ctk.CTkButton(frame, text='Buscar',
                      command=lambda: self._mostrar(self.controller.buscar_por_nome(nome.get()))
                      ).grid(row=0, column=1, padx=5)
        ctk.CTkButton(frame, text='Atualizar',
                      command=lambda: self._atualizar(nome.get(), especie.get(), tutor.get())
                      ).grid(row=0, column=2, padx=5)
        ctk.CTkButton(frame, text='Deletar',
                      command=lambda: self._deletar(nome.get())
                      ).grid(row=0, column=3, padx=5)

        self.area = ctk.CTkTextbox(win, width=350, height=100)
        self.area.pack(pady=5)

    def janela_consulta(self):
        win = ctk.CTkToplevel(self)
        win.grab_set()
        win.title('Consulta')
        win.geometry('400x300')

        ctk.CTkButton(win, text='Listar Todos',
                      command=lambda: self._mostrar(self.controller.listar())
                      ).pack(pady=10)
        self.area = ctk.CTkTextbox(win, width=350, height=200)
        self.area.pack(pady=5)

    def _mostrar(self, lista):
        self.area.configure(state='normal')
        self.area.delete('1.0', 'end')
        if not lista:
            self.area.insert('end', 'Nenhum registro encontrado.\n')
        else:
            for pet in lista:
                linha = f"ID:{pet['id']} | Nome:{pet['nome']} | Espécie:{pet['especie']} | Tutor:{pet['tutor']}\n"
                self.area.insert('end', linha)
        self.area.configure(state='disabled')

    def _atualizar(self, nome, especie, tutor):
        regs = self.controller.buscar_por_nome(nome)
        if regs:
            pet_id = regs[0]['id']
            self.controller.atualizar(pet_id, nome, especie, tutor)
            self._mostrar([{'id': pet_id, 'nome': nome, 'especie': especie, 'tutor': tutor}])

    def _deletar(self, nome):
        regs = self.controller.buscar_por_nome(nome)
        if regs:
            self.controller.deletar(regs[0]['id'])
            self._mostrar([])

if __name__ == '__main__':
    app = PetsView()
    app.mainloop()