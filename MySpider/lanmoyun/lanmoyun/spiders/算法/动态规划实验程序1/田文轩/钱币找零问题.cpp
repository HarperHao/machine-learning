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
	printf("�����ֵ��������");
	scanf("%d",&m);
	for(i=1;i<=m;i++)
	{
		printf("�����%d����ֵ��",i);
		scanf("%d",&a[i]);
	}
	printf("�����ܽ�");
	scanf("%d",&n);
	f=change_making(a,m,n);
	printf("Ӳ�����ٵ���Ŀ:%d",f);
	system("pause");
}