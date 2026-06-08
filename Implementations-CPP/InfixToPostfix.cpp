#include <iostream>
#include <stack>
#include <string>
#include <cctype>
using namespace std;

bool isOperator(char ch)
{
    return (ch == '+' || ch == '-' ||
            ch == '*' || ch == '/' ||
            ch == '^');
}

int precedence(char op)
{
    if(op == '^')
        return 3;
    if(op == '*' || op == '/')
        return 2;
    if(op == '+' || op == '-')
        return 1;

    return 0;
}

string infixToPostfix(string infix)
{
    stack<char> st;
    string postfix = "";

    for(char ch : infix)
    {
        if(isalnum(ch))
        {
            postfix += ch;
        }
        else if(ch == '(')
        {
            st.push(ch);
        }
        else if(ch == ')')
        {
            while(!st.empty() && st.top() != '(')
            {
                postfix += st.top();
                st.pop();
            }
            if(!st.empty())
                st.pop();
        }
        else if(isOperator(ch))
        {
            while(!st.empty() &&
                  st.top() != '(' &&
                  precedence(st.top()) >= precedence(ch))
            {
                postfix += st.top();
                st.pop();
            }
            st.push(ch);
        }
    }
    while(!st.empty())
    {
        postfix += st.top();
        st.pop();
    }

    return postfix;
}
int main()
{
    string infix;
    cout << "Enter infix expression: ";
    cin >> infix;
    string postfix = infixToPostfix(infix);
    cout << "Postfix Expression: " << postfix << endl;

    return 0;
}