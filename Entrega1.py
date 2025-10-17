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
        clientes (diccionario)
    """
    if (buscar in clientes.keys()):
        print("Error, el socio ya existe.\n")
        print(clientes[buscar])
    else:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")

        diaNacimiento = int(input("Dia de nacimiento: "))
        mesNacimiento = int(input("Mes de nacimiento: "))
        anioNacimiento = int(input("año de nacimiento: "))
        anioBiciesto = (anioNacimiento % 4 == 0 and (anioNacimiento % 100 != 0 or anioNacimiento % 400 == 0))


        if (diaNacimiento < 1 or diaNacimiento > 31 or mesNacimiento < 1 or mesNacimiento > 12 or anioNacimiento < 1900 or anioNacimiento > 2025):
            print("Error, fecha invalida")
            return
        elif ((mesNacimiento == 4 or mesNacimiento == 6 or mesNacimiento == 9 or  mesNacimiento == 11) and diaNacimiento == 31):
            print("Error, fecha invalida.")
            return
        elif (not anioBiciesto and mesNacimiento == 2 and diaNacimiento > 29):
            print("Error, fecha invalida")
            return

        fechaNacimiento = "" + str(diaNacimiento) + "/" + str(mesNacimiento) + "/" + str(anioNacimiento)

        clientes[buscar] = {"activo": True, "nombre": nombre, "apellido": apellido, "fechaNacimiento": fechaNacimiento, "telefonos": {} }

        NumTelefonos = int(input("Cantidad de telefonos: "))

        for i in range (NumTelefonos):
            tel = input("Telefono " + str(i+1) + ": ")
            if (int(tel) <= 0):
                print("Error, numero invalido.")
            else:
                clientes[buscar]["telefonos"]["telefono"+str(i+1)] = tel

        print("Socio agregado exitosamente")

        return clientes

def listarSocios(clientes):
    """
    Busca y lista todos los socios activos

    paramentros:
        clientes (dict)
        buscar (str)
    
    devuelve:
        n/a
    """
    for dni, cliente in clientes.items():
        if (clientes[dni]["activo"] == True):
            print("\nNombre:", cliente["nombre"])
            print("Apellido:", cliente["apellido"])
            print("Fecha de nacimiento:", cliente["fechaNacimiento"])
            telefonos = clientes[dni]["telefonos"]
            for k, telefono in telefonos.items():
                print(k + ":", telefono)
    
    return

def modificarSocio(clientes, buscar):
    """
    Modifica el valor de un socio

    Parametros:
        clientes (dict)
        buscar (str)
    Devuelve:
        clientes (diccionario)
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
            print("[1] Modificar estado")
            print("[2] Modificar nombre")
            print("[3] Modificar apellido")
            print("[4] Modificar fecha de nacimiento")
            print("[5] Modificar telefonnos")
            print("---------------------------")
            print("[0] Volver al menú anterior")
            print("---------------------------")

            userInput = int(input("Seleccione una opción: "))

            print("")
            if (userInput == 0):
                break
            elif (userInput == 1):
                res = -1
                estadoSocio = clientes[buscar]["activo"]
                while (res != 1 and res != 0):
                    print("Estado actual:", estadoSocio)
                    if (estadoSocio == True):
                        res = int(input("Desea darlo de baja? [1 = si / 0 = No]: "))
                    else:
                        res = int(input("Desea darlo de alta? [1 = si / 0 = No]: "))

                    if (res == 1 and estadoSocio == True):
                            clientes[buscar]["activo"] = False
                            print("Socio dado de baja exitosamente.\n")
                    elif (res == 1 and estadoSocio == False):
                            clientes[buscar]["activo"] = True
                            print("Socio dado de alta exitosamente.\n")
                    elif (res == 0):
                        print("No se hicieron cambios\n")
                    else:
                        print("Error, input invalido\n")                
            elif (userInput == 2):
                print("Nombre actual:", clientes[buscar]["nombre"])
                cambiar = input("Nuevo nombre: ")
                clientes[buscar]["nombre"] = cambiar
                print("Nombre cambiado existosamente")
            elif (userInput == 3):
                print("Apellido actual:", clientes[buscar]["apellido"])
                cambiar = input("Nuevo apellido: ")
                clientes[buscar]["apellido"] = cambiar
                print("Apellido cambiado existosamente")
            elif (userInput == 4):
                print("Fecha de nacimiento actual:", clientes[buscar]["fechaNacimiento"])
                cambiar = input("Nueva fecha de nacimiento [dd/mm/aaaa]: ")
                clientes[buscar]["fechaNacimiento"] = cambiar
                print("Fecha de nacimiento cambiada existosamente")
            elif (userInput == 5):
                print("Actual cant de telefonos:", len(clientes[buscar]["telefonos"]))
                cant = int(input("Nueva cant de telefonos: "))
                for i in range (cant):
                    cambiar = input("Nuevo telefono " + str(i+1) + ": ")
                    if (int(cambiar) <= 0):
                        print("Error, numero invalido.\n")
                        i -= 1
                    else:
                        clientes[buscar]["telefonos"]["telefono"+str(i)] = cambiar

    return clientes

def bajaSocio(clientes, deportes, pagos, buscar): # Terminar
    """
    Dar de baja logicamente a un socio

    Parametros:
        clientes (dict)
        buscar (str)
    
    Devuelve:
        clientes (diccionario)
    """
    if (buscar not in clientes.keys()):
        print("Error, dni no existe.")
        return

    else:
        ultimoAnioPagado = pagos[buscar]["ano"]
        ultimoMesPagado = pagos[buscar]["mes"]

    userInput = -1
    while (userInput != 1 and userInput != 0):

        for i in range(len(pagos)):
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL > MENÚ DE PAGOS")
            print("---------------------------")
            print("[1] Darse de baja de un deporte")
            print("[2] Darse de baja totalmente")
            print("---------------------------")
            print("[0] Volver al menú anterior")
            print("---------------------------")
            print()

        clienteEliminar = clientes[buscar]
        if (clienteEliminar["activo"] == False):
            print("Error, el socio ya esta dao de baja.")
        else:
            clienteEliminar["activo"] = False
            print("\nSocio", buscar, clienteEliminar["nombre"], clienteEliminar["apellido"] , "dado de baja exitosamente.")
    
    return clientes


#----------------------------------------------------------------------------------------------
# FUNCIONES DE DEPORTES
#----------------------------------------------------------------------------------------------
def crearDeporte(deportes, busqueda):
    """
    Se crea o reactiva un deporte.

    Parámetros:
        deportes: dict
        busqueda: str

    Returns:
        bool: True si se creó o reactivó el deporte, False si se canceló o no se modificó.
    """
    if busqueda in deportes:
        print("Advertencia, este deporte ya existe.")
        deporte = deportes[busqueda]
        if not deporte["activo"]:
            res = -1
            while res not in [0, 1]:
                res = int(input("El deporte está dado de baja. ¿Desea darlo de alta? [1 = Sí / 0 = No]: "))
                if res == 1:
                    nueva_fecha = input("Ingrese la nueva fecha de reactivación (DD-MM-YYYY): ")
                    deporte["activo"] = True
                    deporte["fechas"]["creacion"].append(nueva_fecha)
                    deporte["fechas"]["cierre"] = None
                    print("Deporte reactivado.")
                    return True
                elif res == 0:
                    print("El deporte se mantiene inactivo.")
                    return False
            return False
        else:
            print("El deporte ya está activo.")
            return False
    else:
        arancel = float(input("Arancel: "))
        director = input("Nombre del instructor principal: ")
        fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")

        print("\nDatos ingresados:")
        print("Deporte:", busqueda)
        print("Arancel:", arancel)
        print("Director:", director)
        print("Fecha de creación:", fecha_creacion)

        confirmar = input("¿Los datos son correctos? [si/no]: ").lower()
        if confirmar == "si":
            deportes[busqueda] = {
                "activo": True,
                "arancel": arancel,
                "director principal": director,
                "fechas": {
                    "creacion": [fecha_creacion],
                    "cierre": None
                }
            }
            print("Deporte creado exitosamente.")
            return True
        else:
            print("Operación cancelada.")
            return False


def listaDeDeportes(deportes):
    """
    Muestra todos los deportes activos (sin fecha de cierre).

    Parámetros:
        deportes: dict

    Returns:
        list: Lista de claves de deportes activos.
    """
    activos = []
    print("\nDeportes activos:")
    for clave, datos in deportes.items():
        if datos["activo"] and datos["fechas"]["cierre"] is None:
            activos.append(clave)
            print("---------------------------")
            print("Deporte:", clave)
            print("Arancel:", datos["arancel"])
            print("Director principal:", datos["director principal"])
            print("Fechas de creación:", ", ".join(datos["fechas"]["creacion"]))
    if not activos:
        print("No hay deportes activos registrados.")
    else:
        print("---------------------------")
    return activos


def modificarDeporte(deportes, busqueda):
    """
    Se modifica el deporte.

    Parámetros:
        deportes: dict
        busqueda: str

    Returns:
        bool: True si se realizó alguna modificación, False si no.
    """
    if busqueda not in deportes:
        print("Deporte no existente")
        return False
    else:
        userInput = -1
        modificado = False

        while userInput != 0:
            print(busqueda, ":")
            print(deportes[busqueda])
            print("¿Qué desea modificar?")
            print("---------------------------")
            print("[1] Modificar arancel")
            print("[2] Modificar profesor principal")
            print("---------------------------")
            print("[0] Volver al menú anterior")
            print("---------------------------")

            userInput = int(input("Seleccione una opción: "))
            print("")

            if userInput == 0:
                print("Volviendo al menú anterior...\n")

            elif userInput == 1:
                print("Arancel actual:", deportes[busqueda]["arancel"])
                cambiar = float(input("Nueva tarifa: "))
                confirmar = input(f"¿Desea guardar el nuevo arancel {cambiar}? [si/no]: ").lower()
                if confirmar == "si":
                    deportes[busqueda]["arancel"] = cambiar
                    print("Tarifa modificada exitosamente\n")
                    modificado = True
                else:
                    print("Modificación cancelada\n")

            elif userInput == 2:
                print("Profesor actual:", deportes[busqueda]["director principal"])
                cambiar = input("Nuevo profesor principal: ")
                confirmar = input(f"¿Desea guardar el nuevo profesor '{cambiar}'? [si/no]: ").lower()
                if confirmar == "si":
                    deportes[busqueda]["director principal"] = cambiar
                    print("Profesor cambiado exitosamente\n")
                    modificado = True
                else:
                    print("Modificación cancelada\n")
        return modificado


def eliminarDeporte(deportes, busqueda):
    """
    Da de baja un deporte y registra la fecha de cierre.

    Parámetros:
        deportes: dict
        busqueda: str

    Returns:
        bool: True si se dio de baja, False si no.
    """
    if busqueda not in deportes:
        print("Error, deporte no existe.")
        return False
    else:
        deporte = deportes[busqueda]
        if not deporte["activo"]:
            print("Error, el deporte ya está inactivo.")
            return False
        else:
            print("\nDatos del deporte a eliminar:")
            print("ID:", busqueda)
            print("Fechas de creación:", ", ".join(deporte["fechas"]["creacion"]))

            confirmar = input("¿Está seguro que desea dar de baja este deporte? [si/no]: ").lower()
            if confirmar == "si":
                fechaCierre = input("Ingrese la fecha de cierre (DD-MM-YYYY): ")
                deporte["activo"] = False
                deporte["fechas"]["cierre"] = fechaCierre
                print("Deporte dado de baja exitosamente.")
                return True
            else:
                print("Operación cancelada.")
                return False
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
    id_pago = f"{dni}-{deporte}-{mes}-{anio}" #  año.mes.dia hora.mes.segundo
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
        "arancel": 35000.0,
        "director principal": "Nicolás Medina",
        "fechas": {
            "creacion": ["2025-04-01"],
            "cierre": None
        }
    },
    "hockey": {
        "activo": True,
        "arancel": 27000.0,
        "director principal": "Isabel Fuentes",
        "fechas": {
            "creacion": ["2025-02-14"],
            "cierre": None
        }
    },
            },
    "basketball": {
        "activo": True,
        "arancel": 28000.0,
        "director principal": "Isabel Martinez",
        "fechas": {
            "creacion": ["2025-02-28"],
            "cierre": None
        }
    },
    "voley": {
        "activo": False,
        "arancel": 29000.0,
        "director principal": "Thiago Ribeiro",
        "fechas": {
            "creacion": ["2025-01-10", "2025-07-20"],
            "cierre": "2025-09-30"
        }
    },
    "jiuJitsu": {
        "activo": True,
        "arancel": 26000.0,
        "director principal": "Bruno Sosa",
        "fechas": {
            "creacion": ["2025-05-05"],
            "cierre": None
        }
    },
    "boxeo": {
        "activo": True,
        "arancel": 37000.0,
        "director principal": "Carla Vázquez",
        "fechas": {
            "creacion": ["2025-03-18"],
            "cierre": None
        }
    },
    "karate": {
        "activo": False,
        "arancel": 31000.0,
        "director principal": "Lucía Herrera",
        "fechas": {
            "creacion": ["2025-06-01"],
            "cierre": "2025-08-15"
        }
    },
    "tennis": {
        "activo": True,
        "arancel": 28000.0,
        "director principal": "Tomás Villalba",
        "fechas": {
            "creacion": ["2025-07-10"],
            "cierre": None
        }
    },
    "natacion": {
        "activo": True,
        "arancel": 33000.0,
        "director principal": "Esteban Ríos",
        "fechas": {
            "creacion": ["2025-04-25"],
            "cierre": None
        }
    },
    "handball": {
        "activo": True,
        "arancel": 29000.0,
        "director principal": "María Elena Torres",
        "fechas": {
            "creacion": ["2025-02-05"],
            "cierre": None
        }
    },
    "rugby": {
        "activo": False,
        "arancel": 40000.0,
        "director principal": "Federico Ledesma",
        "fechas": {
            "creacion": ["2025-01-15"],
            "cierre": "2025-07-01"
        }
    }
})

    pagos = {
        "2025.10.15 17:34:18": {
            "idSocio": "11222333",
            "idDeporte": "tennis",
            "estadoDePago": "pagado",
            "monto": 25000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "efectivo",
        },
        "2025.10.20 14:24:48": {
            "idSocio": "99888777",
            "idDeporte": "boxeo",
            "estadoDePago": "pagado",
            "monto": 31000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "tarjeta",
        },
        "2025.10.21 10:15:32": {
            "idSocio": "30456789",
            "idDeporte": "natacion",
            "estadoDePago": "pagado",
            "monto": 32000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "efectivo",
        },
        "2025.10.22 11:45:00": {
            "idSocio": "28543210",
            "idDeporte": "football",
            "estadoDePago": "pagado",
            "monto": 30000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "tarjeta",
        },
        "2025.10.23 09:30:15": {
            "idSocio": "32659874",
            "idDeporte": "basketball",
            "estadoDePago": "pagado",
            "monto": 28000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "efectivo",
        },
        "2025.10.24 16:00:00": {
            "idSocio": "29547681",
            "idDeporte": "rugby",
            "estadoDePago": "pagado",
            "monto": 34000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "tarjeta",
        },
        "2025.10.25 13:22:45": {
            "idSocio": "31478562",
            "idDeporte": "voley",
            "estadoDePago": "pagado",
            "monto": 27000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "efectivo",
        },
        "2025.10.26 18:45:30": {
            "idSocio": "27894561",
            "idDeporte": "hockey",
            "estadoDePago": "pagado",
            "monto": 29000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "tarjeta",
        },
        "2025.10.27 12:10:50": {
            "idSocio": "30985642",
            "idDeporte": "jiuJitsu",
            "estadoDePago": "pagado",
            "monto": 28000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "efectivo",
        },
        "2025.10.28 14:55:20": {
            "idSocio": "29765438",
            "idDeporte": "karate",
            "estadoDePago": "pagado",
            "monto": 26000.0,
            "ano": "2025",
            "mes": "10",
            "metodoDePago": "tarjeta",
        },
    } # Nuevo diccionario para almacenar los pagos



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
                    print("[2] listar socios activos")
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


                if (opcionSubmenu == "1" or opcionSubmenu == "3" or opcionSubmenu == "4"):
                    dniBuscar = input("Ingresar dni: ")
                    while dniBuscar.isdigit() == False:
                        dniBuscar = input("Ingresar dni válido: ")

                if opcionSubmenu == "1":   # Opción 1 del submenú
                    socios = altaSocio(socios, dniBuscar)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    listarSocios(socios)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    socios = modificarSocio(socios, dniBuscar)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    socios = bajaSocio(socios, deportes, pagos, dniBuscar)

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
                
#                if (opcionSubmenu == "1" or opcionSubmenu == "3" or opcionSubmenu == "4"):                        
                deporteBuscar = input("Ingresar deporte: ")
#                    while (deporteBuscar not in deportes.keys()):
#                        deporteBuscar = input("Ingresar deporte valido: ")


                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    crearDeporte(deportes, deporteBuscar)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    listaDeDeportes(deportes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    modificarDeporte(deportes, deporteBuscar)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    eliminarDeporte(deportes, deporteBuscar)

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
