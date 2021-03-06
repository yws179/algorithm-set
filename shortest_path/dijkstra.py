# coding=utf-8

INF = float('inf')


def dijkstra(graph, start, end):
    """
    迪杰斯特拉
    :param graph:   权值图
    :param start:   起点
    :param end:     终点
    :return:        起点终点最短距离
    """
    g_len = len(graph)
    # 初始化最短距离列表:用于记录start点到每个点的最短距离
    dist = [graph[start][i] for i in range(g_len)]
    # 记录每个节点是否遍历的状态
    visit = [False for _ in range(g_len)]
    visit[start] = True
    # 记录最短距路线
    path_r = []
    # key:点A val:点B
    # shortest_distance_A = shortest_distance_B + distance_A_B
    path_map = {start: start}
    # 遍历地图数据
    for i in range(g_len):
        if not visit[i]:
            for j in range(g_len):
                if graph[i][j] != INF:
                    new_dist = dist[i] + graph[i][j]
                    # 若新计算出的距离比原有的最短距离短则保存
                    if new_dist < dist[j]:
                        dist[j] = new_dist
                        path_map[j] = i
            visit[i] = True
    step = end
    while True:
        path_r.append(str(step))
        step = path_map.get(step)
        if step == start or step is None:
            path_r.append(str(start))
            break
    return dist[end], path_r[::-1]


if __name__ == '__main__':
    # 地图: 0 汕头 1 深圳 2 珠海 3 茂名 4 湛江 5 佛山 6 广州 7 清远
    graph_m = [
        [0., INF, INF, INF, INF, INF, INF, INF],
        [INF, 0., INF, INF, INF, INF, INF, INF],
        [INF, INF, 0., INF, INF, INF, INF, INF],
        [INF, INF, INF, 0., INF, INF, INF, INF],
        [INF, INF, INF, INF, 0., INF, INF, INF],
        [INF, INF, INF, INF, INF, 0., INF, INF],
        [INF, INF, INF, INF, INF, INF, 0., INF],
        [INF, INF, INF, INF, INF, INF, INF, 0.]]

    # 初始化地图
    graph_m[0][2] = graph_m[2][0] = 485.2
    graph_m[0][6] = graph_m[6][0] = 442.9
    graph_m[0][7] = graph_m[7][0] = 496.5
    graph_m[1][2] = graph_m[2][1] = 167.8
    graph_m[1][6] = graph_m[6][1] = 147.5
    graph_m[2][3] = graph_m[3][2] = 329.2
    graph_m[2][5] = graph_m[5][2] = 126.8
    graph_m[2][6] = graph_m[6][2] = 127.3
    graph_m[3][4] = graph_m[4][3] = 94.9
    graph_m[3][5] = graph_m[5][3] = 314.
    graph_m[5][6] = graph_m[6][5] = 23.2
    graph_m[6][7] = graph_m[7][6] = 82.9

    s = input("请输入起点序号：（0 汕头 1 深圳 2 珠海 3 茂名 4 湛江 5 佛山 6 广州 7 清远）")
    e = input("请输入终点序号：（0 汕头 1 深圳 2 珠海 3 茂名 4 湛江 5 佛山 6 广州 7 清远）")
    (shortest_dist, path) = dijkstra(graph_m, int(s), int(e))
    print("%s到%s最短路程为%.2f公里, 路径为%s" % (s, e, shortest_dist, '->'.join(path)))
