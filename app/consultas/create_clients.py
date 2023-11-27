import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			sql = "INSERT INTO clients (enterprise_id, type_document, number_doc, business_name, email, phone) VALUES (%s, %s, %s, %s, %s, %s);"

			cursor.execute(sql, (1, 1, "111111111", 'NOMBRE 1', 'correo1@asd.com', '1111111'))
			cursor.execute(sql, (1, 2, "222222222", 'NOMBRE 2', 'correo2@asd.com', '2222222'))
			cursor.execute(sql, (1, 3, "333333333", 'NOMBRE 3', 'correo3@asd.com', '3333333'))

		conexion.commit()
		print('Guardado Correctamente')
	finally:
		conexion.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)