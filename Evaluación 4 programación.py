import os #Para limpiar la terminal
import getpass #Para ocultar la contraseña
import time #Para hacer los tiempos de espera cuando se cierra sesión

#Tema: Gimnasio Privado:         |Dato1|         |Dato2|         |Dato3|         |Dato4|         |Dato5|         |Dato6$|
#                             Identificador    Nómbre Socio     Objetivos         Plan       Fecha Inscripción  $Mensualidad

#Usuarios con acceso:
#- admin      pass: inacap   Permisos: 1.Registrar  2.Listar  3.Estadística  4.Cerrar Sesión
#- operador   pass: 123      Permisos: 1.Listar  2.Cerrar Sesión
#- gestor     pass: 321      Permisos: 1.Estadística  2.Cerrar Sesión

def menu_inicial(): ##LISTO
    os.system("cls")
    opcion= 0
    print("#### Bienvenido(a) al sistema PrivGym 2.0 #####")
    print(" Elija una de las siguientes opciones")
    print("- [1] iniciar Sesión")
    print("- [2] Salir")
    opcion = int(input(": "))

    if opcion == 1:
        print("opcion 1")
        iniciar_sesion()
    
    elif opcion == 2:
        print("opcion 2")
        salir()
    
    else:
        os.system("cls")
        print("### Opción no válida ###")
        os.system("pause")
        menu_inicial()

def iniciar_sesion(): ##FALTA HACER QUE NO SE PUEDA VER LA CONTRASEÑA
    global usuario
    os.system("cls")
    print("#### Menú de inicio de sesión ####")
    usuario = input("Ingrese su usuario: ")
    os.system("cls")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    os.system("cls")
    print("Validando datos...")
    time.sleep(3)
    os.system("cls")

    if (usuario == "admin" and contraseña == "inacap"):
        #print("Ha iniciado sesión como administrador")
        #os.system("pause")
        menu_acciones()

    elif (usuario == "operador" and contraseña == "123"):
        #print("Ha iniciado sesión como operador")
        #os.system("pause")
        menu_acciones()
        
    elif (usuario == "gestor" and contraseña == "321"):
        #print("Ha iniciado sesión como gestor")
        #os.system("pause")
        menu_acciones()

    else:
        print("Usuario/Contraseña no válidos")
        os.system("pause")
        iniciar_sesion()

def menu_acciones(): ##LISTO
    os.system("cls")

    if usuario == "admin":
        opcion=0
        print("#### MENÚ ADMINISTRADOR ####")
        print("- [1]Registrar")
        print("- [2]Listar")
        print("- [3]Estadística")
        print("- [4]Cerrar Sesión")
        opcion = int(input(": "))
        if opcion == 1:
            registrar_datos()
        elif opcion == 2:
            listar_datos()
        elif opcion == 3:
            estadistica()
        elif opcion == 4:
            cerrar_sesion()
        else:
            os.system("cls")
            print("Opción incorrecta en MENÚ ADMINISTRADOR...")
            time.sleep(2)
            menu_acciones()
        
    elif usuario == "operador":
        print("#### MENÚ OPERADOR ####")
        print("- [1]Listar")
        print("- [2]Cerra Sesión")
        opcion = int(input(": "))
        if opcion == 1:
            listar_datos()
        elif opcion == 2:
            cerrar_sesion()
        else:
            os.system("cls")
            print("Opción incorrecta en MENÚ OPERADOR...")
            time.sleep(2)
            menu_acciones()

    elif usuario == "gestor":
        print("#### MENÚ GESTOR ####")
        print("- [1]Estadística")
        print("- [2]Cerrar Sesión")
        opcion = int(input(": "))
        if opcion == 1:
            estadistica()
        elif opcion == 2:
            cerrar_sesion()
        else:
            os.system("cls")
            print("Opción incorrecta en MENÚ GESTOR...")
            time.sleep(2)
            menu_acciones()

def cerrar_sesion(): ##LISTO
    os.system("cls")
    print("Cargando...")
    time.sleep(2)
    os.system("cls")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    print("   #### Sesión Cerrada con éxito ####")
    print("#### Volviendo al menú principal.... ####")
    time.sleep(2)
    menu_inicial()

def registrar_datos(): ##LISTO
    os.system("cls")
    diccionario = dict()
    print("#### Bienvenido al Menú de Registro ####")
    os.system("pause")
    os.system("cls")
    identificador = input("Ingresa tu Identificador: ")
    os.system("cls")
    nombre_socio = input("Ingresa tu Nómbre: ")
    os.system("cls")
    objetivos = input("Ingresa tus Objetivos: ")
    os.system("cls")
    plan = input("Ingresa tu Plan: ")
    os.system("cls")
    fecha_inscripcion = input("Ingresa tu Fecha de Inscripción: ")
    os.system("cls")
    mensualidad = int(input("Ingresa la Mensualidad: $"))
    if mensualidad < 0:
        os.system("cls")
        mensualidad = int(input("Error al ingresar un valor válido para la mensualidad, volver a ingresarlo: "))

    ##FALTA HACER LA VALIDACIÓN DE LA MENSUALIDAD
    diccionario = {"identificador": identificador, "nombre": nombre_socio, "objetivos": objetivos, "plan": plan, "fecha_inscripcion": fecha_inscripcion, "mensualidad": mensualidad}
    lista.append(diccionario)
    menu_acciones()

def listar_datos(): ##LISTO
    os.system("cls")
    print("len: ",len(lista))
    if len(lista) == 0:
        print("No hay datos para listar, volviendo al menú...")
        time.sleep(2)
    else:
        print("#### LISTA DE REGISTROS ####")
        for i in lista:
            print(i)
        os.system('pause')
    menu_acciones()

def estadistica(): ##LISTO
    os.system("cls")
    valor_total = 0
    for i in lista:
        valor_total = valor_total+i["mensualidad"]
    print("#### ESTADISTICAS ####")
    print("- Cantidad de Registros: {}".format(len(lista)))
    print("- Suma de Valores: {}".format(valor_total))
    os.system("pause")
    menu_acciones()

def salir(): ##FALTA TODO
    os.system("cls")
    print("### ¿ESTÁS SEGURO QUE QUIERES SALIR? ###")
    print("- [1] Confirmar")
    print("- [2] Volver")
    decision = int(input(": "))
    os.system("cls")
    if decision == 1:
        print("Programa Finalizado!!")
    elif decision == 2:
        print("Volviendo al menú de inicio de sesión...")
        time.sleep(2)
        menu_inicial()
#global usuario
global lista
lista = []
menu_inicial()