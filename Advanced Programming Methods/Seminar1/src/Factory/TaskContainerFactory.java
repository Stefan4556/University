package Factory;

import Container.Container;
import Container.Strategy;
import Container.StackContainer;
import Container.QueueContainer;

public class TaskContainerFactory implements Factory{

    private static TaskContainerFactory instance = null;

    private TaskContainerFactory(){}

    public static TaskContainerFactory getInstance(){

        if(instance == null)

            instance = new TaskContainerFactory();

        return instance;
    }

    @Override
    public Container createContainer(Strategy strat){

        if(strat == Strategy.LIFO)

            return new StackContainer();

        else

            return new QueueContainer(); // Aceasta este cerinta 7
    }
}
