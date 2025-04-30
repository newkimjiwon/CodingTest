def preorder_traversal(graph, node, result):
    if node == '.':
        return
    result.append(node)
    preorder_traversal(graph, graph[node][0], result)
    preorder_traversal(graph, graph[node][1], result)


def inorder_traversal(graph, node, result):
    if node == '.':
        return
    inorder_traversal(graph, graph[node][0], result)
    result.append(node)
    inorder_traversal(graph, graph[node][1], result)


def postorder_traversal(graph, node, result):
    if node == '.':
        return
    postorder_traversal(graph, graph[node][0], result)
    postorder_traversal(graph, graph[node][1], result)
    result.append(node)


def main():
    n = int(input())
    graph = {}

    for _ in range(n):
        node, left, right = input().split()
        graph[node] = (left, right)

    preorder = []
    inorder = []
    postorder = []

    preorder_traversal(graph, 'A', preorder)
    inorder_traversal(graph, 'A', inorder)
    postorder_traversal(graph, 'A', postorder)

    print(''.join(preorder))
    print(''.join(inorder))
    print(''.join(postorder))


if __name__ == "__main__":
    main()