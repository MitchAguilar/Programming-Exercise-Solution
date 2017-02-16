//100 without recursion=sin recursividad
#include <iostream>
#include <algorithm>
using namespace std;
int main (){
    int i, j;
 
    while ( cin >>i>>j  ) {
 
        unsigned long long int temp_i = i;//saving initialize i
        unsigned long long int temp_j = j;//savinn initialize j
 
        if ( i > j ) swap (i, j);//swap=intercambiar i for j
 
        int max_cycle_length = 0;//max cicle length
        int cycle_length;//cycle length
 
        while ( i <= j ) {//while, when <=j
            int n = i;//initialize for i
            cycle_length = 1;//length of cycle
 
            while ( n != 1 ) {//cycle, if n different 1
                if ( n % 2 == 1 )   n = 3 * n + 1; //n=(n+1)+n+1; "implement"iterative sum
                else n /= 2;//else n divided 2
                ++cycle_length;//increment length of cycle
            }
 
            if ( cycle_length > max_cycle_length )//exchange if cycle length
                max_cycle_length = cycle_length;//exchange..
 
            ++i;//increment i for "give back"=devolver
        }
 		//cout<<i<<" "<<j<<" "<< max_cycle_length << endl;
        cout<<temp_i<<" "<< temp_j<<" "<< max_cycle_length << endl;
    }
    return 0;//return 0, started...
}
	
//solución a problema 100 de uva 
//by:MADI"MITCH";
		



