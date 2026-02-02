# Estructura-de-datos1-laboratorio2

# Call Center Management System – Linked Lists in Python

## Descripción
Este proyecto implementa un sistema de gestión de llamadas para un centro de atención telefónica,
utilizando **listas enlazadas simples y listas enlazadas circulares**, aplicando conceptos de
**Programación Orientada a Objetos (POO)** en Python.

El sistema permite administrar llamadas regulares, llamadas VIP y clientes premium, simulando
un escenario real de atención al cliente con diferentes prioridades y reglas de atención.

---

## Contexto del problema
Una empresa requiere un sistema eficiente para gestionar llamadas entrantes de clientes, donde:

- Las llamadas **regulares** se atienden en orden de llegada.
- Las llamadas **VIP** tienen prioridad y se atienden primero.
- Los clientes **premium** pueden requerir atención continua mediante una lista circular.

Para resolver este problema, se diseñaron estructuras de datos dinámicas basadas en
listas enlazadas.

---

## Funcionalidades

### Llamadas regulares (Lista Enlazada Simple)
- Añadir llamadas al final de la lista.
- Eliminar llamadas atendidas.
- Buscar llamadas por ID.
- Mostrar todas las llamadas con su estado actual.

### Llamadas VIP
- Inserción prioritaria al inicio de la lista.
- Gestión mediante la misma estructura de lista enlazada simple.

### Clientes Premium (Lista Enlazada Circular)
- Añadir clientes al ciclo de atención continua.
- Eliminar clientes del ciclo.
- Recorrer la lista de forma circular.
- Buscar clientes premium por ID.

