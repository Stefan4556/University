package Container;

import Model.Task;
import utils.Constants;

/**
 * Clasa QueueContainer mosteneste din AbstractContainer si suprascrie o singura metoda si anume remove
 * Cerinta 5.2 si 5.3
 */
public class QueueContainer extends AbstractContainer{


    /***
     * Constructorul clasei QueueContainer apeleaza constructorul clasei mostenite
     */
    public QueueContainer(){ // optional

        super();
    }

    /***
     * Aceasta este metoda ce se ocupa cu stergerea unui element dintr-un container de tipul Queue, avand strategia FIFO
     * @return Task - reprezentand task ce a fost sters din lista noastra
     */
    @Override
    public Task remove() {

        if(!isEmpty()){

            Task t = tasks[0];

            if(tasks.length - 1 >= 0)

                System.arraycopy(this.tasks, 1, tasks, 0, size - 1);

            size--;

            return t;
        }

        return null;
    }
}
