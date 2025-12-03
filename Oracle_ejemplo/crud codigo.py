import oracledb
import os
from dotenv import load_dotenv
from typing import Optional
load_dotenv() 


username = os.getenv("ORACLE_USER") 
dsn = os.getenv("ORACLE_DSN") 
password = os.getenv("ORACLE_PASSWORD") 


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)



def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada\n {query}")


    except oracledb.DatabaseError as error:
        print(f"No se puedo crear la tabla: {error}")

def create_all_tables():
    tables = [
        (
            "CREATE TABLE Empleado("
            "IDempleado INTEGER PRIMARY KEY,"
            "Nombre VARCHAR(60),"
            "Direccion VARCHAR(60),"
            "Telefono INT NOT NULL,"
            "Email VARCHAR(30),"
            "FechaInicio DATE NOT NULL,"
            "Sueldo Int not null"
            ")"
        ),
        (
            "CREATE TABLE Departamento("
          "IDdepartamento INT PRIMARY KEY,"
            "Nombre VARCHAR(20),"
            "Gerente VARCHAR(30)"
            ")"
        ),
        (
            "CREATE TABLE Proyecto("
            "IDproyecto INT PRIMARY KEY,"
            "Nombre VARCHAR(30),"
            "Descripcion VARCHAR(200),"
            "FechaInicio DATE NOT NULL"
            ")"
        ),
        (
            "CREATE TABLE Informe("
            "IDinforme INT PRIMARY KEY,"
            "FOREIGN KEY (InformeProyecto) REFERENCES Proyecto(IDproyecto)"
            ")"
        ),
        (
            "CREATE TABLE Usuario("
            "IDusuario INT PRIMARY KEY,"
            "Username VARCHAR(40),"
            "Contraseña VARCHAR(40)"
            ")"
        ),
        (
            "CREATE TABLE RegistrarTiempo("
            "IDRegistrarTiempo INT NOT NULL,"
            "Fecha DATE NOT NULL,"
            "Horas INT NOT NULL,"
            "Descripcion VARCHAR(200),"
            "FOREIGN KEY (Nombre) REFERENCES Empleado(IDempleado)"
            ")"
        )
    ]

    for query in tables:
        create_schema(query)
def create_Empleado(rut, nombre, edad, direccion, telefono, email):
    sql = (
        "INSERT INTO Empleado (rut, nombre, edad, direccion, telefono, email)"
        "VALUES (:rut, :nombre, :edad, :direccion, :telefono, :email)"
    )
    parametros = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono,
        "email": email
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")
def create_Departamento(IDdepartamento,nombre,gerente):
    sql = (
        "INSERT INT Departamento (IDdepartamento, nombre ,gerente)"
        "VALUES(:IDdepartamento, :nombre, :gerente)"
    )
    parametros = {
        "IDdepartamento": IDdepartamento,
        "nombre": nombre,
        "gerente": gerente
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")
    
def create_Proyecto(IDproyecto,Nombre,Descripcion,FechaInicio):
    sql = (
        "INSERT INTO Preyecto(IDproyecto, Nombre, Descripcion,FechaInicio)"
        "VALUES(:IDproyecto, :Nombre, :Descripcion, :FechaInicio)"
    )
    parametro = {
        "IDproyecto": IDproyecto,
        "Nombre": Nombre,
        "Descripcion": Descripcion,
        "FechaInicio": FechaInicio
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_Informe(IDinforme):
    sql = (
        "INSERT INTO Informe (IDinforme)"
        "VALUES (:IDproyecto)"
    )
    parametros = {
        "IDinforme": IDinforme
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_Usuario(IDusuario,Username,Contraseña):
    sql = (
        "INSERT INTO Usuario (IDusuario, Username, Contraseña)"
        "VALUES (:IDusuario, :Username, :Contraseña)"
    )
    parametros = {
        "IDusuario": IDusuario,
        "Username": Username,
        "Contraseña": Contraseña
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_RegistrarTiempo(IDRegistrarTiempo,Fecha,Horas,Descripcion):
    sql = (
        "INSERT INTO RegistrarTimepo(IDRegistrarTiempo, Fecha, Hora, Descripcion)"
        "VALUES (:IDRegistrarTiempo, :Fecha, :Hora, :Descripcion)"
    )

    parametros = {
        "IDRegistroTiempo": IDRegistrarTiempo,
        "Fecha": Fecha,
        "Horas": Horas,
        "Descripcion": Descripcion
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

#READ - Lectura de datos

def read_Empleado():
    sql = "SELECT * FROM EMPLEADO"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")

def read_Empleado_by_id(id: int):
    sql = "SELECT * FROM EMPLEADO WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_Departamento():
    sql = "SELECT * FROM DEPARTAMENTO"

    try:

        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")

def read_Departamento_by_id(id: int):
    sql = "SELECT * FROM DEPARTAMENTO WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_Proyecto():
    sql = "SELECT * FROM PROYECTO"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")

def read_Proyecto_by_id(id: int):
    sql = "SELECT * FROM PROYECTO WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_Informe():
    sql = "SELECT * FROM INFORME"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")

def read_Informe_by_id(id: int):
    sql = "SELECT * FROM INFORME WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_Usuario():
    sql = "SELECT * FROM USUARIO"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")

def read_Usuario_by_id(id: int):
    sql = "SELECT * FROM USUARIO WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_RegistrarTiempo():
    sql = "SELECT * FROM REGISTRARTIEMPO"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")

def read_RegistrarTiempo_by_id(id: int):
    sql = "SELECT * FROM REGISTRARTIEMPO WHERE id = :id"
    parametros = {"id": id}


    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")

#UPDATE - Actualización de datos

def update_Empleado(
    id: int, 
    rut: Optional [str] = None,
    nombre: Optional [str] = None,
    edad: Optional [int] = None,
    direccion: Optional [str] = None,
    telefono: Optional [int] = None,
    email: Optional [str] = None
):
    modificaciones = []
    parametros = {"id": id}
    if rut is not None:
        ([]).append("rut =: rut")
        parametros["rut"] = rut
    if nombre is not None:
        ([]).append("nombre =: nombre")
        parametros["nombre"] = nombre
    if edad is not None:
        ([]).append("edad =: edad")
        parametros["edad"] = edad
    if direccion is not None:
        ([]).append("direccion =: direccion")
        parametros["direccion"] = direccion
    if telefono is not None:
        ([]).append("telefono =: telefono")
        parametros["telefono"] = telefono
    if email is not None:
        ([]).append("email =: email")
        parametros["email"] = email
    if not ([]):
        return print("No has enviado datos por modificar")

    sql = f"UPDATE EMPLEADO SET{ ", ".join(modificaciones) } WHERE id =: id"
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_Departamento(
        id: int,
        nombre: Optional [str],
        gerente: Optional [str]
):
    modificaciones = []
    parametros = {"id": id}
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    if gerente is not None:
        modificaciones.append("gerente =: gerente")
        parametros["gerente"] = gerente
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE DEPARTAMENTO SET{ ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_Proyecto(
        id: int,
        nombre: Optional [str],
        descripcion: Optional [str],
        fechainicio: Optional [int]
):
    modificaciones = []
    parametros = {"id": id}

    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    if descripcion is not None:
        modificaciones.append("descripcion =: descripcion")
        parametros["descripcion"] = descripcion
    if fechainicio is not None:
        modificaciones.append("fechainicio =: fechainicio")
        parametros["fechainicio"] = fechainicio
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE PROYECTO SET{ ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_Informe(
        IDinforme: int,
        Descripcion: Optional [str]
):
    modificaciones = []
    parametros = {"id": id}

    if Descripcion is not None:
        modificaciones.append("Descripcion =: Descripcion")
        parametros["Descripcion"] = Descripcion
    if not modificaciones:
        return print("No has enviado datos por modificar")
    
    sql = f"UPDATE INFORME SET{ ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_Usuario(
        id: int,
        Username: Optional [str],
        Contraseña: Optional [str]
):
    modificaciones = []
    parametros = {"id": id}

    if username is not None:
        modificaciones.append("username =: username")
        parametros["username"] = username
    if Contraseña is not None:
        modificaciones.append("Contraseña =: Contraseña")
        parametros["Contraseña"] = Contraseña
    if not modificaciones:
        return print("No has enviado datos por modificar")
    
    sql = f"UPDATE USUARIO SET{ ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_RegistroTiempo(
        id: int,
        Fecha: Optional [int],
        Horas: Optional [int],
        Descripcion: Optional [str]
):
    modificaciones = []
    parametros = {"id": id}

    if Fecha is not None:
        modificaciones.append("Fecha =: Fecha")
        parametros["Fecha"] = Fecha
    if Horas is not None:
        modificaciones.append("Horas =: Horas")
        parametros["Horas"] = Horas
    if Descripcion is not None:
        modificaciones.append("Descripcion =: Descripcion")
        parametros["Descripcion"] = Descripcion
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE REGISTROTIEMPO SET{ ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


# DELETE - Eliminacion de datos


def delete_Empleado(id: int):
    sql = ("DELETE FROM EMPLEADO WHERE id = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Departamentos(id: int):
    sql = ("DELETE FROM DEPARTAMENTOS WHERE id = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Proyecto(id: int):
    sql = ("DELETE FROM PROYECTO WHERE id = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Informe(id: int):
    sql = ("DELETE FROM IMFORME WHERE id = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def delete_Usuario(id: int):
    sql = ("DELETE FROM USUARIO WHERE id = :id")
    parametros = {"id" : id}


    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def delete_RegistroTiempo(id: int):
    sql = ("DELETE FROM REGISTROTIEMPO WHERE id = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

#Tablero

def menu_personas():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |         Menu: Empleado           |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Modificar un dato             |
                | 5. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-5, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            id = input("Ingrese id de la persona: ")
            rut = input("Ingrese rut de la persona: ")
            nombre = input("Ingrese nombre de la persona: ")
            edad = input("Ingrese edad de la persona: ")
            direccion = input("Ingrese fecha de direccion de la persona: ")
            telefono = input("Ingrese fecha de telefono de la persona: ")
            email = input("Ingrese fecha de email de la persona: ")
            create_Empleado(id, rut, nombre, edad, direccion, telefono, email)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_personas()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            id = input("Ingrese id de la persona: ")
            read_Empleado_by_id(id)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Modificar un dato")
            id = input("Ingrese id de la persona: ")
            print("[Sólo ingrese los datos a modificar del Empleado]")
            rut = input("Ingrese rut del Empleado (opcional): ")
            nombres = input("Ingrese nombre del Empleado (opcional): ")
            edad = input("Ingrese edad del Empleado (opcional): ")
            direccion = input("Ingrese direccion del Empleado(opcional): ")
            telefono = input("Ingrese telefono del Empleado(opcional): ")
            email = input("Ingrese email del Empleado(opcional): ")
            if len(rut.strip()) == 0: rut = None
            if len(nombre.strip()) == 0: nombre = None
            if len(edad.strip()) == 0: edad = None
            if len(direccion.strip()) == 0: direccion = None
            if len(telefono.strip()) == 0: telefono = None
            if len(email.strip()) == 0: email = None
            update_Empleado(id, rut, nombre, edad, direccion, telefono, email)
            input("Ingrese ENTER para continuar...")
        elif opcion == "5":
            os.system("cls")
            print("5. Eliminar un dato")
            id = input("Ingrese id de la persona: ")
            delete_Empleado(id)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def main():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |     CRUD: Oracle + Python        |
                |----------------------------------|
                | 1. Crear todas las tablas        |
                | 2. Gestionar tabla Empleado      |
                | 3. Gestionar tabla Departamento  |
                | 4. Gestionar tabla Proyecto      |
                | 0. Salir del sistema             |
                |----------------------------------|
                | * La tabla empleado necesita al  |
                | menos un registro creado en la   |
                | tabla Proyecto y Departamentos.  |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-4, 0]: ")

        if opcion == "1":
            os.system("cls")
            create_all_tables()
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            menu_Empleado()
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "0":
            pass
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")


if __name__ == "__main__":
    main()