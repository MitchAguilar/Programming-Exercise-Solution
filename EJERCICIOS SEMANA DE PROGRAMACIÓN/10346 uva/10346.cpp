#include <iostream>
using namespace std;

int main(){
	
	int numbercigarettes,butts,cont,res;//creating 
	
	while(cin>>numbercigarettes>>butts){//reading n and k
		cont=0;//initialize
		res=0;//initialize
		
		while(numbercigarettes>0){//cycle
			cont = cont + numbercigarettes;//sum n
			res = res + numbercigarettes;//sum n
			numbercigarettes = res / butts;//res div k
			res = res % butts;//module of k 
		}
		cout<<cont<<endl;
	}
	return 0;
}

