import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "dam_app",
    password = "1234",
    database = "dam_m06"
)
mycursor = mydb.cursor()
mycursor.execute("USE pelis")

def cerca_per_camp(camp: str, valor):
    if type(valor) == str:
        valor = f"'{valor}'"
    mycursor.execute(f"SELECT * FROM PELICULA WHERE {camp} = {valor}")
    print(mydb)
    show_lines(mycursor)

def afegir_pelicula(titol, any, puntuacio, vots):
    mycursor.execute(f"INSERT PELICULA (TITULO, ANYO, PUNTUACION, VOTOS) VALUES ('{titol}', {any}, {puntuacio}, {vots})")
    print(mydb)
    show_lines(mycursor)
    mydb.commit()

def modificar_pelicula(id: int, titol, any, puntuacio, vots):
    mycursor.execute(f"UPDATE PELICULA SET TITULO = '{titol}', ANYO = {any}, PUNTUACION = {puntuacio}, VOTOS = {vots} WHERE ID = {id};")
    print(mydb)
    show_lines(mycursor)
    mydb.commit()

#METODE PER MOSTRAR CONSULTA
def show_lines(cursor):
    for x in cursor:
        print(x)

# afegir_pelicula("Salvat", 2024, 10, 5)
# cerca_per_camp("TITULO", "Salvat")
# modificar_pelicula(1705, "Poma", 2025, 10 , 5)
# cerca_per_camp("ID", 1705)