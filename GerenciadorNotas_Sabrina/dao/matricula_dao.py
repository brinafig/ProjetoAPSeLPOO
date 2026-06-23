from dao.db_config import DatabaseConfig
from model.Matricula import Matricula
from model.Status import Status

class MatriculaDAO:

    def inserir(self, matricula):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO matricula(aluno_id, disciplina_id, presencas, status)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (
                matricula.aluno.id,
                matricula.disciplina.id,
                matricula.presencas,
                matricula.status.value
            )
        )

        matricula.id = cursor.fetchone()[0]

        conexao.commit()
        cursor.close()
        conexao.close()

    def listar(self):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id, aluno_id, disciplina_id, presencas, status
            FROM matricula
            """
        )

        matriculas = []

        for linha in cursor.fetchall():

            matriculas.append(
                Matricula(
                    linha[1],          # aluno (id)
                    linha[2],          # disciplina (id)
                    linha[3],
                    Status(linha[4]),
                    linha[0]
                )
            )

        cursor.close()
        conexao.close()

        return matriculas

    def atualizar(self, matricula):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE matricula
            SET presencas=%s,
                status=%s
            WHERE id=%s
            """,
            (
                matricula.presencas,
                matricula.status.value,
                matricula.id
            )
        )

        conexao.commit()
        cursor.close()
        conexao.close()

    def excluir(self, id_matricula):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM matricula WHERE id=%s",
            (id_matricula,)
        )

        conexao.commit()
        cursor.close()
        conexao.close()