from dao.db_config import DatabaseConfig
from model.Disciplina import Disciplina
from model.Professor import Professor

class DisciplinaDAO:

    def inserir(self, disciplina):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO disciplina(nome, total_aulas, professor_id)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (disciplina.nome, disciplina.total_aulas, disciplina.professor.id)
        )
        disciplina.id = cursor.fetchone()[0]
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar(self):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, total_aulas, professor_id FROM disciplina")
        
        disciplinas = []
        for linha in cursor.fetchall():
            prof_id = linha[3]
            disciplinas.append(
                Disciplina(linha[1], prof_id, total_aulas=linha[2], id=linha[0])
            )
            
        cursor.close()
        conexao.close()
        return disciplinas

    def atualizar(self, disciplina):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """
            UPDATE disciplina
            SET nome=%s, total_aulas=%s, professor_id=%s
            WHERE id=%s
            """,
            (disciplina.nome, disciplina.total_aulas, disciplina.professor.id, disciplina.id)
        )
        conexao.commit()
        cursor.close()
        conexao.close()

    def excluir(self, id_disciplina):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM disciplina WHERE id=%s", (id_disciplina,))
        conexao.commit()
        cursor.close()
        conexao.close()