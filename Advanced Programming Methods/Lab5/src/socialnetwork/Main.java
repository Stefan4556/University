package socialnetwork;

import socialnetwork.domain.*;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.domain.validators.MessageValidator;
import socialnetwork.domain.validators.RequestValidator;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.repository.Repository;
import socialnetwork.repository.database.FriendshipDB;
import socialnetwork.repository.database.MessageDB;
import socialnetwork.repository.database.RequestDB;
import socialnetwork.repository.database.UserDB;
import socialnetwork.service.*;
import socialnetwork.test.Test;
import socialnetwork.ui.UI;

/**
 * The class which builds and runs our app
 */
public class Main {

    /**
     * The method which gets called when we run the program
     *
     * @param args - arguments from command line
     */
    public static void main(String[] args) {

        FriendshipValidator friendshipValidator = new FriendshipValidator();
        UserValidator validator = new UserValidator();
        RequestValidator requestValidator = new RequestValidator();
        MessageValidator messageValidator = new MessageValidator();

        Repository<Long, User> repositoryUserDB = new UserDB("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "admin");
        Repository<Tuple<Long, Long>, Friendship> repositoryFriendshipDB = new FriendshipDB("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "admin");
        Repository<Long, Request> repositoryRequestDB = new RequestDB("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "admin");
        Repository<Long, Message> repositoryMessageDB = new MessageDB("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "admin");


        UserService userService = new UserService(repositoryUserDB, validator);
        FriendshipService friendshipService = new FriendshipService(repositoryFriendshipDB, friendshipValidator);
        RequestService requestService = new RequestService(repositoryRequestDB, requestValidator);
        MessageService messageService = new MessageService(repositoryMessageDB, messageValidator);

        SuperService superService = new SuperService(userService, friendshipService, requestService, messageService);

        UI console = new UI(superService);
        Test t = new Test();
        t.runTests();
        //console.run();
    }
}