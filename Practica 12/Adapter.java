interface ThreePinPlug {
    void plugInThreePin();
}

class TwoPinPlug {
    void plugInTwoPin() {
        System.out.println("Plugged in with Two Pin.");
    }
}

class PlugAdapter implements ThreePinPlug {
    private TwoPinPlug twoPinPlug;

    public PlugAdapter(TwoPinPlug plug) {
        this.twoPinPlug = plug;
    }

    public void plugInThreePin() {
        twoPinPlug.plugInTwoPin();
    }
}

public class Adapter {
    public static void main(String[] args) {
        TwoPinPlug oldPlug = new TwoPinPlug();
        ThreePinPlug adapter = new PlugAdapter(oldPlug);
        adapter.plugInThreePin();
    }
}