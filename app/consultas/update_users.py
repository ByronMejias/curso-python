from turtle import title
import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='oxfactura')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			sql = "UPDATE clients set business_name = %s WHERE id = %s;"
			title = 'AAAA'
			id = 1
			cursor.execute(sql, (title, id))

		conexion.commit()
	finally:
		conexion.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)