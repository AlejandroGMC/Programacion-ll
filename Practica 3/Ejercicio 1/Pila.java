/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pila;

/**
 *
 * @author USUARIO
 */
public class Pila {
    private long[] arreglo; // Almacena los elementos de la pila
    private int top; // Índice del elemento superior
    private int n; // Capacidad máxima de la pila

    public Pila(int n) {
        this.arreglo = new long[n];
        this.top = -1; // Inicialmente la pila está vacía
        this.n = n;
    }

    public void push(long e) {
        if (isFull()) {
            throw new RuntimeException("La pila está llena");
        }
        arreglo[++top] = e; // Incrementar top y agregar elemento
    }

    public long pop() {
        if (isEmpty()) {
            throw new RuntimeException("La pila está vacía");
        }
        return arreglo[top--]; // Retornar elemento y decrementar top
    }

    public long peek() {
        if (isEmpty()) {
            throw new RuntimeException("La pila está vacía");
        }
        return arreglo[top]; // Retorna el elemento superior sin eliminarlo
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args) {
        Pila pila = new Pila(5);
        pila.push(10);
        pila.push(20);
        System.out.println("Elemento superior: " + pila.peek()); // Debe imprimir 20
        System.out.println("Elemento eliminado: " + pila.pop()); // Debe imprimir 20
        System.out.println("¿La pila está vacía? " + pila.isEmpty()); // Debe ser false
    }
}
