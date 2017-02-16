//196
#include <iostream>
#include <string>
using namespace std;

int main(){
	int cases,columns,rows,*pointer;
	while ((cin>>cases)>0){//numbers of cases
		
		cin >> columns;//reading columns  value
		cin >> rows;//reading rows  value
		
		int arrayvalue[columns][rows];//array value. 
		
		int col;//for columns
		int ro;//for rows
		
		for (col=0;columns>col;col++){//writing columns
			for(ro=0;rows>ro;ro++){//writing columns
				cin>>arrayvalue[ro][col];//writing two-dimensional array
				//algorithm not found 
				if(arrayvalue[1] [1]){//pointer if...
				   	pointer=&arrayvalue[1][1];//pointer creating
					*pointer=12;//new value of array
				}
			}
		}
		
	
		for (col=0;columns>col;col++){//reading columns
		cout<<"  "<<endl;//space
			for(ro=0;rows>ro;ro++){//reading columns
				cout << arrayvalue[col][ro]<<" ";//reading two-dimensional array
			}
		}
		
		
	}
}
//solución a problema 196 de uva 
//by:MADI"MITCH";
		
