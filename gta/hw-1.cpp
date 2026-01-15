#include <bits/stdc++.h>
using namespace std;

int main() {
    // payoff[player][p1_strategy][p2_strategy]
    // strategies: 0 -> 1, 1 -> 2

    int payoff[2][2][2] = {
        { {-3,  0}, {-4, -1} },   // Player 1 payoffs
        { {-3, -4}, { 0, -1} }    // Player 2 payoffs
    };

    vector<vector<bool>> bestP1(2, vector<bool>(2, false));
    vector<vector<bool>> bestP2(2, vector<bool>(2, false));

    // Best responses for Player 1
    for(int p2 = 0; p2 < 2; p2++) {
        int mx = INT_MIN;
        for(int p1 = 0; p1 < 2; p1++)
            mx = max(mx, payoff[0][p1][p2]);

        for(int p1 = 0; p1 < 2; p1++)
            if(payoff[0][p1][p2] == mx)
                bestP1[p1][p2] = true;
    }

    // Best responses for Player 2
    for(int p1 = 0; p1 < 2; p1++) {
        int mx = INT_MIN;
        for(int p2 = 0; p2 < 2; p2++)
            mx = max(mx, payoff[1][p1][p2]);

        for(int p2 = 0; p2 < 2; p2++)
            if(payoff[1][p1][p2] == mx)
                bestP2[p1][p2] = true;
    }

    cout << "Nash Equilibria:\n";
    bool found = false;

    for(int p1 = 0; p1 < 2; p1++) {
        for(int p2 = 0; p2 < 2; p2++) {
            if(bestP1[p1][p2] && bestP2[p1][p2]) {
                found = true;
                cout << "(P1 Strategy " << p1 + 1
                     << ", P2 Strategy " << p2 + 1 << ")\n";
            }
        }
    }

    if(!found)
        cout << "No pure Nash Equilibrium exists\n";

    return 0;
}
