# Para ocultar los caracteres
import getpass
# Para limpiar la consola y para manipular archivos
import os
# Para usar delay
from time import sleep
# Para ruleta y generación de likes en matriz
import random
# Para calcular la edad
from datetime import datetime
# Para manipular archivos
import os.path
import pickle
import io
import math

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#--------------------------------REGISTROS-------------------------------#
class likes:
    def __init__(self):
        #ID remitente
        self.idrem=0
        #ID destinatario
        self.iddest=0

class estudiantes:
    def __init__(self):
        #Asigno atributos
        self.idregistro = 0
        self.email = ""
        self.nombre = ""
        self.sexo = ""
        self.contraseña = ""
        self.estado = False
        self.hobbies = ""
        self.materia_fav = ""
        self.deporte_fav = ""
        self.materia_fuerte = ""
        self.materia_debil = ""
        self.biografia = ""
        self.pais = ""
        self.ciudad = ""
        self.fecha_nacimiento = ""

class moderadores:
    def __init__(self):
        self.idregistro = 0
        self.email = ""
        self.contraseña = ""
        self.estado = False

class administradores:
    def __init__(self):
        self.idregistro = 0
        self.email = ""
        self.contraseña = ""

class reportes:
    def __init__(self):
        self.nroreporte = 0
        self.idreportante = 0
        self.reportanteestado = False
        self.idreportado = 0
        self.reportadoestado = False
        self.razon = ""
        self.estadoreporte = 0
        self.detalles = ""
        self.idmoderador = 0

class contadordereportes:
    def __init__(self):
        self.idmoderador = 0
        self.reportesignorados = 0
        self.reportesaceptados = 0
        self.totalreportes = 0



#-------------------------------FORMATEO----------------------------#

def formato_estudiante(self):

    self.email = self.email.ljust(32, " ")
    self.nombre = self.nombre.ljust(32, " ")
    self.contraseña = self.contraseña.ljust(32, " ")
    self.hobbies = self.hobbies.ljust(255, " ")
    self.materia_fav = self.materia_fav.ljust(16, " ")
    self.deporte_fav = self.deporte_fav.ljust(16, " ")
    self.materia_fuerte = self.materia_fuerte.ljust(16, " ")
    self.materia_debil = self.materia_debil.ljust(16, " ")
    self.biografia = self.biografia.ljust(255, " ")
    self.pais = self.pais.ljust(32, " ")
    self.ciudad = self.ciudad.ljust(32, " ")
    self.fecha_nacimiento = self.fecha_nacimiento.ljust(10, " ")
        
def formato_admin_mod(self):
    self.email = self.email.ljust(32, " ")
    self.contraseña = self.contraseña.ljust(32, " ")

def formato_reportes(self):
    self.razon = self.razon.ljust(50, " ")
    self.detalles = self.detalles.ljust(255, " ")


#--------------------------------VERIFICAR ARCHIVO---------------------------#

def verificar_archivo(path):
    #Si existe el archivo, lo abre como escritura
    if os.path.exists(path):
        archivo_log=open(path,"r+b")
    else:
        archivo_log=open(path,"w+b")
        #Si no existe el archivo lo crea y abre
    return archivo_log


#------------------------------VARIABLES CON INFO----------------------------#

currentdate = datetime.now()
CYEAR = int(currentdate.year)
CYEARF = CYEAR - 18
CYEARI = CYEAR - 60
DPY = 365

nombre1 = "Juan Faccio"
nombre2 = "Julian Perez"
nombre3 = "Kevin Dorko"
nombre4 = "Maximo Jesus Gomez"

materia1 = "Fisica"
materia2 = "Matematica"
materia3 = "Algebra"
materia4 = "Algoritmo"
materia5 = "Quimica"
materia6 = "Ingles"
materia7 = "Logica"
materia8 = "Sintaxis"

deporte1 = "Futbol"
deporte2 = "Escalada"
deporte3 = "Tennis"
deporte4 = "PingPong"

hobbies1 = "Cocinar"
hobbies2 = "Programar"
hobbies3 = "Gamer"
hobbies4 = "Poesia"

biografia1 = "Trabajo desde los 18 anios. Me gusta la cocina y soy amante de los perros. Mi favorito es el Siberiano"
biografia2 = "Vivo en Villa Gobernador Galvez, soy empresario exitoso con mucho dinero y tres novias. No suenies tu vida, vivi tus suenios"
biografia3 = "Me gusta estudiar y cuando crezca quiero ser profesor como Milton"
biografia4 = "Quiero ser Ingeniero en sistemas porque me gusta el dinero y si voy a ser explotado, prefiero ser explotado desde la comodidad de mi casa"

pais = "Argentina"

ciudad1 = "Rosario"
ciudad2 = "VGG"
ciudad3 = "Perez"
ciudad4 = "Rufino"

#----------------------------RAZON DE REPORTES-----------------------------------#

razon1 = "Unlike bombing"
razon2 = "No me devolvio el like"
razon3 = "Difamacion"
razon4 = "Es un amigo Buitre"
razon5 = "Otra"


#--------------------------CARGA DE DATOS AUTOMATICO-----------------------------#

def cargar_archivo_estudiantes():
    archivo_logico_estudiantes.seek(0, 0)
    for i in range(0, 4):
        estudiante = estudiantes()
        estudiante.idregistro = i
        estudiante.email = "estudiante" + str(i + 1) + "@ayed.com"
        estudiante.nombre = globals()[f"nombre{i + 1}"]
        estudiante.sexo = "M"
        estudiante.contraseña = str(111222 + 111111 * i)
        estudiante.estado = True
        estudiante.hobbies = globals()[f"hobbies{i + 1}"]
        estudiante.materia_fav = globals()[f"materia{i + 1}"]
        estudiante.deporte_fav = globals()[f"deporte{i + 1}"]
        estudiante.materia_fuerte = globals()[f"materia{random.randint(1, 4)}"]
        estudiante.materia_debil = globals()[f"materia{random.randint(4, 8)}"]
        estudiante.biografia = globals()[f"biografia{i + 1}"]
        estudiante.pais = globals()["pais"]
        estudiante.ciudad = globals()[f"ciudad{i + 1}"]
        estudiante.fecha_nacimiento = rdob()
        formato_estudiante(estudiante)
        pickle.dump(estudiante, archivo_logico_estudiantes)
        archivo_logico_estudiantes.flush()


def cargar_archivo_admin_mod(tipodeusuario, clase):

    if tipodeusuario == "moderador":
        archivo_logico_moderadores.seek(0,0)
    elif tipodeusuario == "administrador":
        archivo_logico_administradores.seek(0,0)
    variable = clase ()
    variable.idregistro = 1
    variable.email = (tipodeusuario) + "0@utn.edu.ar"
    variable.contraseña = "123456"
    if tipodeusuario == "moderador":
        variable.estado = True
        formato_admin_mod(variable)
        pickle.dump(variable,archivo_logico_moderadores)
        archivo_logico_moderadores.flush()
    if tipodeusuario == "administrador":
        formato_admin_mod(variable)
        pickle.dump(variable,archivo_logico_administradores)
        archivo_logico_administradores.flush()

def cargar_archivo_reportes():

    archivo_logico_reportes.seek(0, 0)
    for i in range(0, 4):
        reporte = reportes()
        reporte.nroreporte = i
        reporte.idreportante = 0
        reporte.reportanteestado = True
        reporte.idreportado = 4 - i
        reporte.reportadoestado = True
        reporte.razon = globals()[f"razon{random.randint(1, 4)}"]
        reporte.estadoreporte = 0
        reporte.detalles = ""
        reporte.idmoderador = 0
        formato_reportes(reporte)
        pickle.dump(reporte, archivo_logico_reportes)
        archivo_logico_reportes.flush()

def cargar_archivo_likes():

    archivo_logico_likes.seek(0,0)
    for i in range(4):
        like=likes()
        like.idrem=i
        like.iddest=random.randint(0,3)
        #Para que no se den like a si mismos
        while like.iddest==like.idrem:
            like.iddest=random.randint(0,3)
        pickle.dump(like,archivo_logico_likes)
        archivo_logico_likes.flush()


def rdob():
    rdd = str(random.randint(1,28))
    rmm = str(random.randint(1,12))
    ryear = str(random.randint(CYEARI,CYEARF))
    rdate = str(ryear) + "-" + str(rmm) + "-" + str(rdd)
    rdate = datetime.strptime(rdate, "%Y-%m-%d").date()
    rdate = str(rdate)
    return rdate



def main():
    global archivo_logico_estudiantes, archivo_logico_administradores, archivo_logico_moderadores, archivo_logico_reportes, archivo_logico_likes, archivo_logico_contadordereportes
    global archivo_fisico_estudiantes, archivo_fisico_administradores, archivo_fisico_moderadores, archivo_fisico_reportes, archivo_fisico_likes, archivo_fisico_contadordereportes

    #archivo_fisico_xxxxxxxx="ruta de este .py" + \\xxxxxxxx.dat 
    archivo_fisico_estudiantes = os.getcwd()+"\\estudiantes.dat"
    archivo_fisico_administradores = os.getcwd()+"\\administradores.dat"
    archivo_fisico_moderadores = os.getcwd()+"\\moderadores.dat"
    archivo_fisico_reportes = os.getcwd()+"\\reportes.dat"
    archivo_fisico_likes = os.getcwd()+"\\likes.dat"
    archivo_fisico_contadordereportes = os.getcwd()+"\\contadordereportes.dat"

    archivo_logico_estudiantes = verificar_archivo(archivo_fisico_estudiantes)
    archivo_logico_administradores = verificar_archivo(archivo_fisico_administradores)
    archivo_logico_moderadores = verificar_archivo(archivo_fisico_moderadores)
    archivo_logico_reportes = verificar_archivo(archivo_fisico_reportes)
    archivo_logico_likes = verificar_archivo(archivo_fisico_likes)
    archivo_logico_contadordereportes = verificar_archivo(archivo_fisico_contadordereportes)

    if os.path.getsize(archivo_fisico_estudiantes)==0:
        cargar_archivo_estudiantes()
    if os.path.getsize(archivo_fisico_administradores)==0:
        cargar_archivo_admin_mod("administrador", administradores)
    if os.path.getsize(archivo_fisico_moderadores)==0:
        cargar_archivo_admin_mod("moderador", moderadores)
    if os.path.getsize(archivo_fisico_reportes)==0:
        cargar_archivo_reportes()
    if os.path.getsize(archivo_fisico_likes)==0:
        cargar_archivo_likes()
    
    


#----------------------------VALIDAR CAMPOS / OPCIONES GENERAL-------------------------------#

def validar_campos_texto(campo_validar, longitud):
    campo = input("Ingrese " + campo_validar + " (máximo " + str(longitud) + " caracteres):")
    while len(campo) > longitud:
        limpiar_pantalla()
        print("Ingrese el campo con la longitud adecuada:")
        campo = input("Ingrese " + campo_validar + " (máximo " + str(longitud) + " caracteres):")
    campo = campo.ljust(longitud," ")
    return campo

def validar_campos_contrasenia(campo_validar, longitud):
    campo = getpass.getpass("Ingrese " + campo_validar + " (máximo " + str(longitud) + " caracteres):")
    while len(campo) > longitud:
        limpiar_pantalla()
        print("Ingrese el campo con la longitud adecuada:")
        campo = ("Ingrese " + campo_validar + " (máximo " + str(longitud) + " caracteres):")
    campo = campo.ljust(longitud," ")
    return campo

def validar_fecha(D, M, Y):


    if D.isdigit() and M.isdigit() and Y.isdigit():
        dd = int(D)
        mm = int(M)
        year = int(Y)
        if CYEARI < year < CYEARF:
            if 1 <= mm < 13:
                if mm == 2:
                    ddmax = 28
                elif (mm == 4) or (mm == 6) or (mm == 9) or (mm == 11):
                    ddmax = 30
                else:
                    ddmax = 31
                if 1 <= dd <= ddmax:
                    date = str(year) + "-" + str(mm) + "-" + str(dd)
                    date = datetime.strptime(date, "%Y-%m-%d").date()
                    date = str(date)
                else:
                    date=-1
            else:
                date=-1
        else:
            date=-1
    else:
        date = -1
    #return -1
    return date

def modulo_ingrese_fecha():
    print("Ingresando fecha de nacimiento DD-MM-YYYY")
    ndd = input("Ingrese día formato (DD): ")
    nmm = input("Ingrese mes formato (MM): ")
    nyear = input("Ingrese año formato (YYYY): ")
    fecha = validar_fecha(ndd, nmm, nyear)
    while fecha == -1:
        limpiar_pantalla()
        print("Ingrese una fecha válida")
        ndd = input("Ingrese día formato (DD): ")
        nmm = input("Ingrese mes formato (MM): ")
        nyear = input("Ingrese año formato (YYYY): ")
        fecha = validar_fecha(ndd, nmm, nyear)
    return fecha

def validar_opcion_numerica(opcion, minimo, maximo):

    if opcion.isdigit():
        opcion = int(opcion)
        if not (minimo <= opcion <= maximo):
            opcion=-1
    return opcion


def validar(minimo,maximo):
    opc = input("ingrese una opcion del " + str(minimo) + " al " + str(maximo) + ": ")
    opc = validar_opcion_numerica(opc, minimo, maximo)
    while opc == -1:
        #limpiar_pantalla()
        print ("La opcion es incorrecta")
        opc = input("ingrese una opcion del " + str(minimo) + " al " + str(maximo) + ": ")
        opc = validar_opcion_numerica(opc, minimo, maximo)
    return opc

def validar_opcion_alfabetica(opcion, string):
    i = 0

    while i < len(string) and string[i] != opcion:
        i = i + 1

    if not (i < len(string) and string[i] == opcion):
        #return opcion
        opcion=-1

    return opcion

def validaralfabeticamente(string, letrainicial, letrafinal):
    opc = input("Ingrese una opción de la " + letrainicial + " a " + letrafinal + ": ")
    opc = validar_opcion_alfabetica(opc, string)
    while opc == -1:
        print("La opción es incorrecta")
        opc = input("Ingrese una opción de la " + letrainicial + " a " + letrafinal + ": ")
        opc = validar_opcion_alfabetica(opc, string)
    return opc

def validar_mientras (titulo, condicion1, condicion2):
    campo = input (titulo)
    while campo != condicion1 and campo != condicion2:
        print ("La opcion es incorrecta")
        campo = input (titulo)
    return campo


#--------------------------------MENU PRINCIPAL---------------------------------#

def print_menu_inicio():
    print("0. Salir")
    print("1. Login")
    print("2. Registrarse")


def contador_general (archivologico, archivofisico):
    tamaño = os.path.getsize(archivofisico)
    archivologico.seek (0,0)
    contador = 0
    while archivologico.tell() < tamaño:
            variable = pickle.load(archivologico)
            if variable.email != "":
                  contador = contador + 1
    return contador

def check():
    contador_estudiantes = contador_general (archivo_logico_estudiantes, archivo_fisico_estudiantes)
    contador_moderadores = contador_general (archivo_logico_moderadores, archivo_fisico_moderadores)
    contador_administradores = contador_general (archivo_logico_administradores, archivo_fisico_administradores)
    if (contador_estudiantes >= 4) and (contador_moderadores >= 1) and (contador_administradores >=1):
        return True
    else:
        return False

def validar_usuario_administrador(archivofisico, archivologico, correo, password):
    pos = 0
    tam = os.path.getsize(archivofisico)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivologico.seek (0,0)
        usuario = pickle.load (archivologico)
        while (archivologico.tell() < tam) and (usuario.email != correo):
            pos = archivologico.tell()
            usuario = pickle.load(archivologico)
        if not ((usuario.email == correo) and (usuario.contraseña == password) and (archivologico == archivo_logico_administradores)):
            pos = -1
    return pos

def validar_usuario_estudiante(archivofisico, archivologico, correo, password):
    pos = 0
    tam = os.path.getsize(archivofisico)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivologico.seek (0,0)
        usuario = pickle.load (archivologico)
        while (archivologico.tell() < tam) and (usuario.email != correo):
            pos = archivologico.tell()
            usuario = pickle.load(archivologico)
        if not ((usuario.email == correo) and (usuario.contraseña == password) and (archivologico == archivo_logico_estudiantes) and (usuario.estado == True)):
            pos = -1
    return pos

def validar_usuario_moderador(archivofisico, archivologico, correo, password):
    pos = 0
    tam = os.path.getsize(archivofisico)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivologico.seek (0,0)
        usuario = pickle.load (archivologico)
        while (archivologico.tell() < tam) and (usuario.email != correo):
            pos = archivologico.tell()
            usuario = pickle.load(archivologico)
        if not ((usuario.email == correo) and (usuario.contraseña == password) and (archivologico == archivo_logico_moderadores) and (usuario.estado == True)):
            pos = -1
    return pos

def validar_email_duplicado(archivofisico, archivologico, correo):
    pos = 0
    tam = os.path.getsize(archivofisico)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivologico.seek (0,0)
        usuario = pickle.load (archivologico)
        while (archivologico.tell() < tam) and (usuario.email != correo):
            pos = archivologico.tell()
            usuario = pickle.load(archivologico)
        if not (usuario.email == correo):
                pos = -1
    return pos

def tamaño_registro(archivofisico,archivologico):
    global archivo_logico_estudiantes, archivo_logico_administradores, archivo_logico_moderadores, archivo_logico_reportes, archivo_logico_likes, archivo_logico_contadordereportes
    global archivo_fisico_estudiantes, archivo_fisico_administradores, archivo_fisico_moderadores, archivo_fisico_reportes, archivo_fisico_likes, archivo_fisico_contadordereportes
    tamaño_total = os.path.getsize(archivofisico)
    if tamaño_total == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivologico.seek (0,0)
        reg = pickle.load (archivologico)
    tamaño = archivologico.tell()
    return tamaño

def login():
    global usuario
    if check() == True:
        email = validar_campos_texto("Email", 32)
        password = validar_campos_contrasenia ("Contrasenia", 32)
        busco_estudiante = validar_usuario_estudiante(archivo_fisico_estudiantes, archivo_logico_estudiantes, email, password)
        busco_moderador = validar_usuario_moderador(archivo_fisico_moderadores, archivo_logico_moderadores, email, password)
        busco_administrador = validar_usuario_administrador(archivo_fisico_administradores, archivo_logico_administradores, email, password)
        intentos = 0
        while (intentos < 3) and (busco_estudiante == -1) and (busco_moderador == -1) and (busco_administrador == -1):
            intentos = intentos + 1
            if intentos == 3:
                print ("Ya alcanzo los 3 intentos posibles")
            elif intentos !=3:
                print(f"Le quedan: {3-intentos} intentos")
                print("Usuario y/o contrasenia incorrectas o Usuario inactivo")
                email = validar_campos_texto("Email", 32)
                password = validar_campos_contrasenia ("Contrasenia", 32)
                busco_estudiante = validar_usuario_estudiante(archivo_fisico_estudiantes, archivo_logico_estudiantes, email, password)
                busco_moderador = validar_usuario_moderador(archivo_fisico_moderadores, archivo_logico_moderadores, email, password)
                busco_administrador = validar_usuario_administrador(archivo_fisico_administradores, archivo_logico_administradores, email, password)

        if busco_estudiante != -1:
            usuario=estudiantes()
            tam=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
            pos = busco_estudiante//tam
            archivo_logico_estudiantes.seek(pos*tam,0)
            usuario=pickle.load(archivo_logico_estudiantes)
            menu_estudiantes()
        elif busco_moderador != -1:
            usuario=moderadores()
            tam=tamaño_registro(archivo_fisico_moderadores,archivo_logico_moderadores)
            pos = busco_moderador//tam
            archivo_logico_moderadores.seek(pos*tam,0)
            usuario=pickle.load(archivo_logico_moderadores)
            menu_moderadores()
        elif busco_administrador != -1:
            usuario=administradores()
            tam=tamaño_registro(archivo_fisico_administradores,archivo_logico_administradores)
            pos = busco_administrador//tam
            archivo_logico_administradores.seek(pos*tam,0)
            usuario=pickle.load(archivo_logico_administradores)
            menu_administradores()
        elif intentos == 3:
            salida = True
            email = 0
            password = 0
    else:
        print("No se puede iniciar porque no hay 1 administrador, 1 moderador y 4 estudiantes registrados.")
        sleep(5)
        limpiar_pantalla()

def validar_correo_duplicado():

        email_nuevo = validar_campos_texto("Email", 32)
        busco_email_estudiante = validar_email_duplicado(archivo_fisico_estudiantes, archivo_logico_estudiantes, email_nuevo)
        busco_email_moderador = validar_email_duplicado(archivo_fisico_moderadores, archivo_logico_moderadores, email_nuevo)
        busco_email_administrador = validar_email_duplicado(archivo_fisico_administradores, archivo_logico_administradores, email_nuevo)
        while (busco_email_estudiante != -1) or (busco_email_moderador != -1) or (busco_email_administrador != -1):
            print("El email se encuentra en uso")
            email_nuevo = validar_campos_texto("Email", 32)
            busco_email_estudiante = validar_email_duplicado(archivo_fisico_estudiantes, archivo_logico_estudiantes, email_nuevo)
            busco_email_moderador = validar_email_duplicado(archivo_fisico_moderadores, archivo_logico_moderadores, email_nuevo)
            busco_email_administrador = validar_email_duplicado(archivo_fisico_administradores, archivo_logico_administradores, email_nuevo)
        return email_nuevo

def registro_estudiantes():
        email = validar_correo_duplicado()
        tam_registro=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
        tamaño=os.path.getsize(archivo_fisico_estudiantes)
        cant_reg=tamaño//tam_registro
        nuevo_usuario = estudiantes()
        nuevo_usuario.idregistro = cant_reg
        nuevo_usuario.email = email
        nuevo_usuario.contraseña = validar_campos_contrasenia("Contrasenia", 32)
        nuevo_usuario.nombre = validar_campos_texto("Nombre", 32)
        nuevo_usuario.sexo = validar_mientras ("Ingrese el sexo (M/F): ", "M", "F")
        nuevo_usuario.estado = True
        nuevo_usuario.hobbies = validar_campos_texto("Hobbies", 255)
        nuevo_usuario.materia_fav = validar_campos_texto("Materia Favorita", 16)
        nuevo_usuario.deporte_fav = validar_campos_texto("Deporte Favorito", 16)
        nuevo_usuario.materia_fuerte = validar_campos_texto("Materia Fuerte", 16)
        nuevo_usuario.materia_debil = validar_campos_texto("Materia Debil", 16)
        nuevo_usuario.biografia = validar_campos_texto("Biografia", 255)
        nuevo_usuario.pais = validar_campos_texto("Pais", 32)
        nuevo_usuario.ciudad = validar_campos_texto("Ciudad", 32)
        nuevo_usuario.fecha_nacimiento = modulo_ingrese_fecha()
        formato_estudiante(nuevo_usuario)
        archivo_logico_estudiantes.seek(0,2)
        pickle.dump(nuevo_usuario,archivo_logico_estudiantes)
        archivo_logico_estudiantes.flush()

		
#-------------------------------------MENU ESTUDIANTES-----------------------------------#

def menu_principal_estudiantes():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

def menu_estudiantes():
    global usuario
    opc = 1
    while opc != 0 and usuario.estado==True:
        limpiar_pantalla()
        menu_principal_estudiantes()
        opc=validar(0,4)
        match opc:
            case 1:
                menu_opc_gestion_perfil()
            case 2:
                menu_opc_gestion_candidatos()
            case 3:
                menu_opc_matcheos()
            case 4:
                menu_opc_reportes()
        limpiar_pantalla()
        sleep(2)

#---------------------------MENU GESTION PERFIL--------------------------------#

def menu_print_gestion_perfil():
    print("1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")

def menu_opc_gestion_perfil():
    global usuario
    limpiar_pantalla()
    menu_print_gestion_perfil()
    opc = validaralfabeticamente("abc", "a", "c")
    while opc != "c":
        while usuario.estado==True and opc != "c":
            match opc:
                case "a":
                    menu_editar_datos_personales()
                case "b":
                    menu_eliminar_perfil()
                case "c":
                    print("")
            if usuario.estado==True:
                menu_print_gestion_perfil()
                opc = input("Ingrese una opcion: ")
            else:
                opc="c"

def menu_editar_datos_personales():
    global usuario
    # Asigno los datos del estudiante a la variable auxiliar.
    aux=estudiantes()
    #aux=usuario
    aux.idregistro = usuario.idregistro
    aux.email = usuario.email
    aux.nombre = usuario.nombre
    aux.sexo = usuario.sexo
    aux.contraseña = usuario.contraseña
    aux.estado = usuario.estado
    aux.hobbies = usuario.hobbies
    aux.materia_fav = usuario.materia_fav
    aux.deporte_fav = usuario.deporte_fav
    aux.materia_fuerte = usuario.materia_fuerte
    aux.materia_debil = usuario.materia_debil
    aux.biografia = usuario.biografia
    aux.pais = usuario.pais
    aux.ciudad = usuario.ciudad
    aux.fecha_nacimiento = usuario.fecha_nacimiento
    opc = 1
    while opc != 0:
        print("Sus datos actuales son: ")
        print("Su nombre es: ", aux.nombre)
        print("Su genero es: ", aux.sexo)
        print("Su hobbie es: ", aux.hobbies)
        print("Su materia favorita es: ", aux.materia_fav)
        print("Su deporte favorito es: ", aux.deporte_fav)
        print("Su materia fuerte es: ", aux.materia_fuerte)
        print("Su materia debil es: ", aux.materia_debil)
        print("Su biografia es: ", aux.biografia)
        print("Su pais es: ", aux.pais)
        print("Su ciudad es: ", aux.ciudad)
        print("Su fecha de nacimiento es: ", aux.fecha_nacimiento)
        print("-------------------------------------------------------------")
        print("Que dato desea cambiar?")
        print("1. Nombre")
        print("2. Genero")
        print("3. Hobbie")
        print("4. Materia favorita")
        print("5. Deporte favorito")
        print("6. Materia fuerte")
        print("7. Materia debil")
        print("8. Biografia")
        print("9. Pais")
        print("10. Ciudad")
        print("11. Fecha de nacimiento")
        print("0. Salir")
        opc = validar(0,11)
        match opc:
            case 1:
                aux.nombre=validar_campos_texto("Nombre",32)
            case 2:
                aux.sexo=validar_mientras ("Ingrese el sexo (M/F): ", "M", "F")
            case 3:
                aux.hobbies = validar_campos_texto("Hobbie", 255)
            case 4:
                aux.materia_fav = validar_campos_texto("Materia favorita", 16)
            case 5:
                aux.deporte_fav = validar_campos_texto("Deporte favorito",16)
            case 6:
                aux.materia_fuerte = validar_campos_texto("Materia fuerte",16)
            case 7:
                aux.materia_debil = validar_campos_texto("Materia debil",16)
            case 8:
                aux.biografia = validar_campos_texto ("Biografia",255)
            case 9:
                aux.pais = validar_campos_texto("Pais",32)
            case 10:
                aux.ciudad = validar_campos_texto("Ciudad",32)
            case 11:
                aux.fecha_nacimiento = modulo_ingrese_fecha()
        if opc != 0:
            formato_estudiante(aux)
            tam_reg=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
            archivo_logico_estudiantes.seek((aux.idregistro) * tam_reg,0)
            pickle.dump(aux,archivo_logico_estudiantes)
            archivo_logico_estudiantes.flush()

def menu_eliminar_perfil():
    global usuario
    limpiar_pantalla()
    print("Confirmar eliminacion de perfil")
    print("0. Si")
    print("1. No")
    opc=validar(0,1)
    match opc:
        case 0:
            usuario.estado = False
            anular_usuarioenreporte(usuario.idregistro)
            tam_registro=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
            pos=usuario.idregistro
            archivo_logico_estudiantes.seek(pos*tam_registro,0)
            pickle.dump(usuario,archivo_logico_estudiantes)
            archivo_logico_estudiantes.flush()
        case 1:
            print("")

#---------------------------MENU GESTIONAR CANDIDATOS--------------------------------#

def calcularedad(fecha):
    edad = datetime.strptime(fecha, "%Y-%m-%d").date()
    edad = datetime.now().date() - edad
    edad = math.floor(edad.days / DPY)
    edad = str(edad)
    return edad

def menu_print_gestion_candidatos():
    print("2. Gestionar candidatos")
    print(" a. Ver candidatos")
    print(" b. Reportar candidato")
    print(" c. Volver")

def menu_ver_candidatos():
    global usuario
    estudiante = estudiantes()
    pos = 0
    tam = os.path.getsize(archivo_fisico_estudiantes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_estudiantes.seek (0,0)
        while (archivo_logico_estudiantes.tell() < tam):
            estudiante = pickle.load(archivo_logico_estudiantes)
            if (usuario.email != estudiante.email and estudiante.estado != False):
                edad = calcularedad(estudiante.fecha_nacimiento)
                print("-------------------------------------------------------------")
                print("Estudiante N°: ",estudiante.idregistro)
                print("Su nombre es: ", estudiante.nombre)
                print("Su genero es: ", estudiante.sexo)
                print("Su hobbie es: ", estudiante.hobbies)
                print("Su materia favorita es: ", estudiante.materia_fav)
                print("Su deporte favorito es: ", estudiante.deporte_fav)
                print("Su materia fuerte es: ", estudiante.materia_fuerte)
                print("Su materia debil es: ", estudiante.materia_debil)
                print("Su biografia es: ", estudiante.biografia)
                print("Su pais es: ", estudiante.pais)
                print("Su ciudad es: ", estudiante.ciudad)
                print("Su fecha de nacimiento es: ", estudiante.fecha_nacimiento)
                print("Su edad es: ", edad)
    print("¿Desea dar me gusta a algun estudiante?")
    print("S/N")
    opc=validaralfabeticamente("NS","N","S")
    if opc != "N":
        usuario_id=input("Ingrese ID del estudiante a dar me gusta: ")
        dest=int(usuario_id)
        usuario_id=validar_idregistro_nombre(usuario_id, 1)
        while usuario_id==-1 or dest == usuario.idregistro:
            usuario_id=input("Ingrese ID del estudiante a dar me gusta: ")
            dest=int(usuario_id)
            usuario_id=validar_idregistro_nombre(usuario_id, 1)
        like=likes()
        like.idrem=usuario.idregistro
        like.iddest=dest
        archivo_logico_likes.seek(0,0)
        while archivo_logico_likes.tell()<os.path.getsize(archivo_fisico_likes):
            aux=pickle.load(archivo_logico_likes)
        pickle.dump(like,archivo_logico_likes)
        archivo_logico_likes.flush()

def busca_likes(id_rem,id_dest):
    devolver=0
    archivo_logico_likes.seek(0,0)
    like=likes()
    while archivo_logico_likes.tell()<os.path.getsize(archivo_fisico_likes):# and (like.idrem != id_rem and like.iddest != id_dest):
        like=pickle.load(archivo_logico_likes)
        if (like.idrem == id_rem and like.iddest == id_dest):
            devolver=1
    return devolver

def busca_match(id_rem,id_dest):
    if busca_likes(id_rem,id_dest)==1 and busca_likes(id_dest,id_rem)==1:
        devolver=1
    else:
        devolver=0
    return devolver

def menu_reportar_candidato():
    dest=-1
    print("¿Desea reportar a algun candidato?")
    print("S/N")
    opc=validaralfabeticamente("NS","N","S")
    if opc != "N":
        print("1. Reportar por ID")
        print("2. Reportar por nombre")
        opc_num=validar(1,2)
        if opc_num == 1:
            #Si es por ID es facil, valido y listo
            print("Ingrese ID del candidato a reportar: ")
            reportar_id=validar(0,100)
            dest=int(reportar_id)
            reportar_id=validar_idregistro_nombre(reportar_id, 1)
            while reportar_id==-1 or dest==usuario.idregistro:
                print("Ingrese ID del candidato a reportar: ")
                reportar_id=validar(0,100)
                dest=int(reportar_id)
                reportar_id=validar_idregistro_nombre(reportar_id, 1)
        else:
            #Si es por nombre, tengo que validar y despues buscar la posicion que me devuelve validar para agarrar el id del registro
            reportar_nombre=validar_campos_texto("Ingrese nombre del candidato a reportar: ",32)
            validar_id=validar_idregistro_nombre(reportar_nombre, 2)
            while validar_id==-1 or reportar_nombre==usuario.nombre:
                reportar_nombre=validar_campos_texto("Ingrese nombre del candidato a reportar: ",32)
                validar_id=validar_idregistro_nombre(reportar_nombre, 2)
        razon=validar_campos_texto("Razon",50)
        detalles=validar_campos_texto("Detalles",255)
        #Busco registro con la posición
        if dest==-1:
            archivo_logico_estudiantes.seek(validar_id,0)
            validar_id=pickle.load(archivo_logico_estudiantes)
            dest=validar_id.idregistro
        #Armo reporte y me voy al final del archivo
        reporte=reportes()
        archivo_logico_reportes.seek(0,0)
        while archivo_logico_reportes.tell() < os.path.getsize(archivo_fisico_reportes):
            aux_reporte=pickle.load(archivo_logico_reportes)
        reporte.nroreporte=aux_reporte.nroreporte+1
        reporte.idreportante=usuario.idregistro
        reporte.idreportado=dest
        reporte.razon=razon
        reporte.detalles=detalles
        reporte.reportanteestado = True
        reporte.reportadoestado = True
        formato_reportes(reporte)
        pickle.dump(reporte,archivo_logico_reportes)
        archivo_logico_reportes.flush()

def menu_opc_gestion_candidatos():
    global usuario
    limpiar_pantalla()
    menu_print_gestion_candidatos()
    opc = validaralfabeticamente("abc", "a", "c")
    while opc != "c":
        while opc != "c":
            match opc:
                case "a":
                    menu_ver_candidatos()
                case "b":
                    menu_reportar_candidato()
                case "c":
                    print("")
            menu_print_gestion_candidatos()
            opc = input("Ingrese una opcion: ")

#---------------------------MENU MATCHEOS--------------------------------#
def menu_print_gestion_matcheos():
    print("3. Matcheos")
    print("a. Ver matcheos")
    print("b. Eliminar un matcheo")
    print("c. Volver")

def menu_opc_matcheos():
    global usuario
    limpiar_pantalla()
    menu_print_gestion_matcheos()
    opc = validaralfabeticamente("abc", "a", "c")
    while opc != "c":
        while opc != "c":
            match opc:
                case "a":
                    print("En construccion..")
                case "b":
                    print("En construccion..")
                case "c":
                    print("")
            menu_print_gestion_matcheos()
            opc = input("Ingrese una opcion: ")

#---------------------------MENU REPORTES ESTADISTICOS--------------------------------#
def menu_opc_reportes():
    global usuario
    cant_likes_dados=0
    cant_likes_recibidos=0
    cant_match=0
    print("Reportes estadisticos")
    cant_est=contador_general(archivo_logico_estudiantes,archivo_fisico_estudiantes)
    for i in range(cant_est):
        if i != usuario.idregistro:
            if busca_likes(usuario.idregistro,i)==1 and busca_likes(i,usuario.idregistro)==0:
                cant_likes_dados=cant_likes_dados+1
            if busca_match(usuario.idregistro,i)==1:
                cant_match=cant_match+1
            if busca_likes(i,usuario.idregistro)==1 and busca_likes(usuario.idregistro,i)==0:
                cant_likes_recibidos=cant_likes_recibidos+1
    if cant_match == 0:
        print("Matcheados sobre el % posible: 0%")
    else:
        print("Matcheados sobre el % posible: ",round((cant_match/(cant_est-1))*100),"%")
    print("Likes dados y no recibidos: ",cant_likes_dados)
    print("Likes recibidos y no respondidos: ",cant_likes_recibidos)
    sleep(5)
#-------------------------------------MENU MODERADORES-----------------------------------#

#-------------------------------------PROBAR-----------------------------------#

def menu_principal_moderadores():
    print("1. Gestionar usuarios")
    #print("   a. Desactivar usuarios")
    #print("   b. Volver")
    print("2. Gestionar reportes")
    #print("   a. Ver reportes")
    #print("   b. Volver")
    print("3. Reportes estadisticos")
    print("0. Salir")

def menu_moderadores():
    opc = 1
    while opc != 0:
        limpiar_pantalla()
        menu_principal_moderadores()
        opc= validar(0,5)
        match opc:
            case 1:
                menu_opc_gestion_usuarios()
            case 2:
                menu_opc_gestion_reportes()
            case 3:
                print("En construccion..")
        limpiar_pantalla()

#-----------------------------------MENU GESTION DE USUARIOS---------------------------------#

def menu_print_gestion_usuarios():
    print("1. Gestionar usuarios")
    print("   a. Desactivar usuarios")
    print("   b. Volver")

def menu_opc_gestion_usuarios():
    limpiar_pantalla()
    menu_print_gestion_usuarios()
    opc = validaralfabeticamente("ab", "a", "b")
    while opc != "b":
        match opc:
            case "a":
                menu_gestion_usuarios()
        limpiar_pantalla()
        menu_print_gestion_usuarios()
        opc = validaralfabeticamente("ab", "a", "b")


def menu_gestion_usuarios():
    listado_general_estudiantes ()
    opcion1 = validar_mientras ("Desea desactivar un usuario (S/N)", "S", "N")
    while opcion1 !="N":
        limpiar_pantalla()
        listado_general_estudiantes ()
        usuario_desactivar = input("Ingrese ID o Nombre y Apellido del usuario a desactivar: ")
        if usuario_desactivar.isdigit():
            usuario_desactivar = int(usuario_desactivar)
            usuario_desactivar = validar_idregistro_nombre(usuario_desactivar, 1)
            if usuario_desactivar != -1:
                id_desactivar= desactivar_devolver_id (usuario_desactivar)
                anular_usuarioenreporte (id_desactivar)
            else:
                print("No se encontro")
                sleep(1)
        elif len(usuario_desactivar) < 32:
            usuario_desactivar = usuario_desactivar.ljust(32," ")
            usuario_desactivar = validar_idregistro_nombre (usuario_desactivar, 2)
            if usuario_desactivar != -1:
                id_desactivar= desactivar_devolver_id (usuario_desactivar)
                anular_usuarioenreporte (id_desactivar)
            else:
                print("No se encontro")
                sleep(1)
        listado_general_estudiantes ()
        opcion1 = validar_mientras ("Desea desactivar un usuario (S/N)", "S", "N")

def desactivar_devolver_id (parametro):
    archivo_logico_estudiantes.seek(parametro,0)
    variable = estudiantes ()
    variable = pickle.load(archivo_logico_estudiantes)
    variable.estado = False
    id_desactivar = variable.idregistro
    archivo_logico_estudiantes.seek(parametro,0)
    pickle.dump(variable, archivo_logico_estudiantes)
    archivo_logico_estudiantes.flush()
    return id_desactivar



def listado_general_estudiantes ():

    tam = os.path.getsize(archivo_fisico_estudiantes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_estudiantes.seek (0,0)
        while (archivo_logico_estudiantes.tell() < tam):
            variable = pickle.load(archivo_logico_estudiantes)
            if variable.estado == True:
                print (f" El estudiante {variable.idregistro} es {variable.nombre}")


'''def validar_idregistro_nombre (parametro, condicion):
    pos = 0
    tam = os.path.getsize(archivo_fisico_estudiantes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_estudiantes.seek (0,0)
        variable = pickle.load (archivo_logico_estudiantes)
        if condicion == 1:
            #Agregue esto porque parametro lo leia como string y el tipo de dato en el registro es INT entonces no comparaba bien.
            parametro=int(parametro)
            while (archivo_logico_estudiantes.tell() < tam) and (variable.idregistro != parametro):
                pos = archivo_logico_estudiantes.tell()
                variable = pickle.load(archivo_logico_estudiantes)
            if variable.idregistro == parametro:
                return pos
            else:
                return -1
        elif condicion == 2:
            while (archivo_logico_estudiantes.tell() < tam) and (variable.nombre != parametro):
                pos = archivo_logico_estudiantes.tell()
                variable = pickle.load(archivo_logico_estudiantes)
            if variable.nombre == parametro:
                return pos
            else:
                return -1'''

def validar_idregistro_nombre (parametro, condicion):
    pos = 0
    tam = os.path.getsize(archivo_fisico_estudiantes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_estudiantes.seek (0,0)
        variable = pickle.load (archivo_logico_estudiantes)
        if condicion == 1:
            #Agregue esto porque parametro lo leia como string y el tipo de dato en el registro es INT entonces no comparaba bien.
            parametro=int(parametro)
            while (archivo_logico_estudiantes.tell() < tam) and (variable.idregistro != parametro):
                pos = archivo_logico_estudiantes.tell()
                variable = pickle.load(archivo_logico_estudiantes)
            if not(variable.idregistro == parametro):
                pos = -1
                #return pos
            #else:
                #pos=-1
                #return -1
        elif condicion == 2:
            while (archivo_logico_estudiantes.tell() < tam) and (variable.nombre != parametro):
                pos = archivo_logico_estudiantes.tell()
                variable = pickle.load(archivo_logico_estudiantes)
            if not(variable.nombre == parametro):
                pos = -1
                #return pos
            #else:
                #pos=-1
                #return -1
    return pos


def anular_usuarioenreporte (parametro):

    pos = 0
    tam = os.path.getsize(archivo_fisico_reportes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_reportes.seek (0,0)
        while archivo_logico_reportes.tell() < tam:
            pos = archivo_logico_reportes.tell()
            reporte = reportes ()
            reporte = pickle.load(archivo_logico_reportes)
            if reporte.idreportante == parametro:
                    reporte.reportanteestado = False
                    archivo_logico_reportes.seek(pos,0)
                    pickle.dump(reporte, archivo_logico_reportes)
                    archivo_logico_reportes.flush()
            elif reporte.idreportado == parametro:
                    reporte.reportadoestado = False
                    archivo_logico_reportes.seek(pos,0)
                    pickle.dump(reporte, archivo_logico_reportes)
                    archivo_logico_reportes.flush()

#----------------------------------MENU GESTIONAR REPORTES-----------------------------#

def menu_print_opc_gestion_reportes():
    print ("2. Gestionar reportes")
    print ("    a. Ver reportes")
    print ("    b. Volver")

def menu_adm_gestion_usuarios():
    limpiar_pantalla()
    menu_print_eliminar_usuario_moderador()
    opc = validaralfabeticamente("abcd", "a", "d")
    while opc != "d":
        match opc:
            case "a":
                menu_eliminar_estudiante_moderador()
            case "b":
                menu_alta_moderador()
            case "c":
                menu_gestion_usuarios()
            case "d":
                print("")
        if opc != "d":
            limpiar_pantalla()
            menu_print_eliminar_usuario_moderador()
            opc = validaralfabeticamente("abcd", "a", "d")


def menu_opc_gestion_reportes():
    global usuario
    limpiar_pantalla()
    menu_print_opc_gestion_reportes()
    opc = validaralfabeticamente("ab","a","b")
    while opc != "b":
        match opc:
            case "a":
                listado_general_reportes ()
                opcion = validar_mientras ("Desea actualizar algun reporte (S/N): ", "S", "N")
                while opcion != "N":
                    limpiar_pantalla()
                    listado_general_reportes ()
                    reporte_numero = input ("Ingrese el nro de reporte:")
                    if reporte_numero.isdigit():
                        reporte_numero = int(reporte_numero)
                        reporte_numero = buscar_nro_reporte (reporte_numero)
                        if reporte_numero != -1:
                            print("Que desea hacer:")
                            print("1. Tomar el reporte y desactivar usuario")
                            print("2. Ignorar el reporte")
                            opc = validar(1,2)
                            if opc == 1:
                                id_mod = usuario.idregistro
                                archivo_logico_reportes.seek(reporte_numero,0)
                                auxreportar = reportes ()
                                auxreportar = pickle.load(archivo_logico_reportes)
                                auxiliar_idreportado = int(auxreportar.idreportado)

                                #DESDE ACA DESACTIVA AL USUARIO#
                                desactivar_usuario(auxiliar_idreportado)

                                #DESDE ACA MODIFICA EL REPORTE#
                                auxreportar.reportadoestado = False
                                auxreportar.estadoreporte = 1
                                auxreportar.idmoderador = id_mod
                                archivo_logico_reportes.seek(reporte_numero,0)
                                pickle.dump(auxreportar, archivo_logico_reportes)
                                archivo_logico_reportes.flush()

                            if opc == 2:

                                id_mod = usuario.idregistro

                                #DESDE ACA MODIFICA EL REPORTE#
                                archivo_logico_reportes.seek(reporte_numero,0)
                                auxreportar = reportes ()
                                auxreportar = pickle.load(archivo_logico_reportes)
                                auxreportar.estadoreporte = 2
                                auxreportar.idmoderador = id_mod
                                archivo_logico_reportes.seek(reporte_numero,0)
                                pickle.dump(auxreportar, archivo_logico_reportes)
                                archivo_logico_reportes.flush()
                    limpiar_pantalla()
                    listado_general_reportes ()
                    opcion = validar_mientras ("Desea actualizar algun reporte (S/N): ","S", "N")
            case "b":
                print("")
        limpiar_pantalla()
        menu_print_opc_gestion_reportes()
        opc = validaralfabeticamente("ab","a","b")

'''def buscar_nro_reporte (parametro):

    pos = 0
    tam = os.path.getsize(archivo_fisico_reportes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_reportes.seek (0,0)
        reporte = pickle.load (archivo_logico_reportes)
        while (archivo_logico_reportes.tell() < tam) and (reporte.nroreporte != parametro):
            pos = archivo_logico_reportes.tell()
            reporte = pickle.load(archivo_logico_reportes)
        if reporte.nroreporte == parametro  and reporte.idmoderador == 0:
            return pos
        else:
            return -1'''

def buscar_nro_reporte (parametro):

    pos = 0
    tam = os.path.getsize(archivo_fisico_reportes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_reportes.seek (0,0)
        reporte = pickle.load (archivo_logico_reportes)
        while (archivo_logico_reportes.tell() < tam) and (reporte.nroreporte != parametro):
            pos = archivo_logico_reportes.tell()
            reporte = pickle.load(archivo_logico_reportes)
        if not(reporte.nroreporte == parametro  and reporte.idmoderador == 0):
            pos = -1
            #return pos
        #else:
            #pos=-1
            #return -1
    return pos



def listado_general_reportes ():

    tam = os.path.getsize(archivo_fisico_reportes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_reportes.seek (0,0)
        while (archivo_logico_reportes.tell() < tam):
            reporte = pickle.load(archivo_logico_reportes)
            if reporte.reportanteestado == True and reporte.reportadoestado == True and reporte.estadoreporte == 0:
                mostrar_reporte (reporte)



def mostrar_reporte (reporte):
            print (f'''
                ---------------------------------------------------------------------------------------------------------------------------------------

                REPORTE Nro: {reporte.nroreporte}            ID REPORTANTE: {reporte.idreportante}                 RAZON: {reporte.razon}  ID REPORTADO: {reporte.idreportado}

                DETALLES: {reporte.detalles}

                ESTADO: {reporte.estadoreporte}  MODERADOR: {reporte.idmoderador}

                ---------------------------------------------------------------------------------------------------------------------------------------
                    ''')



def desactivar_usuario (parametro):
    auxiliar_idreportado = parametro
    auxiliar_idreportado = validar_idregistro_nombre (auxiliar_idreportado, 1)
    archivo_logico_estudiantes.seek(auxiliar_idreportado,0)
    a_usuario = estudiantes ()
    a_usuario = pickle.load(archivo_logico_estudiantes)
    a_usuario.estado = False
    archivo_logico_estudiantes.seek(auxiliar_idreportado,0)
    pickle.dump(a_usuario, archivo_logico_estudiantes)
    archivo_logico_estudiantes.flush()

#-----------------------------------BONUS TRACK 1---------------------------------#
def bonus_track_1():
    puntajes = {}
    rachas = {}

    # Inicializar puntajes y rachas
    archivo_logico_estudiantes.seek(0, 0)
    while archivo_logico_estudiantes.tell() < os.path.getsize(archivo_fisico_estudiantes):
        estudiante = pickle.load(archivo_logico_estudiantes)
        puntajes[estudiante.idregistro] = 0
        rachas[estudiante.idregistro] = 0

    # Calcular puntajes
    archivo_logico_likes.seek(0, 0)
    while archivo_logico_likes.tell() < os.path.getsize(archivo_fisico_likes):
        like = pickle.load(archivo_logico_likes)
        remitente = like.idrem
        destinatario = like.iddest

        if busca_match(remitente, destinatario):
            puntajes[remitente] += 1
            rachas[remitente] += 1
            if rachas[remitente] >= 3:
                puntajes[remitente] += 1
        else:
            puntajes[remitente] -= 1
            rachas[remitente] = 0

    # Ordenar y mostrar resultados
    puntajes_ordenados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    print("Listado de candidatos según su puntaje:")
    for id_estudiante, puntaje in puntajes_ordenados:
        estudiante = obtener_estudiante_por_id(id_estudiante)
        if estudiante:
            print(f"ID: {id_estudiante}, Nombre: {estudiante.nombre}, Puntaje: {puntaje}")

def obtener_estudiante_por_id(id_estudiante):
    estudiante=estudiantes()
    archivo_logico_estudiantes.seek(0, 0)
    while (archivo_logico_estudiantes.tell() < os.path.getsize(archivo_fisico_estudiantes)) and (estudiante.idregistro != id_estudiante):
        estudiante = pickle.load(archivo_logico_estudiantes)
    if estudiante.idregistro != id_estudiante:
        estudiante=None
    return estudiante



#-----------------------------------BONUS TRACK 2---------------------------------#
def bonus_track_2():
    pass

#-------------------------------------MENU ADMINISTRADORES------------------------------#


def menu_administradores():
    global usuario

    menu_administradores_principal()
    opc=validar(0,3)
    while opc != 0:
        limpiar_pantalla()
        match opc:
            case 1:
                menu_adm_gestion_usuarios()
            case 2:
                menu_opc_gestion_reportes()
            case 3:
                menu_opc_reportes_estadisticos()
            case 4:
                bonus_track_1()
            case 0:
                print ("")
        if opc != 0:
            limpiar_pantalla()
            menu_administradores_principal()
            opc=validar(0,3)



def menu_administradores_principal():
    print ("1. Gestionar usuarios")
    #print ("    a. Eliminar un usuario")
    #print ("    b. Dar de alta un moderador")
    #print ("    c. Desactivar usuario")
    #print ("    d. Volver")
    print ("2. Gestionar Reportes")
    #print ("    a. Ver Reportes")
    #print ("    b. Volver")
    print ("3. Reportes Estadisticos")
    print ("4. Bonus Track 1 - Puntuando Candidatos")
    print ("0. Salir")


#---------------------------------MENU ADMIN GESTION DE USUARIOS------------------------------------#


def menu_print_eliminar_usuario_moderador():
    print ("1. Gestionar usuarios")
    print ("    a. Eliminar un usuario")
    print ("    b. Dar de alta un moderador")
    print ("    c. Desactivar usuario")
    print ("    d. Volver")

def menu_adm_gestion_usuarios():
    limpiar_pantalla()
    menu_print_eliminar_usuario_moderador()
    opc = validaralfabeticamente("abcd", "a", "d")
    while opc != "d":
        match opc:
            case "a":
                menu_eliminar_estudiante_moderador()
            case "b":
                menu_alta_moderador()
            case "c":
                menu_gestion_usuarios()
            case "d":
                print("")
        if opc != "d":
            limpiar_pantalla()
            menu_print_eliminar_usuario_moderador()
            opc = validaralfabeticamente("abcd", "a", "d")

#---------------------------------------MENU ELIMINAR ESTUDIANTES/MODERADOR-------------------------------------------#

def menu_eliminar_estudiante_moderador():

    opcion1 = validar_mientras ("Desea eliminar a un usuario (S/N)", "S", "N")
    contador_estudiante = contador_inactivos (archivo_logico_estudiantes, archivo_fisico_estudiantes)
    contador_moderadores = contador_inactivos (archivo_logico_moderadores, archivo_fisico_moderadores)
    while opcion1 !="N":
        opcion2 = validar_mientras ("Desea eliminar un Estudiante (E) o un Moderador (M): ", "E", "M")
        if opcion2 == "E" and contador_estudiante != -1:
            limpiar_pantalla()
            listado_general_estudiantes ()
            usuario_desactivar = input("Ingrese ID o Nombre y Apellido del usuario a desactivar: ")
            if usuario_desactivar.isdigit():
                usuario_desactivar = int(usuario_desactivar)
                usuario_desactivar = validar_idregistro_nombre(usuario_desactivar, 1)
                if usuario_desactivar != -1:
                    id_eliminar = borrado_logico_estudiante(usuario_desactivar)
                    anular_usuarioenreporte (id_eliminar)
                else:
                    print ("Campo Incorrecto o no encontrado")
                    sleep(5)
            elif len(usuario_desactivar) < 32:
                usuario_desactivar = usuario_desactivar.ljust(32," ")
                usuario_desactivar = validar_idregistro_nombre (usuario_desactivar, 2)
                if usuario_desactivar != -1:
                    id_eliminar = borrado_logico_estudiante(usuario_desactivar)
                    anular_usuarioenreporte (id_eliminar)
                else:
                    print ("Campo Incorrecto o no encontrado")
                    sleep(5)
        if opcion2 == "M" and contador_moderadores !=-1:
            listado_general_moderadores ()
            usuario_desactivar = input("Ingrese ID del moderador a eliminar: ")
            if usuario_desactivar.isdigit():
                usuario_desactivar = int(usuario_desactivar)
                usuario_desactivar = validar_idregistro_moderador (usuario_desactivar)
                if usuario_desactivar != -1:
                    desactivar_moderador (usuario_desactivar)
        limpiar_pantalla()
        opcion1 = validar_mientras ("Desea eliminar a un usuario (S/N)", "S", "N")
        contador_estudiante = contador_inactivos (archivo_logico_estudiantes, archivo_fisico_estudiantes)
        contador_moderadores = contador_inactivos (archivo_logico_moderadores, archivo_fisico_moderadores)
        if contador_estudiante == -1 and contador_moderadores == -1:
            opcion1 = "N"



def desactivar_moderador (parametro):
    auxiliar_id = parametro
    auxiliar_id = validar_idregistro_nombre (auxiliar_id, 1)
    archivo_logico_moderadores.seek(auxiliar_id,0)
    a_usuario = moderadores ()
    a_usuario = pickle.load(archivo_logico_moderadores)
    a_usuario.email = ""
    a_usuario.contraseña = ""
    a_usuario.email = a_usuario.email.ljust(32, " ")
    a_usuario.contraseña = a_usuario.contraseña.ljust(32, " ")
    a_usuario.estado = False
    archivo_logico_moderadores.seek(auxiliar_id,0)
    pickle.dump(a_usuario, archivo_logico_moderadores)
    archivo_logico_moderadores.flush()

'''def contador_inactivos (archivologico, archivofisico):
    tamaño = os.path.getsize(archivofisico)
    archivologico.seek (0,0)
    contador = 0
    while archivologico.tell() < tamaño:
        variable = pickle.load(archivologico)
        if variable.estado == True:
            return 1
    return -1
'''
def contador_inactivos (archivologico, archivofisico):
    tamaño = os.path.getsize(archivofisico)
    archivologico.seek (0,0)
    contador = 0
    while archivologico.tell() < tamaño:
        variable = pickle.load(archivologico)
        if variable.estado == True:
            devolver=1
            #return 1
        else:
            devolver=-1
    #return -1
    return devolver



'''def validar_idregistro_moderador (parametro):
    pos = 0
    tam = os.path.getsize(archivo_fisico_moderadores)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_moderadores.seek (0,0)
        variable = pickle.load (archivo_logico_moderadores)
        while (archivo_logico_moderadores.tell() < tam) and (variable.idregistro != parametro):
            pos = archivo_logico_moderadores.tell()
            variable = pickle.load(archivo_logico_moderadores)
        if variable.idregistro == parametro:
            return pos
        else:
            return -1
'''
def validar_idregistro_moderador (parametro):
    pos = 0
    tam = os.path.getsize(archivo_fisico_moderadores)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_moderadores.seek (0,0)
        variable = pickle.load (archivo_logico_moderadores)
        while (archivo_logico_moderadores.tell() < tam) and (variable.idregistro != parametro):
            pos = archivo_logico_moderadores.tell()
            variable = pickle.load(archivo_logico_moderadores)
        if not(variable.idregistro == parametro):
            pos = -1
            #return pos
        #else:
            #pos=-1
            #return -1
    return pos



def listado_general_moderadores ():
    tam = os.path.getsize(archivo_fisico_moderadores)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
    else:
        archivo_logico_moderadores.seek (0,0)
        while (archivo_logico_moderadores.tell() < tam):
            variable = pickle.load(archivo_logico_moderadores)
            if variable.estado == True:
                print (f" Moderador {variable.idregistro} ID registro")



def borrado_logico_estudiante(parametro):
    archivo_logico_estudiantes.seek(parametro,0)
    variable = estudiantes ()
    variable = pickle.load(archivo_logico_estudiantes)
    id_desactivar = variable.idregistro
    borrar_estudiante (variable)
    formato_estudiante(variable)
    archivo_logico_estudiantes.seek(parametro,0)
    pickle.dump(variable, archivo_logico_estudiantes)
    archivo_logico_estudiantes.flush()
    return id_desactivar

def borrar_estudiante (self):

        self.email = " "
        self.nombre = " "
        self.sexo = " "
        self.contraseña = " "
        self.estado = False
        self.hobbies = " "
        self.materia_fav = " "
        self.deporte_fav = " "
        self.materia_fuerte = " "
        self.materia_debil = " "
        self.biografia = " "
        self.pais = " "
        self.ciudad = " "
        self.fecha_nacimiento = " "

#----------------------------------MENU DAR ALTA MODERADOR-----------------------------------#

def menu_alta_moderador():

    opcion1 = validar_mientras ("Desea dar de alta un Moderador (S/N)", "S", "N")
    while opcion1 !="N":
        tam = os.path.getsize(archivo_fisico_moderadores)
        archivo_logico_moderadores.seek (0,0)
        variable = pickle.load (archivo_logico_moderadores)
        tamreg = archivo_logico_moderadores.tell()
        pos = tam - tamreg
        archivo_logico_moderadores.seek(pos,0)
        variable = moderadores()
        variable = pickle.load (archivo_logico_moderadores)
        id_siguiente = variable.idregistro + 1
        variable = moderadores ()
        variable.idregistro = id_siguiente
        variable.email = validar_correo_duplicado ()
        variable.contraseña = validar_campos_contrasenia("Contrasenia", 32)
        variable.estado = True
        archivo_logico_moderadores.seek(0,2)
        pickle.dump(variable, archivo_logico_moderadores)
        archivo_logico_moderadores.flush()
        print ("El proceso se completo")
        listado_general_moderadores()
        opcion1 = validar_mientras ("Desea dar de alta un Moderador (S/N)", "S", "N")

#-------------------------------MENU REPORTES ESTADISTICOS-----------------------------------#
def menu_opc_reportes_estadisticos():
    global contador_grabar, puntero

    reportes_total = totaldereportes ()
    reportes_ignorados = contador_reportes (2)
    reportes_ignorados = (reportes_ignorados * 100)/reportes_total
    reportes_aceptados = contador_reportes (1)
    reportes_aceptados = (reportes_aceptados * 100)/reportes_total
    # QUIERO QUE ESTE PROCESO SE EJECUTE SOLAMENTE UNA VEZ EN LA POSICION 0 #
    if contador_grabar == 0:
        grabar_cantidad_reportes(0)
        contador_grabar = contador_grabar + 1
        puntero = totaldereportes ()
    #PROXIMA VEZ QUE SE EJECUTE EL MENU DEBE HACERLO DESDE LA ULTIMA POSICION PUNTERO GRABADA#
    elif contador_grabar != 0:
        grabar_cantidad_reportes(puntero)
        puntero = totaldereportes ()
    #DE ESTA FORMA SE EVITA DUPLICAR LOS DATOS EN LOS CONTADORES TOTALES DE REPORTES POR MODERADOR#
    id_mod_aceptado = listado_general_metricas (1)
    id_mod_ignorados = listado_general_metricas (2)
    id_mod_ambos = listado_general_metricas (3)
    print ("La cantidad de reportes es:", reportes_total)
    print ("La cantidad de reportes ignorados es:", reportes_ignorados)
    print ("La cantidad de reportes aceptados es:", reportes_aceptados)
    print ("El moderador con mayor cantidad de reportes aceptados es:", id_mod_aceptado)
    print ("El moderador con mayor cantidad de reportes ignorados es:", id_mod_ignorados)
    print ("El moderador con mayor cantidad de reportes aceptados e ignorados es:", id_mod_ambos)
    sleep(10)



def listado_general_metricas (condicion):
    id_mod = 0
    contador = 0
    tam = os.path.getsize(archivo_fisico_contadordereportes)
    if tam == 0:
        print("ningun moderador ha gestionado un reporte")
    else:
        archivo_logico_contadordereportes.seek (0,0)
        variable = contadordereportes ()
        variable = pickle.load(archivo_logico_contadordereportes)
        while (archivo_logico_contadordereportes.tell() < tam):
            if condicion == 1 and contador < variable.reportseaceptados:
               contador = variable.reportesaceptados
               id_mod = variable.idmoderador
            if condicion == 2 and contador < variable.reportesignorados:
               contador = variable.reportesignorados
               id_mod = variable.idmoderador
            if condicion == 3 and contador < variable.totalreportes:
               contador = variable.totalreportes
               id_mod = variable.idmoderador
            variable = pickle.load(archivo_logico_contadordereportes)
        return id_mod




def totaldereportes ():
    tam = os.path.getsize(archivo_fisico_reportes)
    archivo_logico_reportes.seek (0,0)
    variable = pickle.load (archivo_logico_reportes)
    tamreg = archivo_logico_reportes.tell()
    cantreg = tam // tamreg
    return cantreg

def contador_reportes (condicion):
    tam = os.path.getsize(archivo_fisico_reportes)
    archivo_logico_reportes.seek (0,0)
    contador = 0
    while archivo_logico_reportes.tell() < tam:
        variable = pickle.load(archivo_logico_reportes)
        if variable.estadoreporte == condicion:
            contador = contador + 1
    return contador

def grabar_cantidad_reportes(pos):
    tam = os.path.getsize(archivo_fisico_reportes)
    #Agrego tamaño de registro
    archivo_logico_reportes.seek(0,0)
    aux_reg=pickle.load(archivo_logico_reportes)
    tam_reg=archivo_logico_reportes.tell()
    ####
    archivo_logico_reportes.seek (pos*tam_reg,0)
    pos = archivo_logico_reportes.tell()
    #reporte = pickle.load(archivo_logico_reportes)
    while archivo_logico_reportes.tell() < tam:
        reporte = pickle.load(archivo_logico_reportes)
        pos = archivo_logico_reportes.tell()
        if reporte.idmoderador != 0:
            id_mod = reporte.idmoderador
            id_parametro = reporte.idmoderador
            id_mod = corroborar_id (id_mod)
            reporte_estado = reporte.estadoreporte
            if id_mod != -1 and id_mod != -2:
                archivo_logico_contadordereportes.seek (id_mod,0)
                grabar_segun_condiciones (id_parametro, reporte_estado, id_mod)
            elif id_mod == -2:
                archivo_logico_contadordereportes.seek (0,0)
                grabar_segun_condiciones (id_parametro, reporte_estado, id_mod)
            elif id_mod == -1:
                archivo_logico_contadordereportes.seek (0,2)
                grabar_segun_condiciones (id_parametro, reporte_estado, id_mod)
        #reporte = pickle.load(archivo_logico_reportes)


#-------------------------------------Modifique reporte como adm y se rompió-----------------------------------#
def grabar_segun_condiciones (idregistro, estadoreporte, posicion):
        variable = contadordereportes ()
        if posicion == -1 or posicion == -2:
            variable.idmoderador = idregistro
        if posicion != -1 and posicion != -2:
            variable = pickle.load(archivo_logico_contadordereportes)
        if estadoreporte == 1:
            variable.reportesaceptados = variable.reportesaceptados + 1
        if estadoreporte == 2:
            variable.reportesignorados = variable.reportesignorados + 1
        variable.totalreportes = variable.totalreportes + 1
        if posicion != -1 and posicion != -2:
            archivo_logico_contadordereportes.seek (posicion,0)
        pickle.dump(variable, archivo_logico_contadordereportes)
        archivo_logico_contadordereportes.flush()

'''def corroborar_id (parametro):
    pos = 0
    tam = os.path.getsize(archivo_fisico_contadordereportes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
        return -2
    else:
        pos = 0
        archivo_logico_contadordereportes.seek (0,0)
        contador = pickle.load (archivo_logico_contadordereportes)
        while (archivo_logico_contadordereportes.tell() < tam) and (contador.idmoderador != parametro):
            pos = archivo_logico_contadordereportes.tell()
            contador = pickle.load(archivo_logico_contadordereportes)
        if contador.idmoderador == parametro:
            return pos
        else:
            return -1'''

def corroborar_id (parametro):
    pos = 0
    tam = os.path.getsize(archivo_fisico_contadordereportes)
    if tam == 0:
        print("no se puede hacer la consulta, cargar datos primero")
        pos=-2
        #return -2
    else:
        pos = 0
        archivo_logico_contadordereportes.seek (0,0)
        contador = pickle.load (archivo_logico_contadordereportes)
        while (archivo_logico_contadordereportes.tell() < tam) and (contador.idmoderador != parametro):
            pos = archivo_logico_contadordereportes.tell()
            contador = pickle.load(archivo_logico_contadordereportes)
        if not (contador.idmoderador == parametro):
            pos = -1
            #return pos
        #else:
            #pos=-1
            #return -1
    return pos


#---------------------------------PROGRAMA---------------------------------#

usuario = [None]
global salida, contador_grabar, puntero
salida = False
contador_grabar = 0
puntero = 0

main()

print_menu_inicio()
opc = validar(0,2)
salida = False

while opc != 0 and salida == False:
    if opc == 1:
        login()
    elif opc == 2:
        registro_estudiantes()
    elif opc == 0 or salida == True:
        print ("Hasta Luego")
    if opc != 0 and salida == False:
        print_menu_inicio()
        opc = validar(0,2)



