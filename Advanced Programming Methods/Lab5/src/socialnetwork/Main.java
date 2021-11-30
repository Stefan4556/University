package socialnetwork;

import socialnetwork.domain.Friendship;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.User;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.repository.Repository;
import socialnetwork.repository.database.FriendshipDB;
import socialnetwork.repository.database.UserDB;
import socialnetwork.service.FriendshipService;
import socialnetwork.service.SuperService;
import socialnetwork.service.UserService;
import socialnetwork.test.Test;
import socialnetwork.ui.UI;

/**
 * The class which builds and runs our app
 */
public class Main {

    /**
     * The method which gets called when we run the program
     * @param args - arguments from command line
     */
    public static void main(String[] args) {

        FriendshipValidator friendshipValidator = new FriendshipValidator();

        UserValidator validator = new UserValidator();

        Repository<Long, User> repositoryUserDB = new UserDB("jdbc:postgresql://localhost:5432/socialnetwork", "postgres","admin");
        Repository<Tuple<Long, Long>, Friendship> repositoryFriendshipDB = new FriendshipDB("jdbc:postgresql://localhost:5432/socialnetwork","postgres","admin");

        UserService userService = new UserService(repositoryUserDB, validator);
        FriendshipService friendshipService = new FriendshipService(repositoryFriendshipDB, friendshipValidator);

        SuperService superService = new SuperService(userService, friendshipService);

        UI console = new UI(superService);
        Test t = new Test();
        t.runTests();
        //console.run();
    }
}