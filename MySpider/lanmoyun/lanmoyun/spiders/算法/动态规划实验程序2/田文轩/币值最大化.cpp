
#include<stdio.h>
#include<stdlib.h>
#define MAX 6
int main(void){
    int i;
    int c[MAX],f[MAX];
    c[0]=0; 
    printf("输入硬币面值：\n");
    for(i=1;i<=MAX;i++)//这里i是从1开始 
		 scanf("%d",&c[i]);
    f[0]=0;f[1]=c[1];
    for(i=2;i<=MAX;i++)
     f[i]=(c[i]+f[i-2])>f[i-1]?(c[i]+f[i-2]):f[i-1];
    printf("最大币值为：%d",f[MAX]);
} 
