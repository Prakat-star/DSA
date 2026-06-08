#include <iostream>
using namespace std;
#define MAX 5
int queueArr[MAX];
int front = -1;
int rear = -1;

void enqueue()
{
    int x;
    if(rear == MAX-1)
    {
        cout << "Queue Overflow\n";
        return;
    }
    cout << "Enter element: ";
    cin >> x;
    if(front == -1)
        front = 0;
    rear++;
    queueArr[rear] = x;
    cout << "Inserted\n";
}

void dequeue()
{
    if(front == -1 || front > rear)
    {
        cout << "Queue Underflow\n";
        return;
    }
    cout << "Deleted element: "
         << queueArr[front] << endl;
    front++;
}

void display()
{
    if(front == -1 || front > rear)
    {
        cout << "Queue Empty\n";
        return;
    }
    for(int i = front; i <= rear; i++)
        cout << queueArr[i] << " ";
    cout << endl;
}

int main()
{
    int choice;
    do
    {
        cout << "\n1.Enqueue";
        cout << "\n2.Dequeue";
        cout << "\n3.Display";
        cout << "\n4.Exit";
        cout << "\nChoice: ";
        cin >> choice;

        switch(choice)
        {
            case 1: enqueue(); break;
            case 2: dequeue(); break;
            case 3: display(); break;
        }
    }while(choice != 4);

    return 0;
}