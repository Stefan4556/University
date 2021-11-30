package Runner;

import utils.Constants;

import java.time.LocalDateTime;

public class PrinterTaskRunner extends AbstractTaskRunner{

    public PrinterTaskRunner(TaskRunner t){

        super(t);
    }

    @Override
    public void executeOneTask() {

        taskRunner.executeOneTask();
        decorateExecuteOneTask();
    }

    public void decorateExecuteOneTask(){

        System.out.println("Executed on: " + LocalDateTime.now().format(Constants.DATE_TIME_FORMATTER));
    }
}
// mesaj
// executed 1
// executed 2
// executed 3
