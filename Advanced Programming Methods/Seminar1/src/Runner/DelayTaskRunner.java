package Runner;

import utils.Constants;

import java.time.LocalDateTime;

/***
 * Aceasta este clasa DelayTaskRunner ce are rolul de a rula un task cu un mic delay pus de noi
 * Cerinta 12.2
 */
public class DelayTaskRunner extends AbstractTaskRunner{

    /***
     * Aceasta este constructorul clasei noastre ce apeleaza constructorul clasei pe care o mosteneste si primeste ca si parametru:
     * @param taskRunner - TaskRunner - task-ul de il are de efectuat
     */
    public DelayTaskRunner(TaskRunner taskRunner) {
        super(taskRunner);
    }

    /***
     * Aceasta este metoda ce este mostenita din AbstractTaskRunner si trebuie suprascrisa pentru a executa task-ul cu un anume delay
     */
    @Override
    public void executeOneTask() {
        try{
            Thread.sleep(3000);
            taskRunner.executeOneTask();
            //decorateExecuteOneTask();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    /***
     * Metoda ce decoreaza un task
     */
    public void decorateExecuteOneTask(){

        System.out.println("Executed on: " + LocalDateTime.now().format(Constants.DATE_TIME_FORMATTER));
    }
}
