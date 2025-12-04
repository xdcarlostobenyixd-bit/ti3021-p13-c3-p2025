import os
import datetime
from typing import Optional, Any, Dict, List, Tuple
from dotenv import load_dotenv
import oracledb

load_dotenv()

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
            connection.commit()
        print("Tabla/process ejecutado.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar: {error}")

def create_all_tables():
    tables = [
        # Empleado
        """
        CREATE TABLE Empleado (
            id NUMBER PRIMARY KEY,
            rut VARCHAR2(30),
            nombre VARCHAR2(100),
            edad NUMBER,
            direccion VARCHAR2(200),
            telefono VARCHAR2(30),
            email VARCHAR2(100),
            fecha_inicio DATE,
            sueldo NUMBER
        )
        """,
        # Departamento
        """
        CREATE TABLE Departamento (
            id NUMBER PRIMARY KEY,
            nombre VARCHAR2(100),
            gerente VARCHAR2(100)
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

    for q in tables:
        create_schema(q)


# CREATE - Inserts

def create_Empleado(id: int, rut: str, nombre: str, edad: Optional[int], direccion: Optional[str],
                    telefono: Optional[str], email: Optional[str], fecha_inicio: Optional[str], sueldo: Optional[float]):
    fecha = parse_date(fecha_inicio) if fecha_inicio else None
    sql = """
        INSERT INTO Empleado (id, rut, nombre, edad, direccion, telefono, email, fecha_inicio, sueldo)
        VALUES (:id, :rut, :nombre, :edad, :direccion, :telefono, :email, :fecha_inicio, :sueldo)
    """
    params = {"id": id, "rut": rut, "nombre": nombre, "edad": edad,
              "direccion": direccion, "telefono": telefono, "email": email,
              "fecha_inicio": fecha, "sueldo": sueldo}
    ok, err = execute_write(sql, params)
    if ok:
        print("Inserción Empleado correcta.")
    else:
        print("Error crear Empleado:", err)

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

def create_Informe(id: int, proyecto_id: int, descripcion: Optional[str]):
    sql = "INSERT INTO Informe (id, proyecto_id, descripcion) VALUES (:id, :proyecto_id, :descripcion)"
    ok, err = execute_write(sql, {"id": id, "proyecto_id": proyecto_id, "descripcion": descripcion})
    if ok:
        print("Inserción Informe correcta.")
    else:
        print("Error crear Informe:", err)

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


# READ - Selects

def read_all(table: str):
    sql = f"SELECT * FROM {table}"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                if not rows:
                    print("No hay registros.")
                for r in rows:
                    print(r)
    except oracledb.DatabaseError as e:
        print("Error lectura:", e)

def read_by_id(table: str, id_val: int):
    sql = f"SELECT * FROM {table} WHERE id = :id"
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, {"id": id_val})
                row = cur.fetchone()
                if row:
                    print(row)
                else:
                    print("Registro no encontrado.")
    except oracledb.DatabaseError as e:
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


# DELETE

def delete_from_table(table: str, id_val: int):
    sql = f"DELETE FROM {table} WHERE id = :id"
    ok, err = execute_write(sql, {"id": id_val})
    if ok:
        print(f"Registro eliminado de {table}.")
    else:
        print("Error eliminar:", err)


# Menús 

def safe_int_input(prompt: str) -> int:
    while True:
        val = input(prompt)
        try:
            return int(val)
        except ValueError:
            print("Ingrese un número válido.")

def menu_Empleado():
    while True:
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
            read_all("Empleado")
            input("ENTER para continuar...")
        elif opcion == "3":
            idv = safe_int_input("ID: ")
            read_by_id("Empleado", idv)
            input("ENTER para continuar...")
        elif opcion == "4":
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
            idv = safe_int_input("ID a eliminar: ")
            delete_from_table("Empleado", idv)
            input("ENTER para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción incorrecta.")
            input("ENTER para continuar...")

def menu_Departamento():
    while True:
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
            ====================================
        """)
        op = input("Opción: ").strip()
        if op == "1":
            idv = safe_int_input("ID: ")
            nombre = input("Nombre: ")
            gerente = input("Gerente (opcional): ").strip() or None
            create_Departamento(idv, nombre, gerente)
            input("ENTER...")
        elif op == "2":
            read_all("Departamento"); input("ENTER...")
        elif op == "3":
            idv = safe_int_input("ID: "); read_by_id("Departamento", idv); input("ENTER...")
        elif op == "4":
            idv = safe_int_input("ID a modificar: ")
            nombre = input("Nuevo nombre (vacío = no cambiar): ").strip() or None
            gerente = input("Nuevo gerente (vacío = no cambiar): ").strip() or None
            update_Departamento(idv, nombre, gerente)
            input("ENTER...")
        elif op == "5":
            idv = safe_int_input("ID a eliminar: "); delete_from_table("Departamento", idv); input("ENTER...")
        elif op == "0":
            return
        else:
            print("Opción inválida."); input("ENTER...")

def menu_Proyecto():
    while True:
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
            ====================================
        """)
        op = input("Opción: ").strip()
        if op == "1":
            idv = safe_int_input("ID: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripcion (opcional): ").strip() or None
            fecha = input("Fecha inicio YYYY-MM-DD (opcional): ").strip() or None
            create_Proyecto(idv, nombre, descripcion, fecha)
            input("ENTER...")
        elif op == "2":
            read_all("Proyecto"); input("ENTER...")
        elif op == "3":
            idv = safe_int_input("ID: "); read_by_id("Proyecto", idv); input("ENTER...")
        elif op == "4":
            idv = safe_int_input("ID a modificar: ")
            nombre = input("Nuevo nombre (vacío = no cambiar): ").strip() or None
            descripcion = input("Nueva descripcion (vacío = no cambiar): ").strip() or None
            fecha = input("Nueva fecha YYYY-MM-DD (vacío = no cambiar): ").strip() or None
            update_Proyecto(idv, nombre, descripcion, fecha)
            input("ENTER...")
        elif op == "5":
            idv = safe_int_input("ID a eliminar: "); delete_from_table("Proyecto", idv); input("ENTER...")
        elif op == "0":
            return
        else:
            print("Opción inválida."); input("ENTER...")

def menu_Informe():
    while True:
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
        """)
        op = input("Opción: ").strip()
        if op == "1":
            idv = safe_int_input("ID: ")
            pid = safe_int_input("ID Proyecto: ")
            desc = input("Descripcion (opcional): ").strip() or None
            create_Informe(idv, pid, desc)
            input("ENTER...")
        elif op == "2":
            read_all("Informe"); input("ENTER...")
        elif op == "3":
            idv = safe_int_input("ID: "); read_by_id("Informe", idv); input("ENTER...")
        elif op == "4":
            idv = safe_int_input("ID a modificar: ")
            pid = input("Nuevo proyecto_id (vacío = no cambiar): ").strip()
            pid_v = int(pid) if pid else None
            desc = input("Nueva descripcion (vacío = no cambiar): ").strip() or None
            update_Informe(idv, proyecto_id=pid_v, descripcion=desc)
            input("ENTER...")
        elif op == "5":
            idv = safe_int_input("ID a eliminar: "); delete_from_table("Informe", idv); input("ENTER...")
        elif op == "0":
            return
        else:
            print("Opción inválida."); input("ENTER...")

def menu_Usuario():
    while True:
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
        """)
        op = input("Opción: ").strip()
        if op == "1":
            idv = safe_int_input("ID: ")
            user = input("Username: ")
            pwd = input("Contraseña: ")
            create_Usuario(idv, user, pwd)
            input("ENTER...")
        elif op == "2":
            read_all("Usuario"); input("ENTER...")
        elif op == "3":
            idv = safe_int_input("ID: "); read_by_id("Usuario", idv); input("ENTER...")
        elif op == "4":
            idv = safe_int_input("ID a modificar: ")
            user = input("Nuevo username (vacío=no cambiar): ").strip() or None
            pwd = input("Nueva contraseña (vacío=no cambiar): ").strip() or None
            update_Usuario(idv, username=user, contrasena=pwd)
            input("ENTER...")
        elif op == "5":
            idv = safe_int_input("ID a eliminar: "); delete_from_table("Usuario", idv); input("ENTER...")
        elif op == "0":
            return
        else:
            print("Opción inválida."); input("ENTER...")

def menu_Tiempo():
    while True:
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
        """)
        op = input("Opción: ").strip()
        if op == "1":
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
            idv = safe_int_input("ID: "); read_by_id("RegistrarTiempo", idv); input("ENTER...")
        elif op == "4":
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
            create_all_tables(); input("ENTER...")
        elif opcion == "2":
            menu_Empleado()
        elif opcion == "3":
            menu_Departamento()
        elif opcion == "4":
            menu_Proyecto()
        elif opcion == "5":
            menu_Informe()
        elif opcion == "6":
            menu_Usuario()
        elif opcion == "7":
            menu_Tiempo()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta.")
            input("ENTER...")

if __name__ == "__main__":
    main()

