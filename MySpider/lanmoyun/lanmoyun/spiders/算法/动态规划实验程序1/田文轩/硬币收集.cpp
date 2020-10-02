#include<stdio.h>
#include<stdlib.h>
#define MAX 100
int b[MAX][MAX]={0};
int f[MAX][MAX];
int robotcoin_colletion(int c[MAX][MAX],int n,int m)
{
	int i,j;
	f[1][1]=c[1][1];
	for(j=2;j<=m;j++)
		f[1][j]=f[1][j-1]+c[1][j];
	for(i=2;i<=n;i++)
	{
		f[i][1]=f[i-1][1]+c[i][1];
		for(j=2;j<=m;j++)
		{
			f[i][j]=(f[i-1][j]>=f[i][j-1]?f[i-1][j]:f[i][j-1])+c[i][j];
		}
	}
	return f[n][m];
}

int main()
{
	int n,m;
	int c[MAX][MAX];
	int num;
	int i,j;
	for(i=0;i<MAX;i++)
		f[0][i]=-1;
	for(i=0;i<MAX;i++)
		f[i][0]=-1;
	printf("输入木板的行和列：");
	scanf("%d%d",&n,&m);
	printf("输入各行列的值：\n");
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			scanf("%d",&c[i][j]);
		}
	}
	num=robotcoin_colletion(c,n,m);
	printf("最大硬币数量：\n",num);
	printf("运行过程：\n");
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			printf("%d  ",f[i][j]);
		}
		printf("\n");
	}
	printf("最优路径:\n");
	printf("第%d行 第%d列\n",n,m);
	i=n,j=m;
	while(i>=1&&j>=1)
	{
		if(i==j&&i==1)
		{
			break;
		}
		if(i-1>=1&&f[i-1][j]>=f[i][j-1])
		{
			printf("第%d行 第%d列\n",i-1,j);
			i=i-1;j=j;
		}
		else
			if(j-1>=1)
			{
					printf("第%d行 第%d列\n",i,j-1);
					i=i;
					j=j-1;
			}
	}
	system("pause");
}