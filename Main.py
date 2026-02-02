#Representa una llamada con los atributos:
# - ID: identificador único de la llamada.
# - nombre: nombre asociado a la llamada.
# - prioridad: prioridad de la llamada.
# - estado: estado actual de la llamada (por ejemplo, "activa" o "finalizada").
class Llamada:
    def __init__(self,ID, nombre, prioridad, estado):
        self.ID=ID
        self.nombre=nombre
        self.prioridad=prioridad
        self.estado=estado
#Nodo individual que contiene un objeto Llamada. Cada nodo tiene:
# - llamada: instancia de Llamada.
# - next: puntero al siguiente nodo en la lista.
class Nodo_Llamada:
    def __init__(self,llamada):
        self.llamada=llamada
        self.next=None
#Lista enlazada de llamadas, contiene métodos para manipular y gestionar las llamadas en la lista.
class Lista_Llamada:
    def __init__(self):
        self.head=None
    #Inserta una llamada al final de la lista.
    def insertar(self,llamada):
        nuevo_nodo=Nodo_Llamada(llamada)
        if not self.head:
            self.head=nuevo_nodo
        else:
            actual=self.head
            while actual.next:
                actual=actual.next
            actual.next=nuevo_nodo
        print("Llamada añadida con exito")
    #Elimina una llamada de la lista por su ID.
    def eliminar(self, ID):
        actual=self.head
        anterior=None
        while actual:
            if actual.llamada.ID==ID:
                if anterior:
                    anterior.next=actual.next
                else:
                    self.head=actual.next
                print(f"Llamada con ID {ID} eliminada")
                return
            anterior=actual
            actual=actual.next
        print(f"Llamada con id {ID} no encontrada")
    #Muestra todas las llamadas en la lista
    def mostrar(self):
        actual=self.head
        print("Lista de las llamadas en la lista:")
        while actual:
            print(f"- ID:{actual.llamada.ID}, nombre:{actual.llamada.nombre}, prioridad:{actual.llamada.prioridad}, estado:{actual.llamada.estado}")
            actual=actual.next
    #Busca y muestra los detalles de una llamada por su ID.
    def buscar_ID(self, ID):
        actual=self.head
        while actual:
            if(actual.llamada.ID==ID):
                print(f"Información de la llamada. ID:{actual.llamada.ID}, nombre:{actual.llamada.nombre}, prioridad:{actual.llamada.prioridad}, estado:{actual.llamada.estado}")
                return
            actual=actual.next
        print(f"Llamada con ID {ID} no encontrada en la lista de clientes regulares o VIP")
    #Verifica si una llamada con el ID especificado existe en la lista.
    def verificar_ID(self, ID):
        actual=self.head
        while actual:
            if(actual.llamada.ID==ID):
                return True
            actual=actual.next
        return False
    #Cambia el estado de la llamada a "finalizada".
    def marcar_llamada_atendida(self,ID):
        actual=self.head
        while actual:
            if actual.llamada.ID==ID:
                actual.llamada.estado="finalizada"
                print(f"llamada con ID {ID} marcada como finalizada. ")
                return
            actual=actual.next
        print(f"llamada con ID {ID} no encontrada")
    #Inserta una llamada al inicio de la lista
    def insertar_al_inicio(self, llamada):
        nuevo_nodo = Nodo_Llamada(llamada)
        nuevo_nodo.next = self.head  # El siguiente del nuevo nodo es el actual head
        self.head = nuevo_nodo       # Actualizamos el head para que apunte al nuevo nodo
        print("Llamada añadida al inicio con éxito")
    #Elimina todas las llamadas con el estado "finalizada" de la lista.
    def eliminar_finalizadas(self):
        actual = self.head
        while actual:
            if actual.llamada.estado == "finalizada":
                Lista_Llamada.eliminar(actual.llamada.ID)
            actual = actual.next
   #Verifica si la lista está vacia, retorna true si está vacia, en caso contrario retorna false
    def esta_vacia(self):
        return self.head is None
#Representa una llamada de tipo premium con atributos:
# - ID: identificador único de la llamada.
# - nombre: nombre asociado a la llamada.
# - prioridad: nivel de prioridad de la llamada.
# - estado: estado actual de la llamada (por ejemplo, "activa" o "finalizada").
class LlamadaPremium:
    def __init__(self, ID, nombre, prioridad, estado):
        self.ID=ID
        self.nombre=nombre
        self.prioridad=prioridad
        self.estado=estado
#Nodo individual en la lista circular que contiene un objeto LlamadaPremium y un puntero al siguiente nodo.
class Nodo_premium:
    def __init__(self,llamadaPremium):
        self.llamadaPremium=llamadaPremium
        self.next=None
#Estructura de lista enlazada circular para administrar llamadas premium, con métodos para insertar, eliminar, buscar, y modificar llamadas.
class Lista_Llamada_Circular:
    def __init__(self):
        self.head=None
    #Inserta una llamada premium al final de la lista circular
    def insertar(self, llamadaPremium):
        nuevo_nodo=Nodo_premium(llamadaPremium)
        if not self.head:
            self.head=nuevo_nodo
            nuevo_nodo.next=self.head
        else:
            actual=self.head
            while actual.next!=self.head:
                actual=actual.next
            actual.next=nuevo_nodo
            nuevo_nodo.next=self.head
    #Verifica si una llamada con el ID especificado existe en la lista circular, se usa en la opcion 1
    def verificar_circular_ID(self, ID):
        if not self.head:
            return False
        actual = self.head
        while True:
            if actual.llamadaPremium.ID == ID:
                return True
            actual = actual.next
            if actual == self.head:
                break
        return False
    #Elimina todas las llamadas con el estado "finalizada" en la lista circular.
    def eliminar_circular_finalizadas(self):
        if not self.head:
            return
        actual = self.head
        while True:
            if actual.llamadaPremium.estado == "finalizada":
                Lista_Llamada_Circular.eliminar(actual.llamadaPremium.ID)
            actual = actual.next
            if actual == self.head:
                break
    # Elimina una llamada premium con el ID especificado de la lista circular
    def eliminar(self, ID):
        if not self.head:
            return
        actual=self.head
        anterior=None
        while True:
            if actual.llamadaPremium.ID==ID:
                if anterior:
                    anterior.next=actual.next
                else:
                    ultimo=self.head
                    while ultimo.next!=self.head:
                        ultimo=ultimo.next
                    if ultimo==self.head:
                        self.head=None
                    else:
                        self.head=actual.next
                        ultimo.next=self.head
                return
            anterior=actual
            actual=actual.next
            if actual==self.head:
                break
    #Muestra todas las llamadas en la lista circular.
    def mostrar(self):
        if not self.head:
            return "La lista está vacía"
        actual=self.head
        while True:
            print(f"- ID:{actual.llamadaPremium.ID}, nombre:{actual.llamadaPremium.nombre}, prioridad:{actual.llamadaPremium.prioridad}, estado:{actual.llamadaPremium.estado}")
            actual=actual.next
            if actual==self.head:
                break
        print("(De vuelta al inicio)")
#Esta posiblemente se tenga que borrar porque con la lista circular preguntaremos el estado de la primera
    def marcar_llamada_atendida_circular(self, ID):
        if not self.head:
            return "La lista está vacía"
        actual=self.head
        while True:
            if(actual.llamadaPremium.ID==ID):
                actual.llamadaPremium.estado="finalizada"
                print(f"llamada con ID {ID} marcada como finalizada. ")
                return
            actual=actual.next
            if actual==self.head:
                break
        print(f"llamada con ID {ID} no encontrada")
    #Busca y muestra los detalles de una llamada premium en la lista circular por su ID.
    def buscar_circular_ID(self, ID):
        if not self.head:
            return f"Llamada con ID {ID} no encontrada en la lista de clientes Premium"
        actual=self.head
        while True:
            if(actual.llamadaPremium.ID==ID):    
                print(f"Información de la llamada. ID:{actual.llamadaPremium.ID}, nombre:{actual.llamadaPremium.nombre}, prioridad:{actual.llamadaPremium.prioridad}, estado:{actual.llamadaPremium.estado}")
                return
            actual=actual.next
            if actual==self.head:
                break
        print(f"Llamada con ID {ID} no encontrada en la lista de clientes regulares o VIP")
    #Acá se trabaja la cabeza de la lista circular para preguntarle al usuario su estado y si es finalizado, entonces se elimina, sino entonces se pasa a lo ultimo de la lista
    def verificar_estado_primera_llamada(self):
        if not self.head:
            print("La lista está vacía")
            return
        actual = self.head
        print(f"Primera llamada - ID:{actual.llamadaPremium.ID}, Nombre:{actual.llamadaPremium.nombre}, Estado actual:{actual.llamadaPremium.estado}")
        nuevo_estado = input("Ingrese el nuevo estado de esta llamada: ")
        if nuevo_estado.lower() == "finalizada":
            # Eliminar la llamada si el estado es "finalizada"
            self.eliminar(actual.llamadaPremium.ID)
            print(f"Llamada con ID {actual.llamadaPremium.ID} eliminada.")
        else:
            # Actualizar el estado y moverla al final si no es "finalizada"
            actual.llamadaPremium.estado = nuevo_estado
            self.head = self.head.next  # Cambiar la cabeza al siguiente nodo
            print(f"Llamada con ID {actual.llamadaPremium.ID} movida al final de la lista con estado actualizado.")
    #Verifica si la lista circular esta vacia
    def esta_vacia(self):
        return self.head is None    
#Procedimientos para el funcionamiento del menú
###########################################################3
#- Solicita al usuario el tipo de cliente (regular, VIP o Premium).
#- Realiza una validación para asegurarse de que el tipo de cliente sea uno de los valores esperados. En caso de error, solicita nuevamente la entrada.
#- Devuelve el tipo de cliente seleccionado.
def preguntar_tipo_llamada():
    sw=True
    while(sw):
        tipo=input("Diga qué clase de cliente, puede ser regular, VIP o Premium: ")
        if(tipo=="regular" or tipo=="VIP" or tipo=="Premium"):
            sw=False
        else:
            print("¡Prioridad mal escrita!")
            sw=True
    return tipo
# - Crea una llamada (regular/VIP o premium) con un ID, nombre y estado proporcionados por el usuario.
# - Valida que el ID sea un número positivo, que el nombre contenga solo letras, y que el estado sea uno de los valores permitidos.
# - Verifica también que el ID no exista ya en las listas regular o circular.
# - Dependiendo del tipo de cliente (prioridad), crea una instancia de la clase Llamada o LlamadaPremium y la devuelve.
def crear_llamada(prioridad):
    sw=True
    while(sw):
        try:
            ID=int(input("Diga el ID: "))
            sw=False
            if(ID<=0):
                print("¡El ID no puede ser negativo o cero!")
                sw=True
            elif(Lista_Llamada.verificar_ID(ID)):
                print("¡El ID ya se encuentra en la lista regular!")
                sw=True
            elif(Lista_Llamada_Circular.verificar_circular_ID(ID)):
                print("¡El ID ya se encuentra en la lista Circular!")
                sw=True
        except:
            print("¡ID mal digitado!")
            sw=True
    sw=True
    while(sw):
        nombre=input("Diga el nombre del cliente:")
        if(all(parte.isalpha() for parte in nombre.split())):
            sw=False
        else:
            print("¡Nombre incorrecto!")
            sw=True
    sw=True
    while(sw):
        estado=input("Diga el estado de la llamada, puede ser pendiente, en proceso, finalizada: ")
        if(estado=="pendiente" or estado=="proceso" or estado=="finalizada"):
            sw=False
        else:
            print("¡Prioridad mal escrita!")
            sw=True
    if(prioridad=="regular" or prioridad=="VIP"):    
        nuevo_objeto_llamada=Llamada(ID, nombre, prioridad, estado)
    else:
        nuevo_objeto_llamada=LlamadaPremium(ID, nombre, prioridad, estado)
    return nuevo_objeto_llamada
#Acá se hace el procedimiento para la opcion dos donde se cambian el estado de las llamadas. en caso de la lista 1
#se se pregunta el ID de la llamada que se desea manejar y en la lista 2 se mira solo la primera llamada con la funcion 
#"verificar_estado_primera_llamada" que corresponde a la clase Llamada_Premium
def opcion2():
    sw=True
    while(sw):
        opcion2=input("""Si desea modificar la lista de clientes regulares y VIP, escriba (lista1)
Si desea modificar la lista de clientes premium escriba (lista2)
Respuesta: """)
        if(opcion2=="lista1" or opcion2=="lista2"):
            sw=False
        else:
            print("¡Nombre incorrecto!")
            sw=True
    if(opcion2=="lista1"):
        sw=True
        while(sw):
            try:
                ID=int(input("Diga el ID de la llamada que desea poner como finalizada: "))
                sw=False
                if(ID<=0):
                    print("¡El ID no puede ser negativo o cero!")
                    sw=True
            except:
                print("¡ID mal digitado!")
                sw=True
        veri1=Lista_Llamada.verificar_ID(ID)
        if(veri1):
            Lista_Llamada.marcar_llamada_atendida(ID)
        else:
            print("El ID suministrado no está en la lista 1, puede que ya haya sido finalizada y borrada o nunca hubo llamada con ese ID")
    elif(opcion2=="lista2"):
        Lista_Llamada_Circular.verificar_estado_primera_llamada()
        
#Inicialización de las listas de llamadas
Lista_Llamada = Lista_Llamada()
Lista_Llamada_Circular=Lista_Llamada_Circular()
## Estos bloques son para el menú
# Menú principal: Controla la interacción del usuario con las opciones disponibles para gestionar las llamadas
repetir_proceso=True  #Controla si el usuario desea realizar más de una operación
mal_digitado=True   #Controla la validez de la opción del menú ingresada
while(repetir_proceso==True):  
    while(mal_digitado==True):   # Solicita al usuario la selección de una opción del menú hasta que se ingrese una válida
        try:
            mal_digitado=False
            print("Digite la acción que desea realizar")
            opcion=int(input("""1-Añadir
2-Modificar los estados de las llamadas al principio de cada lista.
3-Eliminar las llamadas finalizadas
4-Mostrar
5-Buscar
Digite la acción que desea: """))
            if(opcion<1 or opcion>5):  # Valida que la opción esté dentro del rango permitido
                mal_digitado=True
                print("¡Opción del menú mal digitada!")
            else:
                repetir_proceso=False   #si es una opcion valida entonces deja de preguntar las opciones del menú
        except:
            print("Opción del menú mal digitada")
            mal_digitado=True
    
    #Aquí va el desarrollo de las opciones
    if(opcion==1):    # Opción 1: Añadir una nueva llamada según el tipo de cliente (regular, VIP o Premium)
        prioridad=preguntar_tipo_llamada()  # Se obtiene el tipo de llamada
        if(prioridad=="regular" or prioridad=="VIP"):
            llamada=crear_llamada(prioridad)   # Crea una instancia de llamada con los datos 
            if(prioridad=="regular"):
                Lista_Llamada.insertar(llamada)  # Inserta en la lista regular
            else:
                Lista_Llamada.insertar_al_inicio(llamada) # Inserta en la lista regular en la primera posición(en la cabeza)
        else:
            llamada=crear_llamada(prioridad) 
            Lista_Llamada_Circular.insertar(llamada)  # Inserta en la lista circular de Premiums
    elif(opcion==2):
        opcion2() #Se usa la funcion creada para esta opcion
    elif(opcion==3):  #Elimina las llamadas con estado "finalizada" de ambas listas
        Lista_Llamada.eliminar_finalizadas()  
        Lista_Llamada_Circular.eliminar_circular_finalizadas()
    elif(opcion==4):
        #Se pregunta qué lista desea mostrar
        sw=True
        while(sw):
            lista=input("""- Si desea que se le muestre la lista de clientes regulares y VIP, escriba lista1
- Si desea que se le muestre la lista de clientes Premium escriba lista2
respuesta: """)
            if(lista=="lista1" or lista=="lista2"):
                sw=False
            else:
                print("¡Opción mal escrita!")
                sw=True
        
        if(lista=="lista1" and Lista_Llamada.esta_vacia()==False): #verifica si hay que mostrar la lista de clientes regulares y VIP y verifica que no esté vacia
            Lista_Llamada.mostrar()
        elif(lista=="lista2" and Lista_Llamada_Circular.esta_vacia()==False): #verifica si hay que mostrar la lista Premium y verifica que no esté vacia
            Lista_Llamada_Circular.mostrar()
        else:
            print("La Lista está vacía") #En caso de que no caiga en los condicionales, es porque está vacia la lista 1 o 2 dependiendo
            #de cual pregunten
    elif(opcion==5):
        #Se pregunta por el ID de la llamada que desea visualizar
        sw=True
        while(sw):
            try:
                ID=int(input("Diga el ID: "))
                sw=False
                if(ID<=0):
                    print("¡El ID no puede ser negativo o cero!")
                    sw=True
            except:
                print("¡ID mal digitado!")
                sw=True
        #Ambas funciones buscan la llamada e imprime su información. En caso dado no esté en la lista1 o lista2, lo dice.
        Lista_Llamada.buscar_ID(ID) 
        Lista_Llamada_Circular.buscar_circular_ID(ID)
    # Pregunta al usuario si desea realizar otra acción
    if(mal_digitado==False):
        mal_digitado_repetir=True
        while(mal_digitado_repetir):
            try:
                opcion_repetir=int(input("""¿Desea realizar otro proceso? Si la respuesta es "si" digite 1, si es "no" digite 2: """))
                mal_digitado_repetir=False
                if(opcion_repetir==1):
                    repetir_proceso=True
                    mal_digitado=True
                elif(opcion_repetir==2):
                    print("¡Fin del programa!. Muchas gracias por usarlo")
                    repetir_proceso=False
                else:
                    mal_digitado_repetir=True
                    print("¡Opción mal digitada!")
                
            except:
                print("¡Opción mal digitada!")
                mal_digitado_repetir=True