#include <iostream> 
#include <vector>
#include <algorithm>
typedef long long ll;
using namespace std;

ll pow(ll num, ll exp, ll div);

int main(void){
    ll num, exp, div;
    scanf("%lu %lu %lu", &num, &exp, &div);
    printf("%lu", pow(num, exp, div));

    return 0;
}

ll pow(ll num, ll exp, ll div){
    if(exp == 0) return 1;
    ll tmp = pow(num, exp / 2, div);
    tmp = (tmp * tmp) % div;
    if(exp % 2 == 0) return tmp;
    return (num * tmp) % div;
}