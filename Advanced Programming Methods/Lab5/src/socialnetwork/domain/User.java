package socialnetwork.domain;

import java.util.Objects;

/**
 * Cotnains the details of a User
 */
public class User extends Entity<Long>{
    /**
     * The first name of the user.
     */
    private String firstName;

    /**
     * The last name of the user.
     */
    private String lastName;

    /**
     * The username of the user.
     */
    private String userName;

    /**
     * Constructor for user
     * @param firstName - String, the first name of the user
     * @param lastName - String, the last name of the user
     * @param userName - String, the username of the user
     */
    public User(String firstName, String lastName, String userName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.userName = userName;
    }

    /**
     * Getter method for the first name
     * @return the first name of the user
     */
    public String getFirstName() {
        return firstName;
    }

    /**
     * Setter method for the first name
     * @param firstName - the new first name of the user
     */
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    /**
     * Getter method for the last name
     * @return the last name of the user
     */
    public String getLastName() {
        return lastName;
    }

    /**
     * Setter method for the last name
     * @param lastName - the new first name of the user
     */
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    /**
     * Getter method for username
     * @return the username of the user
     */
    public String getUserName() {
        return userName;
    }

    /**
     * Setter methode for username
     * @param newUserName - String, the new username
     */
    public void setUserName(String newUserName){
        this.userName = newUserName;
    }

    /**
     * toString method override
     * @return user as a string
     */
    @Override
    public String toString() {
        return "FirstName = " + firstName +
                ", LastName = " + lastName +
                ", UserName = " + userName;
    }

    /**
     * equals method override
     * @param o - Object
     * @return boolean value
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User)) return false;
        User that = (User) o;
        return getUserName().equals(that.getUserName());
    }

    /**
     * hashCode method override
     * @return hash value for user
     */
    @Override
    public int hashCode() {
        return Objects.hash(getFirstName(), getLastName(), getUserName());
    }
}