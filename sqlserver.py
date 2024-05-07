import pyodbc

def create_connection():

    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=Rust;'
        'UID=sa;'
        'PWD=Enterprise2008'
    )
    return conn

def add_product(name, price, quantity):

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Produtos (Nome, Preco, Quantidade)
        VALUES (?, ?, ?)
    """, (name, price, quantity))
    conn.commit()
    cursor.close()
    conn.close()

def update_product(product_id, name, price, quantity):

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Produtos
        SET Nome = ?, Preco = ?, Quantidade = ?
        WHERE ProdutoID = ?
    """, (name, price, quantity, product_id))
    conn.commit()
    cursor.close()
    conn.close()


def remove_product(product_id):

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Produtos
        WHERE ProdutoID = ?
    """, (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
