#include<queue>
#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

// O(V*E)
int bfs(int nrNoduri, int start, int dest, int** c, int** graf_rezidual, vector<vector<int>> g, int* vector_tati, int* drum_curent){

    // Theta(V)
    for (int i = 0; i < nrNoduri; i++) {    // initializam vectorul de tati si drumul curent

        vector_tati[i] = -1;
        drum_curent[i] = 0;
    }

    queue<int> q;
    q.push(start);
    vector_tati[start] = -1;
    drum_curent[start] = 999;
    while (!q.empty()){

        int NodCurent = q.front();
        q.pop();
        for (int i = 0; i < g[NodCurent].size(); i++){    // O(E)

            int nod_ad = g[NodCurent][i];
            if (vector_tati[nod_ad] == -1){ // verificam daca s-a trecut prin nodul respectiv

                if (c[NodCurent][nod_ad] - graf_rezidual[NodCurent][nod_ad] > 0){   // daca mai este loc pe arcul respectiv 

                    vector_tati[nod_ad] = NodCurent;    // retinem tatal nodului curent
                    drum_curent[nod_ad] = min(drum_curent[NodCurent], c[NodCurent][nod_ad] - graf_rezidual[NodCurent][nod_ad]);     // retinem flow minim curent

                    if (nod_ad == dest){

                        return drum_curent[dest];   // returnam flow-ul minim
                    }
                    q.push(nod_ad);     // adaugam nodul in queue pentru a il explora
                }
            }
        }
    }
    return 0;
}

// Complexitatea pe EdmondsKarp este de O(V * E ^ 2), unde V este nr de varfuri si E - nr de muchii
int edmondsKarp(int nrNoduri, int start, int dest, int** c, int** graf_rezidual, vector<vector<int>> g, int* vector_tati, int* drum_curent){

    int maxFlow = 0;
    while (true){

        int flow = bfs(nrNoduri, start, dest, c, graf_rezidual, g, vector_tati, drum_curent);   // gasim un drum de lungime minima cu un flow minim
        if (flow == 0){

            break;
        }
        maxFlow += flow;              // actualizam fluxul maxim
        int NodCurent = dest;         // pregatim parcurgerea drumului gasit de bfs
        while (NodCurent != start){   // O(E) - actualizam ponderile muchiilor

            int NodPrec = vector_tati[NodCurent];
            graf_rezidual[NodPrec][NodCurent] += flow;
            graf_rezidual[NodCurent][NodPrec] -= flow;
            NodCurent = NodPrec;
        }
    }
    return maxFlow;
}

// Complexitatea Overall a programului este O(C * (V * E ^ 2)), unde C este numarul de camine, V - nr de varfuri si E - nr de muchii
int main(int argc, char** argv){

    int nrNoduri, edCount, C;

    ifstream f(argv[1]);
    ofstream out(argv[2]);

    f >> nrNoduri >> C >> edCount;

    int** c = (int**)malloc(sizeof(int*) * nrNoduri);

    int** graf_rezidual = (int**)malloc(sizeof(int*) * nrNoduri);

    int* vector_tati = (int*)malloc(sizeof(int) * nrNoduri);

    int* drum_curent = (int*)malloc(sizeof(int) * nrNoduri);

    vector<vector<int>> g(nrNoduri);

    for (int i = 0; i < nrNoduri; i++) {

        c[i] = (int*)malloc(sizeof(int) * nrNoduri);
        graf_rezidual[i] = (int*)malloc(sizeof(int) * nrNoduri);
        for (int j = 0; j < nrNoduri; j++) {

            c[i][j] = 0;
            graf_rezidual[i][j] = 0;
        }
    }

    for (int ed = 0; ed < edCount; ed++){

        int x, y, cap;
        f >> x >> y >> cap;
        c[x][y] = cap;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    int suma = 0;

    vector<int> rez;

    for (int source = 0; source < C; source++) {

        int maxFlow = edmondsKarp(nrNoduri, source, nrNoduri - 1, c, graf_rezidual, g, vector_tati, drum_curent);

        suma += maxFlow;

        rez.push_back(maxFlow);
    }


    out << suma << '\n';

    for (auto s : rez)

        out << s << " ";

    f.close();
    out.close();

    for (int i = 0; i < nrNoduri; i++) {

        free(c[i]);
        free(graf_rezidual[i]);
    }

    free(c);

    free(graf_rezidual);

    free(vector_tati);

    free(drum_curent);

    return 0;
}