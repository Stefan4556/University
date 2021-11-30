package socialnetwork.test;

import socialnetwork.domain.Entity;
import socialnetwork.domain.Friendship;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.User;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.domain.validators.ValidationException;

import socialnetwork.network.Graph;
import socialnetwork.repository.Repository;
import socialnetwork.repository.database.FriendshipDB;
import socialnetwork.repository.database.UserDB;

import socialnetwork.service.FriendshipService;
import socialnetwork.service.ServiceException;
import socialnetwork.service.SuperService;
import socialnetwork.service.UserService;
import socialnetwork.service.dto.FriendshipDTO;
import socialnetwork.service.dto.UserDTO;


import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Test {

    private void entityTest(){

        Entity<Long> e = new Entity<>();
        e.setId(1L);
        assert(e.getId() == 1L);
    }

    private void tupleTest(){

        Tuple<Integer, Integer> t = new Tuple<>(1,2);
        assert(t.getLeft() == 1);
        assert(t.getRight() == 2);
        t.setLeft(2);
        t.setRight(1);
        assert(t.getLeft() == 2);
        assert(t.getRight() == 1);

        assert(t.toString().equals("2,1"));
        Tuple<Integer, Integer> t1 = new Tuple<>(2,1);
        assert(t.equals(t1));
        assert(t.hashCode() == Objects.hash(2,1));
    }

    private void userTest(){

        User user = new User("FN","LN", "U1");
        assert(Objects.equals(user.getFirstName(), "FN"));
        assert(Objects.equals(user.getLastName(), "LN"));
        assert(Objects.equals(user.getUserName(), "U1"));
        user.setFirstName("Stefan");
        user.setLastName("Farca");
        user.setUserName("U");
        assert(user.getFirstName().equals("Stefan"));
        assert(user.getLastName().equals("Farca"));
        assert(Objects.equals(user.getUserName(), "U"));
        //assert(user.getFriends().size() == 0);
        user.setId(1L);
        assert(user.toString().equals("FirstName = Stefan, LastName = Farca, UserName = U"));
        assert(user.equals(user));
        Entity<Long> e = new Entity<>();
        assert(!user.equals(e));
        User u = new User("Stefan","Farca","U2");
        u.setId(1L);

        User newUser = new User("FN","LN","FNLN");
        Long o1 = 1L;
        Long o2 = 2L;
        Long o3 = 3L;
    }

    private void dtoTest(){

        User user1 = new User("A","A","A");
        user1.setId(1L);
        UserDTO userDTO1 = new UserDTO(user1.getId(), user1.getFirstName(), user1.getLastName(), user1.getUserName());
        User user2 = new User("B","B","B");
        user2.setId(2L);
        UserDTO userDTO2 = new UserDTO(user2.getId(), user2.getFirstName(), user2.getLastName(), user2.getUserName());

        assert(userDTO2.getUserName().equals("B"));
        assert(userDTO2.getFirstName().equals("B"));
        assert(userDTO2.getLastName().equals("B"));

        assert(userDTO1.getId().equals(user1.getId()));
        assert(userDTO1.toString().equals("A A"));

        assert(userDTO2.getId().equals(user2.getId()));
        assert(userDTO2.toString().equals("B B"));

        LocalDateTime date = LocalDateTime.now();
        FriendshipDTO friendshipDTO = new FriendshipDTO(userDTO1, userDTO2, date);
        friendshipDTO.getUser1().equals(userDTO1);
        friendshipDTO.getUser2().equals(userDTO2);
        friendshipDTO.getDate().equals(date);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        friendshipDTO.toString().equals("A A is friend with B B since " + date.format(formatter));
    }

    private void userDBTest(){

        Repository<Long, User> userRepository = new UserDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");

        Iterable<User> l = userRepository.findAll();
        int ct = 0;
        for(User u : l)
            ct++;

        assert(ct == 5);

        User u = userRepository.findOne(1L);
        assert(u.getUserName().equals("stefan4556"));
        User u2 = userRepository.findOne(20L);
        assert(u2 == null);

        User u3 = new User("a","a","a");
        u3.setId(6L);
        userRepository.save(u3);
        ct = 0;
        l = userRepository.findAll();
        for(User u1 : l)
            ct++;

        assert(ct == 6);

        userRepository.delete(6L);
        ct = 0;
        l = userRepository.findAll();
        for(User u1 : l)
            ct++;

        assert(ct == 5);

        User u4 = new User("b","b", "b");
        u4.setId(1L);
        userRepository.update(u4);

        User u5 = userRepository.findOne(1L);
        assert(u5.getUserName().equals("b"));

        User u6 = new User("Stefan","Farcasanu", "stefan4556");
        u6.setId(1L);
        userRepository.update(u6);
        assert(userRepository.findOne(1L).getUserName().equals("stefan4556"));
    }

    private void friendshipDBTest(){

        Repository<Tuple<Long,Long>, Friendship> friendshipRepository = new FriendshipDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");

        Iterable<Friendship> l = friendshipRepository.findAll();
        int ct = 0;
        for(Friendship f : l)
            ct++;
        assert(ct == 3);

        assert(friendshipRepository.findOne(new Tuple(1L, 5L)).getId().getLeft() == 1L);
        //save delete update

        Friendship f = new Friendship(2L, 3L);
        friendshipRepository.save(f);

        l = friendshipRepository.findAll();
        ct = 0;
        for(Friendship ff : l)
            ct++;
        assert(ct == 4);

        friendshipRepository.delete(new Tuple<>(2L,3L));

        l = friendshipRepository.findAll();
        ct = 0;
        for(Friendship ff : l)
            ct++;
        assert(ct == 3);

        LocalDateTime date = LocalDateTime.of(2020, 10, 10, 10, 10, 10);
        Friendship fu = new Friendship(1L, 5L, date);

        friendshipRepository.update(fu);
        Friendship test = friendshipRepository.findOne(new Tuple<>(1L, 5L));
        assert(test.getDate().getYear() == 2020);

        LocalDateTime dateTime = LocalDateTime.of(2021, 11, 7, 21, 29, 0);
        Friendship friendship = new Friendship(1L, 5L, dateTime);
        friendshipRepository.update(friendship);
        test = friendshipRepository.findOne(new Tuple<>(1L, 5L));
        assert(test.getDate().getYear() == 2021);
    }

    private void graphDBTest(){

        Repository<Long, User> userRepository = new UserDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");
        Repository<Tuple<Long,Long>, Friendship> friendshipRepository = new FriendshipDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");

        Graph graph = new Graph(userRepository.findAll(), friendshipRepository.findAll());

        List<List<Long>> connectedComponents = graph.connectedComponents();
        assert(connectedComponents.size() == 2);

        List<Long> longestPath = graph.getTheMostSociableConnection();
        assert(longestPath.size() == 3);
    }

    private void serviceFriendshipDBTest(){

        Repository<Tuple<Long,Long>, Friendship> friendshipRepository = new FriendshipDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");
        FriendshipValidator friendshipValidator = new FriendshipValidator();
        FriendshipService friendshipService = new FriendshipService(friendshipRepository, friendshipValidator);

        Iterable<Friendship> friendships = friendshipService.getAll();
        int ct = 0;
        for(Friendship f : friendships)
            ct++;
        assert(ct == 3);

        try{
            friendshipService.addFriendship(new Friendship(1L,1L));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            friendshipService.addFriendship(new Friendship(2L, 1L));
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            friendshipService.deleteFriendship(new Tuple<>(7L, 6L));
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        friendshipService.addFriendship(new Friendship(1L, 4L));
        friendships = friendshipService.getAll();
        ct = 0;
        for(Friendship f : friendships)
            ct++;
        assert(ct == 4);

        friendshipService.deleteFriendship(new Tuple<>(4L, 1L));
        friendships = friendshipService.getAll();
        ct = 0;
        for(Friendship f : friendships)
            ct++;
        assert(ct == 3);

        try{
            friendshipService.updateFriendship(new Tuple<>(1L,1L),LocalDateTime.now());
            assert(false);
        }catch(ValidationException err){
            assert(true);
        }

        try{
            friendshipService.updateFriendship(new Tuple<>(7L, 6L), LocalDateTime.now());
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        String str = "2021-11-07 21:25";
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime oldDateTime = LocalDateTime.parse(str, formatter);

        String str2 = "2010-11-07 21:25";
        LocalDateTime newDateTime = LocalDateTime.parse(str2, formatter);

        friendshipService.updateFriendship(new Tuple<>(1L,2L), newDateTime);
        Friendship friendship = friendshipService.findOne(new Tuple<>(1L,2L));
        assert(friendship.getDate().isEqual(newDateTime));

        friendshipService.updateFriendship(new Tuple<>(1L,2L), oldDateTime);
        friendship = friendshipService.findOne(new Tuple<>(1L,2L));
        assert(friendship.getDate().isEqual(oldDateTime));
    }

    private void serviceUserDBTest(){

        Repository<Long, User> userRepository = new UserDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");
        UserValidator userValidator = new UserValidator();
        UserService userService = new UserService(userRepository, userValidator);


        try{
            userService.addUser(new User("","",""));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            userService.addUser(new User("a","a","stefan4556"));
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        Iterable<User> users = userService.getAll();
        int ct = 0;
        for(User u : users)
            ct++;
        assert(ct == 5);

        try{
            userService.deleteUser("");
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            userService.deleteUser("a");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        userService.addUser(new User("a","a","a"));
        ct = 0;
        users = userService.getAll();
        for(User u : users)
            ct++;
        assert(ct == 6);

        userService.deleteUser("a");
        ct = 0;
        users = userService.getAll();
        for(User u : users)
            ct++;
        assert(ct == 5);

        User user = userService.findOne(1L);
        assert(user.getUserName().equals("stefan4556"));

        try{
            userService.validateUsernameOrUsernames("");
            assert(false);
        }catch(ValidationException err){
            assert(true);
        }

        try{
            userService.validateUsernameOrUsernames("","");
            assert(false);
        }catch(ServiceException err){
            assert(true);
        }

        try{
            userService.updateUser("","a","a","a");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            userService.updateUser("a","a","a","");
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            userService.updateUser("a","a","a","a");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        userService.updateUser("stefan4556","test","test","test");

        User u = userService.findOne(1L);
        assert(u.getUserName().equals("test"));

        userService.updateUser("test","Stefan","Farcasanu", "stefan4556");
        u = userService.findOne(1L);
        assert(u.getUserName().equals("stefan4556"));
    }

    private void superServiceDBTest(){

        Repository<Tuple<Long,Long>, Friendship> friendshipRepository = new FriendshipDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");
        FriendshipValidator friendshipValidator = new FriendshipValidator();
        FriendshipService friendshipService = new FriendshipService(friendshipRepository, friendshipValidator);

        Repository<Long, User> userRepository = new UserDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");
        UserValidator userValidator = new UserValidator();
        UserService userService = new UserService(userRepository, userValidator);

        SuperService superService = new SuperService(userService, friendshipService);

        Iterable<User> userIterable = superService.getAll();
        int ctUser = 0;
        for(User u : userIterable)
            ctUser++;
        assert(ctUser == 5);

        assert(superService.getAllFriendships().size() == 3);

        superService.add("a","a","a");
        userIterable = superService.getAll();
        ctUser = 0;
        for(User u : userIterable)
            ctUser++;
        assert(ctUser == 6);

        superService.remove("a");
        userIterable = superService.getAll();
        ctUser = 0;
        for(User u : userIterable)
            ctUser++;
        assert(ctUser == 5);

        superService.add("vic","foca");
        assert(superService.getAllFriendships().size() == 4);

        superService.remove("vic","foca");
        assert(superService.getAllFriendships().size() == 3);

        try{
            superService.add("invalid","invalid");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            superService.add("vic","invalid");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            superService.add("invalid","vic");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        assert(superService.updateUser("stefan4556","a","a","a") == null);
        assert(userRepository.findOne(1L).getUserName().equals("a"));
        assert(superService.updateUser("a","Stefan","Farcasanu","stefan4556") == null);
        assert(userRepository.findOne(1L).getUserName().equals("stefan4556"));

        try{
            superService.updateFriendship("foca","vic","");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        String oldDate = "2021-11-07 21:25";
        String newDate = "2010-11-07 21:25";

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime oldDateTime = LocalDateTime.parse(oldDate, formatter);
        LocalDateTime newDateTime = LocalDateTime.parse(newDate, formatter);

        superService.updateFriendship("stefan4556", "vic", newDate);
        assert(friendshipRepository.findOne(new Tuple<>(1L, 2L)).getDate().equals(newDateTime));

        superService.updateFriendship("stefan4556", "vic", oldDate);
        assert(friendshipRepository.findOne(new Tuple<>(1L, 2L)).getDate().equals(oldDateTime));

        assert(superService.getNumberOfConnectedComponents() == 2);
        assert(superService.getTheMostSociableConnection().size() == 3);
        assert(superService.getAllConnections().size() == 2);
    }

    /**
     * The method which we use to run all the tests
     */
    public void runTests(){

        System.out.println("Running tests...");
        entityTest();
        tupleTest();
        userTest();
        dtoTest();
        userDBTest();
        friendshipDBTest();
        graphDBTest();
        serviceFriendshipDBTest();
        serviceUserDBTest();
        superServiceDBTest();
        System.out.println("Tests ran successfully!");
    }
}