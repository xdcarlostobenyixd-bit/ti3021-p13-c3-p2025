import oracledb
import os
from dotenv import load_dotenv
from typing import Optional
import datetime

import platform 

load_dotenv() 


username = os.getenv("ORACLE_USER") 
dsn = os.getenv("ORACLE_DSN") 
password = os.getenv("ORACLE_PASSWORD") 

# Función para limpiar la consola
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)

## CREATE - Creación de esquema y datos

def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada: {query.split('(')[0].split(' ')[-1]}")
    except oracledb.DatabaseError as error:
        if "ORA-00955" not in str(error):
             print(f"No se pudo crear la tabla: {error}")
        else:
             print(f"La tabla ya existe (ORA-00955).")

def create_all_tables():
    # 1. Empleado
    tables = [
        (
            "CREATE TABLE Empleado("
            "IDempleado NUMBER(10) PRIMARY KEY,"
            "Nombre VARCHAR2(60),"
            "Direccion VARCHAR2(60),"
            "Telefono NUMBER(15) NOT NULL,"
            "Email VARCHAR2(30),"
            "FechaInicio DATE NOT NULL,"
            "Sueldo NUMBER(10, 2) NOT NULL"
            ")"
        ),
        # 2. Departamento
        (
            "CREATE TABLE Departamento("
          "IDdepartamento NUMBER(10) PRIMARY KEY,"
            "Nombre VARCHAR2(20),"
            "Gerente VARCHAR2(30)"
            ")"
        ),
        # 3. Proyecto
        (
            "CREATE TABLE Proyecto("
            "IDproyecto NUMBER(10) PRIMARY KEY,"
            "Nombre VARCHAR2(30),"
            "Descripcion VARCHAR2(200),"
            "FechaInicio DATE NOT NULL"
            ")"
        ),
        # 4. Informe 
        (
            "CREATE TABLE Informe("
            "IDinforme NUMBER(10) PRIMARY KEY"
            ")"
        ),
        # 5. Usuario
        (
            "CREATE TABLE Usuario("
            "IDusuario NUMBER(10) PRIMARY KEY,"
            "Username VARCHAR2(40),"
            "Contraseña VARCHAR2(40)"
            ")"
        ),
        # 6. RegistrarTiempo 
        (
            "CREATE TABLE RegistrarTiempo("
            "IDRegistrarTiempo NUMBER(10) NOT NULL PRIMARY KEY," 
            "IDempleado NUMBER(10) NOT NULL," 
            "Fecha DATE NOT NULL,"
            "Horas NUMBER(4) NOT NULL,"
            "Descripcion VARCHAR2(200),"
            "FOREIGN KEY (IDempleado) REFERENCES Empleado(IDempleado)"
            ")"
        )
    ]

    for query in tables:
        create_schema(query)

# CREATE - INSERT
def create_Empleado(IDempleado: int, nombre: str, direccion: str, telefono: int, email: str, fecha_inicio: str, sueldo: int):
    sql = (
        "INSERT INTO Empleado (IDempleado, Nombre, Direccion, Telefono, Email, FechaInicio, Sueldo)"
        "VALUES (:IDempleado, :Nombre, :Direccion, :Telefono, :Email, TO_DATE(:FechaInicio, 'YYYY-MM-DD'), :Sueldo)"
    )
    parametros = {
        "IDempleado": IDempleado,
        "Nombre": nombre,
        "Direccion": direccion,
        "Telefono": telefono,
        "Email": email,
        "FechaInicio": fecha_inicio,
        "Sueldo": sueldo
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos de Empleado correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_Departamento(IDdepartamento: int, nombre: str, gerente: str):
    sql = (
        "INSERT INTO Departamento (IDdepartamento, Nombre ,Gerente)"
        "VALUES(:IDdepartamento, :Nombre, :Gerente)"
    )
    parametros = {
        "IDdepartamento": IDdepartamento,
        "Nombre": nombre,
        "Gerente": gerente
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos de Departamento correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")
    
def create_Proyecto(IDproyecto: int, Nombre: str, Descripcion: str, FechaInicio: str):
    sql = (
        "INSERT INTO Proyecto(IDproyecto, Nombre, Descripcion, FechaInicio)" 
        "VALUES(:IDproyecto, :Nombre, :Descripcion, TO_DATE(:FechaInicio, 'YYYY-MM-DD'))" 
    )
    parametros = {
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
            print("Inserción de datos de Proyecto correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")


def create_Informe(IDinforme: int):
    sql = (
        "INSERT INTO Informe (IDinforme)"
        "VALUES (:IDinforme)" 
    )
    parametros = {
        "IDinforme": IDinforme
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos de Informe correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_Usuario(IDusuario: int, Username: str, Contraseña: str):
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
            print("Inserción de datos de Usuario correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")


def create_RegistrarTiempo(IDRegistrarTiempo: int, IDempleado: int, Fecha: str, Horas: int, Descripcion: str):
    sql = (
        "INSERT INTO RegistrarTiempo(IDRegistrarTiempo, IDempleado, Fecha, Horas, Descripcion)"
        "VALUES (:IDRegistrarTiempo, :IDempleado, TO_DATE(:Fecha, 'YYYY-MM-DD'), :Horas, :Descripcion)"
    )

    parametros = {
        "IDRegistrarTiempo": IDRegistrarTiempo,
        "IDempleado": IDempleado, 
        "Fecha": Fecha,
        "Horas": Horas,
        "Descripcion": Descripcion
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos de RegistrarTiempo correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

## READ - Lectura de datos

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
    sql = "SELECT * FROM EMPLEADO WHERE IDempleado = :id" 
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
    sql = "SELECT * FROM DEPARTAMENTO WHERE IDdepartamento = :id" 
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
    sql = "SELECT * FROM PROYECTO WHERE IDproyecto = :id" 
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
    sql = "SELECT * FROM INFORME WHERE IDinforme = :id" 
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
    sql = "SELECT * FROM USUARIO WHERE IDusuario = :id" 
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
    sql = "SELECT * FROM REGISTRARTIEMPO WHERE IDRegistrarTiempo = :id" 
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

## UPDATE - Actualización de datos

def update_Empleado(
    id: int, 
    nombre: Optional [str] = None,
    direccion: Optional [str] = None,
    telefono: Optional [int] = None,
    email: Optional [str] = None,
    fechainicio: Optional [str] = None,
    sueldo: Optional [int] = None
):
    modificaciones = []
    parametros = {"id": id}

    if nombre is not None:
        modificaciones.append("Nombre =: Nombre") 
        parametros["Nombre"] = nombre
    if direccion is not None:
        modificaciones.append("Direccion =: Direccion")
        parametros["Direccion"] = direccion
    if telefono is not None:
        modificaciones.append("Telefono =: Telefono")
        parametros["Telefono"] = telefono
    if email is not None:
        modificaciones.append("Email =: Email")
        parametros["Email"] = email
    if fechainicio is not None:
        modificaciones.append("FechaInicio = TO_DATE(:FechaInicio, 'YYYY-MM-DD')") 
        parametros["FechaInicio"] = fechainicio
    if sueldo is not None:
        modificaciones.append("Sueldo =: Sueldo")
        parametros["Sueldo"] = sueldo

    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE EMPLEADO SET { ', '.join(modificaciones) } WHERE IDempleado =: id" 
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID={id} actualizado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato: {error} \n {sql} \n {parametros}")



def update_Departamento(
        id: int,
        nombre: Optional [str] = None,
        gerente: Optional [str] = None
):
    modificaciones = []
    parametros = {"id": id}
    if nombre is not None:
        modificaciones.append("Nombre =: Nombre")
        parametros["Nombre"] = nombre
    if gerente is not None:
        modificaciones.append("Gerente =: Gerente")
        parametros["Gerente"] = gerente
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE DEPARTAMENTO SET { ', '.join(modificaciones) } WHERE IDdepartamento =: id"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID={id} actualizado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato: {error} \n {sql} \n {parametros}")


def update_Proyecto(
        id: int,
        nombre: Optional [str] = None,
        descripcion: Optional [str] = None,
        fechainicio: Optional [str] = None 
):
    modificaciones = []
    parametros = {"id": id}

    if nombre is not None:
        modificaciones.append("Nombre =: Nombre")
        parametros["Nombre"] = nombre
    if descripcion is not None:
        modificaciones.append("Descripcion =: Descripcion")
        parametros["Descripcion"] = descripcion
    if fechainicio is not None:
        modificaciones.append("FechaInicio = TO_DATE(:FechaInicio, 'YYYY-MM-DD')")
        parametros["FechaInicio"] = fechainicio
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE PROYECTO SET { ', '.join(modificaciones) } WHERE IDproyecto =: id" 

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID={id} actualizado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato: {error} \n {sql} \n {parametros}")


def update_Informe(
        id: int, 
        IDProyecto_FK: Optional [int] = None 
):
    modificaciones = []
    parametros = {"id": id}
    
    if not modificaciones:
        return print("No hay campos modificables en la tabla Informe (solo ID)")
    
    sql = f"UPDATE INFORME SET { ', '.join(modificaciones) } WHERE IDinforme =: id"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID={id} actualizado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato: {error} \n {sql} \n {parametros}")


def update_Usuario(
        id: int,
        Username: Optional [str] = None,
        Contraseña: Optional [str] = None
):
    modificaciones = []
    parametros = {"id": id}

    if Username is not None: 
        modificaciones.append("Username =: Username")
        parametros["Username"] = Username
    if Contraseña is not None:
        modificaciones.append("Contraseña =: Contraseña")
        parametros["Contraseña"] = Contraseña
    if not modificaciones:
        return print("No has enviado datos por modificar")
    
    sql = f"UPDATE USUARIO SET { ', '.join(modificaciones) } WHERE IDusuario =: id" 

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID={id} actualizado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato: {error} \n {sql} \n {parametros}")



def update_RegistroTiempo(
        id: int,
        IDempleado: Optional [int] = None,
        Fecha: Optional [str] = None,
        Horas: Optional [int] = None,
        Descripcion: Optional [str] = None
):
    modificaciones = []
    parametros = {"id": id}

    if IDempleado is not None:
        modificaciones.append("IDempleado =: IDempleado")
        parametros["IDempleado"] = IDempleado
    if Fecha is not None:
        modificaciones.append("Fecha = TO_DATE(:Fecha, 'YYYY-MM-DD')")
        parametros["Fecha"] = Fecha
    if Horas is not None:
        modificaciones.append("Horas =: Horas")
        parametros["Horas"] = Horas
    if Descripcion is not None:
        modificaciones.append("Descripcion =: Descripcion")
        parametros["Descripcion"] = Descripcion
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE REGISTRARTIEMPO SET { ', '.join(modificaciones) } WHERE IDRegistrarTiempo =: id" 

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID={id} actualizado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato: {error} \n {sql} \n {parametros}")


## DELETE - Eliminacion de datos


def delete_Empleado(id: int):
    sql = ("DELETE FROM EMPLEADO WHERE IDempleado = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Departamento(id: int): 
    sql = ("DELETE FROM DEPARTAMENTO WHERE IDdepartamento = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Proyecto(id: int):
    sql = ("DELETE FROM PROYECTO WHERE IDproyecto = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Informe(id: int):
    sql = ("DELETE FROM INFORME WHERE IDinforme = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def delete_Usuario(id: int):
    sql = ("DELETE FROM USUARIO WHERE IDusuario = :id")
    parametros = {"id" : id}


    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def delete_RegistroTiempo(id: int):
    sql = ("DELETE FROM REGISTRARTIEMPO WHERE IDRegistrarTiempo = :id")
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

## Tableros (Menús)

def menu_Empleado():
    while True:
        clear_screen()
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
            clear_screen()
            print("1. Insertar un dato")
            try:
                id = int(input("Ingrese ID del Empleado: "))
                nombre = input("Ingrese nombre: ")
                direccion = input("Ingrese direccion: ")
                telefono = int(input("Ingrese telefono: "))
                email = input("Ingrese email: ")
                fechainicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
                sueldo = int(input("Ingrese sueldo: "))
                create_Empleado(id, nombre, direccion, telefono, email, fechainicio, sueldo)
            except ValueError:
                print("Error: ID, Telefono y Sueldo deben ser números enteros.")
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            clear_screen()
            print("2. Consultar todos los datos")
            read_Empleado()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            clear_screen()
            print("3. Consultar dato por ID ")
            try:
                id = int(input("Ingrese ID del Empleado: "))
                read_Empleado_by_id(id)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            clear_screen()
            print("4. Modificar un dato")
            try:
                id = int(input("Ingrese ID del Empleado a modificar: "))
                print("[Sólo ingrese los datos a modificar del Empleado]")
                nombre = input("Ingrese nuevo nombre (opcional): ")
                direccion = input("Ingrese nueva direccion (opcional): ")
                telefono_str = input("Ingrese nuevo telefono (opcional): ")
                email = input("Ingrese nuevo email (opcional): ")
                fechainicio = input("Ingrese nueva fecha de inicio (YYYY-MM-DD, opcional): ")
                sueldo_str = input("Ingrese nuevo sueldo (opcional): ")

                nombre = nombre if nombre.strip() else None
                direccion = direccion if direccion.strip() else None
                email = email if email.strip() else None
                fechainicio = fechainicio if fechainicio.strip() else None
                telefono = int(telefono_str) if telefono_str.strip() else None
                sueldo = int(sueldo_str) if sueldo_str.strip() else None

                update_Empleado(id, nombre, direccion, telefono, email, fechainicio, sueldo)
            except ValueError:
                print("Error: ID, Telefono o Sueldo ingresado no es un número válido.")
            input("Ingrese ENTER para continuar...")
        elif opcion == "5":
            clear_screen()
            print("5. Eliminar un dato")
            try:
                id = int(input("Ingrese ID del Empleado a eliminar: "))
                delete_Empleado(id)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            clear_screen()
            print("Volviendo al menú principal...")
            break
        else:
            clear_screen()
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def menu_Departamento():
    while True:
        clear_screen()
        print("""
                ====================================
                |     MENÚ DEPARTAMENTO            |
                |----------------------------------|
                | 1. Insertar                      |
                | 2. Ver todos                     |
                | 3. Buscar por ID                 |
                | 4. Actualizar                    |
                | 5. Eliminar                      |
                | 0. Volver                        |
                |----------------------------------|
                | * Nota: Requiere configuración   |
                | de conexión Oracle.              |
                ====================================
        """)

        op = input("Opción: ")

        if op == "1":
            try:
                ID = int(input("ID: "))
                Nombre = input("Nombre: ")
                Gerente = input("Gerente: ")
                create_Departamento(ID, Nombre, Gerente)
            except ValueError:
                 print("Error: El ID debe ser un número entero.")
            input("ENTER...")

        elif op == "2":
            read_Departamento()
            input("ENTER...")

        elif op == "3":
            try:
                ID = int(input("ID: "))
                read_Departamento_by_id(ID)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            input("ENTER...")

        elif op == "4":
            try:
                ID = int(input("ID: "))
                Nombre = input("Nuevo nombre: ") or None
                Gerente = input("Nuevo gerente: ") or None
                update_Departamento(ID, Nombre, Gerente)
            except ValueError:
                print("Error: El ID debe ser un número entero.")


        elif op == "5":
            try:
                ID = int(input("ID: "))
                delete_Departamento(ID)
            except ValueError:
                 print("Error: El ID debe ser un número entero.")

        elif op == "0":
            return
        else:
            print("Opción incorrecta, intente nuevamente.")
            input("ENTER...")
        
def menu_Proyecto():
    while True:
        clear_screen()
        print("""
               ====================================
                |     MENÚ PROYECTO                |
                |----------------------------------|
                | 1. Insertar                      |
                | 2. Ver todos                     |
                | 3. Buscar por ID                 |
                | 4. Actualizar                    |
                | 5. Eliminar                      |
                | 0. Volver                        |
                |----------------------------------|
                | * Nota: Requiere configuración   |
                | de conexión Oracle.              |
                ====================================
        """)

        op = input("Opción: ")

        if op == "1":
            try:
                ID = int(input("ID: "))
                Nombre = input("Nombre: ")
                Descripcion = input("Descripción: ")
                Fecha = input("Fecha Inicio (YYYY-MM-DD): ")
                create_Proyecto(ID, Nombre, Descripcion, Fecha)
            except ValueError:
                 print("Error: El ID debe ser un número entero.")
            input("ENTER...")

        elif op == "2":
            read_Proyecto()
            input("ENTER...")

        elif op == "3":
            try:
                ID = int(input("ID: "))
                read_Proyecto_by_id(ID)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            input("ENTER...")

        elif op == "4":
            try:
                ID = int(input("ID: "))
                Nombre = input("Nuevo nombre: ") or None
                Descripcion = input("Nueva descripción: ") or None
                Fecha = input("Nueva fecha (YYYY-MM-DD): ") or None
                update_Proyecto(ID, Nombre, Descripcion, Fecha)
            except ValueError:
                print("Error: El ID debe ser un número entero.")


        elif op == "5":
            try:
                ID = int(input("ID: "))
                delete_Proyecto(ID)
            except ValueError:
                 print("Error: El ID debe ser un número entero.")

        elif op == "0":
            return
        else:
            print("Opción incorrecta, intente nuevamente.")
            input("ENTER...")


def main():
    while True: 
        clear_screen() 
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
            clear_screen()
            create_all_tables()
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            clear_screen()
            menu_Empleado()

        elif opcion == "3":
            clear_screen()
            try:
                menu_Departamento()
            except Exception as e:
                print(f"Error gestionando Departamento: {e}")
                input("Ingrese ENTER para continuar...")
            
        elif opcion == "4":
            clear_screen()
            try:
                menu_Proyecto()
            except Exception as e:
                    print(f"Error gestionando Proyecto: {e}")
            input("Ingrese ENTER para continuar...")
        
        elif opcion == "0":
            clear_screen()
            print("Saliendo del sistema...")
            break 
        
        else: 
            clear_screen()
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")
            
if __name__ == "__main__":
    main()