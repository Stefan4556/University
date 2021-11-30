package socialnetwork.service;

import socialnetwork.domain.Request;
import socialnetwork.domain.validators.Validator;
import socialnetwork.repository.Repository;
import socialnetwork.service.ServiceException;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

/**
 * This is the RequestService class which has the connection to the repo and validator
 */
public class RequestService {

    /**
     * The repository of the requests
     */
    private Repository<Long, Request> repo;

    /**
     * The validator of the requests
     */
    private Validator<Request> validator;

    /**
     * The constructor
     * @param repo - The repository of requests
     * @param validator - The validator of requests
     */
    public RequestService(Repository<Long, Request> repo, Validator<Request> validator){

        this.repo = repo;
        this.validator = validator;
    }

    /**
     * This method returns all the requests
     * @return iterable which has requests
     */
    public Iterable<Request> getAll(){

        return this.repo.findAll();
    }

    /**
     * This method returns the id of a reguest
     * @param id1 - id of user 1
     * @param id2 - id of user 2
     * @return the id of a request
     */
    public Long fromIDsToID(Long id1, Long id2){

        for(Request request : this.repo.findAll())

            if((request.getIdUser1().equals(id1) && request.getIdUser2().equals(id2)) || (request.getIdUser1().equals(id2) && request.getIdUser2().equals(id1)))

                return request.getId();

        return null;
    }

    /**
     * This method returns the first available id for a request
     * @return the first available id
     */
    private Long setIdForRequest(){

        Long id = 1L;
        while(this.repo.findOne(id) != null)

            id++;

        return id;
    }

    /**
     * This method adds a request in our requests db
     * @param id1 - id of the first user
     * @param id2 - id of the second user
     */
    public void addRequest(Long id1, Long id2){

        Request request = new Request(this.setIdForRequest(), id1, id2, "pending");

        this.validator.validate(request);

        Long id = fromIDsToID(id1, id2);

        if(id != null)

            throw new ServiceException("There is already a pending request between these users!\n");

        this.repo.save(request);
    }

    /**
     * This method deletes a request between 2 users
     * @param id1 - the id of the first user
     * @param id2 - the id of the second user
     */
    public void deleteRequest(Long id1, Long id2){

        this.validator.validate(new Request(1L, id1, id2, "rejected"));

        Long id = fromIDsToIDOneDirection(id1, id2);

        if(id == null)

            throw new ServiceException("No pending request found between these users!\n");

        this.repo.delete(id);
    }

    /**
     * This method returns all the requests for a user
     * @param id - The id of the user
     * @return an iterable which contains all user's requests
     */
    public Iterable<Request> getAllRequestsForAUser(Long id){

        List<Request> requestList = new ArrayList<>();

        Iterable<Request> requests = this.repo.findAll();

        List<Request> requests1 = new ArrayList<>();
        requests.forEach(requests1::add);

        Predicate<Request> requestPredicate1 = x -> x.getIdUser1().equals(id);
        Predicate<Request> requestPredicate2 = x -> x.getIdUser2().equals(id);
        Predicate<Request> requestPredicate = requestPredicate1.or(requestPredicate2);

        requests1.stream().filter(requestPredicate).forEach(requestList::add);

        return requestList;
    }

    /**
     * This method is for accepting a request between 2 users if it exists
     * @param id1 - The id of the first user
     * @param id2 - The id of the second user
     */
    public void acceptRequest(Long id1, Long id2){

        this.validator.validate(new Request(1L, id1, id2, "approved"));

        Long id = fromIDsToIDOneDirection(id1, id2);

        if(id == null)

            throw new ServiceException("There is no request between these users!\n");

        this.repo.delete(id);
    }

    /**
     * Method for checking if a request exists only one way.
     * @param id1 id of the first user
     * @param id2 id of the second user
     * @return the id of a friendship if it exists; null otherwise
     */
    private Long fromIDsToIDOneDirection(Long id1, Long id2){

        for(Request r : this.repo.findAll())

            if(r.getIdUser1().equals(id1) && r.getIdUser2().equals(id2))

                return r.getId();

        return null;
    }
}
