import unittest

from route_finder import (
    build_graph,
    find_all_paths
)

class TestRouteFinder(unittest.TestCase):

    test_graph = {
        'TEST': [('TEST1', 4)],
        'OTH': [('OTH1', 6)], 'BOS': [], 'OTH1': [('BOS', 7)], 
        'TEST2': [('BOS', 6)], 
        'TEST1': [('TEST2', 5)], 
        'DUB': [('TEST', 3), ('OTH', 5), ('BOS', 1)]
    }


    test_routes = [
        ['DUB','TEST',3],
        ['TEST','TEST1',4],
        ['TEST1','TEST2',5],
        ['TEST2','BOS',6],
        ['DUB','OTH',5],
        ['OTH','OTH1',6],
        ['OTH1','BOS',7],
        ['DUB','BOS',1]
    ]


    test_paths = [
        [('DUB', 0), ('TEST', 3), ('TEST1', 7), ('TEST2', 12), ('BOS', 18)],
        [('DUB', 0), ('OTH', 5), ('OTH1', 11), ('BOS', 18)], 
        [('DUB', 0), ('BOS', 1)]
    ]


    def test_build_graph(self):
        graph = build_graph(self.test_routes)
        assert(graph == self.test_graph)


    def test_find_all_paths(self):
        graph = build_graph(self.test_routes)
        all_found_paths = find_all_paths(graph, 'DUB', 'BOS', 0)
        assert(all_found_paths == self.test_paths)


if __name__ == '__main__':
    unittest.main()