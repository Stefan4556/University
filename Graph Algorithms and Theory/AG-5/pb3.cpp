/*
 *      Care-i ideea algoritmului lui Hierholzer?
 *
 *              Cautam cicluri euleriene pana cand nu mai avem muchii in graf.
 */

#include<fstream>
#include<vector>
#include<stack>
#include<unordered_map>
using namespace std;
class Graph{

    int vertex; // numarul de varfuri

    vector<unordered_map<int,int>> adj; // lista de adiacenta, unordered_map pentru a fi mai eficienta stergerea

public:

    Graph(int v){
        vertex = v;     // memoram numarul de noduri
        adj = vector<unordered_map<int,int>>(v+1);      // alocam lista
    }

    void addEdge(int u, int v){
        adj[u][v] = 1;
        adj[v][u] = 1;
    }

    void removeEdge(int v,int u){
        adj[v].erase(u);
        adj[u].erase(v);
    }

    void printEulerPathCircuit(string fis_output){

        int odd = 0; // numarul de noduri cu grad impar

        for(int i = 0; i < vertex; i++)

            if(adj[i].size() % 2 == 1)

                odd++;

        if(odd==0)

            printEuler(0, fis_output);

        else {

            ofstream out(fis_output);

            out << "Nu exista!" << endl;

            out.close();
        }
    }

    // the function to print euler path or circuit
    void printEuler(int v, string fis_output){

        ofstream out(fis_output);

        stack<int> cpath;    // current path
        stack<int> epath;    // euler path

        cpath.push(v);        // pornim de la nodul v

        while(!cpath.empty()){
            int u = cpath.top();

            if(adj[u].size()==0){
                // if all edges from u are visited
                // il scoatem pe u si il adaugam la ciclul eulerian
                epath.push(u);
                cpath.pop();
            }
            else{
                // if all edges from u are not visited
                // selectam o muchie random din varful u si o adaugam la curent path si o stergem din graful nostru
                cpath.push(adj[u].begin()->first);
                removeEdge(u,adj[u].begin()->first);
            }
        }

        while(!epath.empty()){
            out<<epath.top()<<" ";
            epath.pop();
        }

        out.close();

    }

};
int main(int argc, char** argv){

    int V,E;

    ifstream in(argv[1]);

    in >> V >> E;

    Graph G(V);

    int x,y;

    for(int i = 0 ; i < E; i++) {

        in >> x >> y;
        G.addEdge(x, y);
    }

    G.printEulerPathCircuit(argv[2]);

    in.close();
    return 0;
}

