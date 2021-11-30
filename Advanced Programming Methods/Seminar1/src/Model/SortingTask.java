package Model;

import Container.Strategy;
import Sorting.AbstractSorter;
import Sorting.BubbleSort;

import java.util.Objects;

/***
 * Aceasta este cerinta numarul 3, clasa SortingTask mosteneste din Task si este nevoita sa suprascrie clasa execute
 */
public class SortingTask extends Task{

    String strategy;
    int[] vector;

    /***
     * Constructorul clasei ce primeste ca parametrii:
     * @param taskId - String - Id-ul taskului
     * @param description - String - Descrierea task-ului
     * @param strategy - String - reprezinta strategia de sortare pe care dorim sa o alegem
     * @param vector - int[] - vectorul ce urmeaza a fi sortat conform strategiei introduse in linia de comanda
     */
    public SortingTask(String taskId, String description, String strategy, int[] vector) {
        super(taskId, description);
        this.strategy = strategy;
        this.vector = vector;
    }

    /***
     * Metoda execute este metoda mostenita din Task si este suprascrisa deoarece rolul acesteia este de a sorta lista de numere dupa o strategie primita in linia de comanda
     */
    @Override
    public void execute() {

        Strategy strat;
        AbstractSorter s;

        if(Objects.equals(strategy, "BUBBLE")) {

            strat = Strategy.BUBBLE;
            s = new BubbleSort(strat, vector);
        }
        else {

            strat = Strategy.QUICK;
            s = new BubbleSort(strat, vector);
        }

        System.out.print("Sirul inainte de a fi sortat: ");

        for(int el : this.vector)

            System.out.print(el + " ");

        System.out.println();

        int[] rez = s.sort();

        System.out.print("Sirul dupa ce a fost sortat folosind " + strat + "Sort: ");

        for(int el : rez)

            System.out.print(el + " ");

        System.out.println();
    }
}
