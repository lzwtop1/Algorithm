# 链表节点的定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建虚拟头结点
        dummy = ListNode(0)
        dummy.next = head

        # 计算链表的长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 计算要删除节点的位置
        pos = length - n  # 3

        # 找到要删除节点的前一个节点
        cur = dummy
        for i in range(pos):
            cur = cur.next

        # 删除要删除的节点
        cur.next = cur.next.next

        # 返回新的链表头
        return dummy.next


# 创建链表
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# 创建解决方案实例并删除倒数第二个节点
s = Solution()
result = s.removeNthFromEnd(head, 2)

# 遍历链表并输出
while result:
    print(result.val, end=' ')
    result = result.next
