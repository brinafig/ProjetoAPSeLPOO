import tkinter as tk
from tkinter import ttk, messagebox
from model.Aluno import Aluno
from dao.aluno_dao import AlunoDAO

class AlunoView:
    def __init__(self):
        self.dao = AlunoDAO()
        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Alunos")
        self.janela.geometry("700x600")

        frame_cadastro = tk.Frame(self.janela)
        frame_cadastro.pack(pady=10)

        tk.Label(frame_cadastro, text="Nome").grid(row=0, column=0, padx=5, pady=5)
        self.nome = tk.Entry(frame_cadastro, width=40)
        self.nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_cadastro, text="Matrícula").grid(row=1, column=0, padx=5, pady=5)
        self.matricula = tk.Entry(frame_cadastro, width=40)
        self.matricula.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_cadastro, text="E-mail").grid(row=2, column=0, padx=5, pady=5)
        self.email = tk.Entry(frame_cadastro, width=40)
        self.email.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(frame_cadastro, text="Salvar Novo", command=self.salvar).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Separator(self.janela, orient='horizontal').pack(fill='x', pady=5)

        frame_busca = tk.Frame(self.janela)
        frame_busca.pack(pady=5)
        tk.Label(frame_busca, text="Buscar por Nome:").pack(side=tk.LEFT, padx=5)
        self.entrada_busca = tk.Entry(frame_busca, width=30)
        self.entrada_busca.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_busca, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_busca, text="Limpar Filtro", command=self.listar).pack(side=tk.LEFT, padx=5)

        frame_acoes = tk.Frame(self.janela)
        frame_acoes.pack(pady=5)
        tk.Button(frame_acoes, text="Atualizar Selecionado", command=self.atualizar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_acoes, text="Excluir Selecionado", command=self.excluir).pack(side=tk.LEFT, padx=5)

        self.tabela = ttk.Treeview(self.janela, columns=("id", "nome", "matricula", "email"), show="headings")
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("matricula", text="Matrícula")
        self.tabela.heading("email", text="E-mail")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tabela.bind("<ButtonRelease-1>", self.preencher_campos)
        self.listar()

    def preencher_campos(self, event):
        selecionado = self.tabela.selection()
        if selecionado:
            valores = self.tabela.item(selecionado[0], 'values')
            self.nome.delete(0, tk.END)
            self.nome.insert(tk.END, valores[1])
            self.matricula.delete(0, tk.END)
            self.matricula.insert(tk.END, valores[2])
            self.email.delete(0, tk.END)
            self.email.insert(tk.END, valores[3])

    def salvar(self):
        if not self.nome.get().strip() or not self.matricula.get().strip():
            return messagebox.showerror("Erro", "Nome e Matrícula são obrigatórios.")

        aluno = Aluno(self.nome.get(), self.matricula.get(), self.email.get())
        self.dao.inserir(aluno)
        messagebox.showinfo("Sucesso", "Aluno cadastrado")
        self.limpar_campos()
        self.listar()

    def atualizar(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            return messagebox.showwarning("Aviso", "Selecione um aluno na tabela.")

        id_aluno = self.tabela.item(selecionado[0], 'values')[0]
        aluno = Aluno(self.nome.get(), self.matricula.get(), self.email.get(), id=id_aluno)
        
        self.dao.atualizar(aluno)
        messagebox.showinfo("Sucesso", "Aluno atualizado!")
        self.limpar_campos()
        self.listar()

    def excluir(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            return messagebox.showwarning("Aviso", "Selecione um aluno na tabela.")
            
        id_aluno = self.tabela.item(selecionado[0], 'values')[0]
        self.dao.excluir(id_aluno)
        messagebox.showinfo("Sucesso", "Aluno excluído!")
        self.limpar_campos()
        self.listar()

    def limpar_campos(self):
        self.nome.delete(0, tk.END)
        self.matricula.delete(0, tk.END)
        self.email.delete(0, tk.END)

    def listar(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for aluno in self.dao.listar():
            self.tabela.insert("", tk.END, values=(aluno.id, aluno.nome, aluno.matricula, aluno.email))

    def buscar(self):
        termo = self.entrada_busca.get().strip()
        if not termo: return self.listar()
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for aluno in self.dao.buscar_por_nome(termo):
            self.tabela.insert("", tk.END, values=(aluno.id, aluno.nome, aluno.matricula, aluno.email))