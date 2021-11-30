#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

struct Arc{

    int vf_sursa, vf_dest, pondere;
};

struct Graf{

    int V, E;

    struct Arc* arc;
};

struct Graf* creeaza_graf(int V, int E){

    struct Graf* graf = new Graf;
    graf->V = V;
    graf->E = E;
    graf->arc = new Arc[E];
    return graf;
}

void afisare_drumuri(int dist[], int n, ofstream& g){

    /*string rezultat="";

    for(int i = 0; i < n; i++)
        if (dist[i] != INT_MAX) {
            char carac;
            carac = '0';
            carac += dist[i];
            rezultat += carac;
            rezultat += " ";
        }                           //g<<dist[i]<<" ";
        else
            rezultat += "INF ";

    return rezultat;*/

    for(int i = 0; i < n; i++)
        if (dist[i] != INT_MAX)
            g<<dist[i]<<" ";
        else
            g<<"INF"<<" ";
}

void BellmanFord(struct Graf* graf, int vf_sursa, ofstream& g){

    int V = graf->V;
    int E = graf->E;
    int dist[V];
    string rezultat;

    for(int i = 0; i < V; i++)
        dist[i] = INT_MAX;
    dist[vf_sursa] = 0;

    for(int i = 1; i <= V - 1; i++){

        for (int j = 0; j < E; j++){

            int u = graf->arc[j].vf_sursa;
            int v = graf->arc[j].vf_dest;
            int pondere = graf->arc[j].pondere;

            if (dist[u] != INT_MAX && dist[u] + pondere < dist[v])

                dist[v] = dist[u] + pondere;
        }
    }

    for(int i = 0; i < E; i++){

        int u = graf->arc[i].vf_sursa;
        int v = graf->arc[i].vf_dest;
        int pondere = graf->arc[i].pondere;

        if (dist[u] != INT_MAX && dist[u] + pondere < dist[v]){

            g<<"Graful contine cicluri negative!\n";
            return;
        }
    }

    afisare_drumuri(dist, V, g);

}

int main(int argc, char** argv){    // de rulat celelalte exemple

    ifstream f(argv[1]);
    ofstream g(argv[2]);

    int V ;
    int E ;
    int sursa;
    string rezultat;

    f >> V >> E >> sursa;
    struct Graf* graf = creeaza_graf(V, E);

    for(int i = 0; i < E; i++){

        int vf_sursa, vf_dest, pondere;
        f>>vf_sursa>>vf_dest>>pondere;
        graf->arc[i].vf_sursa = vf_sursa;
        graf->arc[i].vf_dest = vf_dest;
        graf->arc[i].pondere = pondere;
    }

    BellmanFord(graf, sursa, g);

    f.close();
    g.close();

    return 0;

}
