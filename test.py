import unittest

from dijkstra import Dijkstra

class TestDijkstraAlgorithm(unittest.TestCase):

    def setUp(self):

        self.dijkstra = Dijkstra("vertices.dat", "edges.dat", "S")

    def test_correct_shortest_path(self):

        dist, path = self.dijkstra.shortest_path("E")
        expected_dist, expected_path = 8, ["S", "A", "D", "E"]
        
        self.assertEqual(dist, expected_dist)
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()

