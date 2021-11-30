package Sorting;

import Container.Strategy;

/***
 * Clasa BubbleSort mosteneste din clasa AbstractSorter si suprascrie metoda sort
 * Parte din cerinta 3
 */
public class BubbleSort extends AbstractSorter{

    /***
     * Constructorul clasei BubbleSort ce apeleaza constructorul clasei mostenite si primeste ca si parametrii:
     * @param strategy - Strategy - In cazul de fata o sa fie strategia pentru BubbleSort
     * @param vector - int[] - vectorul de numere ce urmeaza a fi sortat
     */
    public BubbleSort(Strategy strategy, int[] vector) {

        super(strategy, vector);
    }

    /***
     * Aceasta este metoda ce este mostenita din AbstractSorter si suprascrisa
     * @return int[] - Vectorul sortat folosind BubbleSort
     */
    @Override
    public int[] sort() {

        int[] rez = this.vector;

        int length = rez.length;

        for(int i = 0 ; i < length - 1; i++)
            for(int j = 0; j < length - i - 1; j++)
                if(rez[j] > rez[j+1]){
                    int aux = rez[j];
                    rez[j] = rez[j+1];
                    rez[j+1] = aux;
                }

        return rez;
    }
}
