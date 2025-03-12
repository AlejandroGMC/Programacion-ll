/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package cola;

/**
 *
 * @author USUARIO
 */
public class Cola {
    private long[] arreglo; // Arreglo para almacenar elementos
    private int inicio; // Índice del frente
    private int fin; // Índice del final
    private int n; // Capacidad máxima
    private int size; // Tamaño actual

    public Cola(int n) {
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.n = n;
        this.size = 0;
    }

    public void insertar(long e) {
        if (estaLlena()) {
            throw new RuntimeException("La cola está llena");
        }
        fin = (fin + 1) % n; // Movimiento circular
        arreglo[fin] = e;
        size++;
    }

    public long eliminar() {
        if (estaVacia()) {
            throw new RuntimeException("La cola está vacía");
        }
        long elemento = arreglo[inicio];
        inicio = (inicio + 1) % n; // Movimiento circular
        size--;
        return elemento;
    }

    public long frente() {
        if (estaVacia()) {
            throw new RuntimeException("La cola está vacía");
        }
        return arreglo[inicio];
    }

    public boolean estaVacia() {
        return size == 0;
    }

    public boolean estaLlena() {
        return size == n;
    }

    public static void main(String[] args) {
        Cola cola = new Cola(5);
        cola.insertar(10);
        cola.insertar(20);
        System.out.println("Elemento al frente: " + cola.frente()); // Imprime 10
        System.out.println("Elemento eliminado: " + cola.eliminar()); // Imprime 10
        System.out.println("¿La cola está vacía? " + cola.estaVacia()); // Debe ser false
    }
}
