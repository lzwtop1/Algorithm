# 链表节点的定义
class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # 创建虚拟头结点
        cur = dummy  # 创建指针 cur，初始指向虚拟头结点

        carry = 0  # 初始化进位为 0
        while l1 or l2 or carry:  # 当 l1、l2 或进位 carry 不为空时继续循环
            val1 = l1.val if l1 else 0  # 如果 l1 不为空，则取 l1 的值，否则为 0
            val2 = l2.val if l2 else 0  # 如果 l2 不为空，则取 l2 的值，否则为 0

            # 计算当前位的和及进位
            total = val1 + val2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)

            # 更新指针和 l1、l2 的值
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next  # 返回虚拟头结点的下一个节点，即为新的链表头


s = Solution()

# 创建两个链表
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# 计算它们的和
result = s.addTwoNumbers(l1, l2)

# 遍历链表并输出
while result:
    print(result.val, end=' ')
    result = result.next
