#include <iostream>
using namespace std;

int main (){
	int a;
	while(cin>>a){
		int b=0;
		int c=1;
		int d=0;
		for (int i=0;i<a-1;i++){
			d=b+c;
			b=c;
			c=d;	
		}
		cout<<"The Fibonacci number for "<<a<<" is "<<c<<endl;
	}
	return 0;
}
//not found in uva
