#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTEX_NUM 100 				//��󶥵���
#define MAX_INT 10000 					//����� 

typedef struct
{
    int pi[MAX_VERTEX_NUM];			//���v��vi��һ�����·��
    int end;
}PathType;
 


//�ڽӾ����ʾ��ͼ
typedef struct
{
    char V[MAX_VERTEX_NUM]; 		//����洢�ռ� //�趥��Ϊ�ַ�����
    int A[MAX_VERTEX_NUM][MAX_VERTEX_NUM]; //�ڽӾ��� 
}MGraph;

int path[MAX_VERTEX_NUM][MAX_VERTEX_NUM];//v������������·������
int D[MAX_VERTEX_NUM][MAX_VERTEX_NUM];//v�����������·���������� 
    

//Floyd�㷨
//����G�����ڽӾ����ʾ����������������·�� 
//D[][]�����·�����Ⱦ���path[][]���·����־���� 
void Floyd(MGraph * G,int path[][MAX_VERTEX_NUM],int D[][MAX_VERTEX_NUM],int n)
{ 
    int i,j,k;
	//��ʼ��
    for(i=0;i<n;i++)
	{ 
        for(j=0;j<n;j++)
		{
            if(G->A[i][j]<MAX_INT)
			{
                path[i][j]=j;
            }
			else
			{
                path[i][j]=-1;
            }
            D[i][j]=G->A[i][j];
        }
    } 
    
	//����n������
    for(k=0;k<n;k++)
	{ 
        for(i=0;i<n;i++)
		{
            for(j=0;j<n;j++)
			{
                if(D[i][j] > D[i][k] + D[k][j])
				{
                    D[i][j]=D[i][k]+D[k][j];			//ȡС�� 
                    path[i][j]=k;				//��Vi�ĺ�� 
                }
            }
        }
    }
}


int main()
{
    int i,j,k,v=0,n=6;								//vΪ��㣬nΪ������� 
    MGraph G;
    
    //��ʼ�� 
    int a[MAX_VERTEX_NUM][MAX_VERTEX_NUM]=
	{
        {0,12,1,MAX_INT,17,MAX_INT},
        {12,0,10,3,MAX_INT,5},
        {18,10,0,MAX_INT,21,11},
        {MAX_INT,3,MAX_INT,0,MAX_INT,8},
        {17,MAX_INT,21,MAX_INT,0,16},
        {MAX_INT,5,11,8,16,0} 
    };
    for(i=0;i<n;i++)
	{
        for(j=0;j<n;j++)
		{
            G.A[i][j]=a[i][j];
        }
    } 
    
    Floyd(&G,path,D,6);
	//���ÿ�Զ�������·�����ȼ����·��
    for(i=0;i<n;i++)
	{					
        for(j=0;j<n;j++)
		{
            printf("����%d������%d����̳���: ",i,j); 
            printf("%d\t",D[i][j]);						//���Vi��Vj�����·������
            k=path[i][j];								//ȡ·����Vi�ĺ���Vk
            if(k==-1)
			{
                printf("����%d �� ����%d ֮��û��·��\n",i,j);//·�������� 
            }
			else
			{
                printf("���·��Ϊ:"); 
                printf("(%d->",i);					//���Vi�����i
                //k������·���յ�jʱ
				while(k!=j)
				{						 
                    printf("%d->",k);				//���k
                    k=path[k][j];					//��·������һ������� 
                }
                printf("%d)\n",j);			//���·���յ���� 
            }
            printf("\n");
        } 
    }
    system("pause");
}