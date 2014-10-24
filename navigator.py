import networkx as nx
from enum import Enum

class Navigator:
    def __init__(self, current_scene = "port"):
        self.graph = nx.DiGraph()
        self.current_scene = current_scene
    def add_path(self, from_scene, to_scene, action):
        self.graph.add_node(from_scene, to_scene, action=action)
    def navigate_to(self, target_scene):
        if current_scene == target_scene:
            return
        path = nx.shortest_path(self.graph, self.current_scene, target_scene)
        for from_scene, to_scene in zip(path[:-1], path):
            self.graph[from_scene][to_scene]["action"]()

Scene = Enum("Scene", "hokyu port fixing")

navigator = Navigator()

def click_port_button():
    while exists("1413605460003.png", 0):
        click(Location(10, 10))

for scene in [Scene.hokyu, Scene.fixing]:
    navigator.add_path(scene, Scene.port, click_port_button)

def click_and_wait_sidebar(button):
    def nav():
        click(button)
        wait("1413605460003.png")

navigator.path(Scene.port, Scene.hokyu, click_and_wait_sidebar("1413617134671.png"))
