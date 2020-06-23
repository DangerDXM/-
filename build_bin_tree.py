# 剑指offer面试题7 p62 补充后续和中序重建二叉树。
# 从前序或者后续确定根节点，从中序确定左右子树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(in_order, rear_order):
    root = TreeNode(rear_order[-1])
    len_in = len(in_order)
    len_rear = len(rear_order)
    if len_in == 1:
        if len_rear == 1 and in_order == rear_order:
            return root

    count = 0
    while count < len_in:
        if in_order[count] == rear_order[-1]:
            break
        count += 1
    if count == len_in:
        print('Invalid input...')

    root.left = buildTree(in_order[0:count], rear_order[0:count])
    root.right = buildTree(in_order[count+1:], rear_order[count:-1])
    return root


def printTree(root):
    result = []
    treeList = []
    treeList.append(root)
    while treeList:
        if treeList[0]:
            result.append(treeList[0].val)
        else:
            result.append(None)
        if treeList[0]:
            treeList.append(treeList[0].left)
            treeList.append(treeList[0].right)
        del treeList[0]
    return result


def main():
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]
    rear_order = [9, 15, 7, 20, 3]
    root = buildTree(in_order, rear_order)
    result = printTree(root)

    while not result[-1]:
        del result[-1]
    print(result)


if __name__ == '__main__':
    # 中后序重建二叉树
    main()
