//#include <stdio.h>
//#include<stdlib.h>
//#define MAX 100
//int main()
//{
//    //进制转换函数的声明
//    int transfer(int x);
//    int x,a[MAX];
//    printf("请输入一个十进制数:");
//    scanf("%d",&x);
//    printf("转换成二进制数是:%d\n",transfer(x));
//	system("pause");
//}
//long int transfer(int x)
//{
//    int remainder,a[MAX];
//	long int y,p=1;
//    while(1)
//    {
//        remainder=x%2;
//        x/=2;
//        y+=remainder*p;
//        p*=10;
//        if(x<2)
//        {
//            y+=x*p;
//            break;
//        }
//    }
//    return y;
//}


#include<stdio.h>
#include<stdlib.h>

long int binary_exponentiation(int a,int s[],int num)
{
	int i;
	long int p;
	p=a;
	for(i=num-1;i>=0;i--)
	{
		p=p*p;
		if(s[i]==1)
		{
			p=p*a;
		}
	}
	return p;
}

int main()
{
 int a,n;
 int s[20];
 int i = 0, rem;
 long int result;
 printf("Input number(a,n):");
 scanf("%d%d", &a,&n);
 do
 {
  rem = n % 2;

  n = n / 2;
  s[i] = rem;
  i++;
 } while (n != 0);
 result=binary_exponentiation(a,s,i-1);
 printf("result:%ld",result);
 system("pause");
}