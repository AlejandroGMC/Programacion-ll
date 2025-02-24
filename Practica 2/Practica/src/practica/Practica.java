/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package practica;

/**
 *
 * @author USUARIO
 */
import javax.swing.*;
import java.awt.*;
import java.awt.geom.Line2D;
import java.awt.geom.Ellipse2D;

public class Practica {
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

            public void dibujaLinea(Graphics2D g2) {
                g2.draw(new Line2D.Float(p1.x, p1.y, p2.x, p2.y));
                g2.drawString(String.format("(%.2f, %.2f)", p1.x, p1.y), p1.x, p1.y);
                g2.drawString(String.format("(%.2f, %.2f)", p2.x, p2.y), p2.x, p2.y);
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

            public void dibujaCirculo(Graphics2D g2) {
                Ellipse2D circle = new Ellipse2D.Float(centro.x - radio, centro.y - radio, radio * 2, radio * 2);
                g2.draw(circle);
                g2.drawString(String.format("(%.2f, %.2f)", centro.x, centro.y), centro.x, centro.y);
            }
        }
        JFrame frame = new JFrame("Graficos de Linea y Circulo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2 = (Graphics2D) g;

                Punto p1 = new Punto(50, 150);
                Punto p2 = new Punto(150, 200);

                Linea linea = new Linea(p1, p2);
                linea.dibujaLinea(g2);

                Circulo circulo = new Circulo(p1, 50);
                circulo.dibujaCirculo(g2);
            }
        };

        frame.add(panel);
        frame.setVisible(true);
    }
}
