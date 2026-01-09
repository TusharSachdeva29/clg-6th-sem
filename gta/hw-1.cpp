#include <iostream>
using namespace std;

int main() {
    // payoff[player][p1_strategy][p2_strategy]
    // 0 = Deny, 1 = Confess

    int payoff[2][2][2] = {
        { {-1, -10}, {0, -5} },   // Player 1 payoffs
        { {-1, 0}, {-10, -5} }    // Player 2 payoffs
    };

    cout << "Best Responses:\n\n";

    // Best response for Player 1
    for(int p2 = 0; p2 < 2; p2++) {
        int best = 0;
        for(int p1 = 1; p1 < 2; p1++) {
            if(payoff[0][p1][p2] > payoff[0][best][p2])
                best = p1;
        }
        cout << "P1 best response to P2 = "
             << (p2 == 0 ? "Deny" : "Confess")
             << " is "
             << (best == 0 ? "Deny" : "Confess")
             << endl;
    }

    cout << endl;

    // Best response for Player 2
    for(int p1 = 0; p1 < 2; p1++) {
        int best = 0;
        for(int p2 = 1; p2 < 2; p2++) {
            if(payoff[1][p1][p2] > payoff[1][p1][best])
                best = p2;
        }
        cout << "P2 best response to P1 = "
             << (p1 == 0 ? "Deny" : "Confess")
             << " is "
             << (best == 0 ? "Deny" : "Confess")
             << endl;
    }

    cout << "\nNash Equilibrium: (Confess, Confess)\n";

    return 0;
}
