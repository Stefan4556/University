package socialnetwork.repository.database;

import socialnetwork.domain.Message;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * This class contains all the methods for managing the message repository
 */
public class MessageDB extends AbstractRepoDB<Long, Message> {

    /**
     * The constructor of the class
     *
     * @param url      - String, connection link
     * @param username - String, connection username
     * @param password - String, conneciton password
     */
    public MessageDB(String url, String username, String password) {

        super(url, username, password);
    }

    /**
     * Method which extracts a message from an SQL result set
     * @param resultSet - ResultSet
     * @return the request
     */
    @Override
    protected Message extractEntity(ResultSet resultSet) {


        try {

            List<Long> list = new ArrayList<>();
            Long id = resultSet.getLong(1);

            String sql = "SELECT * FROM messagereceivers WHERE message = ?;";

            Connection connection = DriverManager.getConnection(url, username, password);
            PreparedStatement preparedStatement = connection.prepareStatement(sql);

            preparedStatement.setLong(1, id);

            ResultSet resultSet1 = preparedStatement.executeQuery();

            while (resultSet1.next()) {

                list.add(resultSet1.getLong(2));
            }

            Message m = new Message(id, resultSet.getLong(2), list,
                    resultSet.getString(3), resultSet.getObject(4, LocalDateTime.class));

            if (resultSet.getObject(5) != null)

                m.setOriginalMessage(resultSet.getLong(5));

            return m;

        } catch (SQLException e) {

            e.printStackTrace();
        }

        return null;
    }

    /**
     * Returns the SQL query for finding a message by its id.
     *
     * @return the query for finding a message
     */
    @Override
    protected String findOneSQL() {

        return "SELECT * FROM messagedata WHERE id = ?";
    }

    /**
     * Returns the SQL query for finding all the messages.
     * @return the query for finding all the messages
     */
    @Override
    protected String findAllSQL() {

        return "SELECT * FROM messagedata";
    }

    /**
     * Returns the SQL query for saving a message.
     *
     * @return the query for saving a message
     */
    @Override
    protected String saveSQL() {

        return "INSERT INTO messagedata (id, \"from\", message, date, originalmessage) VALUES (?, ?, ?, ?, ?);";
    }

    /**
     * Returns the SQL query for deleting a message.
     *
     * @return the query for deleting a message
     */
    @Override
    protected String deleteSQL() {

        return "DELETE FROM messagedata WHERE id = ?;";
    }

    /**
     * Returns the SQL query for updating a message.
     *
     * @return the query for updating a message
     */
    @Override
    protected String updateSQL() {

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

        } catch (SQLException e) {

            e.printStackTrace();
        }
    }

    /**
     * Sets the parameters for the save prepared statement
     * @param ps - Prepared statement
     * @param entity - The message
     */
    @Override
    protected void saveSet(PreparedStatement ps, Message entity) {

        try {

            ps.setLong(1, entity.getId());
            ps.setLong(2, entity.getFrom());
            ps.setString(3, entity.getMessage());
            ps.setTimestamp(4, Timestamp.valueOf(entity.getDate()));

            if(entity.getOriginalMessage() == null)

                ps.setNull(5,Types.NULL);

            else

                ps.setLong(5, entity.getOriginalMessage());

            ps.executeUpdate();

            String sql = "INSERT INTO messagereceivers (message, \"to\") VALUES (?, ?)";
            Connection connection = DriverManager.getConnection(url, username, password);
            PreparedStatement preparedStatement = connection.prepareStatement(sql);

            preparedStatement.setLong(1, entity.getId());

            for(Long id : entity.getTo()){

                preparedStatement.setLong(2, id);
                preparedStatement.executeUpdate();
            }

        } catch (SQLException e) {

            e.printStackTrace();
        }
    }

    /**
     * Sets the parameters for the delete prepared statement
     * @param ps - Prepared statement
     * @param aLong - The id of the message
     */
    @Override
    protected void deleteSet(PreparedStatement ps, Long aLong) {

        try {
            ps.setLong(1,aLong);

        } catch (SQLException e) {

            e.printStackTrace();
        }
    }

    /**
     * Sets the parameters for the update prepared statement
     * @param ps - Prepared statement
     * @param entity - The new message
     */
    @Override
    protected void updateSet(PreparedStatement ps, Message entity) {

    }
}
