/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package punto1;

/**
 *
 * @author USUARIO
 */
public class Main {
    public static void main(String[] args) {
        class Punto {
            public float x;
            public float y;

            public Punto(float x, float y) {
                this.x = x;
                this.y = y;
            }

            public float[] coord_cartesianas() {
                return new float[]{this.x, this.y};
            }

            public float[] coord_polares() {
                float radio = (float) Math.sqrt(this.x * this.x + this.y * this.y);
                float angulo = (float) Math.atan2(this.y, this.x);
                angulo = (float) Math.toDegrees(angulo);
                return new float[]{radio, angulo};
            }

            @Override
            public String toString() {
                return String.format("(%.2f, %.2f)", this.x, this.y);
            }
        }

        class Linea {
            public Punto p1;
            public Punto p2;

            public Linea(Punto p1, Punto p2) {
                this.p1 = p1;
                this.p2 = p2;
            }

            @Override
            public String toString() {
                return "Linea desde " + p1 + " hasta " + p2;
            }

            public void dibujaLinea() {
                System.out.println(this);
            }
        }

        class Circulo {
            public Punto centro;
            public float radio;

            public Circulo(Punto centro, float radio) {
                this.centro = centro;
                this.radio = radio;
            }

            @Override
            public String toString() {
                return "Circulo con centro en " + centro + " y radio de " + radio;
            }

            public void dibujaCirculo() {
                System.out.println(this);
            }
        }

        // Ejemplo de uso de Punto
        Punto p1 = new Punto(0, 3);
        Punto p2 = new Punto(3, 4);
        System.out.println(p1);
        float[] a = p1.coord_cartesianas();
        System.out.println(a[0] + " " + a[1]);
        float[] b = p1.coord_polares();
        System.out.println(b[0] + " " + b[1]);

        // Ejemplo de uso de Linea
        Linea linea = new Linea(p1, p2);
        linea.dibujaLinea();

        // Ejemplo de uso de Circulo
        Circulo circulo = new Circulo(p1, 5);
        circulo.dibujaCirculo();
    }
}
