#include <stdio.h>


//define function
int r(float add1,float add2);

//remember to define varaible in function
int r(float add1,float add2)
{
 int sum;
 //not necessary
 //float add1,add2;
 sum = add1+add2;
 return sum;
}


int main()
{
// remember to define variable in function
float add1 = 10.3;
float add2 = 20.5;
int i,j,k,m;

for (i=0;i<100;i++) 
    {
    //add1 = 10.3 
    //add2 = 20.5
    //riemann sum
    m = r(add1,add2);
    //printf("%d\n", m);
    j = m - add1;
    //printf("%d\n",j);
    k = i * (j-add1)/100;
    printf("%d\n",k);
 	}
    return k; 
}