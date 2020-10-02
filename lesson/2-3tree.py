# class Node:
#     def __init__(self, key):  # 定义节点的数据结构
#         self.key1 = key
#         self.key2 = None
#         self.left = None
#         self.right = None
#         self.middle = None
#
#     def isFull(self):  # 判断是二节点还是三节点
#         if self.key2 is not None:
#             return True
#         else:
#             return False
#
#     def isLeaf(self):  # 判断是否是叶子节点
#         return self.left is None and self.middle is None and self.right is None
#
#     def getChild(self,key):
#         if key<self.key1:
#             return self.left
#         elif self.key2 is None:#如果是二节点
#             return self.middle #return self.right
#         elif key<self.key2:
#
#
#
# class two_three_Tree:
#     def __init__(self):
#         self.root = None
