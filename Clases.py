#Como definir una clase y definir sus Objetos}

class Profesor:
    def __init__(self, param_nombre, param_email):                                           
        self.nombre = param_nombre #referencia a si mismo (self) 
        self.email = param_email
        self.assitencia = 0
    def cambiar_nombre(self, nuevo_nombre):                                     
        self.nombre = nuevo_nombre
    def cambiar_asistencia(self):
        self.assitencia += 1


if __name__=='__main__':

    profesor_pepe = Profesor("Pepe", "pepeelmascapo420@gmail.com")
    profesor_gabriel = Profesor("Walter", "waltersitoproxd@gmail.com")
    profesor_daniel = Profesor("Daniel", "siempredelseneise@gmail.com")


    print(id(profesor_daniel))
    print (profesor_daniel.nombre)

    print(id(profesor_gabriel))
    print (profesor_gabriel.nombre)
    
    print(id(profesor_pepe))
    print (profesor_pepe.nombre)