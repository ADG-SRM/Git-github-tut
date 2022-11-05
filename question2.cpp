//2. Print 1 to 100 skipping every multiples of 5 and 2
#include<bits/stdc++.h>
using namespace std;
 
 int main(){
    
    for(int i=1;i<=100;i++){
        if(i%2==0&&i%5==0){
            continue;
        }else{
            cout<<i<<endl;
        }
        
    }
    cout<<endl;
    return 0;
 }
