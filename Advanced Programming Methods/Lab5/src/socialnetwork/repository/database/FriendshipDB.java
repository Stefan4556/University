package socialnetwork.repository.database;

import socialnetwork.domain.Friendship;
import socialnetwork.domain.Tuple;

import java.sql.*;
import java.time.LocalDateTime;

/**
 * The class which represents the repository of friendships using a database
 */
public class FriendshipDB extends AbstractRepoDB<Tuple<Long,Long>, Friendship> {


    /**
     * The constructor
     * @param url - String, connection link
     * @param username - String, connection username
     * @param password - String, conneciton password
     */
    public FriendshipDB(String url, String username, String password){

        super(url, username, password);
    }

    /**
     * Method which extract a friendship from a result set
     * @param resultSet - ResultSet
     * @return the friendship
     */
    @Override
    public Friendship extractEntity(ResultSet resultSet)
    {
        try
        {
            return new Friendship(resultSet.getLong(1), resultSet.getLong(2),
                    resultSet.getObject(3, LocalDateTime.class));
        }

        catch (SQLException e)
        {
            e.printStackTrace();
        }

        /// TODO: poate trebuie schimbat
        return null;
    }

    /**
     * Returns the sql query for finding a friendship by id
     * @param longLongTuple - Tuple<Long,Long></Long,Long>, the id of the friendship
     * @return the find a friendship query
     */
    @Override
    public String findOneSQL(Tuple<Long, Long> longLongTuple) {

        return "SELECT * FROM friendships WHERE id1 = " + longLongTuple.getLeft() + " and id2 = " + longLongTuple.getRight();
    }

    /**
     * Returns the sql query for finding all the friendships
     * @return the find all query
     */
    @Override
    public String findAllSQL() {
        return "SELECT * FROM friendships";
    }

    /**
     * Returns the sql query for saving a friendship
     * @param entity the friendship we want to save
     * @return the save friendship query
     */
    @Override
    public String saveSQL(Friendship entity) {
        Timestamp timestamp = Timestamp.valueOf(entity.getDate());
        return "INSERT INTO friendships (id1, id2, date) VALUES ( " + entity.getId().getLeft() + ", " + entity.getId().getRight() + ", '" + timestamp.toString() + "'::timestamp )";
    }

    /**
     * Returns the sql query for deleting a friendship
     * @param longLongTuple - the id of the friendship we want to delete
     * @return the delete friendship query
     */
    @Override
    public String deleteSQL(Tuple<Long, Long> longLongTuple) {
        return "DELETE FROM friendships WHERE id1 = " + longLongTuple.getLeft() + " and id2 = " + longLongTuple.getRight();
    }

    /**
     * Returns the sql query for updating a friendship
     * @param entity - E, the friendship we want to update
     * @return the update friendship query
     */
    @Override
    public String updateSQL(Friendship entity) {
        return "UPDATE friendships SET date = '" + Timestamp.valueOf(entity.getDate()) + "'::timestamp WHERE id1 = " + entity.getId().getLeft() + " and id2 = " + entity.getId().getRight();
    }
}
