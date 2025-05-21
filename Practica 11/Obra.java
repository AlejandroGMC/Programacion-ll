/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package obra;

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
    // Solo getter de precio, ya que es lo que se usa en el problema c.
    // El numero no se usa directamente para calculos, solo para toString.
}
// Clase Artista
class Artista {
    private String nombre;
    private int aniosExperiencia; // ci no es estrictamente necesario para los problemas
    public Artista(String nombre, String ci, int aniosExperiencia) {
        this.nombre = nombre;
        this.aniosExperiencia = aniosExperiencia;
    }
    public String getNombre() { return nombre; }
    public int getAniosExperiencia() { return aniosExperiencia; }
}
// Clase Obra (abstracta)
abstract class Obra {
    protected String titulo;
    protected List<Artista> artistas = new ArrayList<>();
    protected Anuncio anuncio;
    public Obra(String titulo, String material) {
        this.titulo = titulo;
    }
    public List<Artista> getArtistas() { return artistas; }
    public void addArtista(Artista artista) { this.artistas.add(artista); }
    public Anuncio getAnuncio() { return anuncio; }
    public void setAnuncio(Anuncio anuncio) { this.anuncio = anuncio; }
    public String getTitulo() { return titulo; } // Necesario para el toString de Pintura
}
// Clase Pintura
class Pintura extends Obra {
    private String genero;

    public Pintura(String titulo, String material, String genero) {
        super(titulo, material);
        this.genero = genero;
    }
    @Override
    public String toString() {
        return "Pintura [titulo=" + titulo + ", genero=" + genero + ", anuncio=" +
               (anuncio != null ? "Sí (precio: " + anuncio.getPrecio() + ")" : "No") + "]";
    }
}
public class Main {
    public static void main(String[] args) {
        // Artistas de prueba
        Artista leonardo = new Artista("Leonardo da Vinci", "123", 50);
        Artista vincent = new Artista("Vincent van Gogh", "456", 20);
        Artista pablo = new Artista("Pablo Picasso", "789", 60);
        // a. Crear objetos pintura
        System.out.println("--- a. Crear objetos Pintura ---");
        Anuncio anuncio1 = new Anuncio(101, 15000.00);
        Pintura pinturaConAnuncio = new Pintura("La Gioconda", "Óleo", "Retrato");
        pinturaConAnuncio.setAnuncio(anuncio1);
        pinturaConAnuncio.addArtista(leonardo);
        pinturaConAnuncio.addArtista(vincent);
        System.out.println(pinturaConAnuncio);
        Pintura pinturaSinAnuncio = new Pintura("Noche Estrellada", "Óleo", "Paisaje");
        pinturaSinAnuncio.addArtista(vincent);
        System.out.println(pinturaSinAnuncio);
        System.out.println();
        // b. Mostrar el nombre del artista con más años de Experiencia de ambas pinturas
        System.out.println("--- b. Artista con más años de experiencia ---");
        Artista artistaMasExperiencia = null;
        // Búsqueda en pinturaConAnuncio
        for (Artista a : pinturaConAnuncio.getArtistas()) {
            if (artistaMasExperiencia == null || a.getAniosExperiencia() > artistaMasExperiencia.getAniosExperiencia()) {
                artistaMasExperiencia = a;
            }
        }
        // Búsqueda en pinturaSinAnuncio
        for (Artista a : pinturaSinAnuncio.getArtistas()) {
            if (artistaMasExperiencia == null || a.getAniosExperiencia() > artistaMasExperiencia.getAniosExperiencia()) {
                artistaMasExperiencia = a;
            }
        }
        if (artistaMasExperiencia != null) {
            System.out.println("Artista con más experiencia: " + artistaMasExperiencia.getNombre()+
                               " (" + artistaMasExperiencia.getAniosExperiencia() + " años)");
        } else {
            System.out.println("No se encontraron artistas.");
        }
        System.out.println();
        // c. Agregar anuncio a pintura sin anuncio y determinar monto total
        System.out.println("--- c. Venta y monto total ---");
        Anuncio anuncio2 = new Anuncio(102, 25000.00);
        pinturaSinAnuncio.setAnuncio(anuncio2);
        System.out.println("Pintura 'Noche Estrellada' ahora con anuncio: " + pinturaSinAnuncio);
        double totalVenta = 0.0;
        if (pinturaConAnuncio.getAnuncio() != null) {
            totalVenta += pinturaConAnuncio.getAnuncio().getPrecio();
        }
        if (pinturaSinAnuncio.getAnuncio() != null) {
            totalVenta += pinturaSinAnuncio.getAnuncio().getPrecio();
        }
        System.out.println("Monto total de venta de ambas pinturas: $" + totalVenta);
    }
}
