import java.util.ArrayList;
import java.util.List;

interface Subscriber {
    void update(String videoTitle);
}

class User implements Subscriber {
    private String name;

    public User(String name) {
        this.name = name;
    }

    public void update(String videoTitle) {
        System.out.println(name + " got notified about: " + videoTitle);
    }
}

class YouTubeChannel {
    private List<Subscriber> subscribers = new ArrayList<>();
    private String latestVideo;

    public void subscribe(Subscriber s) {
        subscribers.add(s);
    }

    public void unsubscribe(Subscriber s) {
        subscribers.remove(s);
    }

    public void uploadVideo(String title) {
        this.latestVideo = title;
        notifySubscribers();
    }

    private void notifySubscribers() {
        for (Subscriber s : subscribers) {
            s.update(latestVideo);
        }
    }
}

public class Observer {
    public static void main(String[] args) {
        YouTubeChannel channel = new YouTubeChannel();

        Subscriber u1 = new User("Alice");
        Subscriber u2 = new User("Bob");

        channel.subscribe(u1);
        channel.subscribe(u2);

        channel.uploadVideo("Design Patterns in Java!");
    }
}