package socialnetwork.test;

import socialnetwork.domain.*;
import socialnetwork.domain.validators.*;

import socialnetwork.network.Graph;
import socialnetwork.repository.Repository;
import socialnetwork.repository.database.FriendshipDB;
import socialnetwork.repository.database.MessageDB;
import socialnetwork.repository.database.RequestDB;
import socialnetwork.repository.database.UserDB;

import socialnetwork.service.*;
import socialnetwork.service.dto.FriendshipDTO;
import socialnetwork.service.dto.MessageDTO;
import socialnetwork.service.dto.RequestDTO;
import socialnetwork.service.dto.UserDTO;


import java.time.LocalDateTime;
import java.time.Month;
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

        Validator<User> userValidator = new UserValidator();

        try{
            userValidator.validate(new User(null, null, null));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            userValidator.validate(new User("", "", ""));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            userValidator.validate(new User("1", "1", "a-b"));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }
    }

    private void friendhsipTest(){

        String DataS = "2020-10-10 10:30";
        DateTimeFormatter f = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        Friendship friendship = new Friendship(1L,2L,LocalDateTime.parse(DataS,f));

        Friendship friendship2 = new Friendship(1L, 2L);
        Friendship friendship3 = new Friendship(1L, 1L);
        FriendshipValidator validator = new FriendshipValidator();
        try{
            validator.validate(friendship3);
            assert(false);
        }catch(ValidationException e){
            assert(true);
        }

        LocalDateTime date = LocalDateTime.now();
        Friendship friendship1 = new Friendship(2L, 1L, date);
        friendship1.setDate(date);
        assert(friendship1.getDate().isEqual(date));
        assert(friendship1.toString().equals("ID1 = 1, ID2 = 2, Data = " + date));
    }

    private void dtoTest() {

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

        User u1 = new User("A", "B", "ab");
        User u2 = new User("C", "D", "cd");

        u1.setId(1L);
        u2.setId(2L);

        UserDTO uDTO1 = new UserDTO(1L, "A", "B", "ab");
        UserDTO uDTO2 = new UserDTO(2L, "C", "D", "cd");
        UserDTO uDTO3 = new UserDTO(3L, "E", "F", "ef");

        RequestDTO requestDTO = new RequestDTO(uDTO1, uDTO2, LocalDateTime.of(2020, 11, 17, 15, 6), "pending");

        assert (requestDTO.getUser1().getId().equals(1L));
        assert (requestDTO.getUser2().getId().equals(2L));
        assert (requestDTO.getDate().equals(LocalDateTime.of(2020, 11, 17, 15, 6)));
        assert (requestDTO.getStatus().equals("pending"));

        formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        requestDTO.toString().equals("ab requested to be friends with cd on " + date.format(formatter));

        MessageDTO messageDTO = new MessageDTO(1L, uDTO1, List.of(uDTO2, uDTO3), "salut", LocalDateTime.now(), 2L);

    }

    private void messageTest(){

        List<Long> list1 = Arrays.asList(2L, 3L);
        Message message1 = new Message(1L, 1L, list1, "salut");

        assert(message1.getId().equals(1L));
        assert(message1.getFrom().equals(1L));
        assert(message1.getMessage().equals("salut"));
        assert(message1.getTo().equals(list1));

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime date = LocalDateTime.parse("2021-11-11 11:11", formatter);
        message1.setDate(date);
        assert(message1.getDate().equals(date));
        assert(message1.getOriginalMessage() == null);

        List<Long> list2 = Arrays.asList(1L);
        Message message2 = new Message(2L, 2L, list2, "servus", date);
        message2.setOriginalMessage(1L);
        assert(message2.getOriginalMessage().equals(1L));
        message2.setFrom(3L);
        assert(message2.getFrom().equals(3L));
        message2.setTo(list1);
        assert(message2.getTo().equals(list1));
        message2.setMessage("servus draga");
        assert(message2.getMessage().equals("servus draga"));

        MessageValidator validator = new MessageValidator();
        try{

            validator.validate(new Message(1l, null, null, null));
            assert(false);

        } catch (ValidationException err){

            assert(true);
        }

        try{

            validator.validate(new Message(1l, 1L, Arrays.asList(2L), ""));
            assert(false);

        } catch (ValidationException err){

            assert(true);
        }

        try{
            validator.validate(new Message(null, 1L, Arrays.asList(2L),"da"));
            assert (false);
        }catch (ValidationException err){

            assert (true);
        }

        try{
            validator.validate(new Message(-1L, 1L, Arrays.asList(2L),"da"));
            assert (false);
        }catch (ValidationException err){

            assert (true);
        }
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

    // Teste pentru RequestDB.

    private void requestDBTest() {

        Repository<Long, Request> requestRepository = new RequestDB("jdbc:postgresql://localhost:5432/socialnetworktest", "postgres", "admin");

        LocalDateTime ldt = LocalDateTime.of(2021, 9, 15, 18, 55);
        Request r1 = new Request(1L, 1L, 2L, ldt, "pending");
        Request r2 = new Request(2L, 1L, 3L, ldt, "pending");
        Request r3 = new Request(3L, 2L, 3L, ldt, "pending");

        requestRepository.save(r1);
        requestRepository.save(r2);
        requestRepository.save(r3);

        Iterable<Request> iterable = requestRepository.findAll();

        int size = 0;
        for(Request r: iterable)
            size++;

        assert(size == 3);

        Request res = requestRepository.findOne(1L);
        assert(res.getId() == 1L);
        assert(res.getIdUser1() == 1L);
        assert(res.getIdUser2() == 2L);
        assert(res.getDate().getYear() == 2021);
        Month m = Month.SEPTEMBER;
        assert(res.getDate().getMonth().equals(m));
        assert(res.getDate().getDayOfMonth() == 15);
        assert(res.getDate().getHour() == 18);
        assert(res.getDate().getMinute() == 55);
        assert(res.getStatus().getStatus().equals("pending"));

        requestRepository.delete(2L);
        iterable = requestRepository.findAll();

        size = 0;
        for(Request r: iterable)
            size++;

        assert(size == 2);

        requestRepository.delete(3L);
        requestRepository.delete(1L);

        size = 0;
        iterable = requestRepository.findAll();
        for(Request r: iterable)
            size++;

        assert(size == 0);
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

    private void messageDBTest(){

        Repository<Long, Message> messageRepository = new MessageDB("jdbc:postgresql://localhost:5432/socialnetworktest","postgres","admin");

        messageRepository.save(new Message(1L, 1L, Arrays.asList(2L, 3L), "salut"));
        messageRepository.save(new Message(2L, 2L, Arrays.asList(3L, 4L), "salut1"));

        Iterable<Message> messages = messageRepository.findAll();

        int ct = 0;

        for(Message m : messages)

            ct++;

        assert(ct == 2);

        Message message = messageRepository.findOne(1L);

        assert(message.getTo().size() == 2);
        assert(message.getFrom().equals(1L));
        assert(message.getId().equals(1L));
        assert(message.getOriginalMessage() == null);

        messageRepository.delete(2L);
        messageRepository.delete(1L);
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
            friendshipService.updateFriendship(new Tuple<>(1L,1L), "2020-08-09 19:00");
            assert(false);
        }catch(ValidationException err){
            assert(true);
        }

        try{
            friendshipService.updateFriendship(new Tuple<>(7L, 6L), "2020-08-09 19:00");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        String str = "2021-11-07 21:25";
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime oldDateTime = LocalDateTime.parse(str, formatter);

        String str2 = "2010-11-07 21:25";
        LocalDateTime newDateTime = LocalDateTime.parse(str2, formatter);

        friendshipService.updateFriendship(new Tuple<>(1L,2L), str2);
        Friendship friendship = friendshipService.findOne(new Tuple<>(1L,2L));
        assert(friendship.getDate().isEqual(newDateTime));

        friendshipService.updateFriendship(new Tuple<>(1L,2L), str);
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

        Repository<Long, Request> requestRepository = new RequestDB("jdbc:postgresql://localhost:5432/socialnetworktest", "postgres", "admin");
        RequestValidator requestValidator = new RequestValidator();
        RequestService requestService = new RequestService(requestRepository, requestValidator);

        Repository<Long, Message> messageRepository = new MessageDB("jdbc:postgresql://localhost:5432/socialnetworktest", "postgres", "admin");
        MessageValidator messageValidator = new MessageValidator();
        MessageService messageService = new MessageService(messageRepository, messageValidator);

        SuperService superService = new SuperService(userService, friendshipService, requestService, messageService);

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

        // Testing getAllFriendshipsForAUser

        try{
            superService.getAllFriendshipsForAUser("");
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            superService.getAllFriendshipsForAUser("test");
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        List<FriendshipDTO> friendshipDTOList = superService.getAllFriendshipsForAUser("stefan4556");
        assert(friendshipDTOList.size() == 2);

        assert(friendshipDTOList.get(0).getUser2().getFirstName().equals("Victor"));
        assert(friendshipDTOList.get(1).getUser2().getFirstName().equals("Alex"));

        assert(superService.getAllFriendshipsForAUser("ake").size() == 1);

        superService.add("cucu", "mucu", "cumu");

        try {

            superService.getAllFriendshipsForAUser("cumu");
            assert(false);

        } catch(ServiceException ex) {

            assert(true);

        }

        superService.remove("cumu");

        // Tests for getFriendshipsFromMonth method from SuperService class.

        superService.add("Cami", "Serbi", "camserb");
        superService.add("Flori", "Boti", "flobo");

        superService.add("flobo", "vic");
        superService.add("camserb", "flobo");
        superService.add("flobo", "foca");

        newDate = "2020-08-05 22:18";
        superService.updateFriendship("flobo", "camserb", newDate);

        newDate = "2020-08-11 07:55";
        superService.updateFriendship("flobo", "vic", newDate);

        List<FriendshipDTO> friendshipDTOs = superService.getFriendshipsFromMonth("flobo", "AUGUST");

        assert(friendshipDTOs.size() == 2);

        assert(friendshipDTOs.get(0).getUser1().getUserName().equals("flobo"));
        assert(friendshipDTOs.get(1).getUser1().getUserName().equals("flobo"));

        assert(friendshipDTOs.get(0).getUser2().getUserName().equals("vic"));
        assert(friendshipDTOs.get(1).getUser2().getUserName().equals("camserb"));

        friendshipDTOs = superService.getFriendshipsFromMonth("flobo", "november");

        assert(friendshipDTOs.size() == 1);

        assert(friendshipDTOs.get(0).getUser1().getUserName().equals("flobo"));
        assert(friendshipDTOs.get(0).getUser2().getUserName().equals("foca"));

        try {

            superService.getFriendshipsFromMonth("vic", "january");
            assert(false);

        } catch (ServiceException ex) {

            assert(true);

        }

        try {

            superService.getFriendshipsFromMonth("flobo", "invalid");
            assert (false);

        } catch (ServiceException ex) {

            assert (true);

        }

        try {

            superService.getFriendshipsFromMonth("invalid", "October");
            assert (false);

        } catch (ServiceException ex) {

            assert (true);

        }

        superService.remove("flobo");
        superService.remove("camserb");

        try {

            superService.addRequest("invalid", "foca");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addRequest("vic", "invalid");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addRequest("invalid", "foca");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addRequest("", "foca");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addRequest("vic", "");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addRequest("", "");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        // Tests for addRequest method in SuperService class.

        superService.addRequest("vic", "foca");

        List<RequestDTO> list = superService.getAllRequests();

        assert (list.size() == 1);

        assert (list.get(0).getUser1().getUserName().equals("vic"));
        assert (list.get(0).getUser2().getUserName().equals("foca"));

        assert (superService.getAllRequestsForAUser("vic").size() == 1);
        assert (superService.getAllRequestsForAUser("ake").size() == 0);

        int size = superService.getAllFriendships().size();

        try {

            superService.acceptRequest("foca", "vic");
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        superService.acceptRequest("vic", "foca");
        assert (superService.getAllRequests().size() == 0);

        assert (superService.getAllFriendships().size() == size + 1);
        assert (friendshipService.findOne(new Tuple<Long, Long>(2L, 3L)) != null);

        try {

            superService.acceptRequest("stefan4556", "ake");
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        superService.remove("vic", "foca");
        assert (superService.getAllFriendships().size() == size);

        superService.addRequest("vic", "foca");
        assert (superService.getAllRequests().size() == 1);

        try {

            superService.rejectRequest("stefan4556", "ake");
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        superService.rejectRequest("vic", "foca");
        assert (superService.getAllRequests().size() == 0);
        assert (superService.getAllFriendships().size() == size);

        try {

            superService.getAllRequestsForAUser("invalid");
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        try {

            superService.addRequest("ake", "foca");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        superService.addRequest("vic", "foca");

        superService.deleteRequest("vic", "foca");

        list = superService.getAllRequests();

        assert (list.size() == 0);

        try {

            superService.deleteRequest("ake", "foca");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        // Tests for MessageService methods.

        try {

            superService.addMessage("", "vic", List.of("foca"));
            assert (false);
        }

        catch (ValidationException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "", List.of("vic"));
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "vic", List.of(""));
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "invalid", List.of("vic"));
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "vic", List.of("invalid"));
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "vic", List.of());
            assert (false);
        }

        catch (ValidationException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "vic", List.of("vic"));
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.addMessage("aaa", "vic", List.of("foca", "invalid", "ake"));
            assert (false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        Iterable<Message> messages = messageService.getAll();

        List<Message> messageList = new ArrayList<Message>();
        for (Message message: messages)
            messageList.add(message);

        assert (messageList.size() == 1);

        assert (messageList.get(0).getId().equals(1L));

        assert (messageList.get(0).getFrom().equals(2L));

        assert (messageList.get(0).getTo().size() == 2);
        assert (messageList.get(0).getTo().get(0).equals(3L));
        assert (messageList.get(0).getTo().get(1).equals(4L));

        assert (messageList.get(0).getMessage().equals("aaa"));

        //assert (messageList.getReply() == null);

        superService.addMessage("sal", "foca", List.of("vic"));

        messageList.clear();
        assert (superService.getConversations("vic", "foca").size() == 2);
        assert (superService.getConversations("foca", "vic").size() == 2);

        try {

            superService.getConversations("", "vic");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.getConversations("vic", "");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.getConversations("invalid", "vic");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.getConversations("vic", "invalid");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        messageRepository.delete(1L);
        messageRepository.delete(2L);

        messages = messageService.getAll();

        messageList = new ArrayList<Message>();
        for (Message message: messages)
            messageList.add(message);

        assert(messageList.size() == 0);

        try{

            superService.replyToMessage("1", "da", "");
            assert(false);

        }catch (ValidationException err){

            assert (true);
        }

        try{

            superService.replyToMessage("1", "otelul", "dorinel");
            assert (false);

        } catch (ServiceException err){

            assert (true);
        }

        try {

            superService.replyToMessage("", "otelul", "dorinel");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.replyToMessage("servus", "otelul", "dorinel");
            assert (false);
        }

        catch (ServiceException ex) {

            assert (true);
        }

        superService.addMessage("mesaj","stefan4556",List.of("vic", "foca"));

        superService.replyToMessage("1", "mesaj2", "vic");

        assert (superService.getAllMessagesForAUser("stefan4556").size() == 2);

        messageRepository.delete(1L);
        messageRepository.delete(2L);

        try{

            superService.getAllMessagesForAUser("servus");
            assert (false);

        }catch (ServiceException err){

            assert (true);
        }

        superService.addMessage("Alabala", "vic", List.of("stefan4556", "ake", "foca"));

        try {

            superService.replyToAll("baba", "bunasiua", "vic");
            assert (false);

        }
        catch (ServiceException ex) {

            assert (true);
        }

        try {

            superService.replyToAll("1", "uitestamcesafacem", "invalid");
            assert (false);

        }
        catch (ServiceException ex) {

            assert (true);
        }

        superService.replyToAll("1", "Bunasiuuuuaa", "foca");
        assert(messageRepository.findOne(2L).getTo().size() == 3);
        assert(messageRepository.findOne(2L).getTo().contains(1L));
        assert(messageRepository.findOne(2L).getTo().contains(2L));
        assert(messageRepository.findOne(2L).getTo().contains(4L));

        messageRepository.delete(1L);
        messageRepository.delete(2L);

        // assert(false);

    }

    private void requestTest(){

        Request request1 = new Request(1L, 1L, 2L, "pending");

        assert(request1.getId() == 1L);
        assert(request1.getIdUser1() == 1L);
        assert(request1.getIdUser2() == 2L);
        assert(request1.getStatus() == Status.getBySymbol("pending"));

        request1.setId(2L);
        request1.setIdUser1(2L);
        request1.setIdUser2(1L);
        request1.setStatus(Status.getBySymbol("rejected"));

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime date = LocalDateTime.parse("2021-10-10 10:10", formatter);
        request1.setDate(date);

        Request request2 = new Request(1L, 1L, 2L, date, "pending");

        assert(request2.getId() == 1L);
        assert(request2.getIdUser1() == 1L);
        assert(request2.getIdUser2() == 2L);
        assert(request2.getStatus() == Status.getBySymbol("pending"));
        assert(Status.getBySymbol("dadada") == null);
        assert(request2.getStatus().getStatus().equals("pending"));
        assert(request2.getDate().isEqual(date));

        assert(request1.getId() == 2L);
        assert(request1.getIdUser1() == 2L);
        assert(request1.getIdUser2() == 1L);
        assert(request1.getStatus() == Status.getBySymbol("rejected"));
        assert(request1.getDate().isEqual(date));

        Validator<Request> requestValidator = new RequestValidator();

        try{
            requestValidator.validate(new Request(1L, 1L, 1l, "rejected"));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try{
            requestValidator.validate(new Request(1L, null, null, "da"));
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }
    }

    private void serviceRequestDBTest(){

        Repository<Long, Request> requestRepository = new RequestDB("jdbc:postgresql://localhost:5432/socialnetworktest", "postgres", "admin");
        RequestValidator requestValidator = new RequestValidator();
        RequestService requestService = new RequestService(requestRepository, requestValidator);

        requestService.addRequest(1L, 2L);

        try{
            requestService.addRequest(1L, 2L);
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            requestService.addRequest(2L, 1L);
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        Iterable<Request> requests = requestService.getAll();

        int ct = 0;

        for(Request r : requests)

            ct++;

        assert(ct == 1);

        try{
            requestService.addRequest(2L, 1L);
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            requestService.deleteRequest(2L,4L);
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        requestService.deleteRequest(1L, 2L);

        ct = 0;

        for(Request r : requestService.getAll())

            ct++;

        assert(ct == 0);

        requestService.addRequest(1L, 2L);
        requestService.addRequest(1L, 3L);

        Iterable<Request> requestIterable = requestService.getAllRequestsForAUser(1L);

        for(Request r : requestIterable)

            ct++;

        assert(ct == 2);

        try{
            requestService.acceptRequest(3L, 4L);
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        try{
            requestService.acceptRequest(1L, 1L);
            assert(false);
        }catch (ValidationException err){
            assert(true);
        }

        try {
            requestService.acceptRequest(2L, 1L);
            assert(false);
        }catch (ServiceException err){
            assert(true);
        }

        requestService.acceptRequest(1L, 2L);
        ct = 0;
        requestIterable = requestService.getAll();
        for(Request r : requestIterable)
            ct++;
        assert(ct == 1);

        requestService.acceptRequest(1L, 3L);
        ct = 0;
        for(Request r : requestService.getAll())
            ct++;
        assert(ct == 0);
    }

    private void serviceMessageDBTest() {

        Repository<Long, Message> repo = new MessageDB("jdbc:postgresql://localhost:5432/socialnetworktest", "postgres", "admin");
        MessageValidator validator = new MessageValidator();
        MessageService messageService = new MessageService(repo, validator);

        try {

            messageService.addMessage(2L, List.of(), "ccc");
            assert (false);
        }

        catch (ValidationException ex) {

            assert (true);
        }

        messageService.addMessage(2L, List.of(3L, 1L), "servus");

        List<Message> messages = messageService.getMessagesForAUser(2L);
        assert (messages.size() == 1);

        assert (messages.get(0).getId().equals(1L));

        assert (messages.get(0).getFrom().equals(2L));

        assert (messages.get(0).getTo().size() == 2);
        assert (messages.get(0).getTo().get(0).equals(3L));
        assert (messages.get(0).getTo().get(1).equals(1L));

        assert (messages.get(0).getMessage().equals("servus"));

        //assert (messages.getReply() == null);

        repo.delete(1L);

        try{

            messageService.replyToMessage(1L, "da", 2L);
            assert(false);

        }catch (ServiceException err){

            assert(true);
        }

        messageService.addMessage(1L, Arrays.asList(2L, 3L), "salutare");
        messageService.replyToMessage(1L, "servus draga", 2L);

        repo.delete(1L);
        repo.delete(2L);

        messageService.addMessage(1L, Arrays.asList(2L, 3L, 4L), "Buna ziua bat pari");
        messageService.replyToAll(1L, "Servus bat pari si eu", 2L);

        List<Message> messages1 = new ArrayList<>();
        repo.findAll().forEach(messages1::add);

        assert(messages1.size() == 2);

        assert(repo.findOne(2L).getFrom().equals(2L));

        assert(repo.findOne(2L).getOriginalMessage().equals(1L));

        assert(repo.findOne(2L).getTo().size() == 3);
        assert(repo.findOne(2L).getTo().contains(1L));
        assert(repo.findOne(2L).getTo().contains(3L));
        assert(repo.findOne(2L).getTo().contains(4L));

        try {

            messageService.replyToAll(3L, "aloo", 2L);
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        try {

            messageService.replyToAll(1L, "aloo", 1L);
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        try {

            messageService.replyToMessage(1L, "aloo", 1L);
            assert(false);
        }

        catch (ServiceException ex) {

            assert(true);
        }

        repo.delete(1L);
        repo.delete(2L);

    }

    /**
     * The method which we use to run all the tests
     */
    public void runTests(){

        System.out.println("Running tests...");
        entityTest();
        tupleTest();
        userTest();
        messageTest();
        dtoTest();
        userDBTest();
        friendshipDBTest();
        requestDBTest();
        graphDBTest();
        messageDBTest();
        serviceFriendshipDBTest();
        serviceUserDBTest();
        serviceRequestDBTest();
        serviceMessageDBTest();
        superServiceDBTest();
        friendhsipTest();
        requestTest();
        System.out.println("Tests ran successfully!");
    }
}