package Container;

import Model.Task;

/**
 * Clasa QueueContainer mosteneste din AbstractContainer si suprascrie o singura metoda si anume remove
 * Cerinta 5.3
 */
public class StackContainer extends AbstractContainer{

    /***
     * Constructorul clasei QueueContainer apeleaza constructorul clasei mostenite
     */
    public StackContainer(){ // optional

        super();
    }

    /***
     * Aceasta este metoda ce se ocupa cu stergerea unui element dintr-un container de tipul Stack, avand strategia LIFO
     * @return Task - reprezentand task ce a fost sters din lista noastra
     */
    @Override
    public Task remove(){

        if(!isEmpty()){

            size--;
            return tasks[size];
        }
        return null;
    }


}
