"""
-----------------------------------------------------------------------------------------------

Título: Entrega 1 del TP grupal
Fecha: Hecho para el 22/10/2025
Autor: Equipo 1. Federico Sznajderhaus, Benjamín Moyano, Samuel Franco Salazar, Galo Barus.

Descripción: Un club deportivo con actividades aranceladas necesita el desarrollo de una aplicación para informatizar la gestión de los pagos de los socios por cada deporte.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaSocio(clientes, buscar):
    """
    Si el socio no existe lo agrega a la base de datos, si existe y no esta dado de alta, da la opcion de hacerlo.

    Parametros:
        clientes (dict)
        buscar (str)
    Devuelve:
        n/a
    """
    if (buscar in clientes.keys()):
        print("Advertencia, socio ya existe.")
        socio = clientes[buscar]
        if (socio["activo"] == False):
            res = -1
            while (res != 1 and res != 0):
                res = int(input("El usuario esta dado de baja. Desea darlo de alta? [1 = Si / 0 = No]: "))
                if (res == 1):
                    socio["activo"] = True
                    print("\nSocio", buscar, socio["nombre"], socio["apellido"] , "dado de alta exitosamente.")
                elif (res == 0):
                    print("\nEl usuario sigue dado de baja.")
                else:
                    print("\nError, input invalido.")
    else:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fechaNacimiento = input("Fecha de nacimiento [dd/mm/aaaa]: ") 

        clientes[buscar] = {"activo": True, "nombre": nombre, "apellido": apellido, "fechaNacimiento": fechaNacimiento, "telefonos": {} }

        NumTelefonos = int(input("Cantidad de telefonos: "))

        for i in range (NumTelefonos):
            tel = input("Telefono " + str(i+1) + ": ")
            clientes[buscar]["telefonos"][cad] = tel
        
        print("Socio agregado exitosamente")

def buscarSocio(clientes, buscar): ### Buscar por distintas caracteristicas(? && Mostrar mas lindo ###
    """
    Busca un socio por dni y lo muestra en pantalla

    paramentros:
        clientes (dict)
        buscar (str)
    
    devuelve:
        n/a
    """
    if (buscar not in clientes.keys()):
        print("Error, dni no existe.")
    else:
        print("Activo:", clientes[buscar]["activo"])
        print("Nombre:", clientes[buscar]["nombre"])
        print("Apellido:", clientes[buscar]["apellido"])
        print("Fecha de nacimiento:", clientes[buscar]["fechaNacimiento"])
        telefonos = clientes[buscar]["telefonos"]
        for k, telefono in telefonos.items():
            print(k + ":", telefono)

def modificarSocio(clientes, buscar): ### Terminar ###
    """
    Modifica el valor de un socio

    Parametros:
        clientes (dict)
        buscar (str)
    Devuelve:
        n/a
    """
    if (buscar not in clientes.keys()):
        print("Error, dni no existe.")
    else:
        userInput = -1
        while (userInput != 0):
            print(buscar, ":")
            print(clientes[buscar])
            print("Que desea modificar?")
            print("---------------------------")
            print("[1] Modificar nombre")
            print("[2] Modificar apellido")
            print("[3] Modificar fecha de nacimiento")
            print("[4] Modificar telefonnos")
            print("---------------------------")
            print("[0] Volver al menú anterior")
            print("---------------------------")

            userInput = int(input("Seleccione una opción: "))

            print("")
            if (userInput == 0):
                print()
            elif (userInput == 1):
                print("Nombre actual:", clientes[buscar]["nombre"])
                cambiar = input("Nuevo nombre: ")
                clientes[buscar]["nombre"] = cambiar
                print("Nombre cambiado existosamente")
            elif (userInput == 2):
                print("Apellido actual:", clientes[buscar]["apellido"])
                cambiar = input("Nuevo apellido: ")
                clientes[buscar]["apellido"] = cambiar
                print("Apellido cambiado existosamente")
            elif (userInput == 3):
                print("Fecha de nacimiento actual:", clientes[buscar]["fechaNacimiento"])
                cambiar = input("Nueva fecha de nacimiento [dd/mm/aaaa]: ")
                clientes[buscar]["fechaNacimiento"] = cambiar
                print("Fecha de nacimiento cambiada existosamente")
            elif (userInput == 4):
                print("Actual cant de telefonos:", len(clientes[buscar]["telefonos"]))
                cant = int(input("Nueva cant de telefonos: "))
                for j in range (cant):
                    cambiar = input("Nuevo telefono " + str(j+1) + ": ")
                    clientes[buscar]["telefonos"]["telefono"+str(j)] = cambiar

def eliminarSocio(clientes, buscar):
    """
    Dar de baja logicamente a un socio

    Parametros:
        clientes (dict)
        buscar (str)
    
    Devuelve:
        n/a
    """
    if (buscar not in clientes.keys()):
        print("Error, dni no existe.")
    else:
        clienteEliminar = clientes[buscar]
        if (clienteEliminar["activo"] == False):
            print("Error, socio ya inactivo.")
        else:
            clienteEliminar["activo"] = False
            print("\nSocio", buscar, clienteEliminar["nombre"], clienteEliminar["apellido"] , "dado de baja exitosamente.")

#----------------------------------------------------------------------------------------------
# FUNCIONES DE PAGOS
#----------------------------------------------------------------------------------------------
def registrarPago(pagos, socios, deportes):
    """
    Registra un nuevo pago hecho por un socio.
    """
    dni = input("Ingrese DNI del socio: ")

    # Verificar si el socio existe y está activo
    if dni not in socios.keys():
        print("Error: el socio no existe.")
        return
    if not socios[dni]["activo"]:
        print("Error: el socio está dado de baja.")
        return
    
    # Mostrar lista de deportes activos
    print("\nDeportes disponibles:")
    for dep, datos in deportes.items():
        if datos.get("activo", False):
            print(f"- {dep} (${datos.get('arancel',0)})")
    
    deporte = input("\nIngrese el deporte: ").lower()
    if deporte not in deportes.keys() or not deportes[deporte].get("activo", False):
        print("Error: deporte inválido o inactivo.")
        return

    mes = input("Ingrese el mes del pago (ej: 10 para octubre): ")
    anio = input("Ingrese el año del pago: ")

    monto = deportes[deporte]["arancel"]

    # Guardar el pago
    id_pago = f"{dni}-{deporte}-{mes}-{anio}"
    if id_pago in pagos:
        print("Error: este pago ya fue registrado.")
        return
    
    pagos[id_pago] = {
        "dni": dni,
        "deporte": deporte,
        "mes": mes,
        "anio": anio,
        "monto": monto
    }

    print(f"\n✅ Pago registrado con éxito por ${monto} para {socios[dni]['nombre']} {socios[dni]['apellido']} ({deporte}).")

def eliminarPago(pagos):
    """
    Elimina un pago ya registrado.
    """
    dni = input("Ingrese DNI del socio: ")
    deporte = input("Ingrese el deporte: ").lower()
    mes = input("Ingrese el mes del pago (ej: 10 para octubre): ")
    anio = input("Ingrese el año del pago: ")

    id_pago = f"{dni}-{deporte}-{mes}-{anio}"

    if id_pago not in pagos.keys():
        print("Error: no existe ese pago.")
        return
    
    del pagos[id_pago]
    print("✅ Pago eliminado correctamente.")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    socios = {
        "11222333": {
            "activo": False,
            "nombre": "Federico",
            "apellido": "Sznajderhaus",
            "fechaNacimiento": "07/04/2006",
            "telefonos": {
                "telefono1": "5491125456655",
                "telefono2": "5491134546589"
            }
        },
        "99888777": {
            "activo": True,
            "nombre": "Nicolás",
            "apellido": "Sánchez",
            "fechaNacimiento": "02/09/2002",
            "telefonos": {
                "telefono1": "5491134560987"
            }
        },
        "30456789": {
            "activo": True,
            "nombre": "María",
            "apellido": "Fernández",
            "fechaNacimiento": "15/01/1998",
            "telefonos": {
                "telefono1": "5491145671234"
            }
        },
        "28543210": {
            "activo": True,
            "nombre": "Julián",
            "apellido": "Pérez",
            "fechaNacimiento": "20/05/2000",
            "telefonos": {
                "telefono1": "5491139876543",
                "telefono2": "5491123456789"
            }
        },
        "32659874": {
            "activo": True,
            "nombre": "Sofía",
            "apellido": "Martínez",
            "fechaNacimiento": "03/11/2003",
            "telefonos": {
                "telefono1": "5491165432198"
            }
        },
        "29547681": {
            "activo": True,
            "nombre": "Lucas",
            "apellido": "González",
            "fechaNacimiento": "28/07/1999",
            "telefonos": {
                "telefono1": "5491122223333",
                "telefono2": "5491176543210"
            }
        },
        "31478562": {
            "activo": True,
            "nombre": "Camila",
            "apellido": "Rodríguez",
            "fechaNacimiento": "12/12/2001",
            "telefonos": {
                "telefono1": "5491187654321"
            }
        },
        "27894561": {
            "activo": True,
            "nombre": "Martín",
            "apellido": "López",
            "fechaNacimiento": "25/06/2004",
            "telefonos": {
                "telefono1": "5491132109876",
                "telefono2": "5491198765432"
            }
        },
        "30985642": {
            "activo": True,
            "nombre": "Valentina",
            "apellido": "Díaz",
            "fechaNacimiento": "09/09/1997",
            "telefonos": {
                "telefono1": "5491144445555"
            }
        },
        "29765438": {
            "activo": True,
            "nombre": "Tomás",
            "apellido": "Suárez",
            "fechaNacimiento": "18/03/2005",
            "telefonos": {
                "telefono1": "5491155556666",
                "telefono2": "5491177778888"
            }
        },
        "31247859": {
            "activo": True,
            "nombre": "Agustina",
            "apellido": "Romero",
            "fechaNacimiento": "30/10/2002",
            "telefonos": {
                "telefono1": "5491166667777"
            }
        },
        "28965473": {
            "activo": True,
            "nombre": "Diego",
            "apellido": "Castro",
            "fechaNacimiento": "05/08/2000",
            "telefonos": {
                "telefono1": "5491133334444",
                "telefono2": "5491199990000"
            }
        }
    }
    

    deportes = {
        "football": {
            "activo": True,
            "arancel": 30000.0,
            "profesoresNinos": {
                "profesor1": "Juan Ramírez"
            },
            "profesoresAdolecentes": {
                "profesor1": "Matías Méndez",
                "profesor2": "Roberto Chávez",
                "profesor3": "Ramiro Moyano"
            },
            "profesoresAdultos": {
                "profesor1": "Pedro Arroyo",
                "profesor2": "Ramiro Moyano"
            }
        },
        "basketball": {
            "activo": True,
            "arancel": 28000.0,
            "profesoresNinos": {
                "profesor1": "Claudio García"
            },
            "profesoresAdolecentes": {
                "profesor1": "Esteban López",
                "profesor2": "Pablo Giménez"
            },
            "profesoresAdultos": {
                "profesor1": "Carlos Herrera"
            }
        },
        "tenis": {
            "activo": True,
            "arancel": 25000.0,
            "profesoresNinos": {
                "profesor1": "Ana Torres"
            },
            "profesoresAdolecentes": {
                "profesor1": "Luciano Díaz",
                "profesor2": "Gabriela Ortega"
            },
            "profesoresAdultos": {
                "profesor1": "Julián Muñoz"
            }
        },
        "natacion": {
            "activo": True,
            "arancel": 32000.0,
            "profesoresNinos": {
                "profesor1": "Mariana Silva"
            },
            "profesoresAdolecentes": {
                "profesor1": "Andrés Paredes",
                "profesor2": "Diego Bustos"
            },
            "profesoresAdultos": {
                "profesor1": "Laura Pereyra"
            }
        },
        "voley": {
            "activo": True,
            "arancel": 27000.0,
            "profesoresNinos": {
                "profesor1": "Santiago Castro"
            },
            "profesoresAdolecentes": {
                "profesor1": "Hernán Figueroa",
                "profesor2": "Martín Ríos"
            },
            "profesoresAdultos": {
                "profesor1": "Soledad Vega"
            }
        },
        "hockey": {
            "activo": True,
            "arancel": 29000.0,
            "profesoresNinos": {
                "profesor1": "Cecilia Benítez"
            },
            "profesoresAdolecentes": {
                "profesor1": "Julieta Acosta",
                "profesor2": "Paula Rojas"
            },
            "profesoresAdultos": {
                "profesor1": "Marcela Ruiz"
            }
        },
        "gimnasia": {
            "activo": True,
            "arancel": 22000.0,
            "profesoresNinos": {
                "profesor1": "Carolina Sánchez"
            },
            "profesoresAdolecentes": {
                "profesor1": "Tamara Gutiérrez"
            },
            "profesoresAdultos": {
                "profesor1": "Silvia Romero"
            }
        },
        "boxeo": {
            "activo": True,
            "arancel": 31000.0,
            "profesoresNinos": {
                "profesor1": "Oscar Fernández"
            },
            "profesoresAdolecentes": {
                "profesor1": "Pablo Correa"
            },
            "profesoresAdultos": {
                "profesor1": "Jorge Molina",
                "profesor2": "Eduardo Vargas"
            }
        },
        "karate": {
            "activo": True,
            "arancel": 26000.0,
            "profesoresNinos": {
                "profesor1": "Ricardo Soto"
            },
            "profesoresAdolecentes": {
                "profesor1": "Fernando Cruz"
            },
            "profesoresAdultos": {
                "profesor1": "Miguel Navarro"
            }
        },
        "rugby": {
            "activo": True,
            "arancel": 34000.0,
            "profesoresNinos": {
                "profesor1": "Alejandro Méndez"
            },
            "profesoresAdolecentes": {
                "profesor1": "Ignacio Romero",
                "profesor2": "Bruno Quintana"
            },
            "profesoresAdultos": {
                "profesor1": "Gastón Herrera"
            }
        },
        "padel": {
            "activo": True,
            "arancel": 26000.0,
            "profesoresNinos": {
                "profesor1": "Federico Cabrera"
            },
            "profesoresAdolecentes": {
                "profesor1": "Sebastián Olivera",
                "profesor2": "Ramiro Quiroga"
            },
            "profesoresAdultos": {
                "profesor1": "Ignacio Salazar"
            }
        },
        "jiuJitsu": {
            "activo": True,
            "arancel": 28000.0,
            "profesoresNinos": {
                "profesor1": "Diego Ferreira"
            },
            "profesoresAdolecentes": {
                "profesor1": "Marcos Ibarra",
                "profesor2": "Andrés Silva"
            },
            "profesoresAdultos": {
                "profesor1": "Rodrigo Costa",
                "profesor2": "Leonardo Duarte"
            }
        }
    }


    pagos = {

    }  # Nuevo diccionario para almacenar los pagos



    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de socios")
            print("[2] Gestión de deportes")
            print("[3] Gestión de pagos")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE SOCIOS")
                    print("---------------------------")
                    print("[1] Ingresar socio")
                    print("[2] Buscar socio/s")
                    print("[3] Modificar socio")
                    print("[4] Eliminar socio")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior

                DniBuscar = input("Ingresar dni: ")
                while DniBuscar.isdigit() == False:
                    DniBuscar = input("Ingresar dni válido: ")

                if opcionSubmenu == "1":   # Opción 1 del submenú
                    altaSocio(socios, DniBuscar)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    buscarSocio(socios, DniBuscar)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    modificarSocio(socios, DniBuscar)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    eliminarSocio(socios, DniBuscar)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE DEPORTES")
                    print("---------------------------")
                    print("[1] Ingresar deporte")
                    print("[2] Buscar deporte/s")
                    print("[3] Modificar deporte")
                    print("[4] Eliminar deporte")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 2
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE PAGOS")
                    print("---------------------------")
                    print("[1] Ingresar pago")
                    print("[2] Eliminar pago")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    registrarPago(pagos, socios, deportes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    eliminarPago(pagos)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


           
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Pagos del mes")
                    print("[2] Resumen Anual de cantidad de pagos por deporte")
                    print("[3] Resumen Anual de Pagos  (Montos cobrados, deudas, descuentos)")
                    print("[4] Porcentajes de Socios Morosos y al día")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")



        
        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()
