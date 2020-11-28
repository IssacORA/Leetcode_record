# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  示例: 
# 
#  你可以将以下二叉树：
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]" 
# 
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。 
# 
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。 
#  Related Topics 树 设计 

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return
        output = []
        stack = [root]
        def remove_null(output):
            topop = 'null'
            while topop is 'null':
                topop = output.pop()
            output.append(topop)

        # 原理：用stack和temp_stack两个栈层序遍历root
        #不仅仅是要按顺序返回节点的值，还要表示节点的相对位置
        #把stack中的元素倒序插入temp_stack，temp_stack依次出栈然后其右节点左节点依次入stack，出栈元素弃用
        #stack中的元素是反序的
        while stack:  # stack目前有若干节点和若干''

            def judge(root):
                if isinstance(root,str):
                    return root
                else:
                    return root.val

            temp_stack = stack[::-1]
            stack = []
            count=0
            for elem in temp_stack:
                if isinstance(elem, str):
                    output.append('null')
                else:
                    output.append('{}'.format(elem.val))

#temp_stack中有节点也有''，如果节点有右节点，那么右节点入stack，没有则''入stack
#如果是''那么什么都不用做，空值是没有左右节点的也不必将其左右节点记为空值，或者说所有被记录的null一定是某个有效节点的左右节点
            while temp_stack:
                topop = temp_stack.pop()
                if isinstance(topop, str):
                    pass
                else:
                    if topop.right:
                        stack.append(topop.right)
                        count+=1
                    else:
                        stack.append('')

                    if topop.left:
                        stack.append(topop.left)
                        count+=1
                    else:
                        stack.append('')
            if count==0:
                break
        remove_null(output) #只有整个二叉树的最后若干个null是不必要的所以只在最后除一次null
        output_str = ','.join(output)
        res='[' + output_str + ']'
        return res

    def deserialize(self, data):

        if not data:
            return None
        a = data.strip('[')
        data0 = a.strip(']')
        data_list = data0.split(',')[::-1]
        #数据处理部分，至此将字符串转换成list
       
        val_pop=data_list.pop()
        root = TreeNode(val_pop)
        result=root
        stack = []
        temp_stack = [root]
        count=1
        
        #初始化部分
        while data_list:
#假设当前的temp_stack中为顺序排列的二叉树的某一行节点，现在(1)要为这些节点依次找到左右节点，(2)并使下一个循环的temp_stack中为顺序排列的二叉树的下一行节点
#对于一个temp_stack，应该依次处理每个元素，从中弹出一个元素temp_stack_pop后：
#(1)从data_list中弹出两个元素，这两个元素应该就是temp_stack_pop

            while temp_stack:

                temp_stack_pop=temp_stack.pop()
 
                if data_list:

                    data_list_pop_1=data_list.pop()
                    if data_list_pop_1=='null':

                        temp_stack_pop.left=None
                    else:

                        temp_stack_pop.left=TreeNode(data_list_pop_1)
                        stack.append(temp_stack_pop.left)
                if data_list:
                    data_list_pop_2=data_list.pop()
                    if data_list_pop_2=='null':

                        temp_stack_pop.right=None
                    else:

                        temp_stack_pop.right=TreeNode(data_list_pop_2)
                        stack.append(temp_stack_pop.right)
            #现在temp_stack空了，stack里是temp_stack的下一层元素，不包括None
            temp_stack=stack[::-1]
            stack=[]
        return result










# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
