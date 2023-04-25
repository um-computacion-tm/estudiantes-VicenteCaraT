class Persona:
    pass




class Alumno(Persona):#Alumno hereda de la clase persona
    def __init__(self, param_nombre,_param_apellido,param_DNI,param_Legajo,param_Tel,para_email,param_direccion):
        self.nombre = param_nombre
        self.apellido = _param_apellido
        self.DNI = param_DNI
        self.Legajo = param_Legajo
        self.Tel = param_Tel
        self.email = para_email
        self.direccion = param_direccion


class Materia:
    def __init__(self, param_nombre, param_idmat, param_horario,param_duracion,):
        self.nombre = param_nombre
        self.idmat = param_idmat
        self.horario = param_horario
        self.duracion = param_duracion



class Profesor:
    def __init__ (self,param_profid,param_nombre,param_apellido,param_email,param_telefono):
        self.idProf = param_profid
        self.nombre = param_nombre
        self.apellido = param_apellido
        self.email = param_email
        self.telefono = param_telefono


if __name__ == '__main__':
    alumno_vicente = Alumno ("Vicente", "Cara Tapia",  '44909938',  '65432', "299-656-3936","vit.cara@alumno.um.edu.ar", "Los Copihues 135")
    print('Alumno: ' + alumno_vicente.nombre)
    print('Apellido: ' + alumno_vicente.apellido)
    print('D.N.I: ' + alumno_vicente.DNI)
    print('Legajo: ' + alumno_vicente.Legajo)
    print('teléfono: ' + alumno_vicente.Tel)
    print('Email: ' + alumno_vicente.email)
    print('Direccion: ' + alumno_vicente.direccion)


    materia_CalculoI = Materia ("Calculo I", '4567', "Lunes y Miercoes a las 3pm a 5pm", "Semestral")
    print('Nombre de Materia: ' + materia_CalculoI.nombre)
    print('IdMateria: ' + materia_CalculoI.idmat)
    print('Horario: ' + materia_CalculoI.horario)
    print('Duracion: ' + materia_CalculoI.duracion)


    profe_Tomas = Profesor ('4321', "Tomas", "Schugurensky", "elmontedeshugoslavia@edu.ar", "261-435-1231")
    print('idProfe: ' + profe_Tomas.idProf)
    print('Nombre: ' + profe_Tomas.nombre)
    print('Apellido: ' + profe_Tomas.apellido)
    print('Emaio: ' + profe_Tomas.email)
    print('Teléfono: ' + profe_Tomas.telefono)
