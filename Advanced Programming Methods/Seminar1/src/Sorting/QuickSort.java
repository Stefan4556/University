package Sorting;

import Container.Strategy;

/***
 * Clasa QuickSort mosteneste din clasa AbstractSorter si suprascrie metoda sort
 * Parte din cerinta 3
 */
public class QuickSort extends AbstractSorter{

    /***
     * Constructorul clasei QuickSort ce apeleaza constructorul clasei mostenite si primeste ca si parametrii:
     * @param strategy - Strategy - In cazul de fata o sa fie strategia pentru QuickSort
     * @param vector - int[] - vectorul de numere ce urmeaza a fi sortat
     */
    public QuickSort(Strategy strategy, int[] vector) {

        super(strategy, vector);
    }

    /***
     * Metoda folosita in functia partition, ce se ocupa cu interschimbarea elementelor din vector de pe poz i, respectiv poz j
     * @param vec - int[] - Vectorul de elemente
     * @param i - int - prima pozitie
     * @param j - int -  a doua pozitie
     */
    private void swap(int[] vec, int i, int j){

        int aux = vec[i];
        vec[i] = vec[j];
        vec[j] = aux;
    }

    /***
     * Aceasta functie plaseaza pivotul pe pozitia corecta, punand in partea stanga elementele mai mici, iar in dreapta cele mai mari
     * @param vec - int[] - Vectorul de numere
     * @param min - pozitia de unde incepem
     * @param max - pozitia unde terminam
     * @return pozitia ce se afla intre cele 2 partitii ce urmeaza a fi sortate
     */
    private int partition(int[] vec, int min, int max){

        int pivot = vec[max];   // Alegem pivotul ca fiind ultimul element
        int i = min - 1;

        for(int j = min; j <= max; j++){

            if(vec[j] < pivot){

                i++;
                swap(vec, i, j);
            }
        }
        swap(vec, i + 1, max);
        return i + 1;
    }

    /***
     * Functia ce se ocuap cu sortarea vectorului folosind QuickSort
     * @param vec - int[] - vectorul de numere
     * @param min - int - pozitia de unde incepem sortarea
     * @param max - int - pozitia unde terminam sortarea
     */
    private void quickSort(int[] vec, int min, int max){

        if(min < max){

            int p = partition(vec, min, max);

            quickSort(vec, min, p - 1);
            quickSort(vec, p + 1, max);
        }
    }

    /***
     * Aceasta este metoda ce este mostenita din AbstractSorter si suprascrisa
     * @return int[] - Vectorul sortat folosind QuickSort
     */
    @Override
    public int[] sort() {

        int[] rez = this.vector;

        quickSort(rez, 0, rez.length - 1);

        return rez;
    }
}
