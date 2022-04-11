#include <iostream> 
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;

vector< vector< pair<int, int> > > road;
vector<int> costs;

int INF = int(1e9);

int main(void){
    int test, n, m, w;
    scanf("%d", &test);
    for(int i = 0; i < test; ++i){
        scanf("%d %d %d", &n, &m, &w);
        road = vector< vector< pair<int, int> > >(n+1);
        costs = vector<int>(n+1, INF);
        costs[1] = 0;
        bool possible = false;
        int start, end, time;
        for(int j = 0; j < m; ++j){
            scanf("%d %d %d", &start, &end, &time);
            road[start].push_back(make_pair(time, end));
            road[end].push_back(make_pair(time, start));
        }
        for(int j = 0; j < w; ++j){
            scanf("%d %d %d", &start, &end, &time);
            road[start].push_back(make_pair(-time, end));
        }
        for(int j = 0; j < road.size(); ++j){
            sort(road[j].begin(), road[j].end());
        }
        for(int j = 1; j <= n; ++j){
            for(int k = 1; k <= n; ++k){
                for(int z = 0; z < road[k].size(); ++z){
                    pair<int, int> next = road[k][z];
                    if(costs[next.second] > costs[k] + next.first){
                        costs[next.second] = costs[k] + next.first;
                        if(j == n) possible = true;
                    }
                }
            }
        }
        if(possible) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
