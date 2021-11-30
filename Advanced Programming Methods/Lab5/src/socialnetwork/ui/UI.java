package socialnetwork.ui;

import socialnetwork.domain.validators.ValidationException;

import socialnetwork.service.ServiceException;
import socialnetwork.service.SuperService;
import socialnetwork.service.dto.UserDTO;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
     * @param srv - SuperService
     */
    public UI(SuperService srv){

        this.service = srv;
    }

    /**
     * Method used to print menu
     */
    private void printMenu(){

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
        System.out.println("12) Exit");
    }

    /**
     * Add user
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
     * @return null if the user was deleted successfully
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
     * @return null if the user was updated successfully
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
    private void printUsers(){

        this.service.getAll().forEach(System.out::println);
    }

    /**
     * Add a friendship
     * @return null if the friendship was added succesfully
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
     * @return null if the friendship was deleted
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
     * @return null if the friendship was updated successfully
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
    private void printFriendships(){

        this.service.getAllFriendships().forEach(System.out::println);
    }

    /**
     * Get the number of communities
     */
    private void getNumberOfCommunities(){

        int number = this.service.getNumberOfConnectedComponents();

        System.out.println("The number of communities is " + number + "\n");
    }

    /**
     * Get the most sociable community
     */
    private void getTheMostSociableCommunity(){

        List<UserDTO> theMostSociableCommunity = this.service.getTheMostSociableConnection();

        System.out.print("The most sociable community is formed by: ");

        for(UserDTO user : theMostSociableCommunity)

            System.out.print(user.getUserName() + " ");

        System.out.println();
    }

    /**
     * Print all the communities that we have in our network
     */
    private void showAllTheCommunities(){

        List<List<UserDTO>> allCommunities = this.service.getAllConnections();
        int ct = 1;
        for(List<UserDTO> community : allCommunities){
            System.out.print("Community " + ct + " is formed by: ");
            for(UserDTO user : community)
                System.out.print(user.getUserName() + " ");
            System.out.println();
            ct++;
        }
    }

    /**
     * The method which starts our application
     */
    public void run(){

        while(true){

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
                    case "12" -> {
                        System.out.println("Have a great day!");
                        return;
                    }
                    default -> System.out.println("Incorrect command!\n");
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch(ValidationException | IllegalArgumentException | ServiceException e){
                System.out.println(e.getMessage());
            }
        }
    }
}