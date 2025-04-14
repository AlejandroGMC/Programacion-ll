/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.a;

/**
 *
 * @author USUARIO
 */
class A {
    protected int x;
    protected int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        x++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

class B {
    protected int y;
    protected int z;

    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

class D {
    private A a;
    private B b;

    public D(int x, int y, int z) {
        a = new A(x, z);
        b = new B(y, z);
    }

    public void incrementaXYZ() {
        a.x++;
        b.y++;
        a.z++; // o b.z++, ya que z es común
    }

    public void mostrarValores() {
        System.out.println("x: " + a.x + ", y: " + b.y + ", z: " + a.z);
    }
}

// Ejemplo de uso
public class Main {
    public static void main(String[] args) {
        D d = new D(1, 2, 3);
        d.incrementaXYZ();
        d.mostrarValores();
    }
}
