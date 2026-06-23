from dao.db_config import DatabaseConfig
from model.Professor import Professor

class ProfessorDAO:

    def inserir(self, professor):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO professor(nome, titulo)
        VALUES (%s, %s)
        RETURNING id
        """

        cursor.execute(
            sql,
            (professor.nome, professor.titulo)
        )

        professor.id = cursor.fetchone()[0]

        conexao.commit()

        cursor.close()
        conexao.close()

    def listar(self):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, titulo FROM professor"
        )

        professores = []

        for linha in cursor.fetchall():

            professores.append(
                Professor(
                    linha[1],
                    linha[2],
                    linha[0]
                )
            )

        cursor.close()
        conexao.close()

        return professores

    def atualizar(self, professor):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE professor
            SET nome=%s,
                titulo=%s
            WHERE id=%s
            """,
            (
                professor.nome,
                professor.titulo,
                professor.id
            )
        )

        conexao.commit()

        cursor.close()
        conexao.close()

    def excluir(self, id_professor):

        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM professor WHERE id=%s",
            (id_professor,)
        )

        conexao.commit()

        cursor.close()
        conexao.close()