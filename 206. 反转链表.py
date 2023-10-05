# Definition for singly-linked list.
'''
具体实现过程如下：

初始化指针 prev 为 None，指针 cur 为链表头节点 head。

在循环中，对于每个节点，先将指针 next 指向它的后继节点，然后将它的后继节点指向 prev，最后将指针 prev 和 cur 向后移动一位，分别指向原来的 cur 和 next 节点。

当 cur 为 None 时，循环结束，链表反转完成。返回指针 prev，即为反转后的链表头节点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev


s = Solution()

# 创建链表
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 反转链表
result = s.reverseList(head)

# 遍历链表并输出
while result:
    print(result.val, end=' ')
    result = result.next
