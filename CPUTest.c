#include <time.h>
#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>

#define MILLION 10000000
#define ITER	 9998000 
#define SCHEDOFF 3 
int main(int argc, char **argv) {
	long int iterations = MILLION;
	struct timeval start, end;
	long int i;
	long int time;
	long int prevtime = 0;
	float offcount = 0;
	long int offs = 0;
	long int oncount = 0;
	long int inc = 0;
	float cpu = 0;
	float tcpu = 0;

	gettimeofday(&start, NULL);

	for (i = 0; i < iterations; i++) {
	   gettimeofday(&end, NULL);
	   time = (end.tv_sec * 1000000 + end.tv_usec) -
		    (start.tv_sec * 1000000 + start.tv_usec);
	   if ((time - prevtime) > SCHEDOFF) { 
			offs = (time - prevtime)/SCHEDOFF;	
			offcount += offs;
	   }
	   else
			oncount++;
	   cpu = oncount/(offcount + oncount);
	   tcpu += oncount/(offcount + oncount);
	   if (i > ITER) 
	   	printf("\n%ld\t%ld\t%ld\t%f\t%f", i, time, oncount, offcount, cpu); 
	   prevtime = time;
	}
	printf("\t cpu share = %f \n", tcpu/MILLION); 
	return 0;
}
