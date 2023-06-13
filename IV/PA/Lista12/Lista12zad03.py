from Lista12zad01 import CustomGraph


if __name__ == '__main__':
    graph = CustomGraph()
    graph.load_from_json("weighted_conf.json")
    graph.visual_kruskal_algorithm()
