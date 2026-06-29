#include <iostream>
using namespace std;
#define MAX 5
int cq[MAX];
int front = -1;
int rear = -1;

void enqueue(int value)
{
    if ((rear + 1) % MAX == front)
    {
        cout << "Circular Queue is Full" << endl;
        return;
    }
    if (front == -1)
    {
        front = 0;
        rear = 0;
    }
    else
    {
        rear = (rear + 1) % MAX;
    }
    cq[rear] = value;
}

void dequeue()
{
    if (front == -1)
    {
        cout << "Circular Queue is Empty" << endl;
        return;
    }
    cout << "Deleted: " << cq[front] << endl;
    if (front == rear)
    {
        front = -1;
        rear = -1;
    }
    else
    {
        front = (front + 1) % MAX;
    }
}

void display()
{
    if (front == -1)
    {
        cout << "Queue is Empty" << endl;
        return;
    }
    int i = front;
    while (true)
    {
        cout << cq[i] << " ";
        if (i == rear)
            break;

        i = (i + 1) % MAX;
    }
    cout << endl;
}

int main()
{
    enqueue(10);
    enqueue(20);
    display();
    dequeue();
    display();
    enqueue(40);
    enqueue(50);
    dequeue();
    display();
    return 0;
}