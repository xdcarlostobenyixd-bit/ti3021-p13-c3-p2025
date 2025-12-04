import os
from dotenv import load_dotenv
from typing import Optional
load_dotenv() 

import datetime
from typing import Optional, Any, Dict, List, Tuple
from dotenv import load_dotenv
import oracledb

username = os.getenv("ORACLE_USER") 
dsn = os.getenv("ORACLE_DSN") 
password = os.getenv("ORACLE_PASSWORD") 

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
dsn = os.getenv("ORACLE_DSN")

def get_connection():
    if not (username and password and dsn):
        raise RuntimeError("Faltan variables de entorno ORACLE_USER/ORACLE_PASSWORD/ORACLE_DSN")
    return oracledb.connect(user=username, password=password, dsn=dsn)


def execute_write(sql: str, params: Optional[Dict[str, Any]] = None) -> Tuple[bool, Optional[str]]:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params or {})
            conn.commit()
        return True, None
    except oracledb.DatabaseError as e:
        return False, str(e)

def create_schema(query):
def parse_date(s: Optional[str]) -> Optional[datetime.date]:
    if not s:
        return None
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")

# -------------------------
# Creación de tablas
# -------------------------
def create_schema(query: str):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada\n {query}")
            connection.commit()
        print("Tabla/process ejecutado.")
    except oracledb.DatabaseError as error:
        print(f"No se puedo crear la tabla: {error}")
        print(f"No se pudo ejecutar: {error}")

def create_all_tables():
    tables = [
        (
            "CREATE TABLE Empleado("
            "IDempleado INTEGER PRIMARY KEY,"
            "edad INT NOT NULL,"
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
            "InformeProyecto INT NOT NULL,"
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
            "Nombre INT NOT NULL,"
            "FOREIGN KEY (Nombre) REFERENCES Empleado(IDempleado)"
            ")"
        )
        """,
        # Proyecto
        """
        CREATE TABLE Proyecto (
            id NUMBER PRIMARY KEY,
            nombre VARCHAR2(150),
            descripcion VARCHAR2(4000),
            fecha_inicio DATE
        )
        """,
        # Informe
        """
        CREATE TABLE Informe (
            id NUMBER PRIMARY KEY,
            proyecto_id NUMBER,
            descripcion VARCHAR2(4000),
            CONSTRAINT fk_informe_proyecto FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id)
        )
        """,
        # Usuario
        """
        CREATE TABLE Usuario (
            id NUMBER PRIMARY KEY,
            username VARCHAR2(100),
            contrasena VARCHAR2(200)
        )
        """,
        # RegistrarTiempo
        """
        CREATE TABLE RegistrarTiempo (
            id NUMBER PRIMARY KEY,
            empleado_id NUMBER,
            fecha DATE,
            horas NUMBER,
            descripcion VARCHAR2(4000),
            CONSTRAINT fk_regtiempo_empleado FOREIGN KEY (empleado_id) REFERENCES Empleado(id)
        )
        """
    ]

    for query in tables:
        create_schema(query)

def create_Empleado(rut: str, nombre: str, edad: int, direccion: str, telefono: str, email: str):
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

def create_Departamento(IDdepartamento: int, nombre: str, gerente: str):
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
    
def create_Proyecto(IDproyecto: int, Nombre: str, Descripcion: str, FechaInicio: datetime):
    sql = (
        "INSERT INTO Preyecto(IDproyecto, Nombre, Descripcion,FechaInicio)"
        "VALUES(:IDproyecto, :Nombre, :Descripcion, :FechaInicio)"
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
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_Informe(IDinforme: int):
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
            print("Inserción de datos correcta")

    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_RegistrarTiempo(IDRegistrarTiempo: int, Fecha: int, Horas: int, Descripcion: str):
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
def create_Departamento(id: int, nombre: str, gerente: Optional[str]):
    sql = "INSERT INTO Departamento (id, nombre, gerente) VALUES (:id, :nombre, :gerente)"
    ok, err = execute_write(sql, {"id": id, "nombre": nombre, "gerente": gerente})
    if ok:
        print("Inserción Departamento correcta.")
    else:
        print("Error crear Departamento:", err)

def create_Proyecto(id: int, nombre: str, descripcion: Optional[str], fecha_inicio: Optional[str]):
    fecha = parse_date(fecha_inicio) if fecha_inicio else None
    sql = "INSERT INTO Proyecto (id, nombre, descripcion, fecha_inicio) VALUES (:id, :nombre, :descripcion, :fecha_inicio)"
    ok, err = execute_write(sql, {"id": id, "nombre": nombre, "descripcion": descripcion, "fecha_inicio": fecha})
    if ok:
        print("Inserción Proyecto correcta.")
    else:
        print("Error crear Proyecto:", err)

def delete_Departamentos(id: int):
    sql = ("DELETE FROM DEPARTAMENTOS WHERE id = :id")
    parametros = {"id" : id}
def create_Informe(id: int, proyecto_id: int, descripcion: Optional[str]):
    sql = "INSERT INTO Informe (id, proyecto_id, descripcion) VALUES (:id, :proyecto_id, :descripcion)"
    ok, err = execute_write(sql, {"id": id, "proyecto_id": proyecto_id, "descripcion": descripcion})
    if ok:
        print("Inserción Informe correcta.")
    else:
        print("Error crear Informe:", err)

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")
def create_Usuario(id: int, username: str, contrasena: str):
    sql = "INSERT INTO Usuario (id, username, contrasena) VALUES (:id, :username, :contrasena)"
    ok, err = execute_write(sql, {"id": id, "username": username, "contrasena": contrasena})
    if ok:
        print("Inserción Usuario correcta.")
    else:
        print("Error crear Usuario:", err)

def create_RegistrarTiempo(id: int, empleado_id: int, fecha: str, horas: int, descripcion: Optional[str]):
    fecha_val = parse_date(fecha)
    sql = "INSERT INTO RegistrarTiempo (id, empleado_id, fecha, horas, descripcion) VALUES (:id, :empleado_id, :fecha, :horas, :descripcion)"
    ok, err = execute_write(sql, {"id": id, "empleado_id": empleado_id, "fecha": fecha_val, "horas": horas, "descripcion": descripcion})
    if ok:
        print("Inserción RegistrarTiempo correcta.")
    else:
        print("Error crear RegistrarTiempo:", err)

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Proyecto(id: int):
    sql = ("DELETE FROM PROYECTO WHERE id = :id")
    parametros = {"id" : id}
# READ - Selects

def read_all(table: str):
    sql = f"SELECT * FROM {table}"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

                cur.execute(sql)
                rows = cur.fetchall()
                if not rows:
                    print("No hay registros.")
                for r in rows:
                    print(r)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_Informe(id: int):
    sql = ("DELETE FROM IMFORME WHERE id = :id")
    parametros = {"id" : id}
        print("Error lectura:", e)

def read_by_id(table: str, id_val: int):
    sql = f"SELECT * FROM {table} WHERE id = :id"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

                cur.execute(sql, {"id": id_val})
                row = cur.fetchone()
                if row:
                    print(row)
                else:
                    print("Registro no encontrado.")
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
        print("Error lectura por id:", e)


# UPDATE - dinámicos

def build_update_sql(table: str, id_name: str, id_value: Any, cambios: Dict[str, Any]):
    if not cambios:
        return None, None
    sets = []
    params = {}
    for i, (col, val) in enumerate(cambios.items()):
        key = f"v{i}"
        sets.append(f"{col} = :{key}")
        params[key] = val
    params["idval"] = id_value
    sql = f"UPDATE {table} SET {', '.join(sets)} WHERE {id_name} = :idval"
    return sql, params

def update_Empleado(id: int, rut: Optional[str] = None, nombre: Optional[str] = None,
                    edad: Optional[int] = None, direccion: Optional[str] = None,
                    telefono: Optional[str] = None, email: Optional[str] = None,
                    fecha_inicio: Optional[str] = None, sueldo: Optional[float] = None):
    cambios = {}
    if rut is not None: cambios["rut"] = rut
    if nombre is not None: cambios["nombre"] = nombre
    if edad is not None: cambios["edad"] = edad
    if direccion is not None: cambios["direccion"] = direccion
    if telefono is not None: cambios["telefono"] = telefono
    if email is not None: cambios["email"] = email
    if fecha_inicio is not None: cambios["fecha_inicio"] = parse_date(fecha_inicio)
    if sueldo is not None: cambios["sueldo"] = sueldo

    sql, params = build_update_sql("Empleado", "id", id, cambios)
    if not sql:
        print("No hay datos para actualizar.")
        return
    ok, err = execute_write(sql, params)
    if ok:
        print("Empleado actualizado.")
    else:
        print("Error actualizar Empleado:", err)

def update_Departamento(id: int, nombre: Optional[str] = None, gerente: Optional[str] = None):
    cambios = {}
    if nombre is not None: cambios["nombre"] = nombre
    if gerente is not None: cambios["gerente"] = gerente
    sql, params = build_update_sql("Departamento", "id", id, cambios)
    if not sql:
        print("No hay datos para actualizar.")
        return
    ok, err = execute_write(sql, params)
    if ok:
        print("Departamento actualizado.")
    else:
        print("Error actualizar Departamento:", err)

def update_Proyecto(id: int, nombre: Optional[str] = None, descripcion: Optional[str] = None, fecha_inicio: Optional[str] = None):
    cambios = {}
    if nombre is not None: cambios["nombre"] = nombre
    if descripcion is not None: cambios["descripcion"] = descripcion
    if fecha_inicio is not None: cambios["fecha_inicio"] = parse_date(fecha_inicio)
    sql, params = build_update_sql("Proyecto", "id", id, cambios)
    if not sql:
        print("No hay datos para actualizar.")
        return
    ok, err = execute_write(sql, params)
    if ok:
        print("Proyecto actualizado.")
    else:
        print("Error actualizar Proyecto:", err)

def update_Informe(id: int, proyecto_id: Optional[int] = None, descripcion: Optional[str] = None):
    cambios = {}
    if proyecto_id is not None: cambios["proyecto_id"] = proyecto_id
    if descripcion is not None: cambios["descripcion"] = descripcion
    sql, params = build_update_sql("Informe", "id", id, cambios)
    if not sql:
        print("No hay datos para actualizar.")
        return
    ok, err = execute_write(sql, params)
    if ok:
        print("Informe actualizado.")
    else:
        print("Error actualizar Informe:", err)

def update_Usuario(id: int, username: Optional[str] = None, contrasena: Optional[str] = None):
    cambios = {}
    if username is not None: cambios["username"] = username
    if contrasena is not None: cambios["contrasena"] = contrasena
    sql, params = build_update_sql("Usuario", "id", id, cambios)
    if not sql:
        print("No hay datos para actualizar.")
        return
    ok, err = execute_write(sql, params)
    if ok:
        print("Usuario actualizado.")
    else:
        print("Error actualizar Usuario:", err)

def update_RegistrarTiempo(id: int, empleado_id: Optional[int] = None, fecha: Optional[str] = None,
                           horas: Optional[int] = None, descripcion: Optional[str] = None):
    cambios = {}
    if empleado_id is not None: cambios["empleado_id"] = empleado_id
    if fecha is not None: cambios["fecha"] = parse_date(fecha)
    if horas is not None: cambios["horas"] = horas
    if descripcion is not None: cambios["descripcion"] = descripcion
    sql, params = build_update_sql("RegistrarTiempo", "id", id, cambios)
    if not sql:
        print("No hay datos para actualizar.")
        return
    ok, err = execute_write(sql, params)
    if ok:
        print("RegistrarTiempo actualizado.")
    else:
        print("Error actualizar RegistrarTiempo:", err)

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

# DELETE

def delete_RegistroTiempo(id: int):
    sql = ("DELETE FROM REGISTROTIEMPO WHERE id = :id")
    parametros = {"id" : id}
def delete_from_table(table: str, id_val: int):
    sql = f"DELETE FROM {table} WHERE id = :id"
    ok, err = execute_write(sql, {"id": id_val})
    if ok:
        print(f"Registro eliminado de {table}.")
    else:
        print("Error eliminar:", err)

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Date eliminado \n {parametros}")

    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")
# Menús 

#Tablero
def safe_int_input(prompt: str) -> int:
    while True:
        val = input(prompt)
        try:
            return int(val)
        except ValueError:
            print("Ingrese un número válido.")

def menu_Empleado():
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
        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
        print("""
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
        """)
        opcion = input("Elige una opción [1-5, 0]: ").strip()
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            rut = input("Ingrese rut de la persona: ")
            nombre = input("Ingrese nombre de la persona: ")
            edad = input("Ingrese edad de la persona: ")
            direccion = input("Ingrese direccion de la persona: ")
            telefono = input("Ingrese telefono de la persona: ")
            email = input("Ingrese email de la persona: ")
            create_Empleado(rut, nombre, edad, direccion, telefono, email)
            input("Ingrese ENTER para continuar...")
            print("Insertar Empleado")
            idv = safe_int_input("ID (num): ")
            rut = input("RUT: ")
            nombre = input("Nombre: ")
            edad = input("Edad (opcional): ").strip()
            edad_v = int(edad) if edad else None
            direccion = input("Direccion (opcional): ").strip() or None
            telefono = input("Telefono (opcional): ").strip() or None
            email = input("Email (opcional): ").strip() or None
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD) (opcional): ").strip() or None
            sueldo = input("Sueldo (opcional, ejemplo 4500000.0): ").strip()
            sueldo_v = float(sueldo) if sueldo else None
            create_Empleado(idv, rut, nombre, edad_v, direccion, telefono, email, fecha_inicio, sueldo_v)
            input("ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_Empleado()
            input("Ingrese ENTER para continuar...")
            read_all("Empleado")
            input("ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            id = input("Ingrese id de la persona: ")
            read_Empleado_by_id(id)
            input("Ingrese ENTER para continuar...")
            idv = safe_int_input("ID: ")
            read_by_id("Empleado", idv)
            input("ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Modificar un dato")
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
            update_Empleado(rut, nombre, edad, direccion, telefono, email)
            input("Ingrese ENTER para continuar...")
            idv = safe_int_input("ID a modificar: ")
            print("[Solo ingrese los campos a cambiar]")
            rut = input("Nuevo RUT (vacío = no cambiar): ").strip() or None
            nombre = input("Nuevo Nombre (vacío = no cambiar): ").strip() or None
            edad = input("Nueva Edad (vacío = no cambiar): ").strip()
            edad_v = int(edad) if edad else None
            direccion = input("Nueva Direccion (vacío = no cambiar): ").strip() or None
            telefono = input("Nuevo Telefono (vacío = no cambiar): ").strip() or None
            email = input("Nuevo Email (vacío = no cambiar): ").strip() or None
            fecha_inicio = input("Nueva Fecha inicio YYYY-MM-DD (vacío = no cambiar): ").strip() or None
            sueldo = input("Nuevo Sueldo (vacío = no cambiar): ").strip()
            sueldo_v = float(sueldo) if sueldo else None
            update_Empleado(idv, rut=rut, nombre=nombre, edad=edad_v, direccion=direccion, telefono=telefono, email=email, fecha_inicio=fecha_inicio, sueldo=sueldo_v)
            input("ENTER para continuar...")
        elif opcion == "5":
            os.system("cls")
            print("5. Eliminar un dato")
            id = input("Ingrese id de la persona: ")
            delete_Empleado(id)
            input("Ingrese ENTER para continuar...")
            idv = safe_int_input("ID a eliminar: ")
            delete_from_table("Empleado", idv)
            input("ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")
            print("Opción incorrecta.")
            input("ENTER para continuar...")

def menu_Departamento():
    while True:
        os.system("cls")
        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
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
                | * La tabla empleado necesita al  |
                | menos un registro creado en la   |
                | tabla Proyecto y Departamentos.  |
                ====================================
            ====================================
            |     MENÚ DEPARTAMENTO            |
            |----------------------------------|
            | 1. Insertar                      |
            | 2. Ver todos                     |
            | 3. Buscar por ID                 |
            | 4. Actualizar                    |
            | 5. Eliminar                      |
            | 0. Volver                        |
            ====================================
        """)

        op = input("Opción: ")

        op = input("Opción: ").strip()
        if op == "1":
            ID = int(input("ID: "))
            Nombre = input("Nombre: ")
            Gerente = input("Gerente: ")
            create_Departamento(ID, Nombre, Gerente)

        elif op == "2":
            read_Departamento()
            idv = safe_int_input("ID: ")
            nombre = input("Nombre: ")
            gerente = input("Gerente (opcional): ").strip() or None
            create_Departamento(idv, nombre, gerente)
            input("ENTER...")

        elif op == "2":
            read_all("Departamento"); input("ENTER...")
        elif op == "3":
            ID = int(input("ID: "))
            read_Departamento_by_id(ID)
            input("ENTER...")

            idv = safe_int_input("ID: "); read_by_id("Departamento", idv); input("ENTER...")
        elif op == "4":
            ID = int(input("ID: "))
            Nombre = input("Nuevo nombre: ") or None
            Gerente = input("Nuevo gerente: ") or None
            update_Departamento(ID, Nombre, Gerente)

            idv = safe_int_input("ID a modificar: ")
            nombre = input("Nuevo nombre (vacío = no cambiar): ").strip() or None
            gerente = input("Nuevo gerente (vacío = no cambiar): ").strip() or None
            update_Departamento(idv, nombre, gerente)
            input("ENTER...")
        elif op == "5":
            ID = int(input("ID: "))
            delete_Departamentos(ID)

            idv = safe_int_input("ID a eliminar: "); delete_from_table("Departamento", idv); input("ENTER...")
        elif op == "0":
            return
        
        else:
            print("Opción inválida."); input("ENTER...")

def menu_Proyecto():
    while True:
        os.system("cls")
        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
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
                | * La tabla empleado necesita al  |
                | menos un registro creado en la   |
                | tabla Proyecto y Departamentos.  |
                ====================================
            ====================================
            |     MENÚ PROYECTO                |
            |----------------------------------|
            | 1. Insertar                      |
            | 2. Ver todos                     |
            | 3. Buscar por ID                 |
            | 4. Actualizar                    |
            | 5. Eliminar                      |
            | 0. Volver                        |
            ====================================
        """)

        op = input("Opción: ")

        op = input("Opción: ").strip()
        if op == "1":
            ID = int(input("ID: "))
            Nombre = input("Nombre: ")
            Descripcion = input("Descripción: ")
            Fecha = input("Fecha Inicio (YYYY-MM-DD): ")
            create_Proyecto(ID, Nombre, Descripcion, Fecha)

        elif op == "2":
            read_Proyecto()
            idv = safe_int_input("ID: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripcion (opcional): ").strip() or None
            fecha = input("Fecha inicio YYYY-MM-DD (opcional): ").strip() or None
            create_Proyecto(idv, nombre, descripcion, fecha)
            input("ENTER...")

        elif op == "2":
            read_all("Proyecto"); input("ENTER...")
        elif op == "3":
            ID = int(input("ID: "))
            read_Proyecto_by_id(ID)
            input("ENTER...")

            idv = safe_int_input("ID: "); read_by_id("Proyecto", idv); input("ENTER...")
        elif op == "4":
            ID = int(input("ID: "))
            Nombre = input("Nuevo nombre: ") or None
            Descripcion = input("Nueva descripción: ") or None
            Fecha = input("Nueva fecha: ") or None
            update_Proyecto(ID, Nombre, Descripcion, Fecha)

            idv = safe_int_input("ID a modificar: ")
            nombre = input("Nuevo nombre (vacío = no cambiar): ").strip() or None
            descripcion = input("Nueva descripcion (vacío = no cambiar): ").strip() or None
            fecha = input("Nueva fecha YYYY-MM-DD (vacío = no cambiar): ").strip() or None
            update_Proyecto(idv, nombre, descripcion, fecha)
            input("ENTER...")
        elif op == "5":
            ID = int(input("ID: "))

            idv = safe_int_input("ID a eliminar: "); delete_from_table("Proyecto", idv); input("ENTER...")
        elif op == "0":
            return
        else:
            print("Opción inválida."); input("ENTER...")

def menu_Informe():
    while True:
        os.system("cls")
        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
        print("""
        ===== MENÚ INFORME =====
        1. Insertar
        2. Ver todos
        3. Buscar por ID
        4. Actualizar
        5. Eliminar
        0. Volver
            ===== MENÚ INFORME =====
            1. Insertar
            2. Ver todos
            3. Buscar por ID
            4. Actualizar
            5. Eliminar
            0. Volver
        """)

        op = input("Opción: ")

        op = input("Opción: ").strip()
        if op == "1":
            ID = int(input("ID: "))
            IDp = int(input("ID del proyecto: "))
            Descripcion = input("Descripción: ")
            create_Informe(ID, IDp, Descripcion)

        elif op == "2":
            read_Informe()
            idv = safe_int_input("ID: ")
            pid = safe_int_input("ID Proyecto: ")
            desc = input("Descripcion (opcional): ").strip() or None
            create_Informe(idv, pid, desc)
            input("ENTER...")

        elif op == "2":
            read_all("Informe"); input("ENTER...")
        elif op == "3":
            ID = int(input("ID: "))
            read_Informe_by_id(ID)
            input("ENTER...")

            idv = safe_int_input("ID: "); read_by_id("Informe", idv); input("ENTER...")
        elif op == "4":
            ID = int(input("ID: "))
            IDp = input("Nuevo ID proyecto: ") or None
            Desc = input("Nueva descripción: ") or None
            update_Informe(ID, int(IDp) if IDp else None, Desc)

            idv = safe_int_input("ID a modificar: ")
            pid = input("Nuevo proyecto_id (vacío = no cambiar): ").strip()
            pid_v = int(pid) if pid else None
            desc = input("Nueva descripcion (vacío = no cambiar): ").strip() or None
            update_Informe(idv, proyecto_id=pid_v, descripcion=desc)
            input("ENTER...")
        elif op == "5":
            ID = int(input("ID: "))
            delete_Informe(ID)

            idv = safe_int_input("ID a eliminar: "); delete_from_table("Informe", idv); input("ENTER...")
        elif op == "0":
            return

        else:
            print("Opción inválida."); input("ENTER...")

def menu_Usuario():
    while True:
        os.system("cls")
        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
        print("""
        ===== MENÚ USUARIO =====
        1. Insertar
        2. Ver todos
        3. Buscar por ID
        4. Actualizar
        5. Eliminar
        0. Volver
            ===== MENÚ USUARIO =====
            1. Insertar
            2. Ver todos
            3. Buscar por ID
            4. Actualizar
            5. Eliminar
            0. Volver
        """)

        op = input("Opción: ")

        op = input("Opción: ").strip()
        if op == "1":
            ID = int(input("ID: "))
            User = input("Nombre usuario: ")
            Contra = input("Contraseña: ")
            create_Usuario(ID, User, Contra)

        elif op == "2":
            read_Usuario()
            idv = safe_int_input("ID: ")
            user = input("Username: ")
            pwd = input("Contraseña: ")
            create_Usuario(idv, user, pwd)
            input("ENTER...")

        elif op == "2":
            read_all("Usuario"); input("ENTER...")
        elif op == "3":
            ID = int(input("ID: "))
            read_Usuario_by_id(ID)
            input("ENTER...")

            idv = safe_int_input("ID: "); read_by_id("Usuario", idv); input("ENTER...")
        elif op == "4":
            ID = int(input("ID: "))
            User = input("Nuevo usuario: ") or None
            Contra = input("Nueva contraseña: ") or None
            update_Usuario(ID, User, Contra)

            idv = safe_int_input("ID a modificar: ")
            user = input("Nuevo username (vacío=no cambiar): ").strip() or None
            pwd = input("Nueva contraseña (vacío=no cambiar): ").strip() or None
            update_Usuario(idv, username=user, contrasena=pwd)
            input("ENTER...")
        elif op == "5":
            ID = int(input("ID: "))
            delete_Usuario(ID)

            idv = safe_int_input("ID a eliminar: "); delete_from_table("Usuario", idv); input("ENTER...")
        elif op == "0":
            return

        else:
            print("Opción inválida."); input("ENTER...")

def menu_Tiempo():
    while True:
        os.system("cls")
        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
        print("""
        ===== MENÚ REGISTRAR TIEMPO =====
        1. Insertar
        2. Ver todos
        3. Buscar por ID
        4. Actualizar
        5. Eliminar
        0. Volver
            ===== MENÚ REGISTRAR TIEMPO =====
            1. Insertar
            2. Ver todos
            3. Buscar por ID
            4. Actualizar
            5. Eliminar
            0. Volver
        """)

        op = input("Opción: ")

        op = input("Opción: ").strip()
        if op == "1":
            ID = int(input("ID: "))
            IDempleado = int(input("ID Empleado: "))
            Fecha = input("Fecha (YYYY-MM-DD): ")
            Horas = int(input("Horas: "))
            Desc = input("Descripción: ")
            create_RegistrarTiempo(ID, IDempleado, Fecha, Horas, Desc)

        elif op == "2":
            read_RegistrarTiempo()
            idv = safe_int_input("ID: ")
            emp = safe_int_input("ID Empleado: ")
            fecha = input("Fecha (YYYY-MM-DD): ").strip()
            horas = safe_int_input("Horas: ")
            desc = input("Descripcion (opcional): ").strip() or None
            create_RegistrarTiempo(idv, emp, fecha, horas, desc)
            input("ENTER...")

        elif op == "2":
            read_all("RegistrarTiempo"); input("ENTER...")
        elif op == "3":
            ID = int(input("ID: "))
            read_RegistrarTiempo_by_id(ID)
            input("ENTER...")

            idv = safe_int_input("ID: "); read_by_id("RegistrarTiempo", idv); input("ENTER...")
        elif op == "4":
            ID = int(input("ID: "))
            IDE = input("Nuevo ID empleado: ") or None
            Fecha = input("Nueva fecha: ") or None
            Horas = input("Nuevas horas: ") or None
            Desc = input("Nueva descripción: ") or None
            update_RegistroTiempo(
                ID,
                int(IDE) if IDE else None,
                Fecha,
                int(Horas) if Horas else None,
                Desc
            )

            idv = safe_int_input("ID a modificar: ")
            emp = input("Nuevo ID Empleado (vacío = no cambiar): ").strip()
            emp_v = int(emp) if emp else None
            fecha = input("Nueva fecha YYYY-MM-DD (vacío = no cambiar): ").strip() or None
            horas = input("Nuevas horas (vacío = no cambiar): ").strip()
            horas_v = int(horas) if horas else None
            desc = input("Nueva descripcion (vacío = no cambiar): ").strip() or None
            update_RegistrarTiempo(idv, empleado_id=emp_v, fecha=fecha, horas=horas_v, descripcion=desc)
            input("ENTER...")
        elif op == "5":
            ID = int(input("ID: "))
            delete_RegistroTiempo(ID)

            idv = safe_int_input("ID a eliminar: "); delete_from_table("RegistrarTiempo", idv); input("ENTER...")
        elif op == "0":
            return
        else:
            print("Opción inválida."); input("ENTER...")


# -------------------------
# Main
# -------------------------
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

        os_name = "cls" if os.name == "nt" else "clear"
        os.system(os_name)
        print("""
            ====================================
            |     CRUD: Oracle + Python        |
            |----------------------------------|
            | 1. Crear todas las tablas        |
            | 2. Gestionar tabla Empleado      |
            | 3. Gestionar tabla Departamento  |
            | 4. Gestionar tabla Proyecto      |
            | 5. Gestionar tabla Informe       |
            | 6. Gestionar tabla Usuario       |
            | 7. Gestionar RegistrarTiempo     |
            | 0. Salir del sistema             |
            ====================================
        """)
        opcion = input("Elige una opción [0-7]: ").strip()
        if opcion == "1":
            os.system("cls")
            create_all_tables()
            input("Ingrese ENTER para continuar...")
            create_all_tables(); input("ENTER...")
        elif opcion == "2":
            menu_Empleado()

        elif opcion == "3":
            os.system("cls")
            try:
                menu_Departamento()
            except Exception as e:
                print(f"Error gestionando Departamento: {e}")
                input("Ingrese ENTER para continuar...")
            
            menu_Departamento()
        elif opcion == "4":
            os.system("cls")
            try:
                menu_Proyecto()
            except Exception as e:
                    print(f"Error gestionando Proyecto: {e}")
            input("Ingrese ENTER para continuar...")
        

            menu_Proyecto()
        elif opcion == "5":
            menu_Informe()
        elif opcion == "6":
            menu_Usuario()
        elif opcion == "7":
            menu_Tiempo()
        elif opcion == "0":
            os.system("cls")
            print("Saliendo del sistema...")
        break 
        
    else:
        os.system("cls")
        print("Opción incorrecta, intente nuevamente.")
        input("Ingrese ENTER para continuar...")

            print("Saliendo...")
            break
        else:
            print("Opción incorrecta.")
            input("ENTER...")

if __name__ == "__main__":
    main()    main()

