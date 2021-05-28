// #include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;
    for (int i=s.size()-1; i>=0; i--) {
        char subS = s.at(i);
        cout << "sub_s: " << subS << endl;
        if (subS == (int)"6") {
            cout << "9";
        } else if (subS == "9") {
            cout << "6";
        } else {
            cout << subS;
        }
    }
}
