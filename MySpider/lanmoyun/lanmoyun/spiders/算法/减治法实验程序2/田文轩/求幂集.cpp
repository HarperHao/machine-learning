#include<stdlib.h>
#include<stdio.h>
#define N 3  //�̶�λ��
int main()
{
 int arr[N] = {0};//�������ʼ��Ϊ0��λ������ʱ�������0���
 int i;
 int n;
 printf("Input number:");
 scanf("%d",&n);
 for (i = N-1; i >=0; i--)  //������Ӻ���ǰ��ֵ
 {
  arr[i] = n % 2;
  n = n / 2;
 }

 printf("���������:");
 for (i = 0; i <= N - 1; i++)
 {
  printf("%d",arr[i]);
 }
 system("pause");
}