import csv
import click


def build_graph(connexion_times):
    graph = {}
    airports_list = [[airport[0],airport[1]] for airport in connexion_times]
    airports_keys = list(set([item for sublist in airports_list for item in sublist]))

    for airport_key in airports_keys:
        airport_links = [
            tuple(connexion_time[1:]) 
            for connexion_time in connexion_times if airport_key == connexion_time[0]
        ]
        graph[airport_key] = airport_links
    
    return graph


def find_all_paths(graph, start, end, hours, path=[]):
    path = path + [(start, hours)]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node[0], end, hours + int(node[1]), path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def sort_by_shortest_route(routes):
    return sorted(routes , key=lambda tup: tup[-1][1])[0]


def get_routes(file_name):
    connexion_times = []

    with open(file_name) as csvfile:
        connexion_times_read = csv.reader(csvfile)
        connexion_times = list(connexion_times_read)

    return connexion_times


def get_route_description(result, source, destination):
    names = [res[0] for res in result]
    time = result[-1][1]
    prefix = '{} -- {}'.format(source, destination)
    return prefix + ' ( ' + str(time) + ' )'


@click.command()
@click.option('--source')
@click.option('--destination')
@click.option('--routes')
def get_shortest_route(source, destination, routes):
    routes_list = get_routes(routes)
    graph = build_graph(routes_list)
    all_paths = find_all_paths(graph, source, destination, 0)
    shortest = sort_by_shortest_route(all_paths)
    click.echo(get_route_description(shortest, source, destination))


if __name__ == '__main__':
    get_shortest_route()