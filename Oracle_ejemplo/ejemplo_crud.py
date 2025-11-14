import oracledb
import os
from dotenv import load_dotenv
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