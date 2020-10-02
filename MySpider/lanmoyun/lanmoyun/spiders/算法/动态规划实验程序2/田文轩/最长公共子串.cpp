//暴力法
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
//	//将两个字符串看做两个直尺，固定一个直尺，另外一个从头到尾开始移动，逐一与固定的直尺比较值。
//	for(i = 0; i < str1len; i++) 
//	{
//		for(j = 0; j < str2len; j++)
//		{
//			//这里的start1、start2是比较关键的
//			int start1=i;
//			int start2=j;
//			while((start1 <= str1len-1) && (start2 <= str2len-1) && (str1[start1++] == str2[start2++]))
//				num++;
//			if(num > max)//如果num是当前最大匹配的个数，则赋给max，并且在start记下str1最长匹配开始的位置
//			{
//				max=num;
//				start=i; 
//			} 
//			num=0;//如果num不是当前最大的，则赋为0值继续循环
//		}
//	}
//	char *str=(char *)malloc(max + 1);
//	strncpy(str,str1 + start,max);//从字符串str1的start位置开始，拷贝max个字符到str中，这就是我们找出的最大子串
//	str[max] = '\0';
//	printf("最长公共连续子串的长度为：%d\n",max);
//	return str;
//} 
//
//int main()
//{ 
//	char str1[1000],str2[1000];
//	printf("请输入第一个字符串：");
//	gets(str1);
//	printf("请输入第二个字符串：");
//	gets(str2);
//	char *str= longest_common_substring(str1,str2);
//	printf("%s\n",str);
//	system("pause");
//}


//动态规划法

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
		c[i][0]=0;        //第0列都初始化为0
	for(j = 0; j < len2+1; j++)
		c[0][j]=0;        //第0行都初始化为0 
	max = -1;
	for(i = 1 ; i < len1+1 ; i++)
	{
		for(j = 1; j < len2+1; j++)
		{
			if(str1[i-1]==str2[j-1])     //只需要跟左上方的c[i-1][j-1]比较就可以了
				c[i][j]=c[i-1][j-1]+1;
			else                         //不连续的时候还要跟左边的c[i][j-1]、上边的c[i-1][j]值比较，这里不需要
				c[i][j]=0;
			if(c[i][j]>max)
			{
				max=c[i][j];
				x=i;
				y=j;
			}
		}
	}
	//输出公共子串
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
		else       //只要有一个不相等，就说明相等的公共字符断了，不连续了
			break;
	}
	printf("最长公共子串为：");
	puts(s);
	return max;

}

 

int main(void)
{
	char str1[1000],str2[1000];
	printf("请输入第一个字符串：");
	gets(str1);
	printf("请输入第二个字符串：");
	gets(str2);
	int len = longest_common_substring(str1, str2);
	printf("最长公共连续子串的长度为：%d\n",len);
	system("pause");
}





































