import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			sql = "SELECT * FROM clients WHERE business_name like %s;"
			where = 'NOMBRE 1'
			cursor.execute(sql, (where))
 
			# Con fetchall traemos todas las filas
			clients = cursor.fetchall()
 
			# Recorrer e imprimir
			for clients in clients:
				print(clients)
	finally:
		conexion.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)