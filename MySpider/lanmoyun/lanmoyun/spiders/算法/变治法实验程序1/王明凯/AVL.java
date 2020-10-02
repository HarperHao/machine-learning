package �㷨;
import java.util.Stack;

public class AVL {
	Listnode _root;
	private void rotateAt(Listnode v)
	{
		Listnode grand=v.farther.farther.farther;
		Listnode newRoot=null;
		if(v.isLeftChildOf(v.farther) && v.farther.isLeftChildOf(v.farther.farther))
			newRoot = reShape34(v, v.farther, v.farther.farther, v.leftChild, v.rightChild, v.farther.rightChild, v.farther.farther.rightChild);
		else if(v.isRightChildOf(v.farther) && v.farther.isRightChildOf(v.farther.farther))
			newRoot = reShape34(v.farther.farther, v.farther, v, v.farther.farther.leftChild, v.farther.leftChild, v.leftChild, v.rightChild);
		else if(v.isRightChildOf(v.farther) && v.farther.isLeftChildOf(v.farther.farther))
			newRoot = reShape34(v.farther, v, v.farther.farther, v.farther.leftChild, v.leftChild, v.rightChild, v.farther.farther.rightChild);
		else if(v.isLeftChildOf(v.farther) && v.farther.isRightChildOf(v.farther.farther))
			newRoot = reShape34(v.farther.farther, v, v.farther, v.farther.farther.leftChild, v.leftChild, v.rightChild, v.farther.rightChild);
		if(grand.KEY> newRoot.KEY)
			grand.leftChild=newRoot;
		else
			grand.rightChild=newRoot;
		newRoot.farther=grand;
	}
	private Listnode reShape34(Listnode a,Listnode b,Listnode c,Listnode T0,Listnode T1,Listnode T2,Listnode T3)
	{
		b.leftChild=a;
		b.rightChild=c;
		a.farther=b;
		c.farther=b;
		a.leftChild=T0; if(T0!=null) T0.farther=a;
		a.rightChild=T1;if(T1!=null) T1.farther=a;
		c.leftChild=T2; if(T2!=null) T2.farther=c;
		c.rightChild=T3;if(T3!=null) T3.farther=c;
		return b;
	}
	private void updateHight(Listnode v)
	{
		int leftHigh=  v.leftChild==null? -1 :v.leftChild.heigh;
		int rightHight=v.rightChild==null? -1:v.rightChild.heigh;
		v.heigh=leftHigh>rightHight? leftHigh+1 : rightHight+1;
	}
	private Listnode findMax(Listnode v)
	{
		if(null==v)
			return v;//������Ա�����쳣
		while(null != v.rightChild)
			v=v.rightChild;
		return v;
	}
	private Listnode findMin(Listnode v)
	{
		if(null==v)
			return v;//������Ա�����쳣
		while(null != v.leftChild)
			v=v.leftChild;
		return v;
	}
	private void removeTools(Listnode v)//�����ɾ����Ҷ�ӽڵ������������Ķ�����ת��Ϊ�������
	{
		Listnode x=v.farther;
		if(x.KEY>v.KEY)
			x.leftChild=null;//��ָ�����ˣ�jvm������Զ��������,c++��Ҫɾ��������Ͳ�ɾ����
		else
			x.rightChild=null;
		while(null!=x)
		{
			if(x.getBalance()>1||x.getBalance()<-1)
				rotateAt(x);
			updateHight(x);
			x=x.farther;
		}
	}
	public boolean isEmpty()
	{
		return _root==null;
	}
	private void visitLastTools(Listnode v,Stack<Listnode> S)
	{
		while(null!=v)
		{
			S.push(v);
			v=v.leftChild;
		}
	}
	public void visitLast()
	{
		if(this.isEmpty())
			return;
		Stack<Listnode> S=new Stack<Listnode>();
		visitLastTools(_root, S);
		while(!S.isEmpty())
		{
			Listnode v=S.pop();
			if(!v.flag)
			{	
				v.flag=true;
				S.push(v);
				v=v.rightChild;
				visitLastTools(v, S);
			}
			else
				System.out.println(v.KEY);
		}
	}
	private void visitMiddleTools(Listnode v,Stack<Listnode> S)
	{
		while(null!=v)
		{
			S.push(v);
			v=v.leftChild;
		}
	}
	public void visitMiddle()
	{
		Stack<Listnode> S=new Stack<Listnode>();
		visitMiddleTools(_root, S);
		while(!S.isEmpty())
		{
			Listnode v=S.pop();
			System.out.println(v.KEY);
			v=v.rightChild;
			visitMiddleTools(v, S);
		}
	}
	public Listnode search(int Key)
	{
		Listnode target=_root;
		Listnode father=null;
		while(target!=null && target.KEY!=Key)
		{
			father=target;
			target=target.KEY>Key? target.leftChild:target.rightChild;
		}
		return father;
	}
	public void insert(int Key)
	{
		Listnode father = search(Key);
		Listnode node=new Listnode(Key,father);
		if(null == father)
			{
				_root=node;
				return;
			}
		if(father.KEY>Key)
			father.leftChild=node;
		else
			father.rightChild=node;
		while(father!=null)
		{
			if(father.getBalance()>1||father.getBalance()<-1)
			{	
				rotateAt(father);
				break;//ƽ��֮�󣬸߶Ȳ������ֱ���˳�
			}
			updateHight(father);
			father=father.farther;
		}
	}
	public void remove(int Key)
	{
		if(isEmpty())
			return;
		Listnode father=search(Key);
		Listnode node=father.KEY>Key? father.leftChild:father.rightChild;
		if(node==null)//��������Ͳ�������ߣ��ǾͲ��ò�����ֱ���˳��Ϳ���;
			return;
		else//��������������ߣ�������������
		{
			if(null==node.leftChild&&null==node.rightChild)//ɾ��Ҷ�ӽڵ�
				removeTools(node);
			else if(null==node.leftChild && null!=node.rightChild)//ɾ��ֻ���������Ľڵ�
			{
				Listnode targ=findMin(node.rightChild);
				node.KEY=targ.KEY;
				removeTools(targ);
			}
			else if(null!=node.leftChild && null==node.rightChild)//ɾ��ֻ���������Ľڵ�
			{
				Listnode targ=findMax(node.leftChild);
				node.KEY=targ.KEY;
				removeTools(targ);
			}
			else if(null!=node.leftChild && null!=node.rightChild)//ɾ������������Ҳ���������Ľڵ�
			{
				Listnode targ=findMax(node.rightChild);
				node.KEY=targ.KEY;
				removeTools(targ);
			}
		}
	}
}
