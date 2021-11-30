package socialnetwork.domain.validators;

import socialnetwork.domain.Friendship;


/**
 *  FriendshipValidator implements Validator and validates friendships between two users
 */
public class FriendshipValidator implements Validator<Friendship> {

    /**
     * The role of this method is to check if a friendship is valid
     * @param entity entity must not be null
     * @throws ValidationException if the friendship is not valid
     */
    @Override
    public void validate(Friendship entity) throws ValidationException {

        String errors = "";

        if(entity.getId().getLeft().equals(entity.getId().getRight()))

            errors += "You can't have a friendship between identical users!\n";

        if(entity.getId().getLeft() == null || entity.getId().getRight() == null)
            errors += "ID cannot be null!";

        if(!errors.equals(""))

            throw new ValidationException(errors);
    }
}
