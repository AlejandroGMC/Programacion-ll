interface Transport {
    void deliver();
}

class Car implements Transport {
    public void deliver() {
        System.out.println("Delivery by Car.");
    }
}

class Bicycle implements Transport {
    public void deliver() {
        System.out.println("Delivery by Bicycle.");
    }
}

abstract class TransportFactory {
    abstract Transport createTransport();
}

class CarFactory extends TransportFactory {
    Transport createTransport() {
        return new Car();
    }
}

class BicycleFactory extends TransportFactory {
    Transport createTransport() {
        return new Bicycle();
    }
}

public class FactoryMethod {
    public static void main(String[] args) {
        TransportFactory factory = new CarFactory(); // o new BicycleFactory();
        Transport transport = factory.createTransport();
        transport.deliver();
    }
}