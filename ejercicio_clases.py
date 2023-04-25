class Persona:
    pass




class Alumno(Persona):#Alumno hereda de la clase persona
    def __init__(self, param_nombre,_param_apellido,param_DNI,param_Legajo,param_Tel,para_email,param_direccion):
        self.nombre = param_nombre
        self.apellid = _param_apellido
        self.DNI = param_DNI
        self.Legajo = param_Legajo
        self.Tel = param_Tel
        self.email = para_email
        self.direccion = param_direccion


class Materia:
    def __init__(self, param_nombremat, param_idmat, param_horario,param_duracion,):
        self.nombremat = param_nombremat
        self.idmat = param_idmat
        self.horario = param_horario
        self.duracion = param_duracion



class Profesor:
    def __init__ (self,param_profid,param_nombreprof,param_apellido,param_email,param_telefono):
        self.idProf = param_profid
        self.nombreprof = param_nombreprof
        self.apellido = param_apellido
        self.email = param_email
        self.telefono = param_telefono


if __name__ == '__main__':
    alumno_vicente = Alumno ("Vicente", "Cara Tapia", 44909938, 65432, "299-656-3936","vit.cara@alumno.um.edu.ar", "Los Copihues 135")
    alumno_tomas = Alumno ("Tomas", "Rojas", 44909934, 65789, "299-656-3936", "t.rojas@alumno.um.edu.ar", "Colonia Cebolla 1600")
    materia_CalculoI = Materia ("Calculo I", 4567, "Lunes y Miercoes a las 3pm a 5", "semestral")
    materia_Algebra = Materia ("Algebra Analítica", 4587,  "Martes a las 3pm a 7", "anual")
    profe_Tomas = Profesor (4321, "Tomas", "Schugurensky", "elmontedeshugoslavia@edu.ar", "261-435-1231")
    profe_Franco = Profesor (4323, "Franco", "Garcia", "franquilloproxdomg@gmail.com", "261-123-4123")