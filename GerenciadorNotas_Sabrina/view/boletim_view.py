import tkinter as tk
from tkinter import ttk, messagebox
from dao.matricula_dao import MatriculaDAO
from dao.avaliacao_dao import AvaliacaoDAO
from dao.disciplina_dao import DisciplinaDAO
from dao.aluno_dao import AlunoDAO
from dao.nota_dao import NotaDAO
from model.Disciplina import Disciplina
from model.NotificadorEmail import NotificadorEmail
from model.Status import Status

class BoletimView:
    def __init__(self):
        self.mat_dao = MatriculaDAO()
        self.ava_dao = AvaliacaoDAO()
        self.disc_dao = DisciplinaDAO()
        self.aluno_dao = AlunoDAO()
        self.nota_dao = NotaDAO()

        self.janela = tk.Toplevel()
        self.janela.title("Fechamento de Notas")
        self.janela.geometry("500x450")

        tk.Label(self.janela, text="Selecione a Matrícula (ID):").pack(pady=10)
        self.cb_matricula = ttk.Combobox(self.janela, width=30)
        self.cb_matricula.pack(pady=5)
        self.carregar_matriculas()

        tk.Label(self.janela, text="Total de Presenças do Aluno:").pack(pady=10)
        self.presencas = tk.Entry(self.janela, width=20)
        self.presencas.pack()

        tk.Button(self.janela, text="Calcular Fechamento", command=self.calcular_fechamento).pack(pady=20)

        self.resultado_lbl = tk.Label(self.janela, text="Resultado: Aguardando...", font=("Arial", 11), justify="left")
        self.resultado_lbl.pack(pady=20)

    def carregar_matriculas(self):
        matriculas = self.mat_dao.listar()
        self.cb_matricula['values'] = [str(m.id) for m in matriculas]

    def calcular_fechamento(self):
        mat_id_str = self.cb_matricula.get().strip()
        presencas_str = self.presencas.get().strip()
        
        if not mat_id_str or not presencas_str:
            return messagebox.showerror("Erro", "Selecione uma matrícula e informe as presenças.")

        try:
            mat_id = int(mat_id_str)
            qtd_presencas = int(presencas_str)
        except ValueError:
            return messagebox.showerror("Erro", "Valores numéricos inválidos.")

        matricula_atual = next((m for m in self.mat_dao.listar() if m.id == mat_id), None)
        if not matricula_atual:
            return messagebox.showerror("Erro", "Matrícula não encontrada.")

        disc_atual = next((d for d in self.disc_dao.listar() if d.id == matricula_atual.disciplina), None)
        total_aulas = disc_atual.total_aulas if disc_atual else 0
        frequencia = (qtd_presencas / total_aulas * 100) if total_aulas > 0 else 0

        avaliacoes_disciplina = self.ava_dao.listar_por_disciplina(disc_atual.id)
        notas_lancadas = self.nota_dao.listar_por_matricula(mat_id)
        
        pesos = sum(a.peso for a in avaliacoes_disciplina)
        total_notas = 0
        
        for ava in avaliacoes_disciplina:
            nota_obj = next((n for n in notas_lancadas if n.avaliacao_id == ava.id), None)
            valor_nota = nota_obj.valor if nota_obj else 0.0
            total_notas += (ava.peso * valor_nota)

        if pesos == 0:
            return messagebox.showerror("Erro", "A disciplina não possui avaliações com peso.")

        media_final = total_notas / pesos
        
        if frequencia < 75:
            status_final = Status.REPROVADO
            motivo = "Reprovado por Falta"
        elif media_final >= 6:
            status_final = Status.APROVADO
            motivo = "Aprovado por Média"
        else:
            status_final = Status.RECUPERACAO
            motivo = "Em Recuperação"

        texto_exibicao = (
            f"Média Final: {media_final:.1f}\n"
            f"Frequência: {frequencia:.1f}%\n"
            f"Status: {status_final.value} ({motivo})"
        )
        self.resultado_lbl.config(text=texto_exibicao)

        matricula_atual.presencas = qtd_presencas
        matricula_atual.status = status_final
        self.mat_dao.atualizar(matricula_atual)

        aluno = next((a for a in self.aluno_dao.listar() if a.id == matricula_atual.aluno), None)
        email_destino = aluno.email if aluno and aluno.email else "E-mail não cadastrado"

        disciplina_notificadora = Disciplina("Sistema Acadêmico", None)
        observador_email = NotificadorEmail(email_destino)
        disciplina_notificadora.registrar_observador(observador_email)
        disciplina_notificadora.notificar(f"Sua média: {media_final:.1f}. Status: {status_final.value}")