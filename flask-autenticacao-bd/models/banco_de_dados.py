import sqlalchemy
import hashlib
import os

if __name__ != '__main__':
    from .aluno import Aluno


class BancoDeDados:
    def __init__(self):
        # ✅ caminho absoluto (resolve o erro do banco)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'dados.db')

        self.__engine = sqlalchemy.create_engine(f'sqlite:///{db_path}', echo=False)

    def criar_tabelas(self):
        with self.__engine.begin() as connection:
            connection.execute(sqlalchemy.text("""
                CREATE TABLE IF NOT EXISTS Aluno (
                    usuario VARCHAR(50) PRIMARY KEY,
                    senha VARCHAR(128) NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    curso VARCHAR(50),
                    data_inicio DATE,
                    media DECIMAL NOT NULL
                );
            """))

    def inserir_aluno(self, obj_aluno):
        with self.__engine.begin() as connection:
            t = sqlalchemy.text("""
                INSERT INTO Aluno 
                VALUES (:usuario, :senha, :nome, :curso, :data_inicio, :media)
            """)

            hash_da_senha = hashlib.sha512(obj_aluno.senha.encode('UTF-8')).hexdigest()

            # ✅ CORREÇÃO AQUI (dicionário)
            connection.execute(t, {
                "usuario": obj_aluno.usuario,
                "senha": hash_da_senha,
                "nome": obj_aluno.nome,
                "curso": obj_aluno.curso,
                "data_inicio": obj_aluno.data_inicio,
                "media": obj_aluno.media
            })

    def listar_alunos(self):
        alunos = []
        with self.__engine.connect() as connection:
            resultado = connection.execute(sqlalchemy.text("""
                SELECT usuario, senha, nome, curso, data_inicio, media 
                FROM Aluno ORDER BY usuario
            """))

            for linha in resultado:
                usuario, senha, nome, curso, data_inicio, media = linha
                alunos.append(Aluno(usuario, senha, nome, curso, data_inicio, media))

        return alunos

    def obter_aluno(self, usuario):
        with self.__engine.connect() as connection:
            t = sqlalchemy.text("""
                SELECT usuario, senha, nome, curso, data_inicio, media 
                FROM Aluno WHERE usuario = :user
            """)

            resultado = connection.execute(t, {"user": usuario})
            dado = resultado.fetchone()

            if dado:
                _, senha, nome, curso, data_inicio, media = dado
                return Aluno(usuario, senha, nome, curso, data_inicio, media)

        return None


if __name__ == '__main__':
    from aluno import Aluno

    print('O que deseja fazer?')
    print('   1- Criar tabelas e inserir dados no Banco de Dados')
    print('   2- Listar os dados gravados no Banco de Dados')

    opcao = input('Opcao: ').strip()

    bd = BancoDeDados()

    if opcao == '1':
        bd.criar_tabelas()

        bd.inserir_aluno(Aluno('rafael', '1234', 'Rafael Will', 'Ciência da Computação', '01/02/2022', 7.5))
        bd.inserir_aluno(Aluno('maria', '4321', 'Maria dos Santos', 'ADS', '11/08/2022', 8.6))
        bd.inserir_aluno(Aluno('jose', '9876', 'José Silva', 'SI', '31/05/2022', 6.9))
        bd.inserir_aluno(Aluno('ana', '5678', 'Ana Beatriz', 'Engenharia', '05/10/2022', 9.2))

        print("✅ Dados inseridos com sucesso!")

    elif opcao == '2':
        lista = bd.listar_alunos()

        for aluno in lista:
            print('-' * 50)
            print('Usuário:', aluno.usuario)
            print('Senha:', aluno.senha)
            print('Nome:', aluno.nome)
            print('Curso:', aluno.curso)
            print('Data início:', aluno.data_inicio)
            print('Média:', aluno.media)

    else:
        print("❌ Opção inválida")
