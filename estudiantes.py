class Persona():
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.asistencia = 0
    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    def __init__(self,nombre,email,nro_prof):
        super().__init__(nombre,email)
        self.nro_prof = nro_prof

class Alumno(Persona):
    def __init__(self, nombre, email,legajo):
        self.legajo = legajo
        super().__init__(nombre,email)
        self.materias_cursando = []
    def agregar_materia(self,materia):
        self.materias_cursando.append(materia)

class Materia:
    def __init__(self,cod, nombre,carga):
        self.codigo = cod
        self.nombre = nombre
        self.carga = carga
    def __repr__(self) -> str:
        return "Materia: " + self.nombre


#objetos

profesor_pepe = Profesor("Pepe","jose@um.edu.ar","2787")
profesor_walter = Profesor("Walter","dff","134")
profesor_daniel = Profesor("Daniel","fdg","346")
alumno1 = Alumno("Lucas Crosta", "lucas.crosta@gmail.com", 62003)
materia_1 = Materia("0001", "calculo","6hs")
alumno1.agregar_materia(materia_1)

print(repr(alumno1.materias_cursando))
print(alumno1.legajo)
print(alumno1.nombre)
print(alumno1.email)
print(materia_1.nombre)
print("el nombre es: ",profesor_pepe.nombre)
print("el email es: ",profesor_pepe.email)
print("la asistencia es: ",profesor_pepe.asistencia)
print("el profesor fue a clase ")
profesor_pepe.asistencia_clase()
print("la asistencia es: ",profesor_pepe.asistencia)
print(profesor_walter.nombre)
print(profesor_daniel.nombre)

profesor_pepe.cambiar_nombre("Jose")
print(profesor_pepe.nombre)