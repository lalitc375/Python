#include "stdio.h"
#include "stdlib.h"
struct node
{
	int data;
	struct node * right,*left;
	
};
struct node * newnode(int data)
{
	struct node * _node =(struct node *)malloc(sizeof(node));
	_node->data=data;
	_node->right=_node->left=NULL;
	return _node;
}
int numberofleafnode(struct node *root)
{
	if(root->left==NULL&&root->right==NULL)
		return 1;
	if (root->left==NULL)
		return (numberofleafnode(root->right));
	else if(root->right==NULL)
		return (numberofleafnode(root->left));
	else
		return numberofleafnode(root->right)+numberofleafnode(root->left);

}
int main()
{
	struct node * root =(struct node *)malloc(sizeof(node));
	root->data=10;
	root->right=newnode(9);
	root->left=newnode(8);
	root->right->right=newnode(7);
	root->right->left=newnode(6);
	root->left->right=newnode(5);
	root->left->left=newnode(4);
	//printf("Lalit Chauhan\n");
	printf("%d\n",numberofleafnode(root));
	return 0;
}