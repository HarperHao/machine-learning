package 算法;

public class Listnode {
	Listnode farther;//父节点
	Listnode rightChild;//右孩子
	Listnode leftChild;//左孩子
	int KEY;
	int heigh;
	boolean flag;//这个变量时中序遍历的时候用的
	public Listnode()
	{
		this.KEY=0;
		this.heigh=0;
		this.flag=false;
		this.farther=null;
		this.leftChild=null;
		this.rightChild=null;
	}
	public Listnode(int key)
	{
		this.KEY=key;
		this.heigh=0;
		this.flag=false;
		this.farther=null;
		this.leftChild=null;
		this.rightChild=null;
	}
	public Listnode(int key,Listnode father)
	{
		this.KEY=key;
		this.heigh=0;
		this.flag=false;
		this.farther=father;
		this.leftChild=null;
		this.rightChild=null;
	}
	public Listnode(int key,Listnode father,Listnode LC,Listnode RC)
	{
		this.KEY=key;
		this.heigh=0;
		this.flag=false;
		this.farther=father;
		this.leftChild=LC;
		this.rightChild=RC;
	}
	int getBalance()
	{
		int leftHigh=this.leftChild==null? -1:this.leftChild.heigh;
		int rightHight=this.rightChild==null? -1:this.rightChild.heigh;
		return leftHigh-rightHight;
	}
	boolean isLeftChildOf(Listnode par)
	{
		return this==par.leftChild;
	}
	boolean isRightChildOf(Listnode par)
	{
		return this==par.rightChild;
	}
	boolean isFatherOf(Listnode son)
	{
		return this==son.farther;
	}
}
