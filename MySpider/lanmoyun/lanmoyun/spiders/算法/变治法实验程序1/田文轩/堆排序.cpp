#include <stdio.h>
#include <stdlib.h>
#define MAX 100
void HeapAdjust(int a[],int s,int m,int n)//一次筛选的过程
{
    int rc,j;
	printf("s:%d m:%d\n",s,m);
    rc=a[s];
    for(j=2*s;j<=m;j=j*2)//通过循环沿较大的孩子结点向下筛选
    {
        if(j<m&&a[j]<a[j+1]) j++;//j为较大的记录的下标
        if(rc>a[j]) break;
        a[s]=a[j];s=j;
    }
    a[s]=rc;//插入
	for(j=1;j<=n;j++)
			printf("%d ",a[j]);
		printf("\n");
}
void HeapSort(int a[],int n)
{
    int temp,i,j;
    for(i=n/2;i>0;i--)//通过循环初始化顶堆
    {
        HeapAdjust(a,i,n,n);
    }
    for(i=n;i>0;i--)
    {
		printf("**********\n");
        temp=a[1];
        a[1]=a[i];
        a[i]=temp;//将堆顶记录与未排序的最后一个记录交换
        HeapAdjust(a,1,i-1,n);//重新调整为顶堆
    }
}
int main()
{
    int n,i;
    scanf("%d",&n);
	int a[MAX];
    for(i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    HeapSort(a,n);
	for(i=1;i<=n;i++)
    {
       printf("%d ",a[i]);
    }
	system("pause");
}