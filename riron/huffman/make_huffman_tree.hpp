#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

void make_huffman_tree(map<char, int> &dist, vector<tuple<int, vector<int>, string> > &T, priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > &pque){
    for (int i = (int) dist.size(); i < 2*dist.size()-1; i++){
        pair<int, int> temp1 = pque.top();
        pque.pop();
        pair<int, int> temp2 = pque.top();
        pque.pop();
        pair<int, int> temp3 = make_pair(temp1.first+temp2.first, i);
        pque.push(temp3);
        vector<int> temp4 = {temp1.second, temp2.second};
        T[i] = make_tuple(temp3.first, temp4, "");
    }
}

