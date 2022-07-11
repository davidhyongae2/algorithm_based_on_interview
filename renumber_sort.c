#include <stdio.h>
 
int main()
{
  int n, array[1000], c, d, t;
 
  printf("Enter number of elements\n");
  scanf("%d", &n);
 
  printf("Enter %d integers\n", n);
 
  for (c = 0; c < n; c++) {
    scanf("%d", &array[c]);
      //printf("%d\n",c);
  }
 
  for (c = 1 ; c <= n - 1; c++) {
    d = c; //count forward
 	 //printf("%d%d\n",n,d);
    while ( d > 0 && array[d] < array[d-1]) {
        
					//count backwards
      t          = array[d]; //temp store value 
      array[d]   = array[d-1]; //  d-1 is array[d]
      array[d-1] = t;      //move value to array[d-1]
	d--;
    }
  }
//printf("%d\n", d);
//printf("%d\n", t);
//printf("array[%d-1] = %d\n",  array[d-1]);
//printf("array[%d] = %d\n",  array[d]);


 
  printf("Sorted list in ascending order:\n");
 
  for (c = 0; c <= n - 1; c++) {
    printf("%d\n", array[c]);
  }
 
  return 0;
}

