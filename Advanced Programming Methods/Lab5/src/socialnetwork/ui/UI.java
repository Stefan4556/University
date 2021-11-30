package socialnetwork.ui;

import socialnetwork.domain.validators.ValidationException;

import socialnetwork.service.ServiceException;
import socialnetwork.service.SuperService;
import socialnetwork.service.dto.FriendshipDTO;
import socialnetwork.service.dto.RequestDTO;
import socialnetwork.service.dto.UserDTO;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.format.DateTimeFormatter;
import java.util.List;

/**
 * The class which realises the connection between user and the service
 */
public class UI {

    /**
     * Service for users and friendships
     */
    private SuperService service;

    /**
     * Constructor
     *
     * @param srv - SuperService
     */
    public UI(SuperService srv) {

        this.service = srv;
    }

    /**
     * Method used to print menu
     */
    private void printMenu() {

        System.out.println("\n========== TOY SOCIAL NETWORK ==========");
        System.out.println();
        System.out.println("1) Add user");
        System.out.println("2) Delete user");
        System.out.println("3) Update a user");
        System.out.println("4) Show users list");
        System.out.println("5) Add friendship");
        System.out.println("6) Delete friendship");
        System.out.println("7) Update the date of a friendship");
        System.out.println("8) Show friendships list");
        System.out.println("9) Show the number of communities");
        System.out.println("10) Show the most sociable community");
        System.out.println("11) Show all the communities");
        System.out.println("12) Get all friendships for a user");
        System.out.println("13) Get all friendships for a user filtered by month");
        System.out.println("14) Requests sub-menu");
        System.out.println("15) Messages sub-menu");
        System.out.println("0) Exit");
    }

    /**
     * This method is used for printing the request menu
     */
    private void printRequestMenu(){

        System.out.println("\n======= REQUEST MENU =======");
        System.out.println();
        System.out.println("1) Send friend request");
        System.out.println("2) Delete friend request");
        System.out.println("3) Accept friend request");
        System.out.println("4) Reject friend request");
        System.out.println("5) Show friend requests");
        System.out.println("0) Back");
    }

    /**
     * Method used for printing the message menu commands.
     */
    private void printMessageMenu() {

        System.out.println("\n======= MESSAGE MENU =======\n");
        System.out.println("1) Send Message");
        System.out.println("2) Reply To Message");
        System.out.println("3) Reply To All");
        System.out.println("4) Display All Conversations Between Two Users");
        System.out.println("5) Display All Of The User's Messages");
        System.out.println("0) Back");
    }

    /**
     * Add user
     *
     * @throws IOException if an error occurs while reading
     */
    private void addUser() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the first name: ");
        String firstName = reader.readLine();
        System.out.print("Enter the last name: ");
        String lastName = reader.readLine();
        System.out.print("Enter the username: ");
        String userName = reader.readLine();

        this.service.add(firstName, lastName, userName);
    }

    /**
     * Delete user
     *
     * @throws IOException if an error occurs while reading
     */
    private void deleteUser() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the user's username: ");
        String userName = reader.readLine();
        this.service.remove(userName);
    }

    /**
     * Update a user
     *
     * @throws IOException if an error occurs while reading
     */
    private void updateUser() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the user's username: ");
        String userName = reader.readLine();
        System.out.println("Enter the new user's first name: ");
        String newFirstName = reader.readLine();
        System.out.println("Enter the new user's last name: ");
        String newLastName = reader.readLine();
        System.out.println("Enter the new user's username: ");
        String newUserName = reader.readLine();

        this.service.updateUser(userName, newFirstName, newLastName, newUserName);
    }

    /**
     * Print all the users
     */
    private void printUsers() {

        this.service.getAll().forEach(System.out::println);
    }

    /**
     * Add a friendship
     *
     * @throws IOException if an error occurs while reading
     */
    private void addFriendship() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the username of the first user: ");
        String userName1 = reader.readLine();
        System.out.print("Enter the username of the second user: ");
        String userName2 = reader.readLine();
        this.service.add(userName1, userName2);
    }

    /**
     * Delete a friendship
     *
     * @throws IOException if an error occurs while reading
     */
    private void deleteFriendship() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the username of the first user: ");
        String userName1 = reader.readLine();
        System.out.print("Enter the username of the second user: ");
        String userName2 = reader.readLine();
        this.service.remove(userName1, userName2);
    }

    /**
     * Update a friendship
     *
     * @throws IOException if an error occurs while reading
     */
    private void updateFriendship() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the username of the first user: ");
        String username1 = reader.readLine();
        System.out.print("Enter the username of the second user: ");
        String username2 = reader.readLine();
        System.out.print("Enter the date(yyyy-MM-dd HH:mm): ");
        String date = reader.readLine();
        this.service.updateFriendship(username1, username2, date);
    }

    /**
     * Print all the friendships
     */
    private void printFriendships() {

        this.service.getAllFriendships().forEach(System.out::println);
    }

    /**
     * Get the number of communities
     */
    private void getNumberOfCommunities() {

        int number = this.service.getNumberOfConnectedComponents();

        System.out.println("The number of communities is " + number + "\n");
    }

    /**
     * Get the most sociable community
     */
    private void getTheMostSociableCommunity() {

        List<UserDTO> theMostSociableCommunity = this.service.getTheMostSociableConnection();

        System.out.print("The most sociable community is formed by: ");

        for (UserDTO user : theMostSociableCommunity)

            System.out.print(user.getUserName() + " ");

        System.out.println();
    }

    /**
     * Print all the communities that we have in our network
     */
    private void showAllTheCommunities() {

        List<List<UserDTO>> allCommunities = this.service.getAllConnections();
        int ct = 1;
        for (List<UserDTO> community : allCommunities) {
            System.out.print("Community " + ct + " is formed by: ");
            for (UserDTO user : community)
                System.out.print(user.getUserName() + " ");
            System.out.println();
            ct++;
        }
    }

    /**
     * Method used for getting all friendships of a user
     * @throws IOException - if an error occurs while reading
     */
    private void getAllFriendshipsForAUser() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the username of the user: ");
        String username = reader.readLine();
        List<FriendshipDTO> friendshipDTOList = this.service.getAllFriendshipsForAUser(username);

        System.out.println("The friendships of " + friendshipDTOList.get(0).getUser1().getFirstName() + " " + friendshipDTOList.get(0).getUser1().getLastName() + " are: ");
        for (FriendshipDTO f : friendshipDTOList) {

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
            System.out.println(f.getUser2().getFirstName() + " | " + f.getUser2().getLastName() + " | " + f.getDate().format(formatter));
        }

    }

    /**
     * Method used for getting all the friendships from a month
     * @throws IOException if an error occurs while reading
     */
    private void getFriendshipsFromMonth() throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter the user's username: ");
        String userName = reader.readLine();

        System.out.print("Enter the month (as a word): ");
        String month = reader.readLine();

        final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

        List<FriendshipDTO> friendshipDTOs = this.service.getFriendshipsFromMonth(userName, month);

        System.out.println("The friendships of user " + friendshipDTOs.get(0).getUser1().getFirstName() + " " + friendshipDTOs.get(0).getUser1().getLastName() + " on month " + month + " are: ");
        for(FriendshipDTO friendshipDTO: friendshipDTOs)

            System.out.println(friendshipDTO.getUser2().getFirstName() + " | " + friendshipDTO.getUser2().getLastName() + " | " + friendshipDTO.getDate().format(formatter));

    }

    /**
     * UI method for sending friend requests.
     *
     * @param from the username of the user that sends the request
     * @throws IOException if an error occurs while reading
     */
    private void sendFriendRequest(String from) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the target user's username: ");
        String to = reader.readLine();
        this.service.addRequest(from, to);
    }

    /**
     * UI method for deleting friend requests.
     *
     * @param from the username of the user that deletes the request
     * @throws IOException if an error occurs while reading
     */
    private void deleteFriendRequest(String from) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the target user's username: ");
        String to = reader.readLine();
        this.service.deleteRequest(from, to);
    }

    /**
     * UI method for accepting friend requests.
     *
     * @param to the username of the user that accepts the request
     * @throws IOException if an error occurs while reading
     */
    private void acceptFriendRequest(String to) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the sender's username: ");
        String from = reader.readLine();
        this.service.acceptRequest(from, to);
    }

    /**
     * UI method for rejecting friend requests.
     *
     * @param to the username of the user that rejects the request
     * @throws IOException if an error occurs while reading
     */
    private void rejectFriendRequest(String to) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the sender's username: ");
        String from = reader.readLine();
        this.service.rejectRequest(from, to);
    }

    /**
     * Prints all requests for an user.
     *
     * @param username the username of the user
     * @throws IOException if an error occurs while reading
     */
    private void showAllRequestsForUser(String username) throws IOException {

        List<RequestDTO> requestDTOList = this.service.getAllRequestsForAUser(username);

        if(requestDTOList.size() == 0) {

            System.out.println("No requests found!");
            return;
        }

        requestDTOList.forEach(System.out::println);
    }

    /**
     * Request menu method.
     *
     * @throws IOException if an error occurs while reading
     */
    private void requestMenu() throws IOException {

        System.out.print("Enter the user's username: ");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String username = reader.readLine();

        this.service.getAllRequestsForAUser(username);

        while (true) {

            this.printRequestMenu();
            System.out.print("Enter the command: ");
            try {

                String command = reader.readLine();
                switch (command) {

                    case "1" -> {
                        this.sendFriendRequest(username);
                        System.out.println("Request sent!");
                    }

                    case "2" -> {
                        this.deleteFriendRequest(username);
                        System.out.println("Request deleted!");
                    }

                    case "3" -> {
                        this.acceptFriendRequest(username);
                        System.out.println("Request accepted!");
                    }

                    case "4" -> {
                        this.rejectFriendRequest(username);
                        System.out.println("Request rejected");
                    }

                    case "5" -> this.showAllRequestsForUser(username);

                    case "0" -> {
                        System.out.println("Returning to main menu...");
                        return;
                    }

                    default -> System.out.println("Wrong command!");
                }
            }

            catch (IOException e) {

                e.printStackTrace();
            }

            catch (ValidationException | IllegalArgumentException | ServiceException e){

                System.out.println(e.getMessage());
            }
        }
    }

    /**
     * UI method for sending messages.
     *
     * @param from the username of the user that sends the message
     * @throws IOException if an error occurs while reading
     */
    private void sendMessage(String from) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the target users' usernames, separated by a space: ");
        String to = reader.readLine();

        System.out.print("Enter the message: ");
        String message = reader.readLine();

        List<String> toList = List.of(to.split(" "));
        this.service.addMessage(message, from, toList);
    }

    /**
     * UI method for replying to messages.
     *
     * @param userName the username of the user
     * @throws IOException if an error occurs while reading
     */
    private void replyToMessage(String userName) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the ID of the message you want to reply to: ");
        String idString = reader.readLine();

        System.out.print("Enter the reply message: ");
        String message = reader.readLine();

        this.service.replyToMessage(idString, message, userName);
    }

    private void replyToAll(String userName) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the ID of the messages to reply all to: ");
        String idString = reader.readLine();

        System.out.print("Enter the reply message: ");
        String message = reader.readLine();

        this.service.replyToAll(idString, message, userName);
    }

    /**
     * UI method for displaying a user's messages.
     *
     * @param userName the username of the user
     * @throws IOException if an error occurs while reading
     */
    private void getAllMessagesForAUser(String userName) throws IOException {

        this.service.getAllMessagesForAUser(userName).forEach(System.out::println);
    }

    /**
     * UI method for displaying two users' conversations.
     *
     * @param userName the username of the user
     * @throws IOException if an error occurs while reading
     */
    private void getAllConversations(String userName) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the username of the other user: ");
        String other = reader.readLine();

        System.out.println("These users' conversations are:");
        this.service.getConversations(userName, other).forEach(System.out::println);
    }

    /**
     * Message menu method.
     *
     * @throws IOException if an error occurs while reading
     */
    private void messageMenu() throws IOException {

        System.out.print("Enter the user's username: ");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String userName = reader.readLine();

        //this.getAllMessagesForAUser(userName);

        while (true) {

            this.printMessageMenu();
            System.out.print("Enter the command: ");

            try {

                String command = reader.readLine();
                switch (command) {

                    case "1" -> {

                        this.sendMessage(userName);
                        System.out.println("Message sent!");
                    }

                    case "2" -> {

                        this.replyToMessage(userName);
                        System.out.println("Reply sent!");
                    }

                    case "3" -> {

                        this.replyToAll(userName);
                        System.out.println("Reply sent to all!");
                    }

                    case "4" -> this.getAllConversations(userName);
                    case "5" -> this.getAllMessagesForAUser(userName);

                    case "0" -> {

                        System.out.println("Returning to main menu...");
                        return;
                    }

                    default -> System.out.println("Incorrect command!");
                }
            }

            catch (IOException ex) {

                ex.printStackTrace();
            }

            catch (ValidationException | IllegalArgumentException | ServiceException e){

                System.out.println(e.getMessage());
            }
        }
    }

    /**
     * The method which starts our application
     */
    public void run() {

        while (true) {

            printMenu();
            System.out.print("\n Enter the command: ");
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            try {
                String option = reader.readLine();

                switch (option) {
                    case "1" -> {
                        this.addUser();
                        System.out.println("User added!");
                    }

                    case "2" -> {
                        this.deleteUser();
                        System.out.println("The user has been deleted!");
                    }

                    case "3" -> {
                        updateUser();
                        System.out.println("The user has been updated!");
                    }

                    case "4" -> printUsers();

                    case "5" -> {
                        addFriendship();
                        System.out.println("Friendship added!");
                    }

                    case "6" -> {
                        deleteFriendship();
                        System.out.println("The friendship has been deleted!");
                    }

                    case "7" -> {
                        updateFriendship();
                        System.out.println("The friendships has been updated!");
                    }

                    case "8" -> printFriendships();
                    case "9" -> getNumberOfCommunities();
                    case "10" -> getTheMostSociableCommunity();
                    case "11" -> showAllTheCommunities();
                    case "12" -> getAllFriendshipsForAUser();
                    case "13" -> getFriendshipsFromMonth();
                    case "14" -> requestMenu();
                    case "15" -> messageMenu();

                    case "0" -> {
                        System.out.println("Have a great day!");
                        return;
                    }
                    default -> System.out.println("Incorrect command!\n");
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ValidationException | IllegalArgumentException | ServiceException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}