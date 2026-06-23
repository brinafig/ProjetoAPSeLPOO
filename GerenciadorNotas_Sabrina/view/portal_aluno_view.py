import tkinter as tk
from tkinter import ttk, messagebox
from dao.aluno_dao import AlunoDAO
from dao.matricula_dao import MatriculaDAO
from dao.avaliacao_dao import AvaliacaoDAO
from dao.disciplina_dao import DisciplinaDAO
from dao.nota_dao import NotaDAO

class PortalAlunoView:
    def __init__(self):
        self.aluno_dao = AlunoDAO()
        self.mat_dao = MatriculaDAO()
        self.ava_dao = AvaliacaoDAO()
        self.disc_dao = DisciplinaDAO()
        self.nota_dao = NotaDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Portal do Aluno - Consultar Dados")
        self.janela.geometry("650x500")

        tk.Label(self.janela, text="Digite sua Matrícula (ex: 20242PF.CC0019):", font=("Arial", 10)).pack(pady=10)
        
        frame_busca = tk.Frame(self.janela)
        frame_busca.pack(pady=5)
        self.entrada_matricula = tk.Entry(frame_busca, width=30)
        self.entrada_matricula.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_busca, text="Consultar", command=self.consultar_dados).pack(side=tk.LEFT)

        self.info_lbl = tk.Label(self.janela, text="", font=("Arial", 10), justify="left")
        self.info_lbl.pack(pady=10)

        self.tabela = ttk.Treeview(self.janela, columns=("avaliacao", "data", "peso", "nota"), show="headings")
        self.tabela.heading("avaliacao", text="Avaliação")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("peso", text="Peso")
        self.tabela.heading("nota", text="Nota Obtida")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

    def consultar_dados(self):
        matricula_texto = self.entrada_matricula.get().strip()
        if not matricula_texto:
            return messagebox.showerror("Erro", "Informe a matrícula.")

        aluno = next((a for a in self.aluno_dao.listar() if a.matricula == matricula_texto), None)
        if not aluno:
            return messagebox.showerror("Erro", "Aluno não encontrado.")

        matriculas_aluno = [m for m in self.mat_dao.listar() if m.aluno == aluno.id]
        if not matriculas_aluno:
            return messagebox.showinfo("Aviso", "Este aluno não está matriculado em nenhuma disciplina.")
            
        matricula = matriculas_aluno[0]

        disciplina = next((d for d in self.disc_dao.listar() if d.id == matricula.disciplina), None)
        total_aulas = disciplina.total_aulas if disciplina else 0
        frequencia = (matricula.presencas / total_aulas * 100) if total_aulas > 0 else 0

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        avaliacoes_disciplina = self.ava_dao.listar_por_disciplina(disciplina.id)
        notas_lancadas = self.nota_dao.listar_por_matricula(matricula.id)
        
        pesos = 0
        total_notas = 0

        for ava in avaliacoes_disciplina:
    
            nota_obj = next((n for n in notas_lancadas if n.avaliacao_id == ava.id), None)
            valor_nota = nota_obj.valor if nota_obj else 0.0
            texto_nota = f"{valor_nota:.1f}" if nota_obj else "Pendente"
            
            self.tabela.insert("", tk.END, values=(ava.nome, ava.data, ava.peso, texto_nota))
            
            pesos += ava.peso
            total_notas += (ava.peso * valor_nota)

        media = (total_notas / pesos) if pesos > 0 else 0

        texto_info = (
            f"Aluno: {aluno.nome} | E-mail: {aluno.email}\n"
            f"Disciplina: {disciplina.nome if disciplina else 'N/A'}\n"
            f"Frequência: {frequencia:.1f}% ({matricula.presencas}/{total_aulas} presenças)\n"
            f"Média Atual: {media:.1f}\n"
            f"Situação Final: {matricula.status.value}"
        )
        self.info_lbl.config(text=texto_info)