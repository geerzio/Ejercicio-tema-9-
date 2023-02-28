#Crea una clase Persona con las siguientes variables:
#La edad
#El nombre
#El teléfono
#Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, 
#esta nueva clase tendrá la variable credito solo para esa clase.
#Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, 
#tienes que darles valor y mostrarlas por pantalla.
#Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y
#con una variable salario que solo tenga la clase Trabajador

class Persona():
    def __init__(self,nombre,edad,telefono):
        self.name = nombre
        self.age = edad
        self.num = telefono
        
        
        
class Cliente(Persona):
    def __init__(self, nombre, edad, telefono,credito):
        super().__init__(nombre, edad, telefono)
        self.credit = credito    
        
    def mostrar(self):
        print(f"Hola soy,{self.name}, tengo {self.age} años, mi telefono es: {self.num}. Y tengo un credito de {self.credit}%")    
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, telefono,salario):
        super().__init__(nombre, edad, telefono)
        self.moneda = salario        

    def mostrar(self):
        print(f"Hola soy,{self.name}, tengo {self.age} años, mi telefono es: {self.num}. Y tengo un salario de $ {self.moneda}")    
pepe = Cliente("Pepe",28,1532612712,50)
pepe.mostrar()

juan = Trabajador("Juan",35,46415352,30.000)
juan.mostrar()