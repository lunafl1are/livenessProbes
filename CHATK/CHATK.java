import java.util.ArrayList;
import java.util.List;

interface Mediator {
    void sendMessage(String message, User user);
}

class Lobby implements Mediator {
    private List<User> users;

    public Lobby() {
        this.users = new ArrayList<>();
    }

    public void addUser(User user) {
        users.add(user);
    }

    @Override
    public void sendMessage(String message, User user) {
        for (User u : users) {
            if (u != user) {
                u.getMessage(message);
            }
        }
    }
}

interface User {
    void sendMessage(String message);

    void getMessage(String message);
}

// Concrete Colleague
class Chatter implements User {
    private String name;
    private Mediator mediator;

    public Chatter(String name, Mediator mediator) {
        this.name = name;
        this.mediator = mediator;
    }

    @Override
    public void sendMessage(String message) {
        mediator.sendMessage(message, this);
    }

    @Override
    public void getMessage(String message) {
        System.out.println(name + " got: " + message);
    }
}

public class CHATK {
    public static void main(String[] args) {
        Mediator lobby = new Lobby();

        User user1 = new Chatter("User1", lobby);
        User user2 = new Chatter("User2", lobby);
        User user3 = new Chatter("User3", lobby);

        ((Lobby) lobby).addUser((Chatter) user1);
        ((Lobby) lobby).addUser((Chatter) user2);
        ((Lobby) lobby).addUser((Chatter) user3);

        user1.sendMessage("Hello, World!");
        user2.sendMessage("Haaaaaai!");
        user3.sendMessage("Bruh.");
    }
}
