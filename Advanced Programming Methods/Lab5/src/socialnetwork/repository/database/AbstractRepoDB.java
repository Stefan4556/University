package socialnetwork.repository.database;

import socialnetwork.domain.Entity;
import socialnetwork.repository.Repository;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;

/**
 * This is the AbstractDBRepo class which implements the interface Repository and defines some abstract methods
 * @param <ID> - type E must have an attribute of type ID
 * @param <E> -  type of entities saved in repository
 */
public abstract class AbstractRepoDB<ID, E extends Entity<ID>> implements Repository<ID,E> {

    /**
     * The url for the database connection.
     */
    private String url;

    /**
     * The username for the database connection.
     */
    private String username;

    /**
     * The password for the database connection.
     */
    private String password;

    /**
     * The constructor of the class
     * @param url - String, connection link
     * @param username - String, connection username
     * @param password - String, conneciton password
     */
    public AbstractRepoDB(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    /**
     * Method which extracts entity from a result set
     * @param resultSet - ResultSet
     * @return the entity
     */
    public abstract E extractEntity(ResultSet resultSet);

    /**
     * Returns the sql query for finding an entity by id
     * @param id - ID, the id of the entity
     * @return the find an entity query
     */
    public abstract String findOneSQL(ID id);   // sa nu primeasca id ca param

    /**
     * Returns the sql query for finding all the entities
     * @return the find all query
     */
    public abstract String findAllSQL();

    /**
     * Returns the sql query for saving an entity
     * @param entity the entity we want to save
     * @return the save entity query
     */
    public abstract String saveSQL(E entity);

    /**
     * Returns the sql query for deleting an entity
     * @param id - ID, the id of the entity we want to delete
     * @return the delete entity query
     */
    public abstract String deleteSQL(ID id);

    /**
     * Returns the sql query for updating an entity
     * @param entity - E, the entity we want to update
     * @return the update entity query
     */
    public abstract String updateSQL(E entity);

    /**
     * Find an entity by id
     * @param id -the id of the entity to be returned
     *           id must not be null
     * @return entity if we find it
     *         null if we dont find it
     * @throws IllegalArgumentException if the id is null
     */
    @Override
    public E findOne(ID id) {

        if(id == null)

            throw new IllegalArgumentException("ID must not be null!\n");

        String sql = this.findOneSQL(id);

        try(Connection connection = DriverManager.getConnection(url, username,password);
            PreparedStatement statement = connection.prepareStatement(sql)) {

            ResultSet resultSet = statement.executeQuery();

            if(resultSet.next())

                return extractEntity(resultSet);

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        return null;
    }

    /**
     * Return all entities
     * @return the iterable which contains entities
     */
    @Override
    public Iterable<E> findAll() {

        Set<E> entities = new HashSet<>();

        String sql = this.findAllSQL();

        try(Connection connection = DriverManager.getConnection(url, username, password);
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet resultSet = statement.executeQuery()) {

            while(resultSet.next()){

                E e = extractEntity(resultSet);
                entities.add(e);
            }
            return entities;

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        return entities;
    }

    /**
     * The role of this method is to save an entity in the db
     * @param entity - The entity we want to add
     *         entity must be not null
     * @return null if the save was done successfully
     * @throws IllegalArgumentException if entity = null
     */
    @Override
    public E save(E entity) {

        if(entity == null)

            throw new IllegalArgumentException("Entity must not be null!\n");

        String sql = this.saveSQL(entity);

        try(Connection connection = DriverManager.getConnection(url,username,password);
            PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.executeUpdate();

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        return null;
    }

    /**
     * The role of this method is to delete an entity from the db
     * @param id - the id of the entity
     *      id must be not null
     * @return null if the friendship was deleted successfully
     * @throws IllegalArgumentException if the entity is null
     */
    @Override
    public E delete(ID id) {

        if(id == null)

            throw new IllegalArgumentException("ID must not be null!\n");

        String sql = this.deleteSQL(id);

        try(Connection connection = DriverManager.getConnection(url,username,password);
            PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.executeUpdate();

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        return null;
    }

    /**
     * The role of this method is to update an entity from the db
     * @param entity - The entity we want to delete it
     *          entity must not be null
     * @return null if the entity was updated successfully
     * @throws IllegalArgumentException if the entity is null
     */
    @Override
    public E update(E entity) {

        if(entity == null)

            throw new IllegalArgumentException("Entity must not be null!\n");

        String sql = this.updateSQL(entity);

        try(Connection connection = DriverManager.getConnection(url,username,password);
            PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.executeUpdate();

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        return null;
    }

}
