import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='oxfactura')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			sql = "INSERT INTO clients (enterprise_id, type_document, number_doc, business_name, email, phone) VALUES (%s, %s, %s, %s, %s, %s);"

			cursor.execute(sql, (1, 1, "123123123", 'Byroneman', 'bmejias@thefactoryhka.com', '1111111'))
			cursor.execute(sql, (1, 2, "333333333", 'Byroneman 3', 'bmejias444@thefactoryhka.com', '3333333'))
			cursor.execute(sql, (1, 3, "444444444", 'Byroneman 4', 'bmejias555@thefactoryhka.com', '4444444'))

		conexion.commit()
		print('Guardado Correctamente')
	finally:
		conexion.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)