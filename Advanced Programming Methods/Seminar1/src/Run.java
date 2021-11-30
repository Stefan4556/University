import Container.Strategy;
import Model.MessageTask;
import Model.SortingTask;
import Runner.DelayTaskRunner;
import Runner.PrinterTaskRunner;
import Runner.StrategyTaskRunner;
import Runner.TaskRunner;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.List;

public class Run {

    String[] args;

    public static void main(String[] args){



        MessageTask[] messageTasks = Run.createMessageTaskArray();
        SortingTask[] sortingTasks = Run.createSortingTaskArray();

        StrategyTaskRunner strTaskRunner = new StrategyTaskRunner(Strategy.valueOf(args[0].toUpperCase()));
        PrinterTaskRunner printerTaskRunner = new PrinterTaskRunner(strTaskRunner);

        DelayTaskRunner delayTaskRunner = new DelayTaskRunner(strTaskRunner);

        for(MessageTask el:messageTasks) {

            strTaskRunner.addTask(el);
        }

        for(SortingTask el:sortingTasks){

            strTaskRunner.addTask(el);
        }

        strTaskRunner.executeAll();
        //delayTaskRunner.executeAll();

        testTask(args[0]);

    }

    public static MessageTask[] createMessageTaskArray(){

        MessageTask m1 = new MessageTask("1","1","message1","George","Farca", LocalDateTime.now());
        MessageTask m2 = new MessageTask("2","2","message2","George","Farca", LocalDateTime.now());
        MessageTask m3 = new MessageTask("3","3","message3","George","Farca", LocalDateTime.now());

        return new MessageTask[]{m1,m2,m3};
    }

    public static SortingTask[] createSortingTaskArray(){

        SortingTask s1 = new SortingTask("4","BubbleSort","BUBBLE",new int[]{4,3,2,1});
        SortingTask s2 = new SortingTask("4","QuickSort","QUICK",new int[]{4,3,2,1});

        return new SortingTask[]{s1,s2};
    }

    /***
     * Aceasta este metoda ce realizeaza un program de test cerut la cerinta 14.1 si primeste ca si parametrii:
     * @param strategy - String - Strategia containerului nostru
     * Cerinta 14
     * Cerinta 15 - prima parte cu diagrama este salvata poza in folder
     */
    public static void testTask(String strategy){

        System.out.println("\nCerinta numarul 14\n");

        MessageTask[] messageTasks = Run.createMessageTaskArray();

        StrategyTaskRunner strTaskRunner = new StrategyTaskRunner(Strategy.valueOf(strategy.toUpperCase()));
        /*
        System.out.println("Executam MessageTask-urile cu StrategyTaskRunner...\n");
        for(MessageTask el : messageTasks)
            strTaskRunner.addTask(el);
        strTaskRunner.executeAll();

        System.out.println("\nExecutam MessageTask-urile cu DelayTaskRunner...\n");
        DelayTaskRunner delayTaskRunner = new DelayTaskRunner(strTaskRunner);
        for(MessageTask el : messageTasks)
            strTaskRunner.addTask(el);
        delayTaskRunner.executeAll();*/

        System.out.println("\nExecutam MessageTask-urile cu PrinterTaskRunner...\n");
        TaskRunner printerTaskRunner = new PrinterTaskRunner(new PrinterTaskRunner(new PrinterTaskRunner(strTaskRunner)));
        for(MessageTask el : messageTasks)
            strTaskRunner.addTask(el);
        printerTaskRunner.executeAll();



    }
}
