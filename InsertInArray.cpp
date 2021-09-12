#include<iostream>
using namespace std;
void insert(int a[],int cap,int n, int pos, int x);
int main()
{
  int a[6]={1,2,4,5,8};
  int n=5,cap=6;
  int pos, x;
  cout<<"Enter element :";
  cin>>x;
  cout<<"Enter position:";
  cin>>pos;
  if(n==cap)
   cout<<"Array is full";
  else
  insert(a,cap,n,pos,x);
  return 0;
}
void insert(int a[],int cap,int n, int pos, int x)
{
  for(int i=n-1;i>=pos-1;i--)
  {
    a[i+1]=a[i];
  }
  a[pos-1]=x;

  for(int j=0;j<cap;j++)
  {
    cout<<a[j]<<" ";
  }
}
