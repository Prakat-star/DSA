#include <iostream>
using namespace std;
#define MAX 5

int queue[MAX];
int front = -1;
int rear = -1;  

void enqueue(int value)
{
    if (rear == MAX - 1)
    {
        cout << "Queue Full" << endl;
        return;
    }
    if (front == -1)
    {
        front = 0;
    }
    rear++;
    queue[rear] = value;
}

void dequeue()
{
    if (front == -1 || front > rear)
    {
        cout << "Queue Empty" << endl;
        return;
    }
    cout << "Deleted: " << queue[front] << endl;
    front++;
}

void display()
{
    for (int i = front; i <= rear; i++)
    {
        cout << queue[i] << " ";
    }
    cout << endl;
}
int main()
{
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    dequeue();
    display();
    enqueue(40);
    display();
    return 0;
}