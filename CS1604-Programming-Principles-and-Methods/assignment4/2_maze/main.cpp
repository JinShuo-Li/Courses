#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <queue>

using namespace std;

typedef pair<int, int> point;

void bfs_search(point entrance, point destination, const vector<string>& maze) {
    int n = maze.size();
    int m = maze[0].size();

    if (maze[entrance.first][entrance.second] == 'W') {
        cout << "unreachable" << endl;
        return;
    }

    vector<vector<bool>> visited(n, vector<bool>(m, false));

    queue<point> q;
    q.push(entrance);
    visited[entrance.first][entrance.second] = true; // 标记起点已访问

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        point current = q.front();
        q.pop();

        if (current.first == destination.first && current.second == destination.second) {
            cout << "reachable" << endl;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int next_x = current.first + dx[i];
            int next_y = current.second + dy[i];

            if (next_x >= 0 && next_x < n && 
                next_y >= 0 && next_y < m && 
                maze[next_x][next_y] != 'W' && 
                !visited[next_x][next_y]) {
                
                q.push({next_x, next_y});
                visited[next_x][next_y] = true;
            }
        }
    }

    cout << "unreachable" << endl;
}

int main() {
    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<point> entrances(k);
    for (int i = 0; i < k; ++i) {
        cin >> entrances[i].first >> entrances[i].second;
    }

    vector<string> maze(n);
    for (int i = 0; i < n; ++i) {
        cin >> maze[i];
    }

    for (size_t i = 0; i < entrances.size(); i++) {
        point current_entrance = entrances[i];
        point destination(n-1, m-1);
        bfs_search(current_entrance, destination, maze);
    }

    return 0;
}