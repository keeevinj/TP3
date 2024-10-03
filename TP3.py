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

def limpiar_pantalla():
    os.system('cls')

#Creo registro
class estudiantes:
    def __init__(self):
        #Asigno atributos
        self.email=""
        self.nombre=""
        self.sexo=""
        self.contraseña=""
        self.estado=""
        self.hobbies=""
        self.materia_fav=""
        self.deporte_fav=""
        self.materia_fuerte=""
        self.materia_debil=""
        self.biografia=""
        self.pais=""
        self.ciudad=""
        self.fecha_nacimiento=""

#Formateo de campos del registro
def formato_estudiante(self):
    #.ljust(x) justifica a la izquierda el string es decir que "lo pega a la izquierda" y rellena el espacio vacio con x espacios hasta completar los 32 caracteres
    self.email=self.email.ljust(32)
    self.nombre=self.nombre.ljust(32)
    self.contraseña=self.contraseña.ljust(32)
    self.hobbies=self.hobbies.ljust(255)
    self.materia_fav=self.materia_fav.ljust(16)
    self.deporte_fav=self.deporte_fav.ljust(16)
    self.materia_fuerte=self.materia_fuerte.ljust(16)
    self.materia_debil=self.materia_debil.ljust(16)
    self.biografia=self.biografia.ljust(16)
    self.pais=self.pais.ljust(32)
    self.ciudad=self.ciudad.ljust(32)
    self.fecha_nacimiento=self.fecha_nacimiento.ljust(10)
        
def formato_moderadores(self):
    self.email=self.email.ljust(32)
    self.contraseña=self.contraseña.ljust(32)

def formato_administrador(self):
    self.email=self.email.ljust(32)
    self.contraseña=self.contraseña.ljust(32)

class moderadores:
    def __init__(self):
        self.email=""
        self.contraseña=""
        self.estado=""

class administradores:
    def __init__(self):
        self.email=""
        self.contraseña=""

def verificar_archivo(path):
    #Si existe el archivo, lo abre como escritura
    if os.path.exists(path):
        archivo_log=open(path,"r+b")
    else:
        archivo_log=open(path,"w+b")
        #Si no existe el archivo lo crea y abre
    return archivo_log

def inicializar_arr(arreglo,tamaño, clase):
    #Relleno el arreglo con elementos "None"
    arreglo=[None]*tamaño
    for i in range(tamaño):
        arreglo[i]=clase()

def cargar_archivo_administradores(path):
    global archivo_logico_administradores
    archivo_logico_administradores.seek(0,0)
    administrador=administradores()
    administrador.email="admin1@utn.edu.ar"
    administrador.contraseña="123456"
    formato_administrador(administrador)
    pickle.dump(administrador,archivo_logico_administradores)
    archivo_logico_administradores.flush()
    archivo_logico_administradores.close()

def rdob():
    #rdob () es una funcion que crea de forma aleatoria la fecha de nacimiento
    #se toma la fecha con datetime.now, luego se obtiene el anio actual y se guarda en una variable
    #Se crean dos variables y se guardan en cada una el anio actual menos 18 y 60, por separado.
    #determinando asi el intervalo de anio permitido a generar.
    rdd = str(random.randint(1,28))
    rmm = str(random.randint(1,12))
    ryear = str(random.randint(CYEARI,CYEARF))
    rdate = str(ryear) + "-" + str(rmm) + "-" + str(rdd)
    return rdate

def cargar_archivo_estudiantes(path):
    global archivo_logico_estudiantes
    archivo_logico_estudiantes.seek(0, 0)
    estudiante = estudiantes()
    for i in range(0, 4):
        #se cargan los cuatro estudiantes de forma automatica
        #mediante el i, se va cambiando el valor de las variables
        #Con globals, construyo el nombre de la variable existente y, al mismo tiempo, le adjudico al campo, 
        #el valor del nombre de la variable construida.
        #no se utilizan listas ni diccionarios, solo una funcion nativa relacionada con variables globales de python.
        #Antes de guardar la informacion se formatea.
        estudiante.email = "estudiante" + str(i + 1) + "@ayed.com"
        estudiante.nombre = globals()[f"nombre{i + 1}"]
        estudiante.sexo = "M"
        estudiante.contraseña = str(111222 + 111111 * i)
        estudiante.estado = 1
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

    archivo_logico_estudiantes.close()

def cargar_archivo_moderadores(path):
    global archivo_logico_moderadores
    archivo_logico_moderadores.seek(0,0)
    moderador=moderadores()
    moderador.email="mod1@utn.edu.ar"
    moderador.contraseña="123456"
    formato_moderadores(moderador)
    pickle.dump(moderador,archivo_logico_moderadores)
    archivo_logico_moderadores.flush()
    archivo_logico_moderadores.close()

def main():
    global archivo_logico_estudiantes
    global archivo_logico_administradores
    global archivo_logico_moderadores
    global archivo_fisico_estudiantes  
    global archivo_fisico_administradores
    global archivo_fisico_moderadores
    global arr_estudiantes
    global arr_administradores
    global arr_moderadores
    #archivo_fisico_xxxxxxxx="ruta de este .py" + \\xxxxxxxx.dat 
    archivo_fisico_estudiantes= os.getcwd()+"\\estudiantes.dat"
    archivo_fisico_administradores= os.getcwd()+"\\administradores.dat"
    archivo_fisico_moderadores= os.getcwd()+"\\moderadores.dat"
    archivo_logico_estudiantes=verificar_archivo(archivo_fisico_estudiantes)
    archivo_logico_administradores=verificar_archivo(archivo_fisico_administradores)
    archivo_logico_moderadores=verificar_archivo(archivo_fisico_moderadores)
    arr_estudiantes=inicializar_arr(arr_estudiantes,4,estudiantes)
    arr_administradores=inicializar_arr(arr_administradores,4,administradores)
    arr_moderadores=inicializar_arr(arr_moderadores,4,moderadores)
    cargar_archivo_administradores(archivo_fisico_administradores)
    cargar_archivo_estudiantes(archivo_fisico_estudiantes)
    cargar_archivo_moderadores(archivo_fisico_moderadores)

def print_menu_inicio():
    print("0. Salir")
    print("1. Login")
    print("2. Registrarse")

#Validar variable
def validar(var,min,max):
    aux=False
    while aux == False:
        #Me fijo si es numerica
        if (var.isnumeric())==True:
           #Es numerica
           opc=int(var)
           if (opc<min or opc>max):
                print("Opcion incorrecta.")
                var=input("Ingrese la opcion correctamente: ")
           else:
               aux=True
        elif (var.isnumeric())==False:
            #No es numerica
            print("Opcion incorrecta.")
            var=input("Ingrese la opcion correctamente: ")
    var=int(var)
    return var

#Se ingresa el campo a validar entre comillas y la longitud maxima de caractere. Valida que este correcto y formatea el campo.
def validar_campos_texto(campo_validar, longitud):
    campo = input("Ingrese " + str(campo_validar) + " (máximo " + str(longitud) + " caracteres):")
    while len(campo) > longitud:
        limpiar_pantalla()
        print("Ingrese el campo con la longitud adecuada:")
        campo = input("Ingrese " + str(campo_validar) + " (máximo " + str(longitud) + " caracteres):")
    campo = campo.ljust(longitud," ")
    return campo


#Se ingresa la contrasenia a validar entre comillas y la longitud maxima de caractere. Valida que este correcto y formatea el campo.
def validar_campos_contrasenia(campo_validar, longitud):
    campo = getpass.getpass("Ingrese " + str(campo_validar) + " (máximo " + str(longitud) + " caracteres):")
    while len(campo) > longitud:
        limpiar_pantalla()
        print("Ingrese el campo con la longitud adecuada:")
        campo = ("Ingrese " + str(campo_validar) + " (máximo " + str(longitud) + " caracteres):")
    campo = campo.ljust(longitud," ")
    return campo

#Se ingresa el campo y mientras que sea distinto de M o F la iteracion continua
def modulo_validar_sexo():
    campo = input("Ingrese el sexo (M/F): ")
    while campo != "M" and campo != "F":
        limpiar_pantalla()
        print("Ingrese el campo adecuadamente")
        campo = input("Ingrese el sexo (M/F): ")
    return campo

#Validar fecha corrobora que la fecha se ingrese adecuadamente
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

#un modulo para ingresar la fecha hasta que la misma sea ingresada correctamente
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

def contador_estudiante():
    
    global archivo_fisico_estudiantes
    archivo_logico_estudiantes=verificar_archivo(archivo_fisico_estudiantes)
    #Obtengo tamaño del archivo
    tamaño=os.path.getsize(archivo_fisico_estudiantes)
    archivo_logico_estudiantes.seek(0,0)
    contador_estudiantes=0
    #Recorro hasta que 
    while archivo_logico_estudiantes.tell()<tamaño:
            estudiante=pickle.load(archivo_logico_estudiantes)
            if estudiante.email != "":
                  contador_estudiantes=contador_estudiantes+1

    archivo_logico_estudiantes.close()
    return contador_estudiantes

def contador_moderador():
    
    global archivo_fisico_moderadores
    archivo_logico_moderadores=verificar_archivo(archivo_fisico_moderadores)
    archivo_logico_moderadores.seek(0,0)
    tamaño=os.path.getsize(archivo_fisico_moderadores)
    contador_moderadores=0
    while archivo_logico_moderadores.tell()<tamaño:
            moderador=pickle.load(archivo_logico_moderadores)
            if moderador.email != "":
                  contador_moderadores=contador_moderadores+1

    archivo_logico_moderadores.close()
    return contador_moderadores

def contador_administrador():
    
    global archivo_fisico_administradores
    archivo_logico_administradores=verificar_archivo(archivo_fisico_administradores)
    archivo_logico_administradores.seek(0,0)
    tamaño=os.path.getsize(archivo_fisico_administradores)
    contador_administradores=0
    while archivo_logico_administradores.tell()<tamaño:
            administrador=pickle.load(archivo_logico_administradores)
            if administrador.email != "":
                  contador_administradores=contador_administradores+1

    archivo_logico_administradores.close()
    return contador_administradores

def check():
    contador_estudiantes=contador_estudiante()
    contador_moderadores=contador_moderador()
    contador_administradores=contador_administrador()
    if contador_estudiantes >= 4 and contador_moderadores >= 1 and contador_administradores >=1:
        return True
    else:
        return False

def buscar(email,registro):
    #Defino usuario para que sea una variable global donde se va a almacenar el registro (todos los datos) de quien se logea
    global usuario
    #No se si hace falta que sea global tipo_usuario
    global tipo_usuario
    tipo_usuario=""
    #Formateo email y contraseña para buscar
    email=email.ljust(32)
    #Busco los tamaños de los archivos
    tam_est=os.path.getsize(archivo_fisico_estudiantes)
    tam_adm=os.path.getsize(archivo_fisico_administradores)
    tam_mod=os.path.getsize(archivo_fisico_moderadores)
    #Abro los archivos
    archivo_logico_estudiantes=open(archivo_fisico_estudiantes,"r+b")
    archivo_logico_administradores=open(archivo_fisico_administradores,"r+b")
    archivo_logico_moderadores=open(archivo_fisico_moderadores,"r+b")
    #Seteo banderas
    busqueda=False
    busqueda_estudiante=False
    busqueda_administradores=False
    busqueda_moderadores=False
    #Creo registros auxiliares para traer el registro del archivo y comparar
    estudiante=estudiantes()
    moderador=moderadores()
    administrador=administradores()
    #Capaz es mas eficiente obtener el tamaño y abrir el archivo dentro de cada while.. Habria que probar
    while busqueda==False:
        #Me fijo si esta en el final del archivo o si lo encontró.
        while archivo_logico_estudiantes.tell()<tam_est and busqueda_estudiante == False:
            estudiante=pickle.load(archivo_logico_estudiantes)
            if estudiante.email == email:
                if registro==True:
                    busqueda=True
                    busqueda_estudiante=True
                    busqueda_administradores=True
                    busqueda_moderadores=True
                    usuario=estudiante
                    tipo_usuario="Estudiante"
                else:
                    contraseña = validar_campos_contrasenia ("Contrasenia", 32)
                    if estudiante.contraseña==contraseña:
                        #Si lo encuentra, me fijo el estado.
                        if estudiante.estado==1:
                            busqueda=True
                            busqueda_estudiante=True
                            busqueda_administradores=True
                            busqueda_moderadores=True
                            usuario=estudiante
                            tipo_usuario="Estudiante"
                        else:
                            busqueda=True
                            busqueda_estudiante=True
                            busqueda_administradores=True
                            busqueda_moderadores=True
                            usuario=estudiante
                            tipo_usuario="Su usuario esta INACTIVO"
        while archivo_logico_moderadores.tell()<tam_mod and busqueda_moderadores == False:
            moderador=pickle.load(archivo_logico_moderadores)
            if moderador.email == email:
                if registro==False:
                    contraseña = validar_campos_contrasenia ("Contrasenia", 32)
                    if moderador.contraseña==contraseña:
                        busqueda=True
                        busqueda_administradores=True
                        busqueda_moderadores=True
                        usuario=moderador
                        tipo_usuario="Moderador"
                else:
                    busqueda=True
                    busqueda_estudiante=True
                    busqueda_administradores=True
                    busqueda_moderadores=True
                    usuario=estudiante
                    tipo_usuario="Moderador"
        while archivo_logico_administradores.tell()<tam_adm and busqueda_administradores == False:
            administrador=pickle.load(archivo_logico_administradores)
            if administrador.email == email:
                if registro==False:
                    contraseña = gvalidar_campos_contrasenia ("Contrasenia", 32)
                    if administrador.contraseña==contraseña:
                        busqueda=True
                        busqueda_administradores=True
                        usuario=moderador
                        tipo_usuario="Administrador"
        if tipo_usuario=="":
            busqueda=True
            tipo_usuario="No encontrado"
    #Sera trivial poner busqueda=True???
    #Devuelvo el tipo de usuario encontrado, si es un estudiante desactivado o si no lo encontró
    return tipo_usuario

def menu_principal_estudiantes():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

def menu_print_gestion_perfil():
    print("1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")

def menu_editar_datos_personales(usuario):
    # Asigno los datos del estudiante a la variable auxiliar.
    aux=estudiantes()
    #aux=usuario
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
        opc=input("Ingrese la opcion: ")
        opc=validar(opc,0,11)
        match opc:
            case 1:
                aux.nombre=validar_campos_texto("Nombre",32)
            case 2:
                aux.sexo=modulo_validar_sexo()
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
        formato_estudiante(aux)
        archivo_logico_estudiantes=open(archivo_fisico_estudiantes,"r+b")
        tam_est=os.path.getsize(archivo_fisico_estudiantes)
        archivo_logico_estudiantes.seek(0,0)
        pos=pickle.load(archivo_logico_estudiantes)
        tam_reg=archivo_logico_estudiantes.tell()
        cant_reg=tam_est/tam_reg
        i=0
        #Esto esta mal, cuando hace el dump me lo deja en el registro siguiente
        if usuario.nombre == pos.nombre:
            archivo_logico_estudiantes.seek(i*tam_reg,0)
            pickle.dump(aux,archivo_logico_estudiantes)
        else:
            while archivo_logico_estudiantes.tell() < tam_est and usuario.nombre != pos.nombre:
                i=i+1
                pos=pickle.load(archivo_logico_estudiantes)
            archivo_logico_estudiantes.seek(i*tam_reg,0)
            pickle.dump(aux,archivo_logico_estudiantes)
        archivo_logico_estudiantes.flush()
        archivo_logico_estudiantes.close()


def menu_opc_gestion_perfil():
    limpiar_pantalla()
    menu_print_gestion_perfil()
    opc = input("Ingrese una opcion: ")
    while opc != "c":
        while usuario.estado==1 and opc != "c":
            match opc:
                case "a":
                    menu_editar_datos_personales(usuario)
                case "b":
                    menu_eliminar_perfil()
                case "c":
                    print("")
                case _:
                    print("Ingrese la opcion correctamente")
                    sleep(2)   
            limpiar_pantalla()
            #ver
            if usuario.estado==1:
                menu_print_gestion_perfil()
                opc = input("Ingrese una opcion: ")
            else:
                opc="c"


def menu_estudiantes():
    opc = 1
    while opc != 0 and usuario.estado==1:
        limpiar_pantalla()
        menu_principal_estudiantes()
        opc=input("Ingrese su seleccion: ")
        opc=validar(opc,0,4)
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

def menu_moderadores():
    print("Soy moderador")

def menu_administradores():
    print("Soy administrador")

def registro_estudiantes():
    email=validar_campos_texto("Email", 32)
    tipo_usuario= buscar(email,True)
    if tipo_usuario == "No encontrado":
        nuevo_usuario=estudiantes()
        nuevo_usuario.email=email
        nuevo_usuario.contraseña = validar_campos_contrasenia ("Contrasenia", 32)
        nuevo_usuario.nombre = validar_campos_texto("Nombre", 32)
        #Validar M o F
        nuevo_usuario.sexo = modulo_validar_sexo()
        nuevo_usuario.estado=1
        nuevo_usuario.hobbies = validar_campos_texto("Hobbies", 255)
        nuevo_usuario.materia_fav = validar_campos_texto("Materia Favorita", 16)
        nuevo_usuario.deporte_fav = validar_campos_texto("Deporte Favorito", 16)
        nuevo_usuario.materia_fuerte = validar_campos_texto("Materia Fuerte", 16)
        nuevo_usuario.materia_debil = validar_campos_texto("Materia Debil", 16)
        nuevo_usuario.biografia = validar_campos_texto("Biografia", 255)
        nuevo_usuario.pais = validar_campos_texto("Pais", 32)
        nuevo_usuario.ciudad = validar_campos_texto("Ciudad", 32)
        #Revisar fecha de nacimiento
        nuevo_usuario.fecha_nacimiento=modulo_ingrese_fecha()
        formato_estudiante(nuevo_usuario)
        archivo_logico_estudiantes=open(archivo_fisico_estudiantes,"r+b")
        tam_est=os.path.getsize(archivo_fisico_estudiantes)
        #Para que el puntero quede en el ultimo lugar, 
        while archivo_logico_estudiantes.tell()<tam_est:
            aux=pickle.load(archivo_logico_estudiantes)
        pickle.dump(nuevo_usuario,archivo_logico_estudiantes)
        archivo_logico_estudiantes.flush()
        archivo_logico_estudiantes.close()
    else:
        print("El mail ya esta en uso")   

def login():
    if check() == True:
        intentos=0
        while intentos <3:
            email = validar_campos_texto("Email", 32)
            #Busco email y contraseña en los archivos
            estado_login = buscar(email,False)
            if estado_login == "No encontrado" or estado_login == "Su usuario esta INACTIVO":
                if estado_login == "No encontrado":
                    print(estado_login)
                else:
                    print("Contraseña incorrecta")
                intentos=intentos+1
                if intentos != 3:
                    print(f"Le quedan: {3-intentos} intentos")
            else:
                intentos=3
        if estado_login == "Estudiante":
            menu_estudiantes()
        elif estado_login == "Moderador":
            menu_moderadores()
        elif estado_login == "Administrador":
            menu_administradores()
        else:
            print("Acceso denegado")
    else:
        print("No se puede iniciar porque no hay 1 administrador, 1 moderador y 4 estudiantes registrados.")
        sleep(5)
        limpiar_pantalla()




#ARREGLOS
arr_estudiantes=[]
arr_administradores=[]
arr_moderadores=[]

#VARIABLES CON INFO
currentdate = datetime.now()
CYEAR = int(currentdate.year)
CYEARF = CYEAR - 18
CYEARI = CYEAR - 60

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

usuario = [None]

main()

print_menu_inicio()
opc=input("Ingrese opcion: ")
opc=validar(opc,0,2)

while opc != 0:
    
    if opc == 1:
        login()
        
    else:
        registro_estudiantes()
    
    print_menu_inicio()
    opc=input("Ingrese opcion: ")
    opc=validar(opc,0,2) 



