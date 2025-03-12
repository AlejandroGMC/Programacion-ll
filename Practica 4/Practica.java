/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package practica;
public class Practica {

    // Área del círculo
    public static double calcularAreaCirculo(double radio) {
        return Math.PI * Math.pow(radio, 2);
    }
    // Área del rectángulo
    public static double calcularAreaRectangulo(double base, double altura) {
        return base * altura;
    }
    // Área del triángulo rectángulo
    public static double calcularAreaTriangulo(double base, double altura) {
        return (base * altura) / 2;
    }
    // Área del trapecio
    public static double calcularAreaTrapecio(double baseMayor, double baseMenor, double altura) {
        return ((baseMayor + baseMenor) * altura) / 2;
    }
    // Área del pentágono regular
    public static double calcularAreaPentagono(double lado, double apotema) {
        return (5 * lado * apotema) / 2;
    }
    public static void main(String[] args) {
        // Llamadas a los métodos con mensajes descriptivos
        System.out.println("El área del círculo es: " + calcularAreaCirculo(5));
        System.out.println("El área del rectángulo es: " + calcularAreaRectangulo(4, 6));
        System.out.println("El área del triángulo rectángulo es: " + calcularAreaTriangulo(3, 4));
        System.out.println("El área del trapecio es: " + calcularAreaTrapecio(6, 4, 5));
        System.out.println("El área del pentágono es: " + calcularAreaPentagono(4, 3));
    }
}
