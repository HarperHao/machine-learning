#include<stdio.h>
#include<stdlib.h>
#define MAX(a,b) (a>b ? a : b)
#define HEIGHT(p) ((p==NULL) ? 0: (((Node *)(p))->height))
#define LEN(a) ((sizeof(a))/(sizeof(a[0])))

typedef struct AVL
{
	int key;
	int height;
	AVL *left;
	AVL *right;
}Node;

Node * create_node(int key,Node *left,Node *right)
{
	Node *p;
	if((p=(Node*)malloc(sizeof(Node)))==NULL)
	{
		return NULL;
	}
	p->key=key;
	p->height=0;
	p->left=left;
	p->right=right;

	return p;
}

int height(Node * tree)
{
	return HEIGHT(tree);
}

Node * left_left_rotation(Node * k2)
{
	Node * k1;
	k1=k2->left;
	k2->left=k1->right;
	k1->right=k2;
	k2->height=MAX(HEIGHT(k2->left),HEIGHT(k2->right))+1;
	k1->height=MAX(HEIGHT(k1->left),HEIGHT(k2->right))+1;
	return k1;
}

Node * right_right_rotation(Node * k1)
{
	Node * k2;
	k2=k1->right;
	k1->right=k2->left;
	k2->left=k1;
	k1->height=MAX(HEIGHT(k1->left),HEIGHT(k1->right))+1;
	k2->height=MAX(HEIGHT(k2->right),HEIGHT(k1->right))+1;
	return k2;
}

Node * left_right_rotation(Node * k3)
{
	k3->left=right_right_rotation(k3->left);
	return left_left_rotation(k3);
}

Node * right_left_rotation(Node * k1)
{
	k1->right=left_left_rotation(k1->right);
	return right_right_rotation(k1);
}

Node * node_insert(Node * tree,int key)
{
	if(tree==NULL)
	{
		tree=create_node(key,NULL,NULL);
		if(tree==NULL)
		{
			printf("ERROR: create node failed\n");
			return NULL;
		}
	}
	else if(key<tree->key)
	{
		tree->left=node_insert(tree->left,key);
		if((HEIGHT(tree->left)-HEIGHT(tree->right))==2)
		{
			if(key<tree->left->key)
			{
				tree=left_left_rotation(tree);
			}
			else
				tree=left_right_rotation(tree);
		}
	}
	else if(key>tree->key)
	{
		tree->right=node_insert(tree->right,key);
		if((HEIGHT(tree->right)-HEIGHT(tree->left))==2)
		{
			if(key>tree->right->key)
				tree=right_right_rotation(tree);
			else
				tree=right_left_rotation(tree);
		}
	}
	else
	{
		printf("添加失败：不允许添加相同值的结点\n");
	}
	tree->height=MAX(HEIGHT(tree->left),HEIGHT(tree->right))+1;
	return tree;
}

Node * node_min(Node * tree)
{
	if(tree==NULL)
		tree=NULL;
	while(tree->left!=NULL)
		tree=tree->left;
	return tree;
}

Node * node_max(Node * tree)
{
	if(tree==NULL)
		tree=NULL;
	while(tree->right!=NULL)
		tree=tree->right;
	return tree;
}

Node * node_search(Node* x,int key)
{
	if(x==NULL || x->key==key)
		return x;
	if(key<x->key)
		return node_search(x->left,key);
	else
		return node_search(x->right,key);
}

Node *del_node(Node* tree,Node *k)
{
	if(tree==NULL || k==NULL)
	{
		return NULL;
	}

	if(k->key<tree->key)
	{
		tree->left=del_node(tree->left,k);
		if((HEIGHT(tree->right)-HEIGHT(tree->left))==2)
		{
			Node *r=tree->right;
			if(HEIGHT(r->left)>HEIGHT(r->right))
			{
				tree=right_left_rotation(tree);
			}
			else
				tree=right_right_rotation(tree);
		}
	}
	else if(k->key>tree->key)
	{
		tree->right=del_node(tree->right,k);
		if(HEIGHT(tree->left)-HEIGHT(tree->right)==2)
		{
			Node *l=tree->left;
			if(HEIGHT(l->right)>HEIGHT(l->left))
				tree=left_right_rotation(tree);
			else
				tree=left_left_rotation(tree);
		}
	}
	else
	{
		if((tree->left)&&(tree->right))
		{
			if(HEIGHT(tree->left)>HEIGHT(tree->right))
			{
				Node *max=node_max(tree->left);
				tree->key=max->key;
				tree->left=del_node(tree->left,max);
			}
			else
			{
				Node *min=node_min(tree->right);
				tree->key=min->key;
				del_node(tree->right,min);
			}
		}
		else
		{
			Node *tmp=tree;
			tree=tree->left ? tree->left:tree->right;
			free(tmp);
		}
	}
	return tree;
}

Node * del(Node *tree,int key)
{
	Node *k;
	if((k=node_search(tree,key))!=NULL)
	{
		tree=del_node(tree,k);
		return tree;
	}
	else
		return NULL;
}

void print_value(Node * tree,int key,int kind)
{
	if(tree!=NULL)
	{
		if(kind==0)
			printf("%2d is root \n",tree->key);
		else
			printf("%2d is %2d's %6s child\n",tree->key,key,kind==1?"right":"left");
		print_value(tree->left,tree->key,-1);
		print_value(tree->right,tree->key,1);
	}
}

int a[]={3,2,1,4,5,6,7,16,15,14,13,12,11,10,8,9};

int main()
{

	int i,len;
	Node * root=NULL;
	len=LEN(a);
	printf("依次添加：");
	for(i=0;i<len;i++)
	{
			printf("%d  ",a[i]);
			root=node_insert(root,a[i]);
	}
	printf("输出树的信息：\n");
	print_value(root,root->key,0);
	int number;
	printf("输入要删除的元素：");
	scanf("%d",&number);
	root=del(root,number);
	if(root==NULL)
		printf("树中不存在此节点");
	else
		print_value(root,root->key,0);
	system("pause");
}