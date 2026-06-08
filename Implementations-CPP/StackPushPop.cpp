#include <iostream>
using namespace std;
#define MAX 5
int stackArr[MAX];
int top = -1;

void push()
{
    int x;
    if(top == MAX - 1)
    {
        cout << "Stack Overflow\n";
        return;
    }
    cout << "Enter element: ";
    cin >> x;
    top++;
    stackArr[top] = x;
    cout << "Element pushed\n";
}

void pop()
{
    if(top == -1)
    {
        cout << "Stack Underflow\n";
        return;
    }
    cout << "Deleted element: " << stackArr[top] << endl;
    top--;
}

void display()
{
    if(top == -1)
    {
        cout << "Stack Empty\n";
        return;
    }
    for(int i = top; i >= 0; i--)
        cout << stackArr[i] << " ";
    cout << endl;
}

int main()
{
    int choice;
    do
    {
        cout << "\n1.Push";
        cout << "\n2.Pop";
        cout << "\n3.Display";
        cout << "\n4.Exit";
        cout << "\nChoice: ";
        cin >> choice;
        switch(choice)
        {
            case 1: push(); break;
            case 2: pop(); break;
            case 3: display(); break;
        }
    }while(choice != 4);
    
    return 0;
}