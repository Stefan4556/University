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
     *
     * @return the find an user query
     */
    @Override
    public String findOneSQL() {

        return "SELECT * FROM users WHERE id = ?;";
    }

    /**
     * Returns the sql query for finding all the users
     * @return the find all query
     */
    @Override
    public String findAllSQL() {

        return "SELECT * FROM users;";
    }

    /**
     * Returns the sql query for saving an user
     *
     * @return the save user query
     */
    @Override
    public String saveSQL() {

        return "INSERT INTO users (id, first_name, last_name, user_name) VALUES (?, ?, ?, ?);";
    }



    /**
     * Returns the sql query for deleting a user
     *
     * @return the delete user query
     */
    @Override
    public String deleteSQL() {

        return "DELETE FROM users WHERE id = ?;";
    }

    /**
     * Returns the sql query for updating a user
     *
     * @return the update user query
     */
    @Override
    public String updateSQL() {

        return "UPDATE users SET first_name = ?, last_name = ?, user_name = ? WHERE id = ?;";
    }

    /**
     * Sets the parameters for the find one prepared statement
     * @param ps - PreparedStatement
     * @param aLong - The id
     */
    @Override
    protected void findOneSet(PreparedStatement ps, Long aLong) {

        try {

            ps.setLong(1, aLong);
        }

        catch (SQLException e) {

            e.printStackTrace();
        }
    }

    /**
     * Sets the parameters for the save prepared statement
     * @param ps - Prepared statement
     * @param entity - The user
     */
    @Override
    protected void saveSet(PreparedStatement ps, User entity) {

        try {

            ps.setLong(1, entity.getId());
            ps.setString(2, entity.getFirstName());
            ps.setString(3, entity.getLastName());
            ps.setString(4, entity.getUserName());
            ps.executeUpdate();
        }

        catch (SQLException e) {

            e.printStackTrace();
        }
    }

    /**
     * Sets the parameters for the delete prepared statement
     * @param ps - Prepared statement
     * @param aLong - The id of the user
     */
    @Override
    protected void deleteSet(PreparedStatement ps, Long aLong) {

        try {

            ps.setLong(1, aLong);
        }

        catch (SQLException e) {

            e.printStackTrace();
        }
    }

    /**
     * Sets the parameters for the update prepared statement
     * @param ps - Prepared statement
     * @param entity - The new user
     */
    @Override
    protected void updateSet(PreparedStatement ps, User entity) {
        try {

            ps.setString(1, entity.getFirstName());
            ps.setString(2, entity.getLastName());
            ps.setString(3, entity.getUserName());
            ps.setLong(4, entity.getId());
        }

        catch (SQLException e) {

            e.printStackTrace();
        }
    }
}
