#include <iostream> 
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int maxLength = 0, point = 0;
vector<int> visit;
vector< vector< pair<int,int> > > graph;
vector<int> parents;

void findFarPoint(int node, int length);

int main(void){
    int n, par, child, cost;
    scanf("%d", &n);
    graph = vector< vector< pair<int,int> > >(n+1);
    parents = vector<int>(n+1);
    visit = vector<int>(n+1);
    for(int i = 0; i < n-1; ++i){
        scanf("%d %d %d", &par, &child, &cost);
        graph[par].push_back(make_pair(child, cost));
        graph[child].push_back(make_pair(par, cost));
    }
    findFarPoint(1,0);

    for(int i = 0; i < n+1; ++i){
        visit[i] = 0;
    }
    maxLength = 0;
    findFarPoint(point, 0);
    printf("%d", maxLength);
    
    return 0;
}

void findFarPoint(int node, int length){
    if(visit[node] == 0){
        visit[node] = 1;
        if(maxLength < length){
            point = node;
            maxLength = length;
        }
        for(pair<int, int> next : graph[node]){
            findFarPoint(next.first, length + next.second);
        }
    }
}