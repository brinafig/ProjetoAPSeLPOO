import tkinter as tk
from tkinter import ttk, messagebox

from dao.nota_dao import NotaDAO
from dao.matricula_dao import MatriculaDAO
from dao.avaliacao_dao import AvaliacaoDAO
from model.Nota import Nota

class NotaView:
    def __init__(self):
        self.dao = NotaDAO()
        self.mat_dao = MatriculaDAO()
        self.ava_dao = AvaliacaoDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Registrar Notas (UC04)")
        self.janela.geometry("600x400")

        self.matriculas = self.mat_dao.listar()

        tk.Label(self.janela, text="1. Selecione a Matrícula do Aluno").pack(pady=5)
        self.cb_mat = ttk.Combobox(self.janela, width=50, state="readonly")
        self.cb_mat.pack()
        self.carregar_matriculas()

        self.cb_mat.bind("<<ComboboxSelected>>", self.carregar_avaliacoes)

        tk.Label(self.janela, text="2. Selecione a Avaliação").pack(pady=5)
        self.cb_ava = ttk.Combobox(self.janela, width=50, state="readonly")
        self.cb_ava.pack()

        tk.Label(self.janela, text="3. Nota Obtida (ex: 8.5)").pack(pady=5)
        self.valor_nota = tk.Entry(self.janela, width=20)
        self.valor_nota.pack()

        tk.Button(self.janela, text="Salvar Nota", command=self.salvar).pack(pady=20)

    def carregar_matriculas(self):
        valores = []
        for m in self.matriculas:
        
            id_a = m.aluno if isinstance(m.aluno, int) else m.aluno.id
            id_d = m.disciplina if isinstance(m.disciplina, int) else m.disciplina.id
            valores.append(f"{m.id} - Aluno ID: {id_a} | Disc ID: {id_d}")
        
        self.cb_mat['values'] = valores

    def carregar_avaliacoes(self, event=None):
        mat_sel = self.cb_mat.get()
        if not mat_sel: return

        mat_id = int(mat_sel.split(" - ")[0])

        matricula_obj = next((m for m in self.matriculas if m.id == mat_id), None)
        if not matricula_obj: return

        id_d = matricula_obj.disciplina if isinstance(matricula_obj.disciplina, int) else matricula_obj.disciplina.id

        avaliacoes = self.ava_dao.listar_por_disciplina(id_d)
        
        if not avaliacoes:
            self.cb_ava['values'] = ["Nenhuma avaliação cadastrada nesta disciplina"]
            self.cb_ava.set("Nenhuma avaliação cadastrada nesta disciplina")
        else:
            self.cb_ava['values'] = [f"{a.id} - {a.nome} (Peso: {a.peso})" for a in avaliacoes]
            self.cb_ava.set("")  

    def salvar(self):
        mat_sel = self.cb_mat.get()
        ava_sel = self.cb_ava.get()
        
        if not mat_sel or not ava_sel or "Nenhuma" in ava_sel or not self.valor_nota.get().strip():
            return messagebox.showerror("Erro", "Preencha a nota e certifique-se de selecionar uma avaliação válida.")

        mat_id = int(mat_sel.split(" - ")[0])
        ava_id = int(ava_sel.split(" - ")[0])
        
        try:
            valor = float(self.valor_nota.get().strip())
        except ValueError:
            return messagebox.showerror("Erro", "A nota deve ser um número válido (use ponto para casas decimais).")
        
        nota = Nota(valor, ava_id, mat_id)
        self.dao.inserir(nota)
        
        messagebox.showinfo("Sucesso", "Nota registrada com sucesso no sistema!")
        self.valor_nota.delete(0, tk.END)