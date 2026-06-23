from dao.db_config import DatabaseConfig
from model.Avaliacao import Avaliacao

class AvaliacaoDAO:
    def inserir(self, avaliacao):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO avaliacao(nome, peso, data, disciplina_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """
        cursor.execute(sql, (avaliacao.nome, avaliacao.peso, avaliacao.data, avaliacao.disciplina_id))
        avaliacao.id = cursor.fetchone()[0]
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar_por_disciplina(self, disciplina_id):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, peso, data, disciplina_id FROM avaliacao WHERE disciplina_id = %s",
            (disciplina_id,)
        )
        avaliacoes = []
        for linha in cursor.fetchall():
            avaliacoes.append(Avaliacao(linha[1], float(linha[2]), linha[3], linha[4], linha[0]))
        cursor.close()
        conexao.close()
        return avaliacoes