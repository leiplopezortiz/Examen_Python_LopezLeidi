import json
import csv
import time
from datetime import datetime

nomina={}

# def leer_archivo_empleados():
#     try:
#         with open("nomina.json","r")as file:
#             nomina=json.load(file)
#         return nomina
#     except Exception as e:
#         nomina={}

# def agregar_data_archivos_nomina():
#     try:
#         with open("nomina.json","w")as outfile:
#             json.dumps(nomina,outfile,indent=4)
#     except Exception as e:
#         nomina={}

def menu():
    print("")
    print("Bienvenido al gestor de nomina ACME INC")
    print("Te presentamos nuestras opciones")
    print("")
    print("1. Registro de empleados")
    print("2. Registro novedades o inasistencias")
    print("3. Registo de bonos extra-legales")
    print("4. Calculo de total a pagar")
    print("0. Salir")
    print("")

def registro_empleados():
    try:    
        numero_identificación_colaborador=int(input("Ingrese el número de dentificación del colaborador sin puntos ni espacios\n"))
        nombre_empleado=input("Ingrese el nombre completo del colaborador\n")
        cargo_empleado=input("Ingrese el nombre del cargo\n")
        salario_empleado=input("Ingresa el salario del colaborador sin espacios ni puntos\n")
        #nomina_json=leer_archivo_empleados()
        if numero_identificación_colaborador not in nomina:#_json:######
            info_empleado={
                    "nombre_empleado":nombre_empleado,
                    "cargo_empleado": cargo_empleado,
                    "salario_empleado":salario_empleado,
                    "novedades":[]
                    }
            print("La información del empleado es la siguiente:")
            print(f"Número de identificación del colaborador: {numero_identificación_colaborador}")
            print(f"Nombre del colaborador: {nombre_empleado}")
            print(f"Cargo del colaborador: {cargo_empleado}")
            print(f"Salario del colaborador: {salario_empleado}")
            opc=input("¿La información es correcta? s/n\n")
            if opc=="s":        
                nomina[numero_identificación_colaborador]=info_empleado
                #agregar_data_archivos_nomina(nomina)
            if opc=="n":
                return menu()
        else:
            print("Colaborador ya registrado")
    except Exception as e:
        print("Ups! algo salio mal, verifica la información e intentalo de nuevo")

def registro_inasistencias():
    try:
        numero_identificación_colaborador=int(input("Ingrese el número de dentificación del colaborador sin puntos ni espacios\n"))
        #nomina_json=leer_archivo_empleados()
        if numero_identificación_colaborador in nomina:
            try:
                falta=int (input("Ingrese 1 para indicar la falla, de lo contrario ingrese 0\n"))
                fecha=datetime.now().strftime("%d/%m/%y, %H:%M:%S")    
                if falta==1:
                    nomina[numero_identificación_colaborador]['novedades'].append(f"inasistencias:{falta}, fecha:{fecha}") ######
                    #agregar_data_archivos_nomina(falta)
                if falta==0:
                    print("Gracias, regresando al menú principal")
                else:
                    print("valor incorrecto")
            except ValueError:
                print("Verifique las opciones e intentelo de nuevo\nVolviendo al menú pricipal")
    except ValueError:
        print("Ingrese solo números\nvolviendo al menú principal...")

def registro_extra_legales():
    numero_identificación_colaborador=int(input("Ingrese el número de dentificación del colaborador sin puntos ni espacios\n"))
    try:
        if numero_identificación_colaborador in nomina:
            bono_monto=int(input("Ingrese el valor del bono\n"))
            concepto_bono=input("Ingrese el motivo del bono\n")
            fecha=datetime.now().strftime("%d/%m/%y, %H:%M:%S")
            nomina[numero_identificación_colaborador]["novedades"].append(f"monto_bono:{bono_monto}, concepto:{concepto_bono}, fecha:{fecha}") 
        else:
            print("colaborador no encontrado, verifique la información e intente de nuevo")
            print("Volviendo al menú principal...")
    except ValueError:
        print("Ingrese solo números\nvolviendo al menú principal...")

def calculo_de_nomina():
    numero_identificación_colaborador=int(input("Ingrese el número de dentificación del colaborador sin puntos ni espacios\n"))
    try:
        if numero_identificación_colaborador in nomina:
            salud_pension=(nomina[numero_identificación_colaborador]["salario_empleado"]*4/100)
            if nomina[numero_identificación_colaborador]["salario_empleado"]<2000000:
                aux_transporte=(nomina[numero_identificación_colaborador]["salario_empleado"]*10/100)
            if nomina[numero_identificación_colaborador]["novedades"]["inasistencias"]==1:
                sueldo_dias=(nomina[numero_identificación_colaborador]["salario_empleado"]/30)
                sueldo_faltas=nomina[numero_identificación_colaborador]["novedades"]["salario_empleado"]-sueldo_dias
            sueldo_final=((nomina[numero_identificación_colaborador]["salario_empleado"]-salud_pension)-sueldo_faltas)+aux_transporte
            print(f"El salario a pagar del colaborador con número de identificación: {numero_identificación_colaborador} es de: {sueldo_final}")
        else:
            print("colaborador no encontrado, verifique la información e intente de nuevo")
            print("Volviendo al menú principal...")
    except ValueError:
        print("Ingrese solo números\nvolviendo al menú principal...")

while True:
    print(menu())
    opc=int(input("Por favor ingrsa el número de la opción que deseas realizar\n"))
    try:
        if opc==1:
            registro_empleados()
            print(nomina, "prueba")#####
            time.sleep(0.5)
        if opc==2:
            registro_inasistencias()
            print(nomina,"prueba")##########
            time.sleep(0.5)
        if opc==3:
            registro_extra_legales()
            print(nomina,"prueba")##########
            time.sleep(0.5)
        if opc==4:
            calculo_de_nomina()
        if opc==0:
            print("Saliendo del programa...")
            time.sleep(1)
            break
    except ValueError:
        print("Verifique el número de la opciópn e intente de nuevo")