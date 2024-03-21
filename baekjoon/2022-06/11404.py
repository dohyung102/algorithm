import sys
sys.stdin = open('11404.txt')

city_number = int(input())
bus_number = int(input())
bus_cost = [[0] * (city_number + 1) for _ in range(city_number + 1)]
for bus in range(bus_number):
    start_bus_stop, end_bus_stop, time_cost = map(int, input().split())
    if not bus_cost[start_bus_stop][end_bus_stop]:
        bus_cost[start_bus_stop][end_bus_stop] = time_cost
    else:
        bus_cost[start_bus_stop][end_bus_stop] = min(time_cost, bus_cost[start_bus_stop][end_bus_stop])

for middle_number in range(1, city_number + 1): #경유 도시
    for start_number in range(1, city_number + 1): #출발 도시
        if start_number == middle_number: #출발도시와 경유도시가 같으면 패스
            continue
        for end_number in range(1, city_number + 1): #도착 도시
            if end_number == start_number or end_number == middle_number: #도착도시가 출발도시나 경유도시와 같으면 패스
                continue
            direct_bus_cost, start_to_middle_cost, middle_to_end_cost = bus_cost[start_number][end_number], bus_cost[start_number][middle_number], bus_cost[middle_number][end_number]
            if start_to_middle_cost and middle_to_end_cost: #경유해서 갈수 있는지 확인
                if not direct_bus_cost: #출발도시에서 도착도시로 바로갈 수 없는 경우
                    bus_cost[start_number][end_number] = start_to_middle_cost + middle_to_end_cost
                else: #출발도시에서 도착도시로 바로 갈수 있는 경우
                    bus_cost[start_number][end_number] = min(direct_bus_cost, start_to_middle_cost + middle_to_end_cost)

for city in range(1, city_number + 1):
    print(*bus_cost[city][1:])