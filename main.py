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
    # if type(valor) == 'int':
    #     valor = int(valor)
    mycursor.execute(f"SELECT * FROM PELICULA WHERE {camp} = {valor}")
    print(mydb)
    show_lines(mycursor)

def afegir_pelicula(titol, any, puntuacio, vots):
    mycursor.execute(f"INSERT PELICULA * (TITULO, ANYO, PUNTUACION, VOTOS) VALUES ({titol}, {any}, {puntuacio}, {vots})")
    print(mydb)
    show_lines(mycursor)

#METODE PER MOSTRAR CONSULTA
def show_lines(cursor):
    for x in cursor:
        print(x)

cerca_per_camp("ID", "0")