import mysql.connector


def conectar_banco_de_dados():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="matheus",
        password="mvvb27052003",
        database="clone_anki",
    )


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
            difficulty DECIMAL(3, 2)
            )
        """

        # Executar a consulta SQL para criar a tabela
        cursor.execute(create_table_query)
        print(f"A tabela '{nome_tabela}' foi criada com sucesso!")

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


# Outras funções relacionadas a manipulação de baralhos...

# Exemplos de uso:
# criar_baralho()
# listar_baralhos()
