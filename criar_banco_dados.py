import sqlite3

def iniciar_banco():
    conn = sqlite3.connect('ecommerce_v2.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT NOT NULL,
        produto TEXT NOT NULL,
        status TEXT NOT NULL,
        valor REAL
    )
    ''')
    
    cursor.execute('SELECT count(*) FROM pedidos')
    if cursor.fetchone()[0] == 0:
        dados = [
            ('Jailson', 'Notebook Gamer', 'ENVIADO', 4500.00),
            ('Maria', 'Mouse Sem Fio', 'PENDENTE', 120.00),
            ('Carlos', 'Monitor 4K', 'ENTREGUE', 2500.00)
        ]
        cursor.executemany('INSERT INTO pedidos (cliente, produto, status, valor) VALUES (?, ?, ?, ?)', dados)
        conn.commit()
        print("--- [SISTEMA] Banco 'ecommerce_v2.db' pronto! ---")
    
    conn.close()

iniciar_banco()