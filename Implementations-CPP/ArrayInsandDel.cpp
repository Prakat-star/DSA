#include<iostream>
using namespace std;
int main()
{
    int arr[100],n,choice,pos,item;
    cout<<"enter numbers of elememts: ";
    cin>>n;
    cout<<"Enter elements :\n";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<" \n 1.Insertion";
    cout<<"\n 2.Deletation";
    cin>>choice;
    switch(choice){
        case 1:
        cout<<"enter position to insert:";
        cin>>pos;
        cout<<"enter element to insert:";
        cin>>item;
         for(int i = n; i >= pos; i--)
                arr[i] = arr[i - 1];

            arr[pos - 1] = item;
            n++;

            cout << "\nArray after insertion:\n";
            for(int i = 0; i < n; i++)
                cout << arr[i] << " ";
            break;

        case 2:
            cout << "Enter position to delete: ";
            cin >> pos;

            for(int i = pos - 1; i < n - 1; i++)
                arr[i] = arr[i + 1];

            n--;

            cout << "\nArray after deletion:\n";
            for(int i = 0; i < n; i++)
                cout << arr[i] << " ";
            break;

        default:
            cout << "Invalid choice!";
    }

    return 0;
}
        

    