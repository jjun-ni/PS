#include <iostream> 
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;

vector< vector< pair<int, int> > > edges;
vector<int> dist;

void dijkstra(int start);

int main(void){
    int node, edge, root;
    int INF = int(1e9);
    scanf("%d %d", &node, &edge);
    scanf("%d", &root);
    edges = vector< vector< pair<int, int> > >(node+1);
    dist = vector<int>(node+1, INF);
    int start, end, cost;
    for(int i = 0; i < edge; ++i){
        scanf("%d %d %d", &start, &end, &cost);
        edges[start].push_back(make_pair(end, cost));
    }
    dijkstra(root);
    for(int i = 1; i <= node; ++i){
        if(i == root) printf("0\n");
        else{
            if(dist[i] == INF) printf("INF\n");
            else printf("%d\n", dist[i]);
        }
    }

    return 0;
}

void dijkstra(int start){
    priority_queue< pair<int, int> > q;
    pair<int, int> tmp = make_pair(0, start);
    q.push(tmp);
    dist[start] = 0;
    pair<int, int> node;
    pair<int, int> next;
    int cost;
    while(!q.empty()){
        node = q.top();
        q.pop();
        if(dist[node.second] < node.first) continue;
        for(int i = 0; i < edges[node.second].size(); ++i){
            next = edges[node.second][i];
            cost = next.second - node.first;
            if(cost < dist[next.first]){
                dist[next.first] = cost;
                q.push(make_pair(-cost, next.first));
            }
        }
    }
}