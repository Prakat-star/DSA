#include <iostream>
using namespace std;
#define MAX 5
int cq[MAX];
int front = -1;
int rear = -1;
void enqueue()
{
    int x;
    if((rear + 1) % MAX == front)
    {
        cout << "Circular Queue Full\n";
        return;
    }
    cout << "Enter element: ";
    cin >> x;
    if(front == -1)
    {
        front = rear = 0;
    }
    else
    {
        rear = (rear + 1) % MAX;
    }
    cq[rear] = x;
    cout << "Inserted\n";
}

void dequeue()
{
    if(front == -1)
    {
        cout << "Circular Queue Empty\n";
        return;
    }
    cout << "Deleted: "
         << cq[front] << endl;
    if(front == rear)
    {
        front = rear = -1;
    }
    else
    {
        front = (front + 1) % MAX;
    }
}

void display()
{
    if(front == -1)
    {
        cout << "Empty\n";
        return;
    }
    int i = front;
    while(true)
    {
        cout << cq[i] << " ";
        if(i == rear)
            break;
        i = (i + 1) % MAX;
    }
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