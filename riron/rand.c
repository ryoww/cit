#include <stdio.h> 
#include <stdlib.h> 
#include <math.h>  
#include <time.h>

double nrand();
double x;


main(){
         int i;
         int x;

	 /* ascii 65-90 */
	 srand((unsigned int)time(NULL));


	 for(i=0; i < 100; i++)
	   {
	     x = rand()%10;
	     x = x + 85;
	     printf("%c",x);
	   }
}


