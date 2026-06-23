import tkinter as tk
from tkinter import ttk, messagebox
from dao.matricula_dao import MatriculaDAO
from dao.aluno_dao import AlunoDAO
from dao.disciplina_dao import DisciplinaDAO
from model.Matricula import Matricula
from model.Aluno import Aluno
from model.Disciplina import Disciplina
from model.Status import Status

class MatriculaView:
    def __init__(self):
        self.dao = MatriculaDAO()
        self.aluno_dao = AlunoDAO()
        self.disciplina_dao = DisciplinaDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Matrícula de Alunos")
        self.janela.geometry("600x400")

        tk.Label(self.janela, text="Selecione o Aluno:").pack(pady=5)
        self.cb_alunos = ttk.Combobox(self.janela, width=50)
        self.cb_alunos.pack()

        tk.Label(self.janela, text="Selecione a Disciplina:").pack(pady=5)
        self.cb_disciplinas = ttk.Combobox(self.janela, width=50)
        self.cb_disciplinas.pack()

        tk.Button(self.janela, text="Efetuar Matrícula", command=self.salvar).pack(pady=15)

        self.tabela = ttk.Treeview(self.janela, columns=("id", "id_aluno", "id_disciplina"), show="headings")
        self.tabela.heading("id", text="ID Matrícula")
        self.tabela.heading("id_aluno", text="ID Aluno")
        self.tabela.heading("id_disciplina", text="ID Disciplina")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

        self.carregar_comboboxes()
        self.listar()

    def carregar_comboboxes(self):
        self.cb_alunos['values'] = [f"{a.id} - {a.nome}" for a in self.aluno_dao.listar()]
        self.cb_disciplinas['values'] = [f"{d.id} - {d.nome}" for d in self.disciplina_dao.listar()]

    def salvar(self):
        al_sel = self.cb_alunos.get()
        disc_sel = self.cb_disciplinas.get()

        if not al_sel or not disc_sel:
            return messagebox.showerror("Erro", "Selecione aluno e disciplina.")

        id_aluno = int(al_sel.split(" - ")[0])
        id_disciplina = int(disc_sel.split(" - ")[0])

        aluno = Aluno("", "", id=id_aluno)
        disciplina = Disciplina("", None, id=id_disciplina)
        
        matricula = Matricula(aluno, disciplina, presencas=0, status=Status.RECUPERACAO)
        self.dao.inserir(matricula)
        
        messagebox.showinfo("Sucesso", "Matrícula efetuada com sucesso!")
        self.listar()

    def listar(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        for m in self.dao.listar():
            
            id_a = m.aluno if isinstance(m.aluno, int) else m.aluno.id
            id_d = m.disciplina if isinstance(m.disciplina, int) else m.disciplina.id
            self.tabela.insert("", tk.END, values=(m.id, id_a, id_d))