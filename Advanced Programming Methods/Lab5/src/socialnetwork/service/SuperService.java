package socialnetwork.service;

import socialnetwork.domain.*;
import socialnetwork.domain.validators.ValidationException;
import socialnetwork.network.Graph;
import socialnetwork.service.dto.FriendshipDTO;
import socialnetwork.service.dto.MessageDTO;
import socialnetwork.service.dto.RequestDTO;
import socialnetwork.service.dto.UserDTO;

import java.util.*;
import java.util.function.Predicate;

/**
 * Class that manages the userService and the friendshipService
 */
public class SuperService {

    /**
     * User service
     */
    private UserService userService;

    /**
     * Friendship service
     */
    private FriendshipService friendshipService;

    /**
     * Request service
     */
    private RequestService requestService;

    /**
     * Message service
     */
    private MessageService messageService;

    /**
     * Constructor
     *
     * @param userService       - UserService0, user service
     * @param friendshipService - FriendshipService0, friendship service
     */
    public SuperService(UserService userService, FriendshipService friendshipService, RequestService requestService, MessageService messageService) {

        this.userService = userService;
        this.friendshipService = friendshipService;
        this.requestService = requestService;
        this.messageService = messageService;
    }

    /**
     * Get all the users
     *
     * @return list of users
     */
    public Iterable<User> getAll() {

        return this.userService.getAll();
    }

    /**
     * Get all friendships
     *
     * @return all the friendships
     */
    public List<FriendshipDTO> getAllFriendships() {

        Iterable<Friendship> friendships = this.friendshipService.getAll();

        List<FriendshipDTO> result = new LinkedList<>();

        for (Friendship friendship : friendships) {

            User user1 = this.userService.findOne(friendship.getId().getLeft());
            User user2 = this.userService.findOne(friendship.getId().getRight());
            UserDTO dto1 = new UserDTO(user1.getId(), user1.getFirstName(), user1.getLastName(), user1.getUserName());
            UserDTO dto2 = new UserDTO(user2.getId(), user2.getFirstName(), user2.getLastName(), user2.getUserName());
            FriendshipDTO friendshipDTO = new FriendshipDTO(dto1, dto2, friendship.getDate());
            result.add(friendshipDTO);
        }

        return result;
    }

    /**
     * Check if there are 2 users with the usernames given as parameters
     *
     * @param userName1 - String, name of the first username
     * @param userName2 - String, name of the second username
     * @throws ServiceException if one or more users are not found
     */
    private void checkUsersExistenceUsingUsername(String userName1, String userName2) {

        Long id1 = this.userService.fromUserNameToId(userName1);
        Long id2 = this.userService.fromUserNameToId(userName2);

        if (id1 == null && id2 == null)

            throw new ServiceException("No users found with those usernames!\n");

        if (id1 == null)

            throw new ServiceException("No user found with " + userName1 + " as a username!\n");

        if (id2 == null)

            throw new ServiceException("No user found with " + userName2 + " as a username!\n");
    }

    /**
     * Adds a friendship or a user.
     *
     * @param args the arguments for the friendship or the user
     */
    public void add(String... args) {

        // Daca avem trei argumente, vorbim de addUser
        if (args.length == 3) {
            this.userService.addUser(new User(args[0], args[1], args[2]));
        }

        // Daca avem doua, vorbim de addFriendship
        else if (args.length == 2) {
            this.userService.validateUsernameOrUsernames(args[0], args[1]);
            checkUsersExistenceUsingUsername(args[0], args[1]);

            Long id = this.userService.fromUserNameToId(args[0]);
            Long idF = this.userService.fromUserNameToId(args[1]);
            this.friendshipService.addFriendship(new Friendship(id, idF));
        }
    }

    /**
     * Removes a friendship or a user.
     *
     * @param args the arguments for the friendship or the user
     */
    public void remove(String... args) {
        // Daca avem un singur argument, vorbim de removeUser
        if (args.length == 1) {
            this.userService.deleteUser(args[0]);
        }

        // Daca avem doua, vorbim de removeFriendship
        else if (args.length == 2) {
            this.userService.validateUsernameOrUsernames(args[0], args[1]);
            checkUsersExistenceUsingUsername(args[0], args[1]);

            Long id = this.userService.fromUserNameToId(args[0]);
            Long idF = this.userService.fromUserNameToId(args[1]);
            this.friendshipService.deleteFriendship(new Tuple<>(id, idF));
        }
    }

    /**
     * Method for updating all fields of one user
     *
     * @param username     - String, the username of the user we are searching for
     * @param newFirstName - String, the new first name of the user
     * @param newLastName  - String, the new last name of the user
     * @param newUserName- String, the new username of the user
     * @return null if the user is updated successfully
     */
    public User updateUser(String username, String newFirstName, String newLastName, String newUserName) {

        return this.userService.updateUser(username, newFirstName, newLastName, newUserName);
    }

    /**
     * Method for updating the date of a friendship
     *
     * @param username1 - String, the username of the first user
     * @param username2 - String, the username of the second user
     * @param date      - String, the new date
     * @return null if the friendship is updated successfully
     * @throws ServiceException if the date is not valid
     */
    public Friendship updateFriendship(String username1, String username2, String date) {

        this.userService.validateUsernameOrUsernames(username1, username2);

        checkUsersExistenceUsingUsername(username1, username2);
        Long id1 = this.userService.fromUserNameToId(username1);
        Long id2 = this.userService.fromUserNameToId(username2);

        return this.friendshipService.updateFriendship(new Tuple<>(id1, id2), date);
    }

    /**
     * Get the number of connected components
     *
     * @return the number of connected components
     */
    public int getNumberOfConnectedComponents() {

        Graph graph = new Graph(this.userService.getAll(), this.friendshipService.getAll());

        return graph.connectedComponents().size();
    }

    /**
     * Return the most sociable connection
     *
     * @return the list which contains the users who form the biggest community
     */
    public List<UserDTO> getTheMostSociableConnection() {

        Graph graph = new Graph(this.userService.getAll(), this.friendshipService.getAll());

        List<Long> mostSociable = graph.getTheMostSociableConnection();

        List<UserDTO> result = new ArrayList<>();

        for (Long id : mostSociable) {

            User user = this.userService.findOne(id);
            result.add(new UserDTO(id, user.getFirstName(), user.getLastName(), user.getUserName()));
        }

        return result;
    }

    /**
     * Return all the communities
     *
     * @return the list of all the communities found in our network
     */
    public List<List<UserDTO>> getAllConnections() {

        Graph graph = new Graph(this.userService.getAll(), this.friendshipService.getAll());

        List<List<Long>> connections = graph.connectedComponents();
        List<List<UserDTO>> result = new ArrayList<>();

        for (List<Long> connection : connections) {

            List<UserDTO> current = new ArrayList<>();

            for (Long id : connection) {

                User user = this.userService.findOne(id);
                current.add(new UserDTO(id, user.getFirstName(), user.getLastName(), user.getUserName()));
            }

            result.add(current);
        }

        return result;
    }

    /**
     * This method is used for getting all friendships for one user
     *
     * @param username - The username of the user
     * @return a list which has all the friendships of a user
     */
    public List<FriendshipDTO> getAllFriendshipsForAUser(String username) {

        this.userService.validateUsernameOrUsernames(username);

        Long id = this.userService.fromUserNameToId(username);

        if (id == null)

            throw new ServiceException("No username found with the username that you've entered!\n");

        List<FriendshipDTO> friendsList = new ArrayList<>();

        User ourUser = this.userService.findOne(id);
        UserDTO ourUserDTO = new UserDTO(ourUser.getId(), ourUser.getFirstName(), ourUser.getLastName(), ourUser.getUserName());

        Iterable<Friendship> friendshipIterable = this.friendshipService.getAll();

        List<Friendship> friendshipList = new ArrayList<>();
        friendshipIterable.forEach(friendshipList::add);

        Predicate<Friendship> leftPart = x -> x.getId().getLeft().equals(id);
        Predicate<Friendship> rightPart = x -> x.getId().getRight().equals(id);
        Predicate<Friendship> friendshipPredicate = leftPart.or(rightPart);

        friendshipList.stream().filter(friendshipPredicate).map(x -> {

            User user;

            if (x.getId().getLeft().equals(id))

                user = this.userService.findOne(x.getId().getRight());

            else

                user = this.userService.findOne(x.getId().getLeft());

            UserDTO friendDTO = new UserDTO(user.getId(), user.getFirstName(), user.getLastName(), user.getUserName());

            return new FriendshipDTO(ourUserDTO, friendDTO, x.getDate());
        }).forEach(friendsList::add);

        if (friendsList.size() == 0)

            throw new ServiceException("This user has no friendships!\n");

        return friendsList;

    }

    /**
     * Method used for getting a user's friendships which were created on a certain month given as a parameter.
     *
     * @param userName    the username of the user
     * @param monthString the string containing the name of the month
     * @return a list of the corresponding friendships (stored as FriendshipDTOs)
     */
    public List<FriendshipDTO> getFriendshipsFromMonth(String userName, String monthString) {
        final List<String> possibleMonths = Arrays.asList("january", "february", "march", "april", "may", "june", "july", "august", "September", "october", "november", "december");

        this.userService.validateUsernameOrUsernames(userName);

        if (!possibleMonths.contains(monthString.toLowerCase()))

            throw new ServiceException("There is no such month!\n");

        List<FriendshipDTO> friendshipDTOs = this.getAllFriendshipsForAUser(userName);
        List<FriendshipDTO> returnList = new ArrayList<>();

        Predicate<FriendshipDTO> predicate = x -> String.valueOf(x.getDate().getMonth()).equalsIgnoreCase(monthString);
        friendshipDTOs.stream().filter(predicate).forEach(returnList::add);

        if (returnList.size() == 0)

            throw new ServiceException("This user has no friendships on that month!\n");

        return returnList;

    }

    /**
     * Checks if it is possible to add or remove a request between the users with the given usernames.
     *
     * @param userName1 the username of the first user
     * @param userName2 the username of the second user
     * @return a friendship object between the two users with the given usernames, if it is possible to be created
     */
    private Tuple<Long, Long> validateDataForRequests(String userName1, String userName2) {

        this.userService.validateUsernameOrUsernames(userName1, userName2);

        Long id1 = this.userService.fromUserNameToId(userName1);
        if (id1 == null)

            throw new ServiceException("There is no user with " + userName1 + " as an username!\n");

        Long id2 = this.userService.fromUserNameToId(userName2);
        if (id2 == null)

            throw new ServiceException("There is no user with " + userName2 + " as an username!\n");

        return new Tuple<Long, Long>(id1, id2);
    }

    /**
     * Method for adding a friendship request between two users.
     *
     * @param userName1 the username of the first user
     * @param userName2 the username of the second user
     */
    public void addRequest(String userName1, String userName2) {

        Tuple<Long, Long> tuple = this.validateDataForRequests(userName1, userName2);

        try {

            this.friendshipService.friendshipAlreadyExists(new Friendship(tuple.getLeft(), tuple.getRight()));

        }

        catch (ServiceException ex) {

            throw new ServiceException("Request cannot be added because users are already friends!");
        }

        this.requestService.addRequest(tuple.getLeft(), tuple.getRight());

    }

    /**
     * Method for deleting a request between two users.
     *
     * @param userName1 the username of the first user
     * @param userName2 the username of the second user
     */
    public void deleteRequest(String userName1, String userName2) {

        Tuple<Long, Long> tuple = this.validateDataForRequests(userName1, userName2);
        try {

            this.friendshipService.friendshipAlreadyExists(new Friendship(tuple.getLeft(), tuple.getRight()));

        }

        catch (ServiceException ex) {
            throw new ServiceException("There cannot be a request if the users are already friends");
        }

        this.requestService.deleteRequest(tuple.getLeft(), tuple.getRight());

    }

    /**
     * Returns a list of RequestDTOs created from a given iterable of requests.
     *
     * @param requests the iterable of requests
     * @return the list of RequestDTOs
     */
    private List<RequestDTO> fromRequestsToRequestDTOs(Iterable<Request> requests) {

        List<RequestDTO> result = new LinkedList<>();

        for (Request request : requests) {

            User user1 = this.userService.findOne(request.getIdUser1());
            User user2 = this.userService.findOne(request.getIdUser2());
            UserDTO dto1 = new UserDTO(user1.getId(), user1.getFirstName(), user1.getLastName(), user1.getUserName());
            UserDTO dto2 = new UserDTO(user2.getId(), user2.getFirstName(), user2.getLastName(), user2.getUserName());
            RequestDTO requestDTO = new RequestDTO(dto1, dto2, request.getDate(), request.getStatus().getStatus());
            result.add(requestDTO);
        }

        return result;

    }

    /**
     * Gets all the requests.
     *
     * @return an iterable containing all the requests
     */
    public List<RequestDTO> getAllRequests() {

        Iterable<Request> requests = this.requestService.getAll();

        return this.fromRequestsToRequestDTOs(requests);
    }

    /**
     * Gets all the requests for a user with the given username.
     *
     * @param userName the username of the user
     * @return a list of requests for that user
     */
    public List<RequestDTO> getAllRequestsForAUser(String userName) {

        this.userService.validateUsernameOrUsernames(userName);

        Long id = this.userService.fromUserNameToId(userName);
        if (id == null)

            throw new ServiceException("There is no user with this username!");

        Iterable<Request> requests = this.requestService.getAllRequestsForAUser(id);

        return this.fromRequestsToRequestDTOs(requests);
    }

    /**
     * Accepts a friendship request from the user with the first username to the user with the second username.
     * @param userName1 the username of the first user
     * @param userName2 the username of the second user
     */
    public void acceptRequest(String userName1, String userName2) {

        this.userService.validateUsernameOrUsernames(userName1, userName2);

        this.checkUsersExistenceUsingUsername(userName1, userName2);

        Long id1 = this.userService.fromUserNameToId(userName1);
        Long id2 = this.userService.fromUserNameToId(userName2);

        this.requestService.acceptRequest(id1, id2);

        this.friendshipService.addFriendship(new Friendship(id1, id2));

    }

    /**
     * Rejects a friendship request from the user with the first username to the user with the second username.
     *
     * @param userName1 the username of the first user
     * @param userName2 the username of the second
     */
    public void rejectRequest(String userName1, String userName2) {

        this.userService.validateUsernameOrUsernames(userName1, userName2);

        this.checkUsersExistenceUsingUsername(userName1, userName2);

        Long id1 = this.userService.fromUserNameToId(userName1);
        Long id2 = this.userService.fromUserNameToId(userName2);

        this.requestService.deleteRequest(id1, id2);

    }

    /**
     * Gets the conversations between two users.
     * @param userName1 the username of the first user
     * @param userName2 the username of the second user
     * @return a list of messages
     */
    public List<MessageDTO> getConversations(String userName1, String userName2) {

        this.userService.validateUsernameOrUsernames(userName1, userName2);
        this.checkUsersExistenceUsingUsername(userName1, userName2);

        Long id1 = this.userService.fromUserNameToId(userName1);
        Long id2 = this.userService.fromUserNameToId(userName2);

        List<Message> messages = this.messageService.getConversations(id1, id2);
        List<MessageDTO> list = new ArrayList<>();

        messages.forEach(x->{
            User u = this.userService.findOne(x.getFrom());
            List<Long> ids = x.getTo();

            List<UserDTO> l = new ArrayList<>();

            ids.forEach(y->{
                User u1 = this.userService.findOne(y);
                l.add(new UserDTO(u1.getId(), u1.getFirstName(), u1.getLastName(), u1.getUserName()));
            });

            list.add(new MessageDTO(x.getId(), new UserDTO(u.getId(), u.getFirstName(), u.getLastName(), u.getUserName()), l, x.getMessage(), x.getDate(), x.getOriginalMessage()));
        });

        return list;
    }

    /**
     * Adds a message sent from a user to multiple other users.
     * @param messageString the message
     * @param from the sender's username
     * @param to the receivers' usernames
     */
    public void addMessage(String messageString, String from, List<String> to) {

        try {

            this.userService.validateUsernameOrUsernames(from);
        }

        catch (ValidationException ex) {

            throw new ServiceException("Sender's username cannot be null!\n");
        }

        Long idFrom = this.userService.fromUserNameToId(from);
        if (idFrom == null)

            throw new ServiceException("Sender does not exist!\n");

        List<Long> idList = new ArrayList<>();
        String errorMsgs = "";
        boolean flag;

        for (String username : to) {

            flag = false;

            if (from.equals(username)) {

                errorMsgs += "Sender's username cannot be the same as receiver's username!\n";
                flag = true;
            }

            try {

                this.userService.validateUsernameOrUsernames(username);
            }

            catch (ValidationException ex) {

                errorMsgs += "Receiver's username cannot be empty!\n";
                flag = true;
            }

            Long id = this.userService.fromUserNameToId(username);
            if(id == null) {

                if (!flag)
                    errorMsgs += "Receiver's username does not exist!\n";
            }

            else

                if (!flag)
                    idList.add(id);

        }

        if(!errorMsgs.equals("") && idList.isEmpty())

            throw new ServiceException(errorMsgs);

        this.messageService.addMessage(idFrom, idList, messageString);

        if (!errorMsgs.equals(""))

            throw new ServiceException(errorMsgs);
    }

    /**
     * This method is to reply to a message
     * @param messageID - The id of the message
     * @param message - The content of the message
     * @param username - The username of the sender
     */
    public void replyToMessage(String messageID, String message, String username){

        Long mID;
        try {
            mID = Long.parseLong(messageID);
        }

        catch (NumberFormatException ex) {

            throw new ServiceException("Invalid message ID!\n");
        }

        this.userService.validateUsernameOrUsernames(username);

        Long id = this.userService.fromUserNameToId(username);

        if (id == null)

            throw new ServiceException("No user found with the username that you've entered!\n");

        this.messageService.replyToMessage(mID, message, id);

    }

    public void replyToAll(String idString, String message, String userName) {

        long mID;
        try {
            mID = Long.parseLong(idString);
        }

        catch (NumberFormatException ex) {

            throw new ServiceException("Invalid message ID!\n");
        }

        this.userService.validateUsernameOrUsernames(userName);

        Long id = this.userService.fromUserNameToId(userName);

        if (id == null)

            throw new ServiceException("No user found with the username that you've entered!\n");

        this.messageService.replyToAll(mID, message, id);

    }

    /**
     * Get all messages for a user by username
     * @param username - The user's username
     * @throws ServiceException if there is no user with the username given as parameter
     * @return a list which contains all the messages that a user has sent or received
     */
    public List<MessageDTO> getAllMessagesForAUser(String username){

        this.userService.validateUsernameOrUsernames(username);

        Long id = this.userService.fromUserNameToId(username);

        if(id == null)

            throw new ServiceException("No username found with that username!\n");

        List<Message> messages = this.messageService.getMessagesForAUser(id);

        List<MessageDTO> list = new ArrayList<>();

        messages.forEach(x->{
            User u = this.userService.findOne(x.getFrom());
            List<Long> ids = x.getTo();

            List<UserDTO> l = new ArrayList<>();

            ids.forEach(y->{
                User u1 = this.userService.findOne(y);
                l.add(new UserDTO(u1.getId(), u1.getFirstName(), u1.getLastName(), u1.getUserName()));
            });

            list.add(new MessageDTO(x.getId(), new UserDTO(u.getId(), u.getFirstName(), u.getLastName(), u.getUserName()), l, x.getMessage(), x.getDate(), x.getOriginalMessage()));
        });

        return list;
    }

}