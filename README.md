
Santiago Usme - 201822047
Jesús Ospino - 201915195

Reflexión:

Dado que en el requerimiento 1 se usaba un árbol BST, el cual no necesariamente está balanceado, el tiempo de respuesta
era mayor que el requerimiento 2 en el cual se usa un árbol RBT. Si bien el RBT tarda un poco más de tiempo que el BST en formarse, 
tiene menor complejidad temporal a la hora de dar respuesta al usuario, dada su altura menor a la BST. 

# Lab5_202010

Este repositorio contiene una plantilla del laboratorio 5 con un ejemplo de un ADT mapa ordenado que está implementado sobre un árbol rojo y negro (RBT). La aplicación está construida bajo el patrón Modelo-Vista-Controlador que carga datos y realiza consultas usando las estructuras de datos implementadas. Para iniciar la aplicación debe ejecutar: 
```
python App/view.py
```
*	ADT: archivos Python con la definición de los Tipos Abstractos de Datos.
*	App: aplicación Python cliente que usa las ADTs y ordenamientos para dar solución a laboratorios y retos.
    * view.py: Es el punto de entrada de la aplicación, y se encarga de la entrada y salida de datos, e interacción con el usuario
    * controller.py: Comunica la vista con el modelo a través de las operaciones invocadas por el usuario desde la vista
    * model.py: Representa el modelo del mundo.
*	Data: archivos con los datos (csv, json, txt, etc) usados en el laboratorio o reto. El contenido de esta carpeta NO se debe versionar.
*	DataStructures: archivos Python con las estructuras de datos básicas (bst y rbt).
*	Sorting: archivos Python que implementan los algoritmos de ordenamiento.
*	Test: pruebas unitarias en Python para validar el código desarrollado.

![Modelo-Vista-Controlador](http://sistemasproyectos.uniandes.edu.co/iniciativas/architlab/wp-content/uploads/sites/7/2020/02/MVC.png)
