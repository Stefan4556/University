#include <iostream>     // g++ -std=c++11 -Wall -g -o pb2.exe pb2.cpp
#include <vector>
#include <queue>
#include <fstream>
#include <algorithm>

using namespace std;

#define VMAX 1000
#define EMAX 10000
#define INF VMAX * VMAX + 5

struct Muchie
{
    int src, dest, w;
};

vector<vector<pair<int, int> >> adj;
vector<Muchie> muchii;
vector<bool> vizitat;
bool notOk = false;

vector<int> BellmanFord(int varfuriNum, int source, ofstream& of){

    vector <int> dist(varfuriNum, INF);
    dist[source] = 0;

    for (int i = 1; i <= varfuriNum - 1; ++i)
        for (auto muchie : muchii)
            if (dist[muchie.src] + muchie.w < dist[muchie.dest])
                dist[muchie.dest] = dist[muchie.src] + muchie.w;

    for (const auto& muchie : muchii)
        if (dist[muchie.src] + muchie.w < dist[muchie.dest])
            notOk = true;

    return dist;
}

bool cmp2(Muchie e1, Muchie e2){

    if (e1.src < e2.src or (e1.src == e2.src and e1.dest < e2.dest))
        return true;

    return false;
}

vector <int> dist;

void Dijkstra(int varfuriNum, int source){

    vector <bool> vizitat(varfuriNum);

    struct cmp{

        bool operator() (int x, int y){

            return dist[x] > dist[y];
        }
    };

    priority_queue<int, vector<int>, cmp> pq;

    for (int i = 0; i <= varfuriNum - 1; i++)
        dist[i] = INF;

    dist[source] = 0;
    pq.push(source);

    while (!pq.empty()){

        int nod = pq.top();
        pq.pop();

        vizitat[nod] = 0;

        for (auto muchie : adj[nod])
            if (dist[muchie.first] > dist[nod] + muchie.second){

                dist[muchie.first] = dist[nod] + muchie.second;

                if (vizitat[muchie.first] == 0){

                    vizitat[muchie.first] = 1;
                    pq.push(muchie.first);
                }
            }
    }
}

int main(int argc, char** argv){

    int varfuriNum, muchieNum;
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    in >> varfuriNum >> muchieNum;

    dist.resize(varfuriNum);
    adj.resize(varfuriNum);

    pair<int, int> p;
    Muchie e;

    while (muchieNum--){

        int x, y, c;
        in >> x >> y >> c;

        p = make_pair(y, c);
        adj[x].push_back(p);

        e.src = x;
        e.dest = y;
        e.w = c;
        muchii.push_back(e);
    }

    int i;
    for (i = 0; i <= varfuriNum - 1; i++){

        e.src = varfuriNum;
        e.dest = i;
        e.w = 0;
        muchii.push_back(e);
    }

    vector <int> h = BellmanFord(varfuriNum + 1, varfuriNum, out);
    if (notOk){

        out << -1;
        return 0;
    }

    for (i = 0; i <= varfuriNum - 1; i++)
        for (auto& j : adj[i])
            j.second += h[i] - h[j.first];

    sort(muchii.begin(), muchii.end(), cmp2);

    for (auto& i : muchii)
        i.w += h[i.src] - h[i.dest];

    for (const auto& muchie : muchii)
        if (muchie.src != varfuriNum)
            out << muchie.src << ' ' << muchie.dest << ' ' << muchie.w << '\n';

    for (int i = 0; i <= varfuriNum - 1; i++){

        Dijkstra(varfuriNum, i);

        int poz = 0;

        for (auto j : dist){

            if (j == INF)

                out << "INF" << ' ';

            else

                out << j + h[poz] - h[i] << ' ';

            poz++;
        }

        out << '\n';
    }
}