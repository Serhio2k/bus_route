from buses.models import Bus


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_town_id, set())
        graph[q.from_town_id].add(q.to_town_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Bus.objects.all().select_related('from_town', 'to_town')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_town = data['from_town']
    to_town = data['to_town']
    towns = data['towns']
    travelling_time = data['travelling_time']
    all_ways = list(dfs_path(graph, from_town.id, to_town.id))
    if not len(all_ways):
        #  Немає жодного маршруту для даного пошуку
        raise ValueError('Відсутній маршрут за даними критеріями пошуку')
    if towns:
        # Якщо є міста через які потрібно проїхати
        _towns = [town.id for town in towns]
        right_ways = []
        for route in all_ways:
            if all(town in route for town in _towns):
                right_ways.append(route)
        if not right_ways:
            # Якщо список маршрутів пустий
            raise ValueError('Маршрут через ці міста - неможливий')
    else:
        right_ways = all_ways
    routes = []
    all_buses = {}
    for q in qs:
        all_buses.setdefault((q.from_town_id, q.to_town_id), [])
        all_buses[(q.from_town_id, q.to_town_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['buses'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_buses[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['buses'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            routes.append(tmp)
    if not routes:
        raise ValueError('Час в дорозі більший за заданий')
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['towns'] = {'from_town': from_town, 'to_town': to_town}
    return context
