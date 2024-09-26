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

class estudiantes:
	def __init__(self):
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

#Crear metodo para formatear los strings?
#Es para que todos los registros sean del mismo tamaño

	def formato(self):
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
	if os.path.exists(path):
		archivo_log=open(path,"r+b")
	else:
		archivo_log=open(path,"w+b")
	return archivo_log

def inicializar_arr(arreglo,tamaño, clase):
	arreglo=[None]*tamaño
	for i in range(tamaño):
		arreglo[i]=clase()



def rdob():

    rdd = str(random.randint(1,28))
    rmm = str(random.randint(1,12))
    ryear = str(random.randint(CYEARI,CYEARF))
    rdate = str(ryear) + "-" + str(rmm) + "-" + str(rdd)
    return rdate


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



def cargar_archivo_estudiantes(path):
    global archivo_logico_estudiantes
    archivo_logico_estudiantes.seek(0, 0)
    estudiante = estudiantes()
    for i in range(0, 3):
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
        formato(estudiante)
        pickle.dump(estudiante, archivo_logico_estudiantes)
        archivo_logico_estudiantes.flush()

    archivo_logico_estudiantes.close()



def cargar_archivo_administradores(path):
	global archivo_logico_administradores
	archivo_logico_administradores.seek(0,0)
	administrador=administradores()
	administrador.email="Prueba@utn.edu.ar"
	#Hay que ajustar todos los string con el mismo "Largo" para que todos los registros sean del mismo tamaño.
	administrador.email=administrador.email.ljust(32)
	administrador.contraseña="123456"
	administrador.contraseña=administrador.contraseña.ljust(32)
	pickle.dump(administrador,archivo_logico_administradores)
	archivo_logico_administradores.flush()
	archivo_logico_administradores.close()


def main():
	global archivo_logico_administradores
	global arr_estudiantes
	global arr_administradores
	global arr_moderadores
	archivo_fisico_estudiantes= os.getcwd()+"\\estudiantes.dat"
	archivo_fisico_administradores= os.getcwd()+"\\administradores.dat"
	archivo_fisico_moderadores= os.getcwd()+"\\moderadores.dat"
	archivo_logico_estudiantes=verificar_archivo(archivo_fisico_estudiantes)
	archivo_logico_administradores=verificar_archivo(archivo_fisico_administradores)
	archivo_logico_moderadores=verificar_archivo(archivo_fisico_moderadores)
	#arr_estudiantes=inicializar_arr(arr_estudiantes,8,estudiantes)
	arr_administradores=inicializar_arr(arr_administradores,4, administradores)
	#arr_moderadores=inicializar_arr(arr_moderadores,4,moderadores)
	cargar_archivo_administradores(archivo_fisico_administradores)

arr_estudiantes=[]
arr_administradores=[]
arr_moderadores=[]

main()

def print_menu_inicio():
    print("0. Salir")
    print("1. Login")
    print("2. Registrarse")


