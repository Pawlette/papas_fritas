#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/
int main()
{
    vector<int> mountainHeights;
    cout << "Provide eight heights for your mountains" << endl;
    for (int i = 0; i < 8; i++) {
        int mountainH; //represents the height of one mountain.
        cin >> mountainH; cin.ignore();
        mountainHeights.push_back(mountainH);
     }

    int idx = 0;
    int max = mountainHeights.at(idx);
    for(int i = 1; i < mountainHeights.size(); i++) {
        int current = mountainHeights.at(i);
        if(current > max) {
            max = current;
            idx = i;
         }
     }
     cout << "Fire to mountain at index: " << idx << endl; // The index of the mountain to fire on.
return 0;
}
