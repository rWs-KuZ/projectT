#include <iostream>

double add(double a, double b);
double cal(double (*pt)(double,double),double a,double b);

int main(){
    std::cout<<cal(add,1.6,1.8);
    return 0;
}
double add(double a,double b){
    return a+b;
}
double cal(double (*pt)(double,double),double a,double b){
    return (*pt)(a,b);
}
