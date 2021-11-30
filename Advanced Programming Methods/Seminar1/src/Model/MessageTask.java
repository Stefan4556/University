package Model;

import java.time.LocalDateTime;
import utils.Constants;

public class MessageTask extends Task{

    private String message, from, to;
    private LocalDateTime date;

    public MessageTask(String taskId, String description, String message, String from, String to, LocalDateTime date) {
        super(taskId, description);
        this.message = message;
        this.from = from;
        this.to = to;
        this.date = date;
    }

    @Override
    public String toString(){

        return super.toString() + " " + message + " " + from + " " + to + " " + date.format(Constants.DATE_TIME_FORMATTER);
    }

    @Override
    public void execute(){

        System.out.println(toString());
    }
}
