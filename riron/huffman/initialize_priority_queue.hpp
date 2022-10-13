#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

void initialize_priority_queue(map<char, int> &dist, priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > &pque){
    int i = 0;
    for (auto itr : dist){
        pque.push(make_pair(itr.second, i));
        i++;
    }
}

