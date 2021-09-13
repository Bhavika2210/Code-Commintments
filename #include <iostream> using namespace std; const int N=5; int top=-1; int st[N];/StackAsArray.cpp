
#include <iostream>
using namespace std;
const int N=5;
int top=-1;
int st[N];
// stack functions-------
 void push()
 {
     int x;
     
     if(top==N-1)
     {
         cout<<"Stack is full \n";
     }
     else
     {
         cout<<"Enter: ";
         cin>>x;
         top++;
         st[top]=x;
     }
 }
 void pop()
 {
     if(top!=-1)
     {
         cout<<st[top]<<endl;
         top--;
     }
     else
     cout<<"Stack is empty\n";
 }
 void peek()
 {
     if(top==-1)
     cout<<"Stack is empty\n";
     else
     cout<<st[top]<<endl;
 }
 void display()
 {
     if(top==-1)
     cout<<"Nothing to display, STACK IS EMPTY\n";
     for(int i=top;i>-1;i--)
     cout<<st[i]<<endl;
 }
int main()
 {
     int st[N];
     int choice;
     do{
     cout<<"1. push 2.pop 3.peek 4.display 5.exit\n";    // menu
     cin>>choice;
     switch(choice)    
     {
         case 1: push();
                  break;
         case 2:pop();
                 break;
         case 3:peek();
               break;
         case 4: display();
                break;
        case 5: cout<<"Quitting...";
               break;
       
         default: cout<<"Invalid choice.\n";
     }
     }while(choice!=5);
return 0;


 }
