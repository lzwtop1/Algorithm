# 链表节点的定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 计算链表 A 和链表 B 的长度
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)

        # 让较长的链表先走多出来的步数
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                headA = headA.next
        else:
            for i in range(lengthB - lengthA):
                headB = headB.next

        # 遍历链表 A 和链表 B，找到它们的相交点
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        # 如果链表 A 和链表 B 没有相交点，则返回 None
        return None

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

# 创建两个链表
headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
headB = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))

# 创建解决方案实例并查找相交点
s = Solution()
result = s.getIntersectionNode(headA, headB)

# 输出结果
if result:
    print(result.val)
else:
    print("null")
