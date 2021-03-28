import unittest
from route_finder import build_graph

class TestRouteFinder(unittest.TestCase):


    def test_build_graph(self):
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

        graph = build_graph(test_routes)
        print(graph)



if __name__ == '__main__':
    unittest.main()