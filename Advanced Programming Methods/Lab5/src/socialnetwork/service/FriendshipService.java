package socialnetwork.service;

import socialnetwork.domain.Friendship;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.repository.Repository;
import socialnetwork.domain.validators.ValidationException;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.LinkedList;
import java.util.List;

/**
 * Class which handles friendships
 */
public class FriendshipService {

    /**
     * Friendship repository
     */
    private Repository<Tuple<Long,Long>, Friendship> repo;

    /**
     * Friendship validator
     */
    private FriendshipValidator validator;

    /**
     * Constructor
     * @param repo - Repository0<Tuple<Long,Long></Long,Long>>, the connection to the repo
     * @param validator - FriendshipValidator, the validator of Friendship
     */
    public FriendshipService(Repository<Tuple<Long,Long>, Friendship> repo, FriendshipValidator validator){

        this.repo = repo;
        this.validator = validator;
    }

    /**
     * Get all friendships
     * @return all the Friendships
     */
    public Iterable<Friendship> getAll() {

        return repo.findAll();
    }

    /**
     * Add a friendship
     * @param friendship - Friendship, the friendship we want to add
     * @return null
     * @throws ValidationException if the Friendship is not valid
     * @throws ServiceException if the Friendships already exists
     */
    public Friendship addFriendship(Friendship friendship) {

        this.validator.validate(friendship);
        this.friendshipAlreadyExists(friendship);
        Friendship f = repo.save(friendship);
        return f;
    }

    /**
     * Delete a friendship
     * @param id - Tuple<Long,Long></Long,Long>, representing the IDs of the users-
     * @return null
     * @throws ValidationException if the friendship is not valid
     * @throws ServiceException if the friendship doesn't exist
     */
    public Friendship deleteFriendship(Tuple<Long,Long> id) {

        this.validator.validate(new Friendship(id.getLeft(), id.getRight()));

        if(id.getLeft() > id.getRight()){
            Long aux = id.getLeft();
            id.setLeft(id.getRight());
            id.setRight(aux);
        }

        Friendship connection = this.repo.findOne(id);
        if (connection == null)
            throw new ServiceException("There is no friendship between those 2 users!\n");

        Friendship f = repo.delete(id);
        return f;
    }

    /**
     * Get the friendship which has the id equal to the id given as parameter
     * @param id - Tuple<Long,Long></Long,Long>, the id
     * @return the friendship which has the id equal to the one is given as parameter
     */
    public Friendship findOne(Tuple<Long, Long> id){

        return this.repo.findOne(id);
    }

    /**
     * The role of this method is to update the date of a friendship
     * @param id the id of the friendship
     * @param date the date new date
     * @return null
     * @throws ValidationException if the friendship is not valid
     * @throws ServiceException if there is no friendship with the entered id
     */
    public Friendship updateFriendship(Tuple<Long, Long> id, String date) {

        LocalDateTime localDateTime;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

        try {

            localDateTime = LocalDateTime.parse(date, formatter);
        }

        catch (DateTimeParseException err) {

            throw new ServiceException("Invalid date!\n");
        }

        this.validator.validate(new Friendship(id.getLeft(), id.getRight(), localDateTime));

        if(id.getLeft() > id.getRight()){
            Long aux = id.getLeft();
            id.setLeft(id.getRight());
            id.setRight(aux);
        }

        Friendship connection = this.repo.findOne(id);
        if (connection == null)
            throw new ServiceException("Their is no friendship between those 2 users!\n");

        connection.setDate(localDateTime);
        return this.repo.update(connection);
    }

    /**
     * Check if a friendship already exists
     * @param friendship - Friendship, the friendship we are checking
     * @throws ServiceException if the friendship exists
     */
    public void friendshipAlreadyExists(Friendship friendship) {

        Iterable<Friendship> friendships = this.repo.findAll();
        for(Friendship f : friendships)

            if(f.equals(friendship))

                throw new ServiceException("Friendship already exists!\n");
    }
}
