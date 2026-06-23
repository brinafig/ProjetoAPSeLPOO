import tkinter as tk
from tkinter import ttk, messagebox
from dao.avaliacao_dao import AvaliacaoDAO
from dao.disciplina_dao import DisciplinaDAO
from model.Avaliacao import Avaliacao

class AvaliacaoView:
    def __init__(self):
        self.dao = AvaliacaoDAO()
        self.disc_dao = DisciplinaDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Gerenciar Avaliações da Disciplina (UC02)")
        self.janela.geometry("650x550")

        frame_cad = tk.Frame(self.janela)
        frame_cad.pack(pady=10)

        tk.Label(frame_cad, text="Disciplina").grid(row=0, column=0, padx=5, pady=5)
        self.cb_disc = ttk.Combobox(frame_cad, width=35)
        self.cb_disc.grid(row=0, column=1, padx=5, pady=5)
        self.cb_disc['values'] = [f"{d.id} - {d.nome}" for d in self.disc_dao.listar()]

        tk.Label(frame_cad, text="Nome da Avaliação").grid(row=1, column=0, padx=5, pady=5)
        self.nome = tk.Entry(frame_cad, width=38)
        self.nome.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_cad, text="Peso (ex: 3.0)").grid(row=2, column=0, padx=5, pady=5)
        self.peso = tk.Entry(frame_cad, width=38)
        self.peso.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_cad, text="Data (ex: 23/04/2026)").grid(row=3, column=0, padx=5, pady=5)
        self.data = tk.Entry(frame_cad, width=38)
        self.data.grid(row=3, column=1, padx=5, pady=5)

        # Botão duplo (Salvar e Listar)
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=5)
        tk.Button(frame_botoes, text="Salvar Avaliação", command=self.salvar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Listar Avaliações da Disciplina", command=self.listar).pack(side=tk.LEFT, padx=10)

        self.tabela = ttk.Treeview(self.janela, columns=("id", "nome", "data", "peso"), show="headings")
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Avaliação")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("peso", text="Peso")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

    def salvar(self):
        disc_sel = self.cb_disc.get()
        if not disc_sel or not self.nome.get() or not self.peso.get():
            return messagebox.showerror("Erro", "Disciplina, Nome e Peso são obrigatórios.")

        id_disc = int(disc_sel.split(" - ")[0])
        peso = float(self.peso.get())
        
        avaliacao = Avaliacao(self.nome.get(), peso, self.data.get(), disciplina_id=id_disc)
        self.dao.inserir(avaliacao)
        messagebox.showinfo("Sucesso", "Avaliação criada para a disciplina!")
        self.listar()

    def listar(self):
        disc_sel = self.cb_disc.get()
        if not disc_sel:
            return messagebox.showwarning("Aviso", "Selecione uma disciplina na lista acima para ver as avaliações dela.")

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        id_disc = int(disc_sel.split(" - ")[0])
        for a in self.dao.listar_por_disciplina(id_disc):
            self.tabela.insert("", tk.END, values=(a.id, a.nome, a.data, a.peso))