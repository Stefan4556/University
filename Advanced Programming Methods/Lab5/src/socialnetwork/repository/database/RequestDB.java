package socialnetwork.repository.database;

import socialnetwork.domain.Request;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.time.LocalDateTime;

public class RequestDB extends AbstractRepoDB<Long, Request> {

    /**
     * Constructor for RequestDB class.
     * @param url connection url
     * @param username connection username
     * @param password connection password
     */
    public RequestDB(String url, String username, String password) {

        super(url, username, password);
    }

    /**
     * Method which extracts a request from an SQL result set
     * @param resultSet - ResultSet
     * @return the request
     */
    @Override
    public Request extractEntity(ResultSet resultSet) {

        try {

            return new Request(resultSet.getLong(1), resultSet.getLong(2), resultSet.getLong(3),
                    resultSet.getObject(4, LocalDateTime.class), resultSet.getString(5));
        }

        catch(SQLException ex) {
            ex.printStackTrace();
        }

        return null;
    }

    /**
     * Returns the SQL query for finding a request by its id.
     *
     * @return the query for finding a request
     */
    @Override
    public String findOneSQL() {

        return "SELECT * FROM requests WHERE id = ?;";
    }

    /**
     * Returns the SQL query for finding all the requests.
     * @return the query for finding all the requests
     */
    @Override
    public String findAllSQL() {

        return "SELECT * FROM requests";
    }

    /**
     * Returns the SQL query for saving a request.
     *
     * @return the query for saving a request
     */
    @Override
    public String saveSQL() {

        return "INSERT INTO requests(id, id1, id2, date, status) VALUES(?, ?, ?, ?, ?);";
    }

    /**
     * Returns the SQL query for deleting a request.
     *
     * @return the query for deleting a request
     */
    @Override
    public String deleteSQL() {

        return "DELETE FROM requests WHERE id = ?;";
    }

    /**
     * Returns the SQL query for updating a request.
     *
     * @return the query for updating a request
     */
    @Override
    public String updateSQL() {

        return null;
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
     * @param entity - The request
     */
    @Override
    protected void saveSet(PreparedStatement ps, Request entity) {

        try {

            ps.setLong(1, entity.getId());
            ps.setLong(2, entity.getIdUser1());
            ps.setLong(3, entity.getIdUser2());
            ps.setTimestamp(4, Timestamp.valueOf(entity.getDate()));
            ps.setString(5, entity.getStatus().getStatus());

            ps.executeUpdate();
        }

        catch (SQLException e) {

            e.printStackTrace();
        }

    }

    /**
     * Sets the parameters for the delete prepared statement
     * @param ps - Prepared statement
     * @param aLong - The id of the request
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
     * @param entity - The new request
     */
    @Override
    protected void updateSet(PreparedStatement ps, Request entity) {

    }
}
