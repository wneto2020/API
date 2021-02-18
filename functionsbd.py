import sqlite3


def insert(nome, email, senha):
    conexao = sqlite3.connect('api.db')
    cursor = conexao.cursor()
    result = read(nome, email)

    if result is not None:

        if nome in result  and  email in result:
            print("Nome e Email já existem")

        elif nome in result:
            print("Nome já existe")

        elif email in result:
            print("E-mail já existe")

    elif result == None:
        cursor.execute('INSERT INTO usuario VALUES("{}", "{}", "{}")'.format(nome, email, senha))
        conexao.commit()

def delete (nome, email, senha):
    conexao = sqlite3.connect('api.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuario WHERE nome = "{}" AND senha = "{}" AND email = "{}"'.format(nome, senha, email))
    conexao.commit()


def read(nome,email):
    conexao = sqlite3.connect('api.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuario WHERE nome = "{}" OR email = "{}"'.format(nome, email))
    return cursor.fetchone()



def update(nome, senha, email,nova_senha):
    conexao = sqlite3.connect('api.db')
    cursor = conexao.cursor()
    result = read(nome, email)

    if result is not None:

        if nome in result and senha in result:
            cursor.execute('UPDATE usuario SET senha = "{}" WHERE nome = "{}" AND senha = "{}"'.format(nova_senha,nome, senha))
            conexao.commit()

    else:
        print('Dados incorretos')


if __name__ == '__main__':

   update('carlos', 123, 'carlos@santos', 123456)


