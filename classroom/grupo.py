

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:
    
    grado = None
    def __init__(self, grupo="grupo ordinado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self.grado= "grado 12 "
        



    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))
    
    def agregarAlumno(self, alumno, lista=[]):
       
        if (lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
            
        else:
           self.listadoAlumnos = [alumno]
           self.listadoAlumnos = self.listadoAlumnos + lista
          

    def __str__(self):
      hay="Grupo de estudiantes: grupo predeterminado "
      return hay

  #  @ classmethod
   # def asignarNombre(cls, nombre="Grado 12"):
     #   cls.grado = nombre

  #  @ classmethod
    #def asignarNombre(cls, nombre="Grado 6"):
     #   cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
