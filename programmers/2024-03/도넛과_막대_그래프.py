def solution(edges):
    answer = [0, 0, 0, 0]
    max_node_number = max(map(max, edges))
    in_node_count_list = [[] for _ in range(max_node_number + 1)]
    out_node_count_list = [[] for _ in range(max_node_number + 1)]

    for edge in edges:
        in_node_count_list[edge[1]].append(edge[0])
        out_node_count_list[edge[0]].append(edge[1])

    for node in range(1, max_node_number + 1):
        out_line_count = len(out_node_count_list[node])
        if out_line_count >= 2 and not in_node_count_list[node]:
            answer[0] = node
            answer[1] += out_line_count
        elif out_line_count == 2:
            answer[1] -= 1
            answer[3] += 1
        elif out_line_count == 0 and in_node_count_list[node]:
            answer[1] -= 1
            answer[2] += 1
    return answer