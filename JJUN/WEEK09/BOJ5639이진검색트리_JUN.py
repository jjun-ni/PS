import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

binary_search_tree = []

def post_order_print(left, right):
    if left > right:
        return
    else:
        middle = right + 1
        # 현재 구간에서 루트노드보다 큰 노드가 나오는 포인트 찾기
        for i in range(left + 1, right + 1):
            if binary_search_tree[i] > binary_search_tree[left]:
                middle = i
                break

        post_order_print(left + 1, middle - 1)
        post_order_print(middle, right)
        print(binary_search_tree[left])


while True:
    try:
        new_node = int(input())
        binary_search_tree.append(new_node)
    except:
        break

post_order_print(0, len(binary_search_tree) - 1)
