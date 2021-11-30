package socialnetwork.service;

import socialnetwork.domain.Friendship;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.User;
import socialnetwork.network.Graph;
import socialnetwork.service.dto.FriendshipDTO;
import socialnetwork.service.dto.UserDTO;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

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
     * Constructor
     * @param userService - UserService0, user service
     * @param friendshipService - FriendshipService0, friendship service
     */
    public SuperService(UserService userService, FriendshipService friendshipService){

        this.userService = userService;
        this.friendshipService = friendshipService;
    }

    /**
     * Get all the users
     * @return list of users
     */
    public Iterable<User> getAll(){

        return this.userService.getAll();
    }

    /**
     * Get all friendships
     * @return all the friendships
     */
    public List<FriendshipDTO> getAllFriendships(){

        Iterable<Friendship> friendships = this.friendshipService.getAll();

        List<FriendshipDTO> result = new LinkedList<>();

        for(Friendship friendship : friendships){

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
     * @param userName1 - String, name of the first username
     * @param userName2 - String, name of the second username
     * @throws ServiceException if one or more users are not found
     */
    private void checkUsersExistenceUsingUsername(String userName1, String userName2){

        Long id1 = this.userService.fromUserNameToId(userName1);
        Long id2 = this.userService.fromUserNameToId(userName2);

        if(id1 == null && id2 == null)

            throw new ServiceException("No users found with those usernames!\n");

        if(id1 == null)

            throw new ServiceException("No user found with " + userName1 + " as a username!\n");

        if(id2 == null)

            throw new ServiceException("No user found with " + userName2 + " as a username!\n");
    }

    /**
     * Adds a friendship or a user.
     * @param args the arguments for the friendship or the user
     */
    public void add(String... args)
    {

        // Daca avem trei argumente, vorbim de addUser
        if(args.length == 3)
        {
            this.userService.addUser(new User(args[0], args[1], args[2]));
        }

        // Daca avem doua, vorbim de addFriendship
        else if(args.length == 2)
        {
            this.userService.validateUsernameOrUsernames(args[0], args[1]);
            checkUsersExistenceUsingUsername(args[0], args[1]);

            Long id = this.userService.fromUserNameToId(args[0]);
            Long idF = this.userService.fromUserNameToId(args[1]);
            this.friendshipService.addFriendship(new Friendship(id, idF));
        }
    }

    /**
     * Removes a friendship or a user.
     * @param args the arguments for the friendship or the user
     */
    public void remove(String... args)
    {
        // Daca avem un singur argument, vorbim de removeUser
        if(args.length == 1)
        {
            this.userService.deleteUser(args[0]);
        }

        // Daca avem doua, vorbim de removeFriendship
        else if(args.length == 2)
        {
            this.userService.validateUsernameOrUsernames(args[0], args[1]);
            checkUsersExistenceUsingUsername(args[0], args[1]);

            Long id = this.userService.fromUserNameToId(args[0]);
            Long idF = this.userService.fromUserNameToId(args[1]);
            this.friendshipService.deleteFriendship(new Tuple<>(id, idF));
        }
    }

    /**
     * Method for updating all fields of one user
     * @param username - String, the username of the user we are searching for
     * @param newFirstName - String, the new first name of the user
     * @param newLastName - String, the new last name of the user
     * @param newUserName- String, the new username of the user
     * @return null if the user is updated successfully
     */
    public User updateUser(String username, String newFirstName, String newLastName, String newUserName){

        return this.userService.updateUser(username, newFirstName, newLastName, newUserName);
    }

    /**
     * Method for updating the date of a friendship
     * @param username1 - String, the username of the first user
     * @param username2 - String, the username of the second user
     * @param date - String, the new date
     * @return null if the friendship is updated successfully
     * @throws ServiceException if the date is not valid
     */
    public Friendship updateFriendship(String username1, String username2, String date){

        /// TODO: mutat validare data in friendshipService
        this.userService.validateUsernameOrUsernames(username1, username2);
        LocalDateTime localDateTime;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        try{
            localDateTime = LocalDateTime.parse(date, formatter);
        }

        catch (DateTimeParseException err){
            throw new ServiceException("Invalid date!\n");
        }
        checkUsersExistenceUsingUsername(username1, username2);
        Long id1 = this.userService.fromUserNameToId(username1);
        Long id2 = this.userService.fromUserNameToId(username2);

        return this.friendshipService.updateFriendship(new Tuple<>(id1,id2), localDateTime);
    }

    /**
     * Get the number of connected components
     * @return the number of connected components
     */
    public int getNumberOfConnectedComponents(){

        Graph graph = new Graph(this.userService.getAll(), this.friendshipService.getAll());

        return graph.connectedComponents().size();
    }

    /**
     * Return the most sociable connection
     * @return the list which contains the users who form the biggest community
     */
    public List<UserDTO> getTheMostSociableConnection(){

        Graph graph = new Graph(this.userService.getAll(), this.friendshipService.getAll());

        List<Long> mostSociable = graph.getTheMostSociableConnection();

        List<UserDTO> result = new ArrayList<>();

        for(Long id : mostSociable){

            User user = this.userService.findOne(id);
            result.add(new UserDTO(id, user.getFirstName(), user.getLastName(), user.getUserName()));
        }

        return result;
    }

    /**
     * Return all the communities
     * @return the list of all the communities found in our network
     */
    public List<List<UserDTO>> getAllConnections(){

        Graph graph = new Graph(this.userService.getAll(), this.friendshipService.getAll());

        List<List<Long>> connections = graph.connectedComponents();
        List<List<UserDTO>> result = new ArrayList<>();

        for(List<Long> connection : connections) {

            List<UserDTO> current = new ArrayList<>();

            for (Long id : connection) {

                User user = this.userService.findOne(id);
                current.add(new UserDTO(id, user.getFirstName(), user.getLastName(), user.getUserName()));
            }

            result.add(current);
        }

        return result;
    }
}