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
    for i in range(0,4):
        like=likes()
        like.idrem=random.randint(1,4)
        like.iddest=random.randint(1,4)
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
    global archivo_logico_estudiantes, archivo_logico_administradores, archivo_logico_moderadores, archivo_logico_reportes, archivo_logico_likes
    global archivo_fisico_estudiantes, archivo_fisico_administradores, archivo_fisico_moderadores, archivo_fisico_reportes, archivo_fisico_likes

    #archivo_fisico_xxxxxxxx="ruta de este .py" + \\xxxxxxxx.dat 
    archivo_fisico_estudiantes = os.getcwd()+"\\estudiantes.dat"
    archivo_fisico_administradores = os.getcwd()+"\\administradores.dat"
    archivo_fisico_moderadores = os.getcwd()+"\\moderadores.dat"
    archivo_fisico_reportes = os.getcwd()+"\\reportes.dat"
    archivo_fisico_likes = os.getcwd()+"\\likes.dat"

    archivo_logico_estudiantes = verificar_archivo(archivo_fisico_estudiantes)
    archivo_logico_administradores = verificar_archivo(archivo_fisico_administradores)
    archivo_logico_moderadores = verificar_archivo(archivo_fisico_moderadores)
    archivo_logico_reportes = verificar_archivo(archivo_fisico_reportes)
    archivo_logico_likes = verificar_archivo(archivo_fisico_likes)

    cargar_archivo_admin_mod("moderador", moderadores)
    cargar_archivo_admin_mod("administrador", administradores)
    cargar_archivo_estudiantes()
    cargar_archivo_reportes()
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
                    return date

    return -1

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
        if minimo <= opcion <= maximo:
            return opcion
    return -1

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

    if i < len(string) and string[i] == opcion:
        return opcion
    else:
        return -1

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


def validar_usuario(archivofisico, archivologico, correo, password):
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
        if (usuario.email == correo) and (usuario.contraseña == password):
            if archivologico == archivo_logico_administradores:
                return pos
            elif ((archivologico == archivo_logico_estudiantes) or (archivologico == archivo_logico_moderadores)) and (usuario.estado == True):
                return pos
            else:
                return -1
        else:
            return -1

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
        if (usuario.email == correo):
                return pos
        else:
            return -1

def tamaño_registro(archivofisico,archivologico):

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
        busco_estudiante = validar_usuario(archivo_fisico_estudiantes, archivo_logico_estudiantes, email, password)
        busco_moderador = validar_usuario(archivo_fisico_moderadores, archivo_logico_moderadores, email, password)
        busco_administrador = validar_usuario(archivo_fisico_moderadores, archivo_logico_moderadores, email, password)
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
                busco_estudiante = validar_usuario(archivo_fisico_estudiantes, archivo_logico_estudiantes, email, password)
                busco_moderador = validar_usuario(archivo_fisico_moderadores, archivo_logico_moderadores, email, password)
                busco_administrador = validar_usuario(archivo_fisico_moderadores, archivo_logico_moderadores, email, password)

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
        while (busco_email_estudiante != -1) and (busco_email_moderador != -1) and (busco_email_administrador != -1):
            print("El email se encuentra en uso")
            email_nuevo = validar_campos_texto("Email", 32)
            busco_email_estudiante = validar_email_duplicado(archivo_fisico_estudiantes, archivo_logico_estudiantes, email_nuevo)
            busco_email_moderador = validar_email_duplicado(archivo_fisico_moderadores, archivo_logico_moderadores, email_nuevo)
            busco_email_administrador = validar_email_duplicado(archivo_fisico_administradores, archivo_logico_administradores, email_nuevo)
        return email_nuevo

def registro_estudiantes():
    email = validar_campos_texto("Email", 32)
    busco_estudiante = validar_email_duplicado(archivo_fisico_estudiantes, archivo_logico_estudiantes, email)
    busco_moderador = validar_email_duplicado(archivo_fisico_moderadores, archivo_logico_moderadores, email)
    busco_administrador = validar_email_duplicado(archivo_fisico_administradores, archivo_logico_administradores, email)	
    if (busco_estudiante == -1 and busco_moderador == -1 and busco_administrador == -1):
        tam_registro=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
        tamaño=os.path.getsize(archivo_fisico_estudiantes)
        cant_reg=tamaño//tam_registro
        nuevo_usuario = estudiantes()
        nuevo_usuario.idregistro = cant_reg-1
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
        archivo_logico_estudiantes.seek(0,0)
        tam_est=os.path.getsize(archivo_fisico_estudiantes)
        while archivo_logico_estudiantes.tell()<tam_est:
            aux=pickle.load(archivo_logico_estudiantes)
        pickle.dump(nuevo_usuario,archivo_logico_estudiantes)
        archivo_logico_estudiantes.flush()
    else:
        print("El mail ya esta en uso")
		
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
                fecha = modulo_ingrese_fecha()
        if opc != 0:
            formato_estudiante(aux)
            tam_reg=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
            #No se porque se agrega uno al idregistro pero sino pisa el anterior jajaja
            #Debe ser porque no hago el picke.load
            archivo_logico_estudiantes.seek((aux.idregistro+1) * tam_reg,0)
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
            tam_registro=tamaño_registro(archivo_fisico_estudiantes,archivo_logico_estudiantes)
            pos=usuario.idregistro
            archivo_logico_estudiantes=open(archivo_fisico_estudiantes,"r+b")
            archivo_logico_estudiantes.seek(pos*tam_registro,0)
            pickle.dump(usuario,archivo_logico_estudiantes)
            archivo_logico_estudiantes.flush()
        case 1:
            print("")

#---------------------------MENU GESTIONAR CANDIDATOS--------------------------------#




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
        estudiante = pickle.load(archivo_logico_estudiantes)
        while (archivo_logico_estudiantes.tell() < tam):
            if (usuario.email != estudiante.email):
                edad = estudiante.fecha_nacimiento
                edad = datetime.strptime(edad, "%Y-%m-%d").date()
                edad = calcularedad(edad)
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
                print("-------------------------------------------------------------")
            estudiante = pickle.load(archivo_logico_estudiantes)
    print("¿Desea dar me gusta a algun estudiante?")
    print("S/N")
    opc=validaralfabeticamente("NS","N","S")
    if opc != "N":
        usuario_id=input("Ingrese ID del estudiante a dar me gusta: ")
        dest=int(usuario_id)
        usuario_id=validar_idregistro_nombre(usuario_id, 1)
        while usuario_id==-1:
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


def calcularedad(fecha):
    edad = datetime.now().date() - fecha
    edad = math.floor(edad.days / DPY)
    edad = str(edad)
    return edad
        
def busca_likes(id_rem,id_dest):
    archivo_logico_likes.seek(0,0)
    like=likes()
    like=pickle.load(archivo_logico_likes)
    while archivo_logico_likes.tell()<os.path.getsize(archivo_fisico_likes) and (like.idrem != id_rem and like.iddest != id_dest):
        like=pickle.load(archivo_logico_likes)
    if (like.idrem == id_rem and like.iddest == id_dest):
        print("Le dio like!")
    else:
        print("No le dio like")

def busca_match(id_rem,id_dest):
    archivo_logico_likes.seek(0,0)
    like=likes()
    like=pickle.load(archivo_logico_likes)
    while archivo_logico_likes.tell()<os.path.getsize(archivo_fisico_likes) and ((like.idrem != id_rem and like.iddest != id_dest) or (like.idrem != id_dest and like.iddest != id_rem)):
        like=pickle.load(archivo_logico_likes)
    if (like.idrem == id_rem and like.iddest == id_dest) or (like.idrem == id_dest and like.iddest == id_rem):
        print("Hubo match!")
    else:
        print("No hubo match")



######QUEDE ACA
######KEVIN

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


#-------------------------------------MENU MODERADORES-----------------------------------#

def menu_principal_moderadores():
    print("1. Gestionar usuarios")
    print("   a. Desactivar usuarios")
    print("   b. Volver")
    print("2. Gestionar reportes")
    print("   a. Ver reportes")
    print("   b. Volver")
    print("3. Reportes estadisticos")
    print("4. Bonus track 1")
    print("5. Bonus track 2")
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
            case 4:
                bonus_track_1()
            case 5:
                bonus_track_2()
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
                return -1


def anular_usuarioenreporte (parametro, condicion):

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


def menu_gestion_reportes():
    global usuario
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
                    #AGREGAR LA POSICION DEL MODERADOR ACTUAL PARA OBTENER EL ID
                    archivo_logico_moderadores.seek(0,0)
                    usuario = moderadores()
                    usuario = pickle.load(archivo_logico_moderadores)
                    id_mod = usuario.idregistro
                    archivo_logico_reportes.seek(reporte_numero,0)
                    auxreportar = reportes ()
                    auxreportar = pickle.load(archivo_logico_reportes)
                    auxiliar_idreportado = int(auxreportar.idreportado)

                    #DESDE ACA DESACTIVA AL USUARIO#
                    desactivar_usuario (auxiliar_idereportado)

                    #DESDE ACA MODIFICA EL REPORTE#
                    auxreportar.reportadoestado = False
                    auxreportar.estadoreporte = opc
                    auxreportar.idmoderador = id_mod
                    archivo_logico_reportes.seek(reporte_numero,0)
                    pickle.dump(auxreportar, archivo_logico_reportes)
                    archivo_logico_reportes.flush()

                if opc == 2:
                    #AGREGAR LA POSICION DEL MODERADOR ACTUAL PARA OBTENER EL ID
                    archivo_logico_moderadores.seek(0,0)
                    usuario = moderadores()
                    usuario = pickle.load(archivo_logico_moderadores)
                    id_mod = usuario.idregistro

                    #DESDE ACA MODIFICA EL REPORTE#
                    archivo_logico_reportes.seek(reporte_numero,0)
                    auxreportar = reportes ()
                    auxreportar = pickle.load(archivo_logico_reportes)
                    auxreportar.estadoreporte = opc
                    auxreportar.idmoderador = id_mod
                    archivo_logico_reportes.seek(reporte_numero,0)
                    pickle.dump(auxreportar, archivo_logico_reportes)
                    archivo_logico_reportes.flush()
        limpiar_pantalla()
        listado_general_reportes ()
        opcion = validar_mientras ("Desea actualizar algun reporte (S/N): ","S", "N")


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
        if reporte.nroreporte == parametro  and reporte.idmoderador == 0:
            return pos
        else:
            return -1



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

#-------------------------------------MENU ADMINISTRADORES------------------------------#



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

def contador_inactivos (archivologico, archivofisico):
    tamaño = os.path.getsize(archivofisico)
    archivologico.seek (0,0)
    contador = 0
    while archivologico.tell() < tamaño:
        variable = pickle.load(archivologico)
        if variable.estado == True:
            return 1
    return -1



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
        if variable.idregistro == parametro:
            return pos
        else:
            return -1


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

#---------------------------------PROGRAMA---------------------------------#

usuario = [None]
global salida
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
    if opc != 0:
        print_menu_inicio()
        opc = validar(0,2)



