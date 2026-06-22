#include <iostream>
#include <stack>
using namespace std;
int main()
{
    string infix, postfix = "";
    stack<char> s;
    cout << "Enter Infix Expression: ";
    cin >> infix;
    for(int i = 0; i < infix.length(); i++)
    {
        char ch = infix[i];
        if((ch >= 'A' && ch <= 'Z') ||
           (ch >= 'a' && ch <= 'z') ||
           (ch >= '0' && ch <= '9'))
        {
            postfix += ch;
        }
        else if(ch == '(')
        {
            s.push(ch);
        }
        else if(ch == ')')
        {
            while(!s.empty() && s.top() != '(')
            {
                postfix += s.top();
                s.pop();
            }
            if(!s.empty())
                s.pop();
        }
        else
        {
            while(!s.empty() && s.top() != '(')
            {
                int p1, p2;
                if(ch == '+' || ch == '-')
                    p1 = 1;
                else if(ch == '*' || ch == '/')
                    p1 = 2;
                else
                    p1 = 3;
                if(s.top() == '+' || s.top() == '-')
                    p2 = 1;
                else if(s.top() == '*' || s.top() == '/')
                    p2 = 2;
                else
                    p2 = 3;
                if(p2 >= p1)
                {
                    postfix += s.top();
                    s.pop();
                }
                else
                    break;
            }
            s.push(ch);
        }
    }
    while(!s.empty())
    {
        postfix += s.top();
        s.pop();
    }
    cout << "Postfix Expression: " << postfix;
    return 0;
}