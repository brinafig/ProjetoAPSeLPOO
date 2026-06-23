import tkinter as tk
from tkinter import messagebox

from view.aluno_view import AlunoView
from view.professor_view import ProfessorView
from view.disciplina_view import DisciplinaView
from view.avaliacao_view import AvaliacaoView
from view.matricula_view import MatriculaView
from view.boletim_view import BoletimView
from view.portal_aluno_view import PortalAlunoView
from view.nota_view import NotaView

class MenuPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema Acadêmico")
        self.janela.geometry("600x400")

        barra = tk.Menu(self.janela)

        menu_admin = tk.Menu(barra, tearoff=0)
        menu_admin.add_command(label="Alunos", command=self.abrir_alunos)
        menu_admin.add_command(label="Professores", command=self.abrir_professores)
        menu_admin.add_command(label="Disciplinas", command=self.abrir_disciplinas)
        menu_admin.add_separator()
        menu_admin.add_command(label="Matrículas", command=self.abrir_matriculas)
        menu_admin.add_command(label="Criar Avaliações", command=self.abrir_avaliacoes)
        menu_admin.add_command(label="Registrar Notas dos Alunos", command=self.abrir_notas)
        menu_admin.add_command(label="Fechamento de Boletim", command=self.abrir_boletim)
        barra.add_cascade(label="Administração/Professores", menu=menu_admin)

        menu_aluno = tk.Menu(barra, tearoff=0)
        menu_aluno.add_command(label="Acessar Portal", command=self.abrir_portal)
        barra.add_cascade(label="Portal do Aluno", menu=menu_aluno)

        menu_ajuda = tk.Menu(barra, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)
        barra.add_cascade(label="Ajuda", menu=menu_ajuda)

        self.janela.config(menu=barra)
        self.janela.mainloop()

    def abrir_alunos(self):
        AlunoView()

    def abrir_professores(self):
        ProfessorView()

    def abrir_disciplinas(self):
        DisciplinaView()

    def abrir_matriculas(self):
        MatriculaView()

    def abrir_avaliacoes(self):
        AvaliacaoView()
        
    def abrir_notas(self):
        NotaView()

    def abrir_boletim(self):
        BoletimView()

    def abrir_portal(self):
        PortalAlunoView()

    def mostrar_sobre(self):
        texto = "Autora: Sabrina Figueiredo. \nGerenciador Acadêmico.\nSistema para gerenciar disciplinas, matricular alunos, cadastrar professores, avaliações e notas. Ao final do semestre o sistema calcula a média final e a frequência e mostra o status do aluno."
        messagebox.showinfo("Sobre", texto)
