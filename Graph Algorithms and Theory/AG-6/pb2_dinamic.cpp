#include<queue>
#include<cstring>
#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

int bfs(int sNode, int eNode, int** c, int** flowPassed, vector<int> g[1001], int* parList, int* currentPathC)//breadth first search
{

    memset(parList, -1, 1001);
    memset(currentPathC, 0, 1001);
    queue<int> q;//declare queue vector
    q.push(sNode);
    parList[sNode] = -1;//initialize parlist’s source node
    currentPathC[sNode] = 999;//initialize currentpath’s source node
    while (!q.empty())// if q is not empty
    {
        int currNode = q.front();
        q.pop();
        for (int i = 0; i < g[currNode].size(); i++)
        {
            int to = g[currNode][i];
            if (parList[to] == -1)
            {
                if (c[currNode][to] - flowPassed[currNode][to] > 0)
                {
                    parList[to] = currNode;
                    currentPathC[to] = min(currentPathC[currNode],
                                           c[currNode][to] - flowPassed[currNode][to]);
                    if (to == eNode)
                    {
                        return currentPathC[eNode];
                    }
                    q.push(to);
                }
            }
        }
    }
    return 0;
}
int edmondsKarp(int sNode, int eNode, int** c, int** flowPassed, vector<int> g[1001], int* parList, int* currentPathC)
{
    int maxFlow = 0;
    while (true)
    {
        int flow = bfs(sNode, eNode, c, flowPassed, g, parList, currentPathC);
        if (flow == 0)
        {
            break;
        }
        maxFlow += flow;
        int currNode = eNode;
        while (currNode != sNode)
        {
            int prevNode = parList[currNode];
            flowPassed[prevNode][currNode] += flow;
            flowPassed[currNode][prevNode] -= flow;
            currNode = prevNode;
        }
    }
    return maxFlow;
}
int main(int argc, char** argv)
{
    int nodCount, edCount, C;

    int **c = (int**)malloc(sizeof(int*) * 1001);

    int **flowPassed = (int**)malloc(sizeof(int*) * 1001);

    int* parList = (int*)malloc(sizeof(int) * 1001);

    int* currentPathC = (int*)malloc(sizeof(int) * 1001);

    vector<int> g[1001];

    for(int i = 0 ; i < 1001; i++) {

        c[i] = (int *) malloc(sizeof(int) * 1001);
        flowPassed[i] = (int *) malloc(sizeof(int) * 1001);
    }

    ifstream f(argv[1]);
    ofstream out(argv[2]);

    f >> nodCount >> C >> edCount;

    for (int ed = 0; ed < edCount; ed++)
    {

        int from, to, cap;
        f >> from >> to >> cap;
        c[from][to] = cap;
        g[from].push_back(to);
        g[to].push_back(from);
    }

    int suma = 0;

    vector<int> rez;

    for (int source = 0; source < C; source++) {

        int maxFlow = edmondsKarp(source, nodCount - 1, c, flowPassed, g, parList, currentPathC);

        suma += maxFlow;

        rez.push_back(maxFlow);
    }


    out << suma << '\n';

    for (auto s : rez)

        out << s << " ";

    f.close();
    out.close();

    for(int i = 0; i < 1001; i++) {

        free(c[i]);
        free(flowPassed[i]);
    }

    free(c);

    free(flowPassed);

    free(parList);

    free(currentPathC);

    return 0;
}