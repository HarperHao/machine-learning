#include<stdio.h>
#include<stdlib.h>
#define max 4
int main()
{
	double sum,a_inverse[max][max]={0},u_inverse[max][max]={0},l_inverse[max][max]={0},L[max][max]={0},U[max][max]={0},A[max][max]={4,2,1,5,8,7,2,10,4,8,3,6,12,6,11,20};
	int i,j,k;
	
	for(j=0;j<4;j++) 
		U[0][j]=A[0][j];
	for(i=1;i<4;i++)
		L[i][0]=A[i][0]/U[0][0];
	for(i=0;i<4;i++) 
		L[i][i]=1;
	for(i=1;i<4;i++)
		for(j=i;j<4;j++)
		{
			sum=0;
			for(k=0;k<=i-1;k++)
				sum+=L[i][k]*U[k][j];
			U[i][j]=A[i][j]-sum;
			sum=0;
			for(k=0;k<=i-1;k++)
				sum+=L[j][k]*U[k][i];
			L[j][i]=(A[j][i]-sum)/U[i][i];
		}

	printf("A的二维数组为：\n");
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			printf("%5.4lf\t",A[i][j]);
		printf("\n");
	}
	printf("L的二维数组为：\n");
	  for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			printf("%5.4lf\t",L[i][j]);
		printf("\n");
	}
	printf("U的二维数组为：\n");
	for(i=0;i<4;i++)
	{

		for(j=0;j<4;j++)
			printf("%5.4lf\t",U[i][j]);
		printf("\n");
	}

	for (i = 0;i < 4;i++)        
    {
        l_inverse[i][i] = 1;
    }
    for (i= 1;i < 4;i++)
    {
        for (j = 0;j < i;j++)
        {
            sum= 0;
            for (k = 0;k < i;k++)
            {
                sum+= L[i][k] * l_inverse[k][j];
            }
            l_inverse[i][j] = -sum;
        }
    }


	for (i = 0;i < 4;i++)                    
    {
        u_inverse[i][i] = 1 / U[i][i];
    }
    for (i = 1;i < 4;i++)
    {
        for (j = i - 1;j >=0;j--)
        {
            sum = 0;
            for (k = j + 1;k <= i;k++)
            {
                sum += U[j][k] * u_inverse[k][i];
            }
            u_inverse[j][i] = -sum / U[j][j];
        }
    }
	printf("L矩阵的逆矩阵为:\n");
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			printf("%5.4lf\t",l_inverse[i][j]);
		}
		printf("\n");
	}
	printf("U矩阵的逆矩阵为:\n");
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			printf("%5.4lf\t",u_inverse[i][j]);
		}
		printf("\n");
	}
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			 sum = 0;
			for (k= 0; k< 4; k++)
			{
				sum = sum + (u_inverse[i][k] * l_inverse[k][j]);
			}
			a_inverse[i][j] = sum;
		}
	}
	printf("A的逆矩阵为：\n");
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			printf("%5.4lf\t",a_inverse[i][j]);
		}
		printf("\n");
	}
	system("pause");
}