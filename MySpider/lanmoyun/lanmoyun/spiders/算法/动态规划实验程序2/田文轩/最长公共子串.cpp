//������
//
//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
//
//char* longest_common_substring(char *str1,char *str2)
//{
//	int str1len = strlen(str1);
//	int str2len = strlen(str2);
//	int i,j,index,max=0,num=0; 
//	int start;
//	//�������ַ�����������ֱ�ߣ��̶�һ��ֱ�ߣ�����һ����ͷ��β��ʼ�ƶ�����һ��̶���ֱ�߱Ƚ�ֵ��
//	for(i = 0; i < str1len; i++) 
//	{
//		for(j = 0; j < str2len; j++)
//		{
//			//�����start1��start2�ǱȽϹؼ���
//			int start1=i;
//			int start2=j;
//			while((start1 <= str1len-1) && (start2 <= str2len-1) && (str1[start1++] == str2[start2++]))
//				num++;
//			if(num > max)//���num�ǵ�ǰ���ƥ��ĸ������򸳸�max��������start����str1�ƥ�俪ʼ��λ��
//			{
//				max=num;
//				start=i; 
//			} 
//			num=0;//���num���ǵ�ǰ���ģ���Ϊ0ֵ����ѭ��
//		}
//	}
//	char *str=(char *)malloc(max + 1);
//	strncpy(str,str1 + start,max);//���ַ���str1��startλ�ÿ�ʼ������max���ַ���str�У�����������ҳ�������Ӵ�
//	str[max] = '\0';
//	printf("����������Ӵ��ĳ���Ϊ��%d\n",max);
//	return str;
//} 
//
//int main()
//{ 
//	char str1[1000],str2[1000];
//	printf("�������һ���ַ�����");
//	gets(str1);
//	printf("������ڶ����ַ�����");
//	gets(str2);
//	char *str= longest_common_substring(str1,str2);
//	printf("%s\n",str);
//	system("pause");
//}


//��̬�滮��

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 100
 

int longest_common_substring(char *str1, char *str2)
{
	int i,j,k,len1,len2,max,x,y;
	len1 = strlen(str1);
	len2 = strlen(str2);
	int c[MAX][MAX];
	for(i = 0; i < len1+1; i++)
		c[i][0]=0;        //��0�ж���ʼ��Ϊ0
	for(j = 0; j < len2+1; j++)
		c[0][j]=0;        //��0�ж���ʼ��Ϊ0 
	max = -1;
	for(i = 1 ; i < len1+1 ; i++)
	{
		for(j = 1; j < len2+1; j++)
		{
			if(str1[i-1]==str2[j-1])     //ֻ��Ҫ�����Ϸ���c[i-1][j-1]�ȽϾͿ�����
				c[i][j]=c[i-1][j-1]+1;
			else                         //��������ʱ��Ҫ����ߵ�c[i][j-1]���ϱߵ�c[i-1][j]ֵ�Ƚϣ����ﲻ��Ҫ
				c[i][j]=0;
			if(c[i][j]>max)
			{
				max=c[i][j];
				x=i;
				y=j;
			}
		}
	}
	//��������Ӵ�
	char s[1000];
	k=max;
	i=x-1,j=y-1;
	s[k--]='\0';
	while(i>=0 && j>=0)
	{
		if(str1[i]==str2[j])
		{
			s[k--]=str1[i];
			i--;
			j--;
		}
		else       //ֻҪ��һ������ȣ���˵����ȵĹ����ַ����ˣ���������
			break;
	}
	printf("������Ӵ�Ϊ��");
	puts(s);
	return max;

}

 

int main(void)
{
	char str1[1000],str2[1000];
	printf("�������һ���ַ�����");
	gets(str1);
	printf("������ڶ����ַ�����");
	gets(str2);
	int len = longest_common_substring(str1, str2);
	printf("����������Ӵ��ĳ���Ϊ��%d\n",len);
	system("pause");
}





































