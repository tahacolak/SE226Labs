// author:tahacolak
#include <iostream>
using namespace std;


double harmonic_recursive(int n) {
    if (n == 1) return 1.0;
    return (1.0 / n) + harmonic_recursive(n - 1);
}


double harmonic_recursive() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive integer." << endl;
        return 0; // To invalid input
    }
    
    return harmonic_recursive(n);
}

int main() {
    int choice;
    cout << "Choose an option:\n";
    cout << "1. Enter n in main\n";
    cout << "2. Enter n inside the function\n";
    cout << "Your choice: ";
    cin >> choice;

    if (choice == 1) {
        int n;
        cout << "Enter n: ";
        cin >> n;

        if (n <= 0) {
            cout << "Please enter a positive integer." << endl;
        } else {
            cout << "Harmonic sum H(" << n << ") = " << harmonic_recursive(n) << endl;
        }
    } 
    else if (choice == 2) {
        cout << "Harmonic sum = " << harmonic_recursive() << endl;
    } 
    else {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}
