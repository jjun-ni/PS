#include <iostream> 
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(void){
    string eq;
    cin >> eq;
    vector<char> stack;
    string out = "";
    for(int i = 0; i < eq.size(); ++i){
        if(eq[i] == '*' || eq[i] == '/'){
            if(!stack.empty()){
                if(stack.back() == '*' || stack.back() == '/'){
                    while(stack.back() != 0 && stack.back() != '+' 
                    && stack.back() != '-' && stack.back() != '('){
                        out += stack.back();
                        stack.pop_back();
                    }
                }
            }
            stack.push_back(eq[i]);
        }
        else if(eq[i] == '(') stack.push_back(eq[i]);
        else if(eq[i] == ')'){
            while(stack.back() != '('){
                out += stack.back();
                stack.pop_back();
            }
            stack.pop_back();
        }
        else if(eq[i] == '+' || eq[i] == '-'){
            if(!stack.empty()){
                while(stack.size() != 0 && stack.back() != '('){
                    out += stack.back();
                    stack.pop_back();
                }
                stack.push_back(eq[i]);
            }
            else stack.push_back(eq[i]);
        }
        else out += eq[i];
    }

    while(!stack.empty()){
        out += stack.back();
        stack.pop_back();
    }
    cout << out;    
    return 0;
}
