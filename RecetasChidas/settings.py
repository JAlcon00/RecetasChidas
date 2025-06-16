DATABASES = {
    """
    Configuración de la base de datos para una aplicación Django.

    Este módulo define los parámetros de conexión para la base de datos MySQL que se
    utilizará en la aplicación. Se especifica el motor de base de datos, el nombre, el usuario,
    la contraseña, el host y el puerto.

    Atributos:
        DATABASES (dict): Diccionario que contiene la configuración de la base de datos.
            - 'ENGINE' (str): Define el backend de Django para MySQL.
            - 'NAME' (str): Nombre de la base de datos.
            - 'USER' (str): Usuario empleado para la autenticación en la base de datos.
            - 'PASSWORD' (str): Contraseña correspondiente al usuario.
            - 'HOST' (str): Dirección del servidor donde se aloja la base de datos.
            - 'PORT' (str): Puerto de conexión al servidor de la base de datos.

    Nota:
        Es importante mantener seguros estos datos de conexión para evitar accesos no autorizados.
    """
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bewxu3beblubeal18sqn',  
        'USER': 'ugainnbokjrunp1k',        
        'PASSWORD': 'CYMeGZtxWE3puAlXTi2D', 
        'HOST': 'bewxu3beblubeal18sqn-mysql.services.clever-cloud.com',        
        'PORT': '3306',
    }
}