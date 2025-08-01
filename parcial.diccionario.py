trabajadores = {}
class Empleados ():
    def __init__(self, nombre, departamento, antiguedad):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

class Desempeno ():
    def __init__(self, puntualidad1, equipo1, productividad1):
        self.puntualidad1 = puntualidad1
        self.equipo1 = equipo1
        self.productividad1 = productividad1
        promedio = float(puntualidad1 + equipo1 + productividad1) / 3
        return

opcion = 0
while opcion != 3:
    try :
        print("[1] Registrar empleado")
        print("[2] Registro de empleados")
        print("[3] Salir")
        opcion = int(input("Elija una opcion: "))
        if opcion in [1,2,3] :
            match opcion:
                case 1:
                    cantidad = int(input("Ingrese la cantidad de empleados que desea registrar: "))
                    for i in range(cantidad) :
                        codigo = input("Ingrese el codigo del empleado: ")
                        trabajadores[codigo] = {}
                        trabajadores[codigo]["nombre"]=input("Ingrese el nombre del empleado: ")
                        trabajadores[codigo]["departamento"] = input("Ingrese el departamento del empleado: ")
                        trabajadores[codigo]["antiguedad"]=int(input("Ingrese la antiguedad del empleado: "))
                        print("\nCalificacion de empleado")
                        trabajadores[codigo]["puntuacion"]={}
                        codigo_puntuacion = input("Ingrese el codigo de puntuacion: ")
                        puntualidad = float(input("Ingrese la puntuacion de la puntualidad: "))
                        equipo = float(input("Ingrese la puntuacion del trabajo en equipo: "))
                        productividad = float(input("Ingrese la puntuacion de la productividad: "))
                        trabajadores[codigo]["puntuacion"][codigo_puntuacion] ={
                            "puntualidad" : puntualidad,
                            "equipo" : equipo,
                            "productividad" : productividad
                        }
                        print("\n contacto")
                        trabajadores[codigo]["contacto"]={}
                        codigo_contacto = input("Ingrese el codigo del contacto: ")
                        telefono = int(input("Ingrese el telefono del empleado "))
                        correo = input("Ingrese el correo del empleado: ")

                        trabajadores[codigo][codigo_contacto] = {
                            "telefono" : telefono,
                            "correo" : correo
                        }
                        print("Informacion guardada")
                case 2:
                    print("Informacion guardada")
                    for codigo,datos1 in trabajadores.items():
                        print(f"\nNombre: {datos1["nombre"]}")
                        print(f"Departamento: {datos1["departamento"]}")
                        print(f"Antiguedad: {datos1["antiguedad"]}")
                        print("\nPuntuacion")
                        for codigo_puntuacion, datos2 in datos1["puntuacion"].items():
                            print(f"Puntuacion: {datos2["puntualidad"]}")
                            print(f"Correo: {datos2["equipo"]}")
                            print(f"Correo: {datos2["productividad"]}")
                            promedio = (datos2["productividad"] + datos2["equipo"] + datos2["productividad"])/3
                            print("Promedio de empleado: ", promedio)
                            if promedio >= 7 :
                                print("Desempeño satisfactorio")
                            elif promedio < 7 :
                                print("Debe mejorar")

                            for codigo_contacto, datos3 in datos1["contacto"].items():
                                print(f"Contacto: {datos3["telefono"]}")
                                print(f"Correo: {datos3["correo"]}")
                case 3 :
                    print("SALIENDO DEL MENÚ...")

        else:
            print("Opcion no valida")
    except ValueError:
        print("Ingrese un numero entero")
    if opcion!=3:
        print("Presione Enter para volverlo a intentar o elejir otra opción")
        input()
