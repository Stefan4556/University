package socialnetwork.service;

import socialnetwork.domain.Message;
import socialnetwork.domain.validators.MessageValidator;
import socialnetwork.repository.Repository;

import java.time.LocalDateTime;
import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class MessageService {

    /**
     * Message repository.
     */
    private Repository<Long, Message> repo;

    /**
     * Message validator.
     */
    private MessageValidator validator;

    /**
     * Constructor for Message Service class.
     * @param repo the message repository
     * @param validator the message validator
     */
    public MessageService(Repository<Long, Message> repo, MessageValidator validator) {

        this.repo = repo;
        this.validator = validator;
    }

    /**
     *
     * @return all the messages
     */
    public Iterable<Message> getAll() {

        return this.repo.findAll();
    }

    /**
     * Gets all the messages that a user either sent or received.
     * @param id the id of the user
     * @return a list of messages
     */
    public List<Message> getMessagesForAUser(Long id) {

        Iterable<Message> messages = this.repo.findAll();

        List<Message> result = new ArrayList<Message>();

        for (Message message: messages) {

            if(message.getFrom().equals(id) || message.getTo().contains(id))

                result.add(message);
        }

        result.sort(Comparator.comparing(Message::getDate).reversed());

        return result;
    }

    /**
     * Gets all the conversations between two users.
     * @param id1 the id of the first user
     * @param id2 the id of the second user
     * @return a list of messages
     */
    public List<Message> getConversations(Long id1, Long id2) {

        Iterable<Message> messages = this.repo.findAll();

        List<Message> result = new ArrayList<Message>();

        for (Message message: messages) {

            if((message.getFrom().equals(id1) && message.getTo().contains(id2)) || (message.getFrom().equals(id2)  && message.getTo().contains(id1)))

                result.add(message);
        }

        result.sort(Comparator.comparing(Message::getDate).reversed());

        return result;
    }

    /**
     * Creates an id for a new request.
     * @return an id
     */
    private Long setIdForMessage() {

        Long id = 1L;
        while(this.repo.findOne(id) != null)

            id++;

        return id;
    }

    /**
     * Adds a message from a sender to multiple receivers.
     * @param from the id of the sender
     * @param to the list of ids of the receivers
     * @param messageString the message
     */
    public void addMessage(Long from, List<Long> to, String messageString) {

        Message message = new Message(this.setIdForMessage(), from, to, messageString, LocalDateTime.now());

        this.validator.validate(message);

        this.repo.save(message);
    }

    /**
     * The role of this method is to save a reply to a message
     * @param messageID - The message id
     * @param message - The content of the message
     * @param sender - The id of the sender
     * @throws ServiceException if there is no message with the id given as parameter
     */
    public void replyToMessage(Long messageID, String message, Long sender){

        this.validator.validate(new Message(messageID, sender, Arrays.asList(1L), message));

        Message message1 = this.repo.findOne(messageID);

        if (message1 == null)

            throw new ServiceException("No message found with the id that you've entered!\n");

        if (sender.equals(message1.getFrom()))

            throw new ServiceException("You cannot reply to yourself!\n");

        Message message2 = new Message(this.setIdForMessage(), sender, List.of(message1.getFrom()), message);
        message2.setOriginalMessage(messageID);

        this.repo.save(message2);
    }

    public void replyToAll(Long messageID, String message, Long sender) {

        this.validator.validate(new Message(messageID, sender, List.of(1L), message));

        Message message1 = this.repo.findOne(messageID);

        if (message1 == null)

            throw new ServiceException("No message found with the id that you've entered!\n");

        if (sender.equals(message1.getFrom()))

            throw new ServiceException("You cannot reply to yourself!\n");

        Predicate<Long> predicate = x -> !x.equals(sender);

        List<Long> list = message1.getTo().stream().filter(predicate).collect(Collectors.toList());
        list.add(message1.getFrom());

        Message message2 = new Message(this.setIdForMessage(), sender, list, message);

        message2.setOriginalMessage(messageID);

        this.repo.save(message2);
    }
}
