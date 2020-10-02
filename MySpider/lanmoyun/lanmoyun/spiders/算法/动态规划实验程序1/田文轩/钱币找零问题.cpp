#include<stdio.h>
#include<stdlib.h>
#define MAX 100


int change_making(int a[],int m,int n)
{
	int i,j,f[MAX],temp;
	f[0]=0;
	for(i=1;i<=n;i++)
	{
		temp=10000;
		j=1;
		while(j<=m&&i>=a[j])
		{	
			temp=f[i-a[j]]>=temp?temp:f[i-a[j]];
			j=j+1;
		}
		f[i]=temp+1;
	}
	return f[n];
}

int main()
{
	int i,n,m,a[MAX];
	int f;
	printf("输入币值种类数：");
	scanf("%d",&m);
	for(i=1;i<=m;i++)
	{
		printf("输入第%d个币值：",i);
		scanf("%d",&a[i]);
	}
	printf("输入总金额：");
	scanf("%d",&n);
	f=change_making(a,m,n);
	printf("硬币最少的数目:%d",f);
	system("pause");
}