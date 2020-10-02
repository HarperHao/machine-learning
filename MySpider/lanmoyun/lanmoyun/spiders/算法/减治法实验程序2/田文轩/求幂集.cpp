#include<stdlib.h>
#include<stdio.h>
#define N 3  //固定位数
int main()
{
 int arr[N] = {0};//将数组初始化为0（位数不满时，将输出0填补）
 int i;
 int n;
 printf("Input number:");
 scanf("%d",&n);
 for (i = N-1; i >=0; i--)  //对数组从后往前赋值
 {
  arr[i] = n % 2;
  n = n / 2;
 }

 printf("输出二进制:");
 for (i = 0; i <= N - 1; i++)
 {
  printf("%d",arr[i]);
 }
 system("pause");
}