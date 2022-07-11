//
//  test.c
//  
//
//  Created by david gae on 12/28/13.
//
//

#include <stdio.h>




void main ()
{
    int number[6]={10,11,12,210,1,5};
    int j;
    int i;
    int k; 
    int key;
    int numelements = sizeof(number)/sizeof(int) ;
    
	for ( i = 0; i<numelements; i++)  {

	        key = number[i];

		printf("before number[%d] = %d\n", i, number[i] );
		//printf("%d\n", numelements);
       				 }

	for ( i =1; i <=(numelements-1); i++) 
          { 
		//printf("%d\n",i);
		for ( j = 0; j< i; j++)
		{
		//printf("%d%d\n",j,i);
		 if (number[j] > number[i])
			{
			key = number[j];
		        number[j] = number[i];

			for (k = i; k > j; k--) //look through reverse over
				number[k] = number[ k -1]; //back value is
				
				number[k+1] = key;
				//printf("%d%d\n",k);

			}
		}
	 }
        for ( i = 0 ; i <= numelements ; i++ )
               printf ( "after number[%d] = %d\n", i, number[i] ) ;

}
       
