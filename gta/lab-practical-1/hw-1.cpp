#include <iostream>
using namespace std;

int main() {
    long long R, C;
    cin >> R >> C;
    
    // Each withdrawal unit is 1000 rupees, and costs (1000 + C) total
    // Maximum number of units that can be withdrawn
    long long units = R / (1000 + C);
    
    // Maximum withdrawal amount
    long long max_withdrawal = units * 1000;
    
    cout << max_withdrawal << endl;
    
    return 0;
}
