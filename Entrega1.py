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
def altaCliente(clientes):
    ...
    return clientes



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    socios = {
        "11222333": {
            "activo": True,
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
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    clientes = altaCliente(clientes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

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
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...

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
