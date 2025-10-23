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
import time


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
    
    nombre = str(input("Nombre: "))
    while nombre.isalpha() == False:
        nombre = str(input("Error! Seleccione nuevo nombre: "))
    apellido = str(input("Apellido: "))
    while apellido.isalpha() == False:
        apellido = str(input("Error! Seleccione nuevo nombre: "))

    diaNacimiento = int(input("Dia de nacimiento: "))
    if diaNacimiento < 1 or diaNacimiento > 31:
        print("Error, fecha invalida")
        return clientes

    mesNacimiento = int(input("Mes de nacimiento: "))
    if mesNacimiento < 1 or mesNacimiento > 12 or ((mesNacimiento == 4 or mesNacimiento == 6 or mesNacimiento == 9 or  mesNacimiento == 11) and diaNacimiento == 31):
        print("Error, fecha invalida")
        return clientes
    
    anioNacimiento = int(input("año de nacimiento: "))
    if (anioNacimiento < 1900 or anioNacimiento > 2025):
        print("Error, fecha invalida")
        return clientes
    
    anioBiciesto = (anioNacimiento % 4 == 0 and (anioNacimiento % 100 != 0 or anioNacimiento % 400 == 0))        
    if (not anioBiciesto and mesNacimiento == 2 and diaNacimiento > 29):
        print("Error, fecha invalida")
        return clientes
    
    if len(str(diaNacimiento)) == 1:
        diaNacimiento = "0" + str(diaNacimiento)
    if len(str(mesNacimiento)) == 1:
        mesNacimiento = "0" + str(mesNacimiento)
    fechaNacimiento = f"{str(diaNacimiento)}/{str(mesNacimiento)}/{str(anioNacimiento)}"

    clientes[buscar] = {"activo": True, "nombre": nombre, "apellido": apellido, "fechaNacimiento": fechaNacimiento, "telefonos": {} }

    numTelefonos = int(input("Cantidad de telefonos: "))
    while numTelefonos < 1:
        numTelefonos = int(input("Error! Ingrese cantidad de telefonos de nuevo: "))  
    for i in range (numTelefonos):
        tel = int(input("Telefono " + str(i + 1) + ": "))
        while len(str(tel)) < 10 or len(str(tel)) > 13 or tel < 0:
            tel = int(input("Error! Ingrese Telefono " + str(i + 1) + " de nuevo: "))
        clientes[buscar]["telefonos"]["telefono" + str(i + 1)] = tel

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
    Modifica los atributos de un socio

    Parametros:
        clientes (dict)
        buscar (str)
    Devuelve:
        clientes (diccionario)
    """
   
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
                    res = int(input("Desea darlo de baja? [1 = si / 0 = No]: ")) #PODEMOS DARLO DE BAJA DE UN DEPORTE ACA MEJOR Y LO QUE ESTA ACA LO PONEMOS EN ELIMINAR
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
            print("Nombre actual: ", clientes[buscar]["nombre"])
            cambiar = str(input("Nuevo nombre: "))
            while cambiar.isalpha() == False:
                cambiar = str(input("Error! Seleccione nuevo nombre: "))
            clientes[buscar]["nombre"] = cambiar
            print("Nombre cambiado existosamente")

        elif (userInput == 3):
            print("Apellido actual: ", clientes[buscar]["apellido"])
            cambiar = str(input("Nuevo apellido: "))
            while cambiar.isalpha() == False:
                cambiar = str(input("Error! Seleccione nuevo apellido: "))
            clientes[buscar]["apellido"] = cambiar
            print("Apellido cambiado existosamente")

        elif (userInput == 4):
            print("Fecha de nacimiento actual: ", clientes[buscar]["fechaNacimiento"])
            diaNacimiento = int(input("Dia de nacimiento: "))
            if diaNacimiento < 1 or diaNacimiento > 31:
                print("Error, fecha invalida")
                return clientes
            mesNacimiento = int(input("Mes de nacimiento: "))
            if mesNacimiento < 1 or mesNacimiento > 12 or ((mesNacimiento == 4 or mesNacimiento == 6 or mesNacimiento == 9 or  mesNacimiento == 11) and diaNacimiento == 31):
                print("Error, fecha invalida")
                return clientes
            anioNacimiento = int(input("año de nacimiento: "))
            if (anioNacimiento < 1900 or anioNacimiento > 2025):
                print("Error, fecha invalida")
                return clientes
            anioBiciesto = (anioNacimiento % 4 == 0 and (anioNacimiento % 100 != 0 or anioNacimiento % 400 == 0))        
            if (not anioBiciesto and mesNacimiento == 2 and diaNacimiento > 29):
                print("Error, fecha invalida")
                return clientes
            if len(str(diaNacimiento)) == 1:
                diaNacimiento = "0" + str(diaNacimiento)
            if len(str(mesNacimiento)) == 1:
                mesNacimiento = "0" + str(mesNacimiento)
            fechaNacimiento = f"{str(diaNacimiento)}/{str(mesNacimiento)}/{str(anioNacimiento)}"
            clientes[buscar]["fechaNacimiento"] = fechaNacimiento
            print("Fecha de nacimiento cambiada existosamente")

        elif (userInput == 5):
            print("Actual cant de telefonos: ", len(clientes[buscar]["telefonos"]))
            numTelefonos = int(input("Cantidad de telefonos: "))
            while numTelefonos < 1:
                numTelefonos = int(input("Error! Ingrese cantidad de telefonos de nuevo: "))  
            for i in range (numTelefonos):
                tel = int(input("Telefono " + str( i+ 1) + ": "))
                while len(str(tel)) < 10 or len(str(tel)) > 13 or tel < 0:
                    tel = int(input("Error! Ingrese Telefono " + str(i + 1) + " de nuevo: "))
                clientes[buscar]["telefonos"]["telefono"+str(i + 1)] = tel

    return clientes

def bajaSocio(clientes, deportes, pagos, buscar): # COMENTARIO MENCIONADO EN MODIFICAR
    """
    Dar de baja logicamente a un socio

    Parametros:
        clientes (dict)
        buscar (str)
    
    Devuelve:
        clientes (diccionario)
    """
    if (not clientes[buscar]["activo"]):
        print("Cliente ya inactivo")
        return clientes

    print(f"\nLista de pagos de {clientes[buscar]["nombre"]} {clientes[buscar]["apellido"]}:")

    for k, v in pagos.items():
        if (v["idSocio"] == buscar):
            print(k, v)

    res = -1
    while (res < 0 or res > 1):
        res = int(input("\nDesea dar de baja al socio? [1 = Si / 0 = No]: "))
        if (res == 1):
            clientes[buscar]["activo"] = False
            print("Cliente dado de baja existosamente.")
        elif (res == 0):
            print("No pasó nada.")
        else:
            print("Input invalido.")

    return clientes


#----------------------------------------------------------------------------------------------
# FUNCIONES DE DEPORTES
#----------------------------------------------------------------------------------------------
def crearDeporte(deportes, busqueda):
    """
    Se crea o reactiva un deporte.

    Parámetros:
        deportes (dict)
        busqueda (str)
    Devuelve:
        deportes (dict)
    """
    if busqueda in deportes.keys():
        print("Advertencia, este deporte ya existe.")
        if deportes[busqueda]["activo"] == False:
            res = -1
            while res not in [0, 1]:
                res = int(input("El deporte está dado de baja. ¿Desea darlo de alta? [1 = Sí / 0 = No]: "))
                if res == 1:
                    deportes[busqueda]["activo"] = True
                    n = 1 + len(deportes[busqueda]["fechasActividad"])
                    deportes[busqueda]["fechasActividad"][f"fecha{n}"] = [time.strftime("%d/%m/%Y")]
                elif res == 0:
                    print("El deporte se mantiene inactivo.")
    else:
        arancel = float(input("Arancel: "))
        while arancel < 0:
            arancel = float(input("Error! Ingrese arancel de nuevo: "))
        director = str(input("Nombre del director principal: "))
        fecha_creacion = time.strftime("%d/%m/%Y")

        print("\nDatos ingresados:")
        print("Deporte:", busqueda)
        print("Arancel:", arancel)
        print("Director:", director)
        print("Fecha de creación:", fecha_creacion)

       
        res = -1
        while res not in [0, 1]:
            res = int(input("¿Los datos son correctos? [1 = Sí / 0 = No]: "))
            if res == 1:
                deportes[busqueda] = {
                    "activo": True,
                    "arancel": arancel,
                    "director principal": director,
                    "fechasActividad": {
                        "fecha1": [fecha_creacion]
                    }
                }
                print("Deporte creado exitosamente.")
            elif res == 0:
                print("Operación cancelada.")
    return deportes


def listaDeDeportes(deportes):
    """
    Muestra todos los deportes activos (sin fecha de cierre).

    Parámetros:
        deportes: dict
    """
    activos = False
    print("\nDeportes activos:")
    for clave, datos in deportes.items():
        if datos["activo"] == True:
            activos = True
            print("---------------------------")
            print("Deporte:", clave)
            print("Arancel:", datos["arancel"])
            print("Director principal:", datos["director principal"])
            print("Fechas de actividad: ", datos["fechasActividad"])
    if activos == False:
        print("No hay deportes activos registrados.")
    else:
        print("---------------------------")
    
    return


def modificarDeporte(deportes):
    """
    Se modifica el deporte.

    Parámetros:
        deportes: dict

    Returns:
        Deportes
    """
    keys = list(deportes.keys())
    for i in range(len(keys)): 
        print (f"[{i+1}] {keys[i]}")
    eleccion = int(input("Seleccione el número del deporte que desea modificar: "))
    while eleccion < 1 or eleccion > len(keys):
        eleccion = int(input("Error seleccionar un numero apropiado: "))
    deporteSeleccionado = keys[eleccion - 1]

    userInput = -1                   
    while userInput != 0:
        print(deporteSeleccionado, ":")
        print(deportes[deporteSeleccionado]) 
        print("¿Qué desea modificar?")
        print("---------------------------")
        print("[1] Modificar arancel")
        print("[2] Modificar director principal")
        print("---------------------------")
        print("[0] Volver al menú anterior")
        print("---------------------------")

        userInput = int(input("Seleccione una opción: "))
        print("")

        if userInput == 0:
            print("Volviendo al menú anterior...\n")

        elif userInput == 1:
            print("Arancel actual:", deportes[deporteSeleccionado]["arancel"])
            cambiar = float(input("Nueva tarifa: "))
            while cambiar < 0:
                cambiar = float(input("Error! Ingrese arancel de nuevo: "))
            res = -1
            while res not in [0, 1]:
                res = int(input(f"¿Desea guardar el nuevo arancel {cambiar}? [1 = Sí / 0 = No]: "))
                if res == 1:
                    deportes[deporteSeleccionado]["arancel"] = cambiar
                    print("Tarifa modificada exitosamente\n")
                elif res == 0:
                    print("Modificación cancelada\n")

        elif userInput == 2:
            print("Profesor actual:", deportes[deporteSeleccionado]["director principal"])
            cambiar = str(input("Nuevo director principal: "))
            res = -1
            while res not in [0, 1]:
                res = int(input(f"¿Desea guardar el nuevo director principal {cambiar}? [1 = Sí / 0 = No]: "))
                if res == 1:
                    deportes[deporteSeleccionado]["director principal"] = cambiar
                    print("Tarifa modificada exitosamente\n")
                elif res == 0:
                    print("Modificación cancelada\n")

    return deportes



def eliminarDeporte(deportes):
    """
    Da de baja un deporte activo y registra la fecha de cierre.

    Parámetros:
        deportes: dict

    Returns:
        deportes (dict)
    """
    keys = [k for k, v in deportes.items() if v["activo"] == True]

    if not keys:
        print("No hay deportes activos para dar de baja.")
        return deportes

    print("\nDeportes activos:")
    for i in range(len(keys)): 
        print(f"[{i+1}] {keys[i]}")

    eleccion = int(input("Seleccione el número del deporte que desea dar de baja: "))
    while eleccion < 1 or eleccion > len(keys):
        eleccion = int(input("Error: seleccione un número válido: "))
    
    deporteSeleccionado = keys[eleccion - 1]

    res = -1
    while res not in [0, 1]:
        res = int(input(f"¿Desea dar de baja {deporteSeleccionado}? [1 = Sí / 0 = No]: "))
        if res == 1:
            deportes[deporteSeleccionado]["activo"] = False
            n = len(deportes[deporteSeleccionado]["fechasActividad"])
            deportes[deporteSeleccionado]["fechasActividad"][f"fechas{n}"].append(time.strftime("%d/%m/%Y"))
            print(f"Deporte '{deporteSeleccionado}' dado de baja exitosamente.\n")
        elif res == 0:
            print("Baja cancelada.\n")
    return deportes

#----------------------------------------------------------------------------------------------
# FUNCIONES DE PAGOS
#----------------------------------------------------------------------------------------------
def registrarPago(pagos, socios, deportes):
    """
    Registra un nuevo pago hecho por un socio.

    parametros:
        pagos (dict)
        socios (dict)
        deportes (dict)

    devuelve
        pagos (dict)
    """
    anioActual = int(time.strftime("%Y"))
    mesActual = int(time.strftime("%m"))
    dni = str(input("Ingrese DNI del socio: "))

    # Verificar si el socio existe y está activo
    if dni not in socios.keys():
        print("Error: el socio no existe.")
        return pagos
    if not socios[dni]["activo"]:
        print("Error: el socio está dado de baja.")
        return pagos

    keysDeportes = list(deportes.keys())
    for i in range(len(keysDeportes)): 
        print (f"[{i+1}] {keysDeportes[i]}")
    eleccion = int(input("Seleccione el número del deporte: "))
    while eleccion < 1 or eleccion > len(keysDeportes):
        eleccion = int(input("Error seleccionar un numero apropiado: "))
    deporteSeleccionado = keysDeportes[eleccion - 1]

    mes = 13
    anio = anioActual
    while (mes > mesActual and anio == anioActual):
        mes = -1
        while (mes < 1 or mes > 12):
            mes = int(input("\nIngrese el mes del pago (ej: 10 para octubre): "))
        anio = 9999
        while (anio < 1900 or anio > anioActual):
            anio = int(input("\nIngrese el año del pago: "))
        if (mes > mesActual and anio == anioActual):
            print("\nError, fecha invalida.")
    
    keysPagos = list(pagos.keys())
    for i in range(len(keysPagos)):
        if pagos[keysPagos[i]]["mes"] == mes and pagos[keysPagos[i]]["ano"] == anio and dni == pagos[keysPagos[i]]["idSocio"] and deporteSeleccionado == pagos[keysPagos[i]]["idDeporte"]:
            print("Pago invalido, pago ya efectuado.")
            return pagos
    
    activoEnFecha = False
    for periodo in deportes[deporteSeleccionado]["fechasActividad"].values():
        # Fecha de inicio
        diaI, mesI, anioI = periodo[0].split("/")
        anioI = int(anioI)
        mesI = int(mesI)

        # Fecha de cierre (si existe)
        if len(periodo) == 2:
            diaF, mesF, anioF = periodo[1].split("/")
            anioF = int(anioF)
            mesF = int(mesF)
        else:
            # Si no hay cierre, se asume activo hasta hoy
            anioF = int(time.strftime("%Y"))
            mesF = int(time.strftime("%m"))
        
        if (anio > anioI or (anio == anioI and mes >= mesI)) and (anio < anioF or (anio == anioF and mes <= mesF)):
            activoEnFecha = True
    if not activoEnFecha:
        print(f"Error: el deporte seleccionado no estaba activo en esa fecha")
        return pagos


    
    opcionDePago = -1
    while (opcionDePago < 1 or opcionDePago > 3):
        print("\nSeleccione el medio de pago:")
        print("[1] Efectivo")
        print("[2] Tarjeta")
        print("[3] Transferencia")
        opcionDePago = int(input(("\nOpcion elegida:")))

    if (opcionDePago == 1):
        metodoDePago = "efectivo"
    elif (opcionDePago == 2):
        metodoDePago = "tarjeta"
    else:
        metodoDePago = "transferencia"


    monto = deportes[deporteSeleccionado]["arancel"]
    if (mesActual > mes and anioActual == anio) or (anioActual > anio):
        monto *= 1.2
        print(f"Usted debe pagar {monto} que está un 20% aumentado, debido a que está atrasado. Aceptas el pago? [1 = si / 0 = No]")
    else:
        print(f"Usted debe pagar {monto}. Aceptas el pago? [1 = si / 0 = No]")
    res = -1
    while (res < 0 or res > 1):
        res = int(input(""))
        if (res == 1):
            id_pago = f"{anioActual}.{mesActual}.{time.strftime("%d")} {time.strftime("%H")}:{time.strftime("%M")}:{time.strftime("%S")}"

            pagos[id_pago] = {
                "idSocio": dni,
                "idDeporte": deporteSeleccionado,
                "estadoDePago": "pagado",
                "monto": monto,
                "ano": anio,
                "mes": mes,
                "metodoDePago": metodoDePago
            }
            

            print(f"\nPago registrado con éxito por ${monto} para {socios[dni]['nombre']} {socios[dni]['apellido']} ({deporteSeleccionado}).")
            print(pagos)

            return pagos

        elif (res == 0):
            print("No se realizo el pago.")
            return pagos
        else:
            print("Error, opcion invalida. Ingrese de nuevo.")



    return pagos

def eliminarPago(pagos, socios):
    """
    Elimina un pago

    Parámetros:
        pagos (dict)
        socios (dict)
        deportes (dict)

    Devuelve:
        pagos (dict)
    """
    dni = str(input("Ingrese DNI del socio: "))
    if dni not in socios.keys():
        print("Error: el socio no existe.")
        return pagos
    
    # Filtrar los deportes en los que el socio tenga pagos
    listaKeysPagos = list(pagos.keys())
    listaDeportesPorSocio = []
    for key in listaKeysPagos:
        if pagos[key]["idSocio"] == dni and pagos[key]["idDeporte"] not in listaDeportesPorSocio:
            listaDeportesPorSocio.append(pagos[key]["idDeporte"])

    if not listaDeportesPorSocio:
        print("El socio no tiene pagos registrados.")
        return pagos

    # Elegir deporte
    for i, dep in enumerate(listaDeportesPorSocio):
        print(f"[{i+1}] {dep}")
    eleccion = int(input("Seleccione el número de deporte del pago: "))
    while eleccion < 1 or eleccion > len(listaDeportesPorSocio):
        eleccion = int(input("Error! Seleccionar un número apropiado: "))
    deporteSeleccionado = listaDeportesPorSocio[eleccion - 1]

    # Mostrar los pagos correspondientes al socio y deporte elegido
    pagosFiltrados = []
    contador = 0
    for key in listaKeysPagos:
        if pagos[key]["idSocio"] == dni and pagos[key]["idDeporte"] == deporteSeleccionado:
            contador += 1
            pagosFiltrados.append(key)
            print(f"[{contador}] {pagos[key]}")

    if not pagosFiltrados:
        print("No hay pagos para este deporte.")
        return pagos

    # Elegir cuál eliminar
    eleccion = int(input("Seleccione el número de pago: "))
    while eleccion < 1 or eleccion > len(pagosFiltrados):
        eleccion = int(input("Error! Seleccionar un número apropiado: "))

    keySeleccionada = pagosFiltrados[eleccion - 1]
    print("\nEste es el pago seleccionado:")
    print(pagos[keySeleccionada])

    print("ALERTA: Si confirmas, se eliminará permanentemente.")
    confirmar = int(input("¿Quieres eliminar el pago? [1 = Sí / 0 = No]: "))
    if confirmar == 1:
        del pagos[keySeleccionada]
        print("Pago eliminado exitosamente.")
    else:
        print("Operación cancelada.")

    return pagos

    
#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------
def mostrarPagosPorMesYAnio(pagos, socios, mesObjetivo, anoObjetivo):
    def rellenar(texto, ancho, alineacion):
        texto = str(texto)
        largo = len(texto)
        if largo >= ancho:
            return texto[:ancho]
        espacios = ancho - largo
        if alineacion == "izquierda":
            return texto + " " * espacios
        else:
            return " " * espacios + texto

    anchoFecha = 21
    anchoCliente = 25
    anchoMonto = 10

    encabezado = rellenar("Fecha/Hora", anchoFecha, "izquierda") + " | " + \
                 rellenar("Cliente", anchoCliente, "izquierda") + " | " + \
                 rellenar("Monto", anchoMonto, "derecha")
    print(encabezado)
    print("-" * len(encabezado))

    for fechaHora in pagos:
        registro = pagos[fechaHora]
        if "idSocio" in registro and "mes" in registro and "ano" in registro and "monto" in registro:
            if registro["mes"] == mesObjetivo and registro["ano"] == anoObjetivo:
                idSocio = registro["idSocio"]
                monto = registro["monto"]

                if idSocio in socios:
                    nombre = socios[idSocio]["nombre"]
                    apellido = socios[idSocio]["apellido"]
                    cliente = nombre + " " + apellido

                    linea = rellenar(fechaHora, anchoFecha, "izquierda") + " | " + \
                            rellenar(cliente, anchoCliente, "izquierda") + " | " + \
                            rellenar(int(monto), anchoMonto, "derecha")
                    print(linea)


def matrizInforme2(pagos, anoObjetivo):
    matriz = {}

    for fechaHora in pagos:
        registro = pagos[fechaHora]

        if "ano" in registro and "mes" in registro and "idDeporte" in registro:
            ano = registro["ano"]
            mes = registro["mes"]
            deporte = registro["idDeporte"]

            if ano == anoObjetivo:
                if deporte not in matriz:
                    matriz[deporte] = [0] * 12
                matriz[deporte][mes - 1] += 1

    return matriz


def rellenar(texto, ancho, alineacion):
    texto = str(texto)
    largo = len(texto)
    if largo >= ancho:
        return texto[:ancho]
    espacios = ancho - largo
    if alineacion == "izquierda":
        return texto + " " * espacios
    else:
        return " " * espacios + texto

def matrizInforme3(pagos, anoObjetivo):
    matriz = {}

    for fechaHora in pagos:
        registro = pagos[fechaHora]

        if "ano" in registro and "mes" in registro and "idDeporte" in registro and "monto" in registro:
            ano = registro["ano"]
            mes = registro["mes"]
            deporte = registro["idDeporte"]
            monto = registro["monto"]

            if ano == anoObjetivo:
                if deporte not in matriz:
                    matriz[deporte] = [0] * 12
                matriz[deporte][mes - 1] += monto


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
                "telefono1": 5491125456655,
                "telefono2": 5491134546589
            }
        },
        "99888777": {
            "activo": True,
            "nombre": "Nicolás",
            "apellido": "Sánchez",
            "fechaNacimiento": "02/09/2002",
            "telefonos": {
                "telefono1": 5491134560987
            }
        },
        "30456789": {
            "activo": True,
            "nombre": "María",
            "apellido": "Fernández",
            "fechaNacimiento": "15/01/1998",
            "telefonos": {
                "telefono1": 5491145671234
            }
        },
        "28543210": {
            "activo": True,
            "nombre": "Julián",
            "apellido": "Pérez",
            "fechaNacimiento": "20/05/2000",
            "telefonos": {
                "telefono1": 5491139876543,
                "telefono2": 5491123456789
            }
        },
        "32659874": {
            "activo": True,
            "nombre": "Sofía",
            "apellido": "Martínez",
            "fechaNacimiento": "03/11/2003",
            "telefonos": {
                "telefono1": 5491165432198
            }
        },
        "29547681": {
            "activo": True,
            "nombre": "Lucas",
            "apellido": "González",
            "fechaNacimiento": "28/07/1999",
            "telefonos": {
                "telefono1": 5491122223333,
                "telefono2": 5491176543210
            }
        },
        "31478562": {
            "activo": True,
            "nombre": "Camila",
            "apellido": "Rodríguez",
            "fechaNacimiento": "12/12/2001",
            "telefonos": {
                "telefono1": 5491187654321
            }
        },
        "27894561": {
            "activo": True,
            "nombre": "Martín",
            "apellido": "López",
            "fechaNacimiento": "25/06/2004",
            "telefonos": {
                "telefono1": 5491132109876,
                "telefono2": 5491198765432
            }
        },
        "30985642": {
            "activo": True,
            "nombre": "Valentina",
            "apellido": "Díaz",
            "fechaNacimiento": "09/09/1997",
            "telefonos": {
                "telefono1": 5491144445555
            }
        },
        "29765438": {
            "activo": True,
            "nombre": "Tomás",
            "apellido": "Suárez",
            "fechaNacimiento": "18/03/2005",
            "telefonos": {
                "telefono1": 5491155556666,
                "telefono2": 5491177778888
            }
        },
        "31247859": {
            "activo": True,
            "nombre": "Agustina",
            "apellido": "Romero",
            "fechaNacimiento": "30/10/2002",
            "telefonos": {
                "telefono1": 5491166667777
            }
        },
        "28965473": {
            "activo": True,
            "nombre": "Diego",
            "apellido": "Castro",
            "fechaNacimiento": "05/08/2000",
            "telefonos": {
                "telefono1": 5491133334444,
                "telefono2": 5491199990000
            }
        }
    }
    

    deportes = {
        "netball": {
            "activo": False,
            "arancel": 29000.0,
            "director principal": "Robert Lee",
            "fechasActividad": {
                "fechas1" : ["10/01/2025", "30/09/2025"]
            }
        },
        "football": {
            "activo": True,
            "arancel": 35000.0,
            "director principal": "Nicolás Medina",
            "fechasActividad": {
                "fechas1" : ["01/04/2025"]
            }
        },
        "hockey": {
            "activo": True,
            "arancel": 27000.0,
            "director principal": "Isabel Fuentes",
            "fechasActividad": {
                "fechas1" : ["14/02/2025"]
            }
        },
        "basketball": {
            "activo": True,
            "arancel": 28000.0,
            "director principal": "Isabel Martinez",
            "fechasActividad": {
                "fechas1": ["28/02/2025"],
            }
        },
        "voley": {
            "activo": True,
            "arancel": 29000.0,
            "director principal": "Thiago Ribeiro",
            "fechasActividad": {
                "fechas1": ["10/01/2025"],
            }
        },
        "jiuJitsu": {
            "activo": True,
            "arancel": 26000.0,
            "director principal": "Bruno Sosa",
            "fechasActividad": {
                "fechas1": ["05/05/2025"],
            }
        },
        "boxeo": {
            "activo": True,
            "arancel": 37000.0,
            "director principal": "Carla Vázquez",
            "fechasActividad": {
                "fechas1": ["18/03/2025"],
            }
        },
        "karate": {
            "activo": True,
            "arancel": 31000.0,
            "director principal": "Lucía Herrera",
            "fechasActividad": {
                "fechas1": ["01/06/2025"],
            }
        },
        "tennis": {
            "activo": True,
            "arancel": 28000.0,
            "director principal": "Tomás Villalba",
            "fechasActividad": {
                "fechas1": ["10/07/2025"],
            }
        },
        "natacion": {
            "activo": True,
            "arancel": 33000.0,
            "director principal": "Esteban Ríos",
            "fechasActividad": {
                "fechas1": ["25/04/2025"],
            }
        },
        "handball": {
            "activo": True,
            "arancel": 29000.0,
            "director principal": "María Elena Torres",
            "fechasActividad": {
                "fechas1": ["05/02/2025"],
            }
        },
        "rugby": {
            "activo": True,
            "arancel": 40000.0,
            "director principal": "Federico Ledesma",
            "fechasActividad": {
                "fechas1": ["15/01/2025"],
            }
        }
    }


    pagos = {
        "2025.10.15 17:34:18": {
            "idSocio": "11222333",
            "idDeporte": "tennis",
            "estadoDePago": "pagado",
            "monto": 25000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "efectivo",
        },
        "2025.10.20 14:24:48": {
            "idSocio": "99888777",
            "idDeporte": "boxeo",
            "estadoDePago": "pagado",
            "monto": 31000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "tarjeta",
        },
        "2025.10.21 10:15:32": {
            "idSocio": "30456789",
            "idDeporte": "natacion",
            "estadoDePago": "pagado",
            "monto": 32000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "efectivo",
        },
        "2025.10.22 11:45:00": {
            "idSocio": "28543210",
            "idDeporte": "football",
            "estadoDePago": "pagado",
            "monto": 30000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "tarjeta",
        },
        "2025.10.23 09:30:15": {
            "idSocio": "32659874",
            "idDeporte": "basketball",
            "estadoDePago": "pagado",
            "monto": 28000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "efectivo",
        },
        "2025.10.24 16:00:00": {
            "idSocio": "29547681",
            "idDeporte": "rugby",
            "estadoDePago": "pagado",
            "monto": 34000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "tarjeta",
        },
        "2025.10.25 13:22:45": {
            "idSocio": "31478562",
            "idDeporte": "voley",
            "estadoDePago": "pagado",
            "monto": 27000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "efectivo",
        },
        "2025.10.26 18:45:30": {
            "idSocio": "27894561",
            "idDeporte": "hockey",
            "estadoDePago": "pagado",
            "monto": 29000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "tarjeta",
        },
        "2025.10.27 12:10:50": {
            "idSocio": "30985642",
            "idDeporte": "jiuJitsu",
            "estadoDePago": "pagado",
            "monto": 28000.0,
            "ano": 2025,
            "mes": 10,
            "metodoDePago": "efectivo",
        },
        "2025.10.28 14:55:20": {
            "idSocio": "29765438",
            "idDeporte": "karate",
            "estadoDePago": "pagado",
            "monto": 26000.0,
            "ano": 2025,
            "mes": 10,
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
                    if (dniBuscar in socios.keys()):
                        print("Error, el socio ya existe.\n")
                        print(socios[dniBuscar])
                    else:
                        socios = altaSocio(socios, dniBuscar)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    listarSocios(socios)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    if (dniBuscar not in socios.keys()):
                        print("Error, el socio no existe.\n")
                    else:
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
                    print("[2] Listar deportes")
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
                    deporte = str(input("Ingresar deporte: ").lower())
                    deportes = crearDeporte(deportes, deporte)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    listaDeDeportes(deportes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    deportes = modificarDeporte(deportes)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    deportes = eliminarDeporte(deportes)

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
                    pagos = registrarPago(pagos, socios, deportes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    pagos = eliminarPago(pagos, socios)

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
                    print("[4] ...")
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
                    mes = int(time.strftime("%m"))
                    ano = int(time.strftime("%Y"))
   

                    mostrarPagosPorMesYAnio(pagos, socios, mes, ano)

                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    
                    anoIngresado = int(input("Ingrese el año para el informe (ej: 2023): "))
                    while anoIngresado < 1900 or anoIngresado > int(time.strftime("%Y")):
                        anoIngresado = int(input("Año inválido. Ingrese un año válido: "))
                        
                    matriz = matrizInforme2(pagos, anoIngresado)

    
                    anchoDeporte = 20
                    anchoMes = 4
                    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

              
                    encabezado = rellenar("Deporte", anchoDeporte, "izquierda") + " | " + " | ".join(rellenar(m, anchoMes, "derecha") for m in meses)
                    print(encabezado)
                    print("-" * len(encabezado))

         
                    for deporte in matriz:
                        fila = matriz[deporte]
                        linea = rellenar(deporte, anchoDeporte, "izquierda") + " | " + " | ".join(rellenar(valor, anchoMes, "derecha") for valor in fila)
                        print(linea)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    

                    anchoDeporte = 20
                    anchoMes = 10
                    anchoTotal = 12
                    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

                    encabezado = rellenar("Deporte", anchoDeporte, "izquierda") + " | " + " | ".join(rellenar(m, anchoMes, "derecha") for m in meses) + " | " + rellenar("TOTAL", anchoTotal, "derecha")
                    print(encabezado)
                    print("-" * len(encabezado))

                    for deporte in matriz:
                        fila = matriz[deporte]
                        total = sum(fila)
                        linea = rellenar(deporte, anchoDeporte, "izquierda") + " | " + " | ".join(rellenar(int(valor), anchoMes, "derecha") for valor in fila) + " | " + rellenar(int(total), anchoTotal, "derecha")
                        print(linea)
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...


                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
                
        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()

