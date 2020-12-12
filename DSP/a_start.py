# Time Complexity는 H에 따라 다르다.
# O(b^d), where d = depth, b = 각 노드의 하위 요소 수
# heapque를 이용하면 길을 출력할 때 reverse를 안해도 됨
class Node:
    def __init__(self, parent=None, position=None): # 초기 생성자
        self.parent = parent
        self.position = position # (i,j)

        self.g = 0    # 현재 노드에서 출발 지점까지의 총 cost, 지나온 길의 거리
        self.h = 0    # 현재 노드에서 목적지까지의 추정 거리
        self.f = 0    # 출발 지점에서 목적지까지 총 cost의 합

    def __eq__(self, other):   # 현재 위치와 같은 곳인지 True or False 반환
        return self.position == other.position


def heuristic(node, goal, D=0.00000000001):  # 이동 방향이 상하좌우(4가지)라서 맨해튼 거리 사용
    dx = abs(node.position[0] - goal.position[0])   # 맨해튼 거리 구하는 법 
    dy = abs(node.position[1] - goal.position[1])   # x = (i1,j1), y = (i2, j2)
    return D * (dx + dy)                            # L1 = |i1 - i2| + |j1 - j2|


def aStar(maze, start, end):
    # startNode와 endNode 초기화
    startNode = Node(None, start)
    endNode = Node(None, end)

    # openList, closedList 초기화
    openList = []         # 현재 위치에서 이동 가능한 노드의 리스트, 매번 F,G,H를 계산한다.
    closedList = []       # F값이 가장 작은 노드

    # openList에 시작 노드 추가
    openList.append(startNode)

    # endNode를 찾을 때까지 실행
    while openList:

        # 현재 노드 지정
        currentNode = openList[0]
        currentIdx = 0

        # currentNode와 같은 노드가 이미 openList에 있고, f 값이 더 크면 (우리의 목표와 멀어지면)
        # currentNode를 openList안에 있는 값으로 교체( 이전 위치로 다시 돌아간다.)
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIdx = index

        # openList에서 제거하고 closedList에 추가
        openList.pop(currentIdx)
        closedList.append(currentNode)

        # 현재 노드가 목적지면 current.position 추가하고
        # current의 부모로 이동
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                # maze 길을 표시하려면 주석 해제
                # x, y = current.position
                # maze[x][y] = 7 
                path.append(current.position)
                current = current.parent
            return path[::-1]  # reverse

        children = []
        # 인접한 xy좌표 중 상하좌우만 탐색
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            # 노드 위치 업데이트
            nodePosition = (
                currentNode.position[0] + newPosition[0],  # X
                currentNode.position[1] + newPosition[1])  # Y
                
            # 미로 maze index 범위 안에 있어야함
            within_range_criteria = [
                nodePosition[0] > (len(maze) - 1),
                nodePosition[0] < 0,
                nodePosition[1] > (len(maze[len(maze) - 1]) - 1),
                nodePosition[1] < 0,
            ]

            if any(within_range_criteria):  # 하나라도 true면 범위 밖임
                continue

            # 장애물이 있으면 다른 위치 불러오기
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            new_node = Node(currentNode, nodePosition)
            children.append(new_node)

        # 자식들 모두 loop
        for child in children:

            # 자식이 closedList에 있으면 continue
            if child in closedList:
                continue

            # f, g, h값 업데이트
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) **
                       2) + ((child.position[1] - endNode.position[1]) ** 2)
            # child.h = heuristic(child, endNode) 다른 휴리스틱
            # print("position:", child.position) 거리 추정 값 보기
            # print("from child to goal:", child.h)
            
            child.f = child.g + child.h

            # 자식이 openList에 있으고, g값이 더 크면 continue
            if len([openNode for openNode in openList
                    if child == openNode and child.g > openNode.g]) > 0:
                continue
                    
            openList.append(child)

import timeit
start = timeit.default_timer()
def main():
    
    
    # 0은 통로, 1은 장애물, 2는 시작점, 3은 도착점
    maze = [[1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [2, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 1, 1, 0, 1, 1]]

    # 기존 코드가 0 -> 0 이라 어쩔 수 없이 2와 3을 0으로 바꿔주고, start와 end로 지정해줌
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                maze[i][j] = 0
                start = (i,j)
            elif maze[i][j] == 3:
                maze[i][j] = 0
                end = (i,j)

    path = aStar(maze, start, end)
    print(path)




if __name__ == '__main__':
    main()
    # D값이 1일 때
    # [(2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), 
    # (7, 3), (7, 4), (7, 5), (7, 6), (8, 6), (8, 7), (8, 8), (8, 9)]
stop = timeit.default_timer()
print(stop - start)

# D값을 바꿔보았지만 큰 차이는 없었다.

# D가 1일 때
# 0.000627599999999999
# 0.0005628999999999981
# 0.0005990000000000023

# D가 0.001일 때
# 0.0006632000000000027
# 0.0005119000000000026
# 0.0005790999999999991

# D가 0.00000000001일 때
# 0.0005845000000000017
# 0.0006492999999999985
# 0.0005287