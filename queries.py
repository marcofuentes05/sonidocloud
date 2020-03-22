# #
# import pgdb

# conexion = pgdb.connect(host="", database="", user="", password="", port="")

# cur = conexion.cursor()

# print(" ")
# print("\nGeneros con más canciones\n")
# cur.execute("SELECT genre.name, COUNT(track.genreid) FROM  track JOIN genre ON track.genreid = genre.genreid GROUP BY genre.name ORDER BY COUNT(track.genreid) DESC ")

# for cancion in cur.fetchall():
#     print (cancion.name,': ', cancion.count,' canciones')

# print(" ")
# print("Artistas con más albums individuales\n")
# cur.execute("SELECT artist.name, COUNT(album.artistid) FROM artist JOIN album ON artist.artistid = album.artistid GROUP BY artist.name ORDER BY COUNT(album.artistid) DESC")

# for artista in cur.fetchall():
#     print(artista.name, artista.count)

# print(" ")
# print("Canciones de mayor duración, en milisegundos, con la información de sus artistas\n")
# cur.execute("SELECT track.name, artist.name as artista, track.milliseconds FROM track JOIN album ON track.albumid = album.albumid JOIN artist ON artist.artistid = album.artistid ORDER BY track.milliseconds DESC")
# for cancion in cur.fetchall():
#     print(cancion.name, cancion.artista, cancion.milliseconds)

# print(" ")
# print("Usuarios que han registrado más canciones\n")
# cur.execute("SELECT user_client.username, COUNT(track.trackid) FROM user_client JOIN customer ON customer.customerid = user_client.clientid JOIN invoice ON invoice.customerid = customer.customerid JOIN invoiceline ON invoiceline.invoiceid = invoice.invoiceid JOIN track ON track.trackid = invoiceline.trackid GROUP BY user_client.username ORDER BY COUNT(track.trackid) DESC")
# for usuario in cur.fetchall():
# 	print(usuario.username, usuario.count)

# print(" ")
# print("Promedio de duración de canciones por género")
# cur.execute("SELECT genre.name, AVG(track.milliseconds) FROM track JOIN genre ON genre.genreid = track.genreid GROUP BY genre.name ORDER BY AVG(track.milliseconds) DESC")
# for genero in cur.fetchall():
#     print(genero.name, genero.avg)

def query2():
	query = "SELECT genre.name, COUNT(track.genreid) FROM  track JOIN genre ON track.genreid = genre.genreid GROUP BY genre.name ORDER BY COUNT(track.genreid) DESC "
	return query

def query3():
	query = "SELECT artist.name, COUNT(album.artistid) FROM artist JOIN album ON artist.artistid = album.artistid GROUP BY artist.name ORDER BY COUNT(album.artistid) DESC"
	return query 

def query4():
	query = "SELECT track.name, artist.name as artista, track.milliseconds FROM track JOIN album ON track.albumid = album.albumid JOIN artist ON artist.artistid = album.artistid ORDER BY track.milliseconds DESC"
	return query

def query5():
	query ="SELECT user_client.username, COUNT(track.trackid) FROM user_client JOIN customer ON customer.customerid = user_client.clientid JOIN invoice ON invoice.customerid = customer.customerid JOIN invoiceline ON invoiceline.invoiceid = invoice.invoiceid JOIN track ON track.trackid = invoiceline.trackid GROUP BY user_client.username ORDER BY COUNT(track.trackid) DESC"
	return query

def query6():
	query = "SELECT genre.name, AVG(track.milliseconds) FROM track JOIN genre ON genre.genreid = track.genreid GROUP BY genre.name ORDER BY AVG(track.milliseconds) DESC"
	return query