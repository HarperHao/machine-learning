#include<stdio.h>
#include<stdlib.h>
#define max(a,b) (a>b? a:b)
int m,n;
#define MAX 100
int w[MAX];
int p[MAX];
int c[MAX][MAX]={0};
int item[MAX];
void findWhat(int i, int j) {				//最优解情况
	if (i >= 0) {
		if (c[i][j] == c[i - 1][j]) {
			item[i] = 0;
			findWhat(i - 1, j);
		}
		else if (j - w[i] >= 0 && c[i][j] == c[i - 1][j - w[i]] + p[i]) {
			item[i] = 1;
			findWhat(i - 1, j - w[i]);
		}
	}
}

int main()
{
	printf("输入元素个数：\n");
    scanf("%d",&m);
	printf("输入背包容量：\n");
    scanf("%d",&n);
	int i,j;
    for(i=1;i<=m;++i)
	{
	   printf("输入第%d个商品的重量：",i);
	   scanf("%d",&w[i]);
	}
	printf("\n");
	 for(i=1;i<=m;++i)
	{
	   printf("输入第%d个商品的价值：",i);
	   scanf("%d",&p[i]);
	}
    for(i=1;i<=m;++i)
    {
        for(j=0;j<=n;++j)
        {
			c[i][j]=c[i-1][j];
            if(j-w[i]>=0) 
			   c[i][j]=max(c[i][j],c[i-1][j-w[i]]+p[i]);
        }
    }
	for(i=1;i<=m;++i)
    {
        for(j=0;j<=n;++j)
        {
			printf("%d\t",c[i][j]);
		}
		printf("\n");
	}
    printf("最优解：%d\n",c[m][n]);
	findWhat(m,n);
	for(i=1;i<=m;i++)
		if(item[i]==1)
			printf("第%d个 ",i);
    system("pause");
} 
