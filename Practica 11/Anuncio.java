/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package anuncio;


import java.util.ArrayList;
import java.util.List;

// Clase Anuncio
class Anuncio {
    private int numero;
    private double precio;
    public Anuncio(int numero, double precio) {
        this.numero = numero;
        this.precio = precio;
    }
    public double getPrecio() { return precio; }
    public void setPrecio(double precio) { this.precio = precio; }
    @Override
    public String toString() {
        return "Anuncio [Nº=" + numero + ", Precio=$" + precio + "]";
    } }
// Clase Artista
class Artista {
    private String nombre;
    private int aniosExperiencia;
    public Artista(String nombre, String ci, int aniosExperiencia) {
        this.nombre = nombre;
        this.aniosExperiencia = aniosExperiencia;
    }
    public String getNombre() { return nombre; }
    public int getAniosExperiencia() { return aniosExperiencia; }
    @Override
    public String toString() {
        return nombre + " (" + aniosExperiencia + " años)";
    } }
// Clase Obra (Abstracta, para mantener la herencia)
abstract class Obra {
    protected String titulo;
    protected List<Artista> artistas = new ArrayList<>(); // Inicialización directa
    protected Anuncio anuncio;
    public Obra(String titulo, String material) {
        this.titulo = titulo;         }
    public List<Artista> getArtistas() { return artistas; }
    public void addArtista(Artista artista) { this.artistas.add(artista); }
    public Anuncio getAnuncio() { return anuncio; }
    public void setAnuncio(Anuncio anuncio) { this.anuncio = anuncio; }
    public String getTitulo() { return titulo; } // Necesario para mensajes
    // Método simplificado para incrementar precio, se llama directamente en main
    public void incrementarPrecioAnuncio(double cantidad) {
        if (this.anuncio != null) {
            this.anuncio.setPrecio(this.anuncio.getPrecio() + cantidad);
        }  }
    @Override
    public String toString() {
        return "Obra [Título=" + titulo + ", Artistas=" + artistas +
               ", Anuncio=" + (anuncio != null ? anuncio.getPrecio() : "N/A") + "]";
    } }
// Clase Pintura
class Pintura extends Obra {
    private String genero;
    public Pintura(String titulo, String material, String genero) {
        super(titulo, material);
        this.genero = genero;   }
    @Override
    public String toString() {
        return "Pintura [Título=" + titulo + ", Género=" + genero +
               ", Artistas=" + artistas +
               ", Precio Anuncio=" + (anuncio != null ? "$" + anuncio.getPrecio() : "N/A") + "]";
    } }
// Clase Principal
public class Main {
    public static void main(String[] args) {
        // Artistas
        Artista michelangelo = new Artista("Miguel Angel", "MA1", 45);
        Artista frida = new Artista("Frida Kahlo", "FK2", 30);
        Artista diego = new Artista("Diego Rivera", "DR3", 55);
        // a. Crear dos objetos pintura que tengan anuncios de venta
        System.out.println("--- a. Crear dos objetos pintura con anuncios ---");
        Pintura pintura1 = new Pintura("La Creación", "Fresco", "Religioso");
        pintura1.addArtista(michelangelo);
        pintura1.setAnuncio(new Anuncio(1, 100000.00));
        System.out.println("Pintura 1: " + pintura1);
        Pintura pintura2 = new Pintura("Autorretrato", "Óleo", "Retrato");
        pintura2.addArtista(frida);
        pintura2.setAnuncio(new Anuncio(2, 75000.00));
        System.out.println("Pintura 2: " + pintura2);
        System.out.println();
        // b. Calcular el promedio de años Experiencia de los artistas de ambas pinturas
        System.out.println("--- b. Promedio de años de experiencia de artistas ---");
        double sumaExperiencia = 0;
        int contadorArtistas = 0;
        for (Artista a : pintura1.getArtistas()) {
            sumaExperiencia += a.getAniosExperiencia();
            contadorArtistas++;
        }
        for (Artista a : pintura2.getArtistas()) {
            sumaExperiencia += a.getAniosExperiencia();
            contadorArtistas++;
        }
        if (contadorArtistas > 0) {
            System.out.println("Promedio de experiencia: " + String.format("%.2f", (sumaExperiencia / contadorArtistas)) + " años.");
        } else {
            System.out.println("No hay artistas para calcular el promedio.");
        }
        System.out.println();
        // c. Incrementar el precio en X a la pintura del artista con nombre X
        System.out.println("--- c. Incrementar precio de pintura por artista ---");
        String artistaObjetivo = "Miguel Angel";
        double incrementoValor = 5000.00; // Valor de X a incrementar
        // Intentar incrementar precio para pintura1
        boolean encontrado = false;
        for (Artista a : pintura1.getArtistas()) {
            if (a.getNombre().equalsIgnoreCase(artistaObjetivo)) {
                if (pintura1.getAnuncio() != null) {
                    double precioOriginal = pintura1.getAnuncio().getPrecio();
                    pintura1.incrementarPrecioAnuncio(incrementoValor);
                    System.out.println("Pintura '" + pintura1.getTitulo() + "' (Artista: " + artistaObjetivo + "): Precio de $" + String.format("%.2f", precioOriginal) + " a $" + String.format("%.2f", pintura1.getAnuncio().getPrecio()));
                    encontrado = true;
                } else {
                    System.out.println("Pintura '" + pintura1.getTitulo() + "' no tiene anuncio para incrementar.");
                }
                break; // Se encontró al artista en esta pintura, no es necesario seguir buscando aquí
            }
        }
        // Si no se encontró en pintura1, buscar en pintura2
        if (!encontrado) {
            for (Artista a : pintura2.getArtistas()) {
                if (a.getNombre().equalsIgnoreCase(artistaObjetivo)) {
                    if (pintura2.getAnuncio() != null) {
                        double precioOriginal = pintura2.getAnuncio().getPrecio();
                        pintura2.incrementarPrecioAnuncio(incrementoValor);
                        System.out.println("Pintura '" + pintura2.getTitulo() + "' (Artista: " + artistaObjetivo + "): Precio de $" + String.format("%.2f", precioOriginal) + " a $" + String.format("%.2f", pintura2.getAnuncio().getPrecio()));
                        encontrado = true;
                    } else {
                        System.out.println("Pintura '" + pintura2.getTitulo() + "' no tiene anuncio para incrementar.");
                    }
                    break;
                }    }   }
        if (!encontrado) {
            System.out.println("No se encontró una pintura asociada al artista '" + artistaObjetivo + "'.");
        }}}
