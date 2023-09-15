from datetime import datetime, timedelta

import mysql.connector


def conectar_banco_de_dados():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="matheus",
        password="mvvb27052003",
        database="clone_anki",
    )


def tabelas_baralhos():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para criar a tabela "baralhos"
        create_table_query = """
            CREATE TABLE IF NOT EXISTS baralhos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                next_review DATETIME
            )
        """

        # Executar a consulta SQL para criar a tabela
        cursor.execute(create_table_query)
        print("Tabela 'baralhos' criada com sucesso!")

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def criar_baralho():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Solicitar ao usuário um nome para a tabela
        nome_tabela = input("Digite o nome do baralho que deseja criar: ")

        # Validar o nome da tabela para evitar injeção de SQL
        if not nome_tabela.isalnum():
            print("Nome de tabela inválido. Use apenas letras e números.")
            return

            # Consulta SQL para criar a tabela
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            front TEXT,
            back TEXT,
            difficulty DECIMAL(3, 2),
            next_review DATETIME
            )
        """

        # Executar a consulta SQL para criar a tabela
        cursor.execute(create_table_query)
        print(f"A tabela '{nome_tabela}' foi criada com sucesso!")

        # Inserir um registro na tabela de baralhos
        inserir_baralho_query = "INSERT INTO baralhos (nome) VALUES (%s)"
        cursor.execute(inserir_baralho_query, (nome_tabela,))

        # Executar a consulta SQL para criar a tabela do baralho
        cursor.execute(create_table_query)
        print(f"A tabela '{nome_tabela}' foi criada com sucesso!")

        conector.commit()

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def listar_baralhos():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para obter todos os nomes das tabelas no banco de dados
        show_tables_query = "SHOW TABLES"

        # Executar a consulta SQL
        cursor.execute(show_tables_query)

        # Obter os resultados da consulta
        tabelas = cursor.fetchall()

        # Exibir os nomes das tabelas ao usuário
        print("Tabelas existentes no banco de dados:")
        for tabela in tabelas:
            print(tabela[0])

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def listar_tabelas():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para obter todos os nomes das tabelas no banco de dados
        show_tables_query = "SHOW TABLES"

        # Executar a consulta SQL
        cursor.execute(show_tables_query)

        # Obter os resultados da consulta
        tabelas = cursor.fetchall()

        # Exibir os nomes das tabelas ao usuário
        print("Tabelas disponíveis:")
        for i, tabela in enumerate(tabelas, start=1):
            print(f"{i}. {tabela[0]}")

        # Solicitar ao usuário que escolha uma tabela pelo número
        escolha = int(input("Escolha o número da tabela onde deseja adicionar a carta: "))

        if 1 <= escolha <= len(tabelas):
            return tabelas[escolha - 1][0]
        else:
            print("Escolha inválida.")
            return None

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def adicionar_card(tabela):
    if tabela is None:
        return

    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Solicitar informações do card ao usuário
        front = input("Digite o conteúdo da frente do card: ")
        back = input("Digite o conteúdo do verso do card: ")

        # Consulta SQL para inserir o card na tabela escolhida
        inserir_card_query = f"INSERT INTO {tabela} (front, back) VALUES (%s, %s)"
        dados_card = (front, back)

        # Executar a consulta SQL para inserir o card
        cursor.execute(inserir_card_query, dados_card)
        conector.commit()
        print("Card adicionado com sucesso!")

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def verificar_tabela_baralhos():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para verificar se a tabela "baralhos" existe
        check_table_query = "SHOW TABLES LIKE 'baralhos'"

        # Executar a consulta SQL
        cursor.execute(check_table_query)

        # Verificar se a tabela existe
        if cursor.fetchone():
            print("A tabela 'baralhos' existe.")
        else:
            print("A tabela 'baralhos' não existe.")

    except mysql.connector.Error as err:
        print("Erro ao verificar a tabela 'baralhos':", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def listar_baralhos_com_numeros():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para obter todos os nomes das tabelas no banco de dados
        show_tables_query = "SHOW TABLES"

        # Executar a consulta SQL
        cursor.execute(show_tables_query)

        # Obter os resultados da consulta
        tabelas = cursor.fetchall()

        # Exibir os nomes das tabelas ao usuário com números
        print("Tabelas disponíveis:")
        for i, tabela in enumerate(tabelas, start=1):
            print(f"{i}. {tabela[0]}")

        return tabelas

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def apagar_baralho_por_numero():
    tabelas = listar_baralhos_com_numeros()

    if not tabelas:
        print("Nenhum baralho disponível para apagar.")
        return

    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        while True:
            try:
                res = int(input("Digite o número do baralho que deseja apagar: "))
                if 1 <= res <= len(tabelas):
                    nome_tabela = tabelas[res - 1][0]
                    break
                else:
                    print("Número fora do intervalo válido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

        # Confirmar com o usuário antes de apagar o baralho
        confirmacao = (
            input(f"Tem certeza que deseja apagar o baralho '{nome_tabela}'? (S/N): ")
            .strip()
            .lower()
        )
        if confirmacao == "s":
            cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela}")
            cursor.execute("DELETE FROM baralhos WHERE nome = %s", (nome_tabela,))
            conector.commit()
            print(f"O baralho '{nome_tabela}' foi apagado com sucesso!")
        else:
            print(f"O baralho '{nome_tabela}' não foi apagado.")

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def listar_baralhos():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para obter todos os nomes dos baralhos no banco de dados
        listar_baralhos_query = "SELECT id, nome FROM baralhos"

        # Executar a consulta SQL
        cursor.execute(listar_baralhos_query)

        # Obter os resultados da consulta
        baralhos = cursor.fetchall()

        if not baralhos:
            print("Nenhum baralho disponível.")
            return

        # Exibir os baralhos disponíveis e permitir que o usuário escolha um
        print("Baralhos disponíveis:")
        for baralho in baralhos:
            print(f"{baralho[0]}. {baralho[1]}")

        escolha = int(input("Escolha o número do baralho que deseja revisar: "))

        if 1 <= escolha <= len(baralhos):
            return baralhos[escolha - 1]
        else:
            print("Escolha inválida.")
            return None

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def listar_baralhos_com_numeros():
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para obter todos os nomes dos baralhos no banco de dados
        listar_baralhos_query = "SELECT id, nome FROM baralhos"

        # Executar a consulta SQL
        cursor.execute(listar_baralhos_query)

        # Obter os resultados da consulta
        baralhos = cursor.fetchall()

        if not baralhos:
            print("Nenhum baralho disponível.")
            return []

        # Exibir os baralhos disponíveis com números à esquerda
        print("Baralhos disponíveis:")
        for i, baralho in enumerate(baralhos, start=1):
            print(f"{i}. {baralho[1]}")

        return baralhos

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return []

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


def revisar_cartoes(baralho_id):
    try:
        conector = conectar_banco_de_dados()
        cursor = conector.cursor()

        # Consulta SQL para obter os cartões a serem revisados no baralho especificado
        revisao_query = """
             SELECT id, front, back, difficulty
             FROM {nome_da_sua_tabela}
             WHERE next_review <= %s
          """

        # Data atual
        data_atual = datetime.now()

        # Formatar a data atual como uma string no formato 'YYYY-MM-DD HH:MM:SS'
        data_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")
        # Substituir {nome_da_sua_tabela} pelo nome real da tabela
        revisao_query = revisao_query.format(nome_da_sua_tabela=str(f"{baralho_id}"))

        # Usar data_formatada como parâmetro na consulta SQL
        cursor.execute(revisao_query, (data_formatada,))

        # Obter os resultados da consulta
        cartoes = cursor.fetchall()

        if not cartoes:
            print("Nenhum cartão para revisar no momento.")
            return

        # Exibir os cartões a serem revisados
        for cartao in cartoes:
            print(f"Cartão ID: {cartao[0]}")
            print(f"Frente: {cartao[1]}")
            resposta = input("Lembrança (L) ou não (N)? ").strip().lower()

            if resposta == "l":
                # Se lembrado, aumentar a dificuldade (pode ajustar esse valor)
                nova_dificuldade = cartao[3] + 0.1
            else:
                # Se não lembrado, resetar a dificuldade (pode ajustar esse valor)
                nova_dificuldade = 1.0

            # Calcular a próxima data de revisão com base na nova dificuldade
            proxima_revisao = data_atual + timedelta(days=1) * nova_dificuldade

            # Atualizar o cartão com a nova dificuldade e próxima data de revisão
            atualizar_cartao_query = f"""
                UPDATE {baralho_id}
                SET difficulty = %s, next_review = %s
                WHERE id = %s
            """

            dados_atualizar_cartao = (nova_dificuldade, proxima_revisao, cartao[0])
            cursor.execute(atualizar_cartao_query, dados_atualizar_cartao)
            conector.commit()

        print("Revisão concluída!")

    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)

    finally:
        if cursor:
            cursor.close()
        if conector:
            conector.close()


# Outras funções relacionadas a manipulação de baralhos...

# Exemplos de uso:
# criar_baralho()
# listar_baralhos()
