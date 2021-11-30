package Sorting;

import Container.Strategy;

/***
 * Clasa AbstractSorter este clasa pe care atat BubbleSort cat si QuickSort o mostenesc, pentru a face mult mai usor codul
 * Parte din cerinta 3
 */
public abstract class AbstractSorter {

    Strategy strategy;
    int[] vector;

    /**
     * Constructorul clasei AbstractSorter
     * @param strategy - Strategy - Strategia de sortare
     * @param vector - int[] - Vectorul de numere
     */
    public AbstractSorter(Strategy strategy, int[] vector){

        this.strategy = strategy;
        this.vector = vector;
    }

    /***
     * Aceasta este functia abstracta sort ce urmeaza a fi suprascrisa de clasele ce mostenesc din aceasta
     * @return vectorul sortat;
     */
    public abstract int[] sort();
}
