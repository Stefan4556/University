package socialnetwork.service;

import socialnetwork.domain.User;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.domain.validators.ValidationException;
import socialnetwork.repository.Repository;

/**
 * Class which handles users
 */
public class UserService {
    /**
     * User repository
     */
    private Repository<Long, User> repo;

    /**
     * User validator.
     */
    private UserValidator validator;

    /**
     * Constructor
     * @param repo - Repository0<Long,User></Long,User>, the connection to the user repo
     * @param validator - UserValidator, the validator of the User
     */
    public UserService(Repository<Long, User> repo, UserValidator validator) {

        this.repo = repo;
        this.validator = validator;
    }

    /**
     *  Method for adding a user
     * @param user - User, the user we want to add
     * @return null
     * @throws ValidationException if the user is not valid
     * @throws ServiceException if the a user with the same username already exists
     */
    public User addUser(User user) {
        this.validator.validate(user);   // validator
        this.checkUniqueUserName(user.getUserName()); // business
        this.setIdForUser(user);
        User task = repo.save(user);
        return task;
    }

    /**
     * Get all the users
     * @return all the users
     */
    public Iterable<User> getAll(){

        return repo.findAll();
    }

    /**
     * Delete a user
     * @param userName - String, the username of the user we want to delte
     * @return null
     * @throws ValidationException if the username is not valid
     * @throws ServiceException if there is no user with the username
     */
    public User deleteUser(String userName){

        User u = new User("a","a",userName);
        u.setId(1L);
        this.validator.validate(u);
        Long id = this.fromUserNameToId(userName);
        if(id == null)
            throw new ServiceException("No user found with the username that you've entered!");

        return repo.delete(id);
    }

    /**
     * Method used for updating all users fields
     * @param oldUsername - String, the old username of the user
     * @param newFirstName - String, the new first name of the user
     * @param newLastName - String, the new last name of the user
     * @param newUserName - String, the new username of the user
     * @return null
     * @throws ServiceException if the old username is invalid or no user found with old username
     * @throws ValidationException if the new fields of the user are invalid
     */
    public User updateUser(String oldUsername, String newFirstName, String newLastName, String newUserName){

        User user = new User("a","a",oldUsername);

        try {
            this.validator.validate(user);
        }
        catch(ValidationException err) {
            throw new ServiceException("Old username is invalid!\n");
        }

        user = new User(newFirstName, newLastName, newUserName);
        this.validator.validate(user);

        this.checkUniqueUserName(newUserName);

        Long id = this.fromUserNameToId(oldUsername);

        if(id == null)
            throw new ServiceException("No user found with the username that you've entered!\n");
        user.setId(id);

        return this.repo.update(user);
    }

    /**
     * Set the id for an user given as an argument
     * @param user - User
     */
    private void setIdForUser(User user) {

        Long id = 1L;
        User u = this.repo.findOne(id);
        while(u != null) { // means already exists
            id++;
            u = this.repo.findOne(id);
        }
        user.setId(id);
    }

    /**
     * Returns the id of a user which has a specific username
     * @param userName - String, the username we are looking for
     * @return id, if the user is found
     *         null, otherwise
     */
    public Long fromUserNameToId(String userName){
        Iterable<User> users = this.repo.findAll();
        for(User user : users)

            if(user.getUserName().equals(userName))

                return user.getId();

        return null;
    }

    /**
     * Check if a username is unique
     * @param userName - String, the username we are searching for
     * @throws ServiceException if the username is not unique
     */
    public void checkUniqueUserName(String userName){

        Iterable<User> users = this.repo.findAll();
        for(User user : users)

            if(user.getUserName().equals(userName))

                throw new ServiceException("It already exists one user with this username!\n");
    }

    /**
     * Get user by id
     * @param id - Long, the user id
     * @return the user having the id given as parameter
     */
    public User findOne(Long id){

        return this.repo.findOne(id);
    }

    /**
     * Validate one or more usernames
     * @param userNames - String[], containing usernames which we want to check if they are valid or not
     * @throws ServiceException if the usernames / usernames are not valid
     */
    public void validateUsernameOrUsernames(String ... userNames) {

        if(userNames.length == 1){

            User u = new User("a","a",userNames[0]);
            u.setId(1L);
            this.validator.validate(u);
        }

        else if(userNames.length == 2){

            String erori = "";
            User u1 = new User("a","a",userNames[0]);
            u1.setId(1L);
            User u2 = new User("a","a",userNames[1]);
            u2.setId(2L);

            try{
                this.validator.validate(u1);
            }catch(ValidationException e){
                erori += "First username can't be empty!\n";
            }
            try{
                this.validator.validate(u2);
            }

            catch(ValidationException e){
                erori += "Second username can't be empty!\n";
            }

            if(!erori.equals(""))

                throw new ServiceException(erori);
        }
    }
}
