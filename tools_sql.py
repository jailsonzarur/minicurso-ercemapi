import sqlite3
from langchain_core.tools import tool

@tool
def consultar_pedidos(nome_cliente: str) -> str:
    """Consulta pedidos de um cliente."""
    conn = sqlite3.connect('ecommerce_v2.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, produto, status, valor FROM pedidos WHERE cliente LIKE ?", (f'%{nome_cliente}%',))
    res = cursor.fetchall()
    conn.close()
    
    if not res: return f"Nenhum pedido encontrado para '{nome_cliente}'."
    
    txt = f"Pedidos de '{nome_cliente}':\n"
    for p in res: txt += f"- ID {p[0]}: {p[1]} ({p[2]}) - R$ {p[3]:.2f}\n"
    return txt

@tool
def cancelar_pedido(id_pedido: int) -> str:
    """Cancela um pedido (apenas se status for PENDENTE)."""
    conn = sqlite3.connect('ecommerce_v2.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT status FROM pedidos WHERE id = ?", (id_pedido,))
    res = cursor.fetchone()
    if not res:
        conn.close()
        return "Erro: Pedido não existe."
    
    if res[0] != 'PENDENTE':
        conn.close()
        return f"Erro: Status é '{res[0]}'. Apenas PENDENTE pode ser cancelado."
    
    cursor.execute("UPDATE pedidos SET status = 'CANCELADO' WHERE id = ?", (id_pedido,))
    conn.commit()
    conn.close()
    return f"Sucesso: Pedido {id_pedido} cancelado."

@tool
def criar_pedido(nome_cliente: str, produto: str, valor: float) -> str:
    """
    Cria um novo pedido no sistema.
    O status inicial será sempre 'PENDENTE'.
    """
    conn = sqlite3.connect('ecommerce_v2.db')
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO pedidos (cliente, produto, status, valor) VALUES (?, ?, 'PENDENTE', ?)",
        (nome_cliente, produto, valor)
    )
    novo_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return f"Sucesso! Pedido #{novo_id} criado para {nome_cliente} (Produto: {produto}, R$ {valor:.2f})."