from dao.db_config import DatabaseConfig
from model.Nota import Nota

class NotaDAO:
    def inserir(self, nota_obj):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO nota(valor, avaliacao_id, matricula_id)
        VALUES (%s, %s, %s)
        RETURNING id
        """
        cursor.execute(sql, (nota_obj.valor, nota_obj.avaliacao_id, nota_obj.matricula_id))
        nota_obj.id = cursor.fetchone()[0]
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar_por_matricula(self, matricula_id):
        conexao = DatabaseConfig.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, valor, avaliacao_id, matricula_id FROM nota WHERE matricula_id = %s", (matricula_id,))
        notas = []
        for linha in cursor.fetchall():
            notas.append(Nota(float(linha[1]), linha[2], linha[3], linha[0]))
        cursor.close()
        conexao.close()
        return notas