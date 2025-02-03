import copy
import sys
from typing import List
'''
    사내 네트워크는 N개의 노드를 가지는 트리 형태의 네트워크
    간선은 N-1개 있어서 모든 노드간의 통신이 가능

    x->y번 노드는 양방향으로 연결되며, 통신에 걸리는 시간은 ti이다.
    Dij는 i와 j노드 사이의 거리를 나타나ㅐ는데, i번에서 j번 노드를 도달하기 위해 걸리는 최소 시간
    (여러 연결을 거침)

    현호는 네트워크 분석을 위해 어떤 노드 i를 기준으로 다른 노드 사이와의 거리 합을 알고 싶다.

    # 첫 시도
        55문제 중에 5개 정답, 50개 시간초과
'''


class TreeNode:
    def __init__(
        self,
        id,
        parent,
        parent_edge,
        sub_nodes,
        sub_node_sum,
        connect_vals
    ):
        self.id: int = id
        self.parent = parent
        self.parent_edge = parent_edge
        self.sub_nodes: List[int] = sub_nodes
        self.sub_node_sum: int = sub_node_sum
        self.connect_vals: List[int] = connect_vals


# 입력
N = int(input()) # 노드의 개수

edge_infos = []
for _ in range(N-1):
    edge = list(map(int, sys.stdin.readline().split()))
    edge_infos.append(edge)
edge_infos.sort(key=lambda x: x[0])

# 트리 만들기
tree_infos = [ 
        TreeNode(id=i, parent=-1, sub_nodes=[], parent_edge=0, sub_node_sum=0, connect_vals=[]) 
        for i in range(N + 1) 
    ]
for edge in edge_infos:
    tree_infos[edge[0]].sub_nodes.append(edge[1])
    tree_infos[edge[0]].connect_vals.append(edge[-1])    
    
    tree_infos[edge[1]].parent = edge[0]
    
# 출력
for item in tree_infos:
    print(item.id, item.parent, item.sub_node_sum, item.sub_nodes, item.connect_vals)

# Top-down
root_dist_infos = [ 0 for _ in range(N + 1) ]
def top_down(
    root_node: int,
    node_id: int,
    dist_sum: int,
):
    tree_node: TreeNode = tree_infos[node_id]
    if tree_node.id != -1:
        root_dist_infos[node_id] = dist_sum

    for sdx, sub_node_id in enumerate(tree_node.sub_nodes):
        tree_infos[sub_node_id].parent_edge = tree_node.connect_vals[tree_node.sub_nodes.index(sub_node_id)]
        top_down(
            root_node=root_node,
            node_id=sub_node_id,
            dist_sum=dist_sum + tree_node.connect_vals[sdx]
        )

top_down(root_node=1, node_id=1, dist_sum=0) # Start from root.
print(f"root_dist_infos: {root_dist_infos}, sum: {sum(root_dist_infos)}")

# child 노드 거리 합 = 
#   root_node 거리합 - (child 서브 노드 개수 * root와 child의 거리) 
#   + (child 서브 노드아닌 개수 + root 와 child의 거리)
all_dist_info = [ [0 for _ in range(N + 1)] for _ in range(N + 1) ]
all_dist_info[1] = sum(root_dist_infos)

visited = [ False for _ in range(N + 1)]
def get_child_node_dist(
    child_node_id: int,
    cur_node_id: int,
    cur_dist_sum: int,
):
    cur_node = tree_infos[cur_node_id]

    if 0 < cur_dist_sum and (child_node_id == cur_node_id):
        return

    if child_node_id != cur_node_id:
        all_dist_info[child_node_id][cur_node.id] = cur_dist_sum
        print(child_node_id, cur_node.id, cur_dist_sum)
    
    new_sub_nodes = copy.deepcopy(cur_node.sub_nodes)
    new_sub_nodes.append(cur_node.parent)
    
    new_sub_edges = copy.deepcopy(cur_node.connect_vals)
    new_sub_edges.append(cur_node.parent_edge)

    for nidx, next_id in enumerate(new_sub_nodes):
        if visited[next_id]:
            continue

        visited[next_id] = True
        get_child_node_dist(
            child_node_id=child_node_id,
            cur_node_id=next_id,
            cur_dist_sum=cur_dist_sum + new_sub_edges[nidx]
        )
        visited[next_id] = False
    

for node_id in range(2, N+1):
    visited = [ False for _ in range(N + 1)]
    get_child_node_dist(
        child_node_id=node_id,
        cur_node_id=node_id,
        cur_dist_sum=0,
    )
    print(f"{node_id}: {all_dist_info[node_id]}, sum: {sum(all_dist_info[node_id])}")
    

# 출력
print('\n------------\n')
for item in tree_infos:
    print(f"""
        id: {item.id}\n
        parent:{item.parent}\n
        parent_edge:{item.parent_edge}\n
        sub_node_sum:{item.sub_node_sum}\n
        sub_nodes:{item.sub_nodes}\n
        connect_vals:{item.connect_vals}\n
    """)
# 

'''
4
1 2 1
2 3 2
3 4 4

7
1 2 5
1 3 2
1 4 8
3 5 4
3 6 1
4 7 6

[5, 3, 6]
[6, 3, 5]

[2, 1, 3, 6]
[6, 3, 1, 2]
-> 경로의 값은 같다. 어떻게 처리할 것인가?

6
1 2 1
1 3 2
1 4 3
1 5 4
1 6 5
'''