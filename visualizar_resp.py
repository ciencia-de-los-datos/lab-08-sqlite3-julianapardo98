import sqlite3

# Conexión a la base de datos en memoria
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

# Consulta para obtener PREGUNTA #
cur.execute("SELECT strftime('%Y', c23), AVG(c21) FROM tbl2 GROUP BY strftime('%Y', c23)")
print(cur.fetchall())

from tabulate import tabulate

# Imprimir resultados en formato de tabla
headers = [description[0] for description in cur.description]  # Obtener los nombres de las columnas
print(tabulate(cur, headers=headers, tablefmt="grid"))