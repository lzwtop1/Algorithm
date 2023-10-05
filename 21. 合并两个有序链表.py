# 链表节点的定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建虚拟头结点
        dummy = ListNode(0)
        cur = dummy  # 创建指针 cur，初始指向虚拟头结点

        # 遍历 l1 和 l2，将较小的节点添加到新链表中
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # 将剩余的节点添加到新链表的末尾
        cur.next = l1 if l1 else l2

        # 返回新的链表头
        return dummy.next


# 创建两个链表
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# 创建解决方案实例并合并两个链表
s = Solution()
result = s.mergeTwoLists(l1, l2)

# 遍历链表并输出
while result:
    print(result.val, end=' ')
    result = result.next
