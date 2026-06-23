import tkinter as tk
from tkinter import ttk, messagebox
from dao.professor_dao import ProfessorDAO
from dao.disciplina_dao import DisciplinaDAO
from model.Disciplina import Disciplina
from model.Professor import Professor

class DisciplinaView:
    def __init__(self):
        self.dao = DisciplinaDAO()
        self.prof_dao = ProfessorDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Disciplinas")
        self.janela.geometry("600x500")

        frame_cad = tk.Frame(self.janela)
        frame_cad.pack(pady=10)

        tk.Label(frame_cad, text="Nome da Disciplina").grid(row=0, column=0, padx=5, pady=5)
        self.nome = tk.Entry(frame_cad, width=30)
        self.nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_cad, text="Total de Aulas").grid(row=1, column=0, padx=5, pady=5)
        self.total_aulas = tk.Entry(frame_cad, width=30)
        self.total_aulas.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_cad, text="Professor").grid(row=2, column=0, padx=5, pady=5)
        self.cb_professores = ttk.Combobox(frame_cad, width=27)
        self.cb_professores.grid(row=2, column=1, padx=5, pady=5)
        self.carregar_professores()

        tk.Button(frame_cad, text="Salvar Novo", command=self.salvar).grid(row=3, column=0, columnspan=2, pady=10)

        self.tabela = ttk.Treeview(self.janela, columns=("id", "nome", "aulas", "prof_id"), show="headings")
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("aulas", text="Total Aulas")
        self.tabela.heading("prof_id", text="ID Professor")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.listar()

    def carregar_professores(self):
        self.cb_professores["values"] = [f"{p.id} - {p.nome}" for p in self.prof_dao.listar()]

    def salvar(self):
        prof_sel = self.cb_professores.get()
        if not self.nome.get() or not self.total_aulas.get() or not prof_sel:
            return messagebox.showerror("Erro", "Preencha todos os campos!")

        id_prof = int(prof_sel.split(" - ")[0])
        aulas = int(self.total_aulas.get())
        disciplina = Disciplina(self.nome.get(), Professor("", "", id=id_prof), total_aulas=aulas)
        
        self.dao.inserir(disciplina)
        messagebox.showinfo("Sucesso", "Disciplina salva!")
        self.listar()

    def listar(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        for d in self.dao.listar():
           
            prof_id = d.professor if isinstance(d.professor, int) else getattr(d.professor, 'id', 'N/A')
            self.tabela.insert("", tk.END, values=(d.id, d.nome, d.total_aulas, prof_id))