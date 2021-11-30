package socialnetwork.service.dto;

/**
 * The class which converts an ID to a User
 */
public class UserDTO {

    /**
     * The id of the user.
     */
    private Long id;

    /**
     * The first name of the user.
     */
    private String firstName;

    /**
     * The last name of the user.
     */
    private String lastName;

    /**
     * The user name of the user.
     */
    private String userName;

    /**
     * The constructor of the class
     * @param id - Long, the id of the user
     * @param fn - String, the first name of the user
     * @param ln - String, the last name of the user
     * @param un - String, the username of the user
     */
    public UserDTO(Long id, String fn, String ln, String un){

        this.id = id;
        this.firstName = fn;
        this.lastName = ln;
        this.userName = un;
    }

    /**
     * Getter method for id
     * @return the id
     */
    public Long getId() {

        return this.id;
    }

    /**
     * Get the first name of a DTO
     * @return the first name
     */
    public String getFirstName() {

        return this.firstName;
    }

    /**
     * Get the last name of a DTO
     * @return the last name
     */
    public String getLastName() {

        return this.lastName;
    }

    /**
     * Get the userName of a DTO
     * @return the username
     */
    public String getUserName() {

        return this.userName;
    }

    /**
     * toString method override
     * @return userDTO as a string
     */
    @Override
    public String toString(){

        return this.firstName + " " + this.lastName;
    }
}
