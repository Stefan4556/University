package Container;

import Model.Task;
import utils.Constants;

/***
 * Aceasta este clasa AbstractContainer din care mostenesc si StackContainer si QueueContainer si care implementeaza Container
 * Cerinte 5.3
 */
public abstract class AbstractContainer implements Container{

    protected Task[] tasks;

    protected int size;

    /***
     * Constructorul clasei AbstractContainer ce initializeaza vectorul si lungimea acestuia
     */
    public AbstractContainer(){

        tasks = new Task[Constants.INITIAL_SIZE];
        size = 0;
    }

    /***
     * Aceasta este metoda ce este suprascrisa de catre cele 2 containere
     * @return Task - task-ul ce este sters
     */
    public abstract Task remove();

    /***
     * Aceasta este metoda ce se ocupa cu adaugarea unui task in vectorul de taskuri
     * @param task - Task - task-ul ce urmeaza a fi adaugat in vector
     */
    public void add(Task task){

        int v = tasks.length;
        if(v == size){
            Task[] t = new Task[v * 2];
            System.arraycopy(tasks, 0,t,0,v);
            tasks = t;
        }

        tasks[size] = task;
        size++;
    }

    /***
     * Metoda ce se ocupa cu returnarea marimii vectorului
     * @return int - lungimea vectorului
     */
    public int size() {

        return size;
    }

    /***
     * Metoda ce se ocupa cu verificarea daca containerul este vid sau nu
     * @return true - daca este
     *         false - altfel
     */
    public boolean isEmpty() {

        return size == 0;
    }
}
