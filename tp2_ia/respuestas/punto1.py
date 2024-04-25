def search(start, stop):
    """
    : param start : estado inicial
    : param stop : test objetivo
    trajectory () nos devuelve el recorrido al nodo
    """
    frontera = deque()  # crea una cola doblemente terminada para manejar la frontera.
    explored = set()  # crea un conjunto para manejar los nodos explorados.
    if (stop(start)):  # comprueba que el estado inicial es o no una solución.
        # en caso de que el estado inicial sea solución se devuelve el recorrido al estado inicial.
        return trajectory(start)
    frontera.append(start) # añade el estado inicial a la frontera.
    while (frontera): # mientras haya nodos en la frontera:
        nodo = frontera.popleft() # saca el primer nodo guardado en la frontera. (FIFO)
        explored.add(nodo) # añade el nodo a los nodos explorados
        for child in nodo.expand(): # expande cada uno de los hijos del nodo
            if stop(child): # comprueba que el hijo que se está expandiendo del nodo es un estado solución.
                return trajectory(child) # si el nodo hijo es estado solución se devuelve el camino hasta el nodo.
            elif not child in explored: # si el nodo hijo no es solución, comprueba que no se encuentre dentro de los nodos explorados.
                frontera.append(child) # si no se encuentra en los nodos explorados lo añade a la frontera.
    return None # en caso de que no se encuentre una solución falla.

# Punto b)
# El código corresponde a una búsqueda primero en anchura.

# Punto c)
''' 
Para implementar la búsqueda primero en profundidad,
hay que manejar la frontera como una pila o cola LIFO,
para ello en el código habría que cambiar la llamada al método popLeft()
que saca el primer nodo que ingresó a la frontera
por la llamada al método pop() para sacar el último nodo que ingresó a la frontera.
'''