from dao.db_config import DatabaseConfig
from model.Aluno import Aluno

class AlunoDAO:

    def inserir(self, aluno):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO aluno(nome, matricula, email)
        VALUES (%s, %s, %s)
        RETURNING id
        """
        cursor.execute(sql, (aluno.nome, aluno.matricula, aluno.email))
        aluno.id = cursor.fetchone()[0]
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar(self):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, matricula, email FROM aluno")
        alunos = []
        for linha in cursor.fetchall():
            alunos.append(Aluno(linha[1], linha[2], linha[3], linha[0]))
        cursor.close()
        conexao.close()
        return alunos

    def buscar_por_nome(self, nome_busca):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, nome, matricula, email FROM aluno WHERE nome ILIKE %s"
        cursor.execute(sql, (f"%{nome_busca}%",))
        alunos = []
        for linha in cursor.fetchall():
            alunos.append(Aluno(linha[1], linha[2], linha[3], linha[0]))
        cursor.close()
        conexao.close()
        return alunos

    def atualizar(self, aluno):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """
            UPDATE aluno
            SET nome=%s, matricula=%s, email=%s
            WHERE id=%s
            """,
            (aluno.nome, aluno.matricula, aluno.email, aluno.id)
        )
        conexao.commit()
        cursor.close()
        conexao.close()

    def excluir(self, id_aluno):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM aluno WHERE id=%s", (id_aluno,))
        conexao.commit()
        cursor.close()
        conexao.close()
