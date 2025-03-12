#include <iostream>

using namespace std;

int main()
{
    cout << "Enter a number: ";
    int n;
    cin >> n;

    int fact = 1;
    for (int i = 1; i < n; i++)
    {
        cout << i << "\n";
        fact *= i;
    }

    cout << "The factorial of " << n << " is " << fact << endl;
}
