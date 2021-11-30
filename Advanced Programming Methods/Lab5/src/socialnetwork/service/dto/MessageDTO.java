package socialnetwork.service.dto;

import java.time.LocalDateTime;
import java.util.List;

public class MessageDTO {

    /**
     * The id of the message
     */
    private Long id;
    
    /**
     * The user who sent the message
     */
    private UserDTO from;

    /**
     * The users list of the receivers of the message
     */
    private List<UserDTO> to;

    /**
     * The content of the message
     */
    private String message;

    /**
     * The date when the message was sent
     */
    private LocalDateTime date;

    /**
     * The message which we answer to
     */
    private Long originalMessage;

    /**
     * The constructor of the class
     * @param id - The id of the message
     * @param from - The user who sent the message
     * @param to - The list of users who received this message
     * @param message - The content of the message
     * @param date - The date of the message
     * @param originalMessage - The id of the original message
     */
    public MessageDTO(Long id, UserDTO from, List<UserDTO> to, String message, LocalDateTime date, Long originalMessage) {

        this.id = id;
        this.from = from;
        this.to = to;
        this.message = message;
        this.date = date;
        this.originalMessage = originalMessage;
    }

    /**
     * To String method override
     * @return the object as a string
     */
    @Override
    public String toString() {
        return "id = " + id +
                ", from = " + from.getUserName() +
                ", to = " + to +
                ", message = '" + message + '\'' +
                ", date = " + date +
                ", original message = " + originalMessage;
    }
}
