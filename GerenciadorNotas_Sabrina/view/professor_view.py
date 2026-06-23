import tkinter as tk
from tkinter import ttk, messagebox

from dao.professor_dao import ProfessorDAO
from model.Professor import Professor


class ProfessorView:

    def __init__(self):
        self.dao = ProfessorDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Professores")
        self.janela.geometry("600x500")

        frame_cadastro = tk.Frame(self.janela)
        frame_cadastro.pack(pady=10)

        tk.Label(frame_cadastro, text="Nome").grid(row=0, column=0, padx=5, pady=5)
        self.nome = tk.Entry(frame_cadastro, width=40)
        self.nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_cadastro, text="Título").grid(row=1, column=0, padx=5, pady=5)
        self.titulo = tk.Entry(frame_cadastro, width=40)
        self.titulo.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_cadastro, text="Salvar Novo", command=self.salvar).grid(row=2, column=0, columnspan=2, pady=10)

        frame_acoes = tk.Frame(self.janela)
        frame_acoes.pack(pady=5)
        tk.Button(frame_acoes, text="Atualizar Selecionado", command=self.atualizar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_acoes, text="Excluir Selecionado", command=self.excluir).pack(side=tk.LEFT, padx=5)

        self.tabela = ttk.Treeview(self.janela, columns=("id", "nome", "titulo"), show="headings")
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("titulo", text="Título")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

        self.tabela.bind("<ButtonRelease-1>", self.preencher_campos)
        self.listar()

    def preencher_campos(self, event):
        selecionado = self.tabela.selection()
        if selecionado:
            valores = self.tabela.item(selecionado[0], 'values')
            self.nome.delete(0, tk.END)
            self.nome.insert(tk.END, valores[1])
            self.titulo.delete(0, tk.END)
            self.titulo.insert(tk.END, valores[2])

    def salvar(self):
        professor = Professor(self.nome.get(), self.titulo.get())
        self.dao.inserir(professor)
        self.listar()

    def atualizar(self):
        selecionado = self.tabela.selection()
        if not selecionado: return
        id_prof = self.tabela.item(selecionado[0], 'values')[0]
        professor = Professor(self.nome.get(), self.titulo.get(), id=id_prof)
        self.dao.atualizar(professor)
        self.listar()

    def excluir(self):
        selecionado = self.tabela.selection()
        if not selecionado: return
        id_prof = self.tabela.item(selecionado[0], 'values')[0]
        self.dao.excluir(id_prof)
        self.listar()

    def listar(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for professor in self.dao.listar():
            self.tabela.insert("", tk.END, values=(professor.id, professor.nome, professor.titulo))