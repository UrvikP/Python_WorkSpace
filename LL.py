class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convert_arr_to_ll(arr):
    if not arr: return None
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head

def convert_ll_to_arr(lst):
    if not lst: return []
    arr = []
    curr = lst
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    return arr

def solution(list):
    head = convert_arr_to_ll(list)
    #TODO: use head to solve the problem provided.
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
            continue  
        curr = curr.next
    
    headToArr = convert_ll_to_arr(head)
    return headToArr

list1 = [1, 2, 4]
list2 = [1, 1, 2, 2, 2]
list3 = [1, 2, 2, 2, 3, 3, 4]
print(solution(list1))
print(solution(list2))
print(solution(list3))