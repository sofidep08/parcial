trabajadores = {}
class Empleados ():
    def __init__(self, nombre, departamento, antiguedad):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad


opcion = 0
while opcion != 3:
    try :
        print("[1] Registrar empleado")
        print("[2] Buscar empleado por codigo")
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

        else:
            print("Opcion no valida")
    except ValueError:
        print("Ingrese un numero entero")
    if opcion!=4:
        print("Presione Enter para volverlo a intentar o elejir otra opción")
        input()
