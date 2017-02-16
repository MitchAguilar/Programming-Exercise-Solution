#include <iostream>
#include <string>
//#include <algorithm>
using namespace std;

int main(){
	string word;//creating string
	//while(cin>>word){//reading string
	while(getline(cin,word)){//reading string
		string aux_string=" ";//creating string aux
		string aux_stringtwo=" ";
		
		/*for (int i=word.size();i<=word.size();--i){//creating cycle, size of string 
			aux_string +=word[i];//string aux = string aux +word[vector];	
		}*/
		for (int i=word.size();i<=word.size();--i){//creating cycle, size of string 
			aux_string +=word[i];//string aux = string aux +word[vector];	
			//cout<<aux_string;
			//aux_stringtwo+=aux_string[i];
				
		}
	
		string reversed = string(aux_string.rbegin(), aux_string.rend());  
		/*for (int i=aux_string.size();i<=aux_string.size() ;++i){
			aux_string+=aux_string[i];
			aux_stringtwo+=aux_string[i];
			//for(int i=aux_stringtwo.size();i>=aux_stringtwo.size();--i ){
			//aux_string+=word[1];	
			//}*/
			
		
		//cout<<aux_stringtwo;
		cout<<reversed;
		//cout<<aux_string<<endl;//see..
	}
	return 0;
}

/*#include <iostream>
#include <sstream>

int main(int argc, char** argv){

    std::string str("Texto para dividir");
    std::istringstream isstream(str);

    while(!isstream.eof()){

        std::string tempStr;

        isstream >> tempStr;

        std::cout << tempStr << std::endl;
    }

    return 0;
}*/
