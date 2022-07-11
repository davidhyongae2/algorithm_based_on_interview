// 

#include <stdio.h>

const int primes[10]={1,2,3,4,5,6,10,12,14};

int main(int argc, char* argv[])
{
    int i,j;
    int numelements= sizeof(primes)/sizeof(int) ;
    for ( j=0; j<10000000000000000000; j++) {
	 	printf(" odd \n", primes[i]*2);
		printf(" even \n", primes[i]*2 + 1); 
    			}
    return 0;
}
