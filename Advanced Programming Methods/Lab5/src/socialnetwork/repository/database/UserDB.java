package socialnetwork.repository.database;

import socialnetwork.domain.User;

import java.sql.*;

/**
 * The class which represents the repository of users using a database
 */
public class UserDB extends AbstractRepoDB<Long, User> {


    /**
     * The constructor
     * @param url - String, connection link
     * @param username - String, connection username
     * @param password - String, conneciton password
     */
    public UserDB(String url, String username, String password){

        super(url, username, password);
    }

    /**
     * Creates a user from an SQL query result.
     * @param resultSet the result of the SQL query
     * @return the user created from the given result
     */
    @Override
    public User extractEntity(ResultSet resultSet)
    {
        try
        {
            User u = new User(resultSet.getString(2),
                    resultSet.getString(3), resultSet.getString(4));

            u.setId(resultSet.getLong(1));

            return u;
        }

        catch (SQLException e)
        {
            e.printStackTrace();
        }

        return null;
    }

    /**
     * Returns the sql query for finding a user by id
     * @param aLong - Tuple<Long,Long></Long,Long>, the id of the user
     * @return the find an user query
     */
    @Override
    public String findOneSQL(Long aLong) {

        return "SELECT * FROM users WHERE id = " + aLong;
    }

    /**
     * Returns the sql query for finding all the users
     * @return the find all query
     */
    @Override
    public String findAllSQL() {

        return "SELECT * FROM users";
    }

    /**
     * Returns the sql query for saving an user
     * @param entity the user we want to save
     * @return the save user query
     */
    @Override
    public String saveSQL(User entity) {

        return "INSERT INTO users (id, first_name, last_name, user_name) VALUES (" + entity.getId() + ", '" + entity.getFirstName() + "', '" + entity.getLastName() + "', '" + entity.getUserName() + "')";
    }

    /**
     * Returns the sql query for deleting a user
     * @param aLong - the id of the user we want to delete
     * @return the delete user query
     */
    @Override
    public String deleteSQL(Long aLong) {

        return "DELETE FROM users WHERE id = " + aLong;
    }

    /**
     * Returns the sql query for updating a user
     * @param entity - E, the user we want to update
     * @return the update user query
     */
    @Override
    public String updateSQL(User entity) {

        return "UPDATE users SET first_name = '" + entity.getFirstName() + "', last_name = '" + entity.getLastName() + "', user_name = '" + entity.getUserName() + "' WHERE id = " + entity.getId();
    }
}
