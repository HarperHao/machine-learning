#include <stdio.h>
#include <stdlib.h>
#define MAX 100
void HeapAdjust(int a[],int s,int m,int n)//һ��ɸѡ�Ĺ���
{
    int rc,j;
	printf("s:%d m:%d\n",s,m);
    rc=a[s];
    for(j=2*s;j<=m;j=j*2)//ͨ��ѭ���ؽϴ�ĺ��ӽ������ɸѡ
    {
        if(j<m&&a[j]<a[j+1]) j++;//jΪ�ϴ�ļ�¼���±�
        if(rc>a[j]) break;
        a[s]=a[j];s=j;
    }
    a[s]=rc;//����
	for(j=1;j<=n;j++)
			printf("%d ",a[j]);
		printf("\n");
}
void HeapSort(int a[],int n)
{
    int temp,i,j;
    for(i=n/2;i>0;i--)//ͨ��ѭ����ʼ������
    {
        HeapAdjust(a,i,n,n);
    }
    for(i=n;i>0;i--)
    {
		printf("**********\n");
        temp=a[1];
        a[1]=a[i];
        a[i]=temp;//���Ѷ���¼��δ��������һ����¼����
        HeapAdjust(a,1,i-1,n);//���µ���Ϊ����
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