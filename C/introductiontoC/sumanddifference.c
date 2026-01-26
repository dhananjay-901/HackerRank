#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a;
    int b;
    float c;
    float d;
    int sum;
    int sub;
    float sum1;
    float sub1;
    
    scanf("%d %d",&a, &b);
    scanf("%f %f",&c, &d);
    sum = a+b;
    sub = a-b;
    sum1=c+d;
    sub1=c-d;
    
    printf("%d ", sum);
    printf("%d\n", sub);
    printf("%.1f ", sum1);
    printf("%.1f\n", sub1);
    
    return 0;
}
