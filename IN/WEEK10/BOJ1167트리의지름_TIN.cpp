#include <iostream> 
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

int maxLength, point;

void findFarPoint(int node, int length, vector<int>& visit, vector< vector< pair<int,int> > >& graph);

int main(void){
    int n;
    scanf("%d", &n);
    vector< vector< pair<int,int> > > graph(n+1);
    int tmp, node;

    for(int i = 0; i < n; ++i){
        scanf("%d", &node);
        vector<int> info;
        while(true){
            scanf("%d", &tmp);
            if(tmp == -1) break;
            info.push_back(tmp);
        }
        for(int j = 0; j < info.size(); j+=2){
            pair<int, int> p = make_pair(info[j], info[j+1]);
            graph[node].push_back(p);
        }
    }


    vector<int> visit(n+1, 0);
    findFarPoint(1,0,visit,graph);
    for(int i = 0; i < visit.size(); ++i){
        visit[i] = 0;
    }
    maxLength = 0;
    findFarPoint(point,0,visit,graph);
    printf("%d", maxLength);
    return 0;
}

void findFarPoint(int node, int length, vector<int>& visit, vector< vector< pair<int,int> > >& graph){
    if(visit[node] == 0){
        visit[node] = 1;
        if(maxLength < length){
            point = node;
            maxLength = length;
        }
        for(int i = 0; i < graph[node].size(); ++i){
            int next = graph[node][i].first;
            int weight = graph[node][i].second;
            findFarPoint(next, length+weight,visit,graph);
        }
    }
}