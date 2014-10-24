import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(sys.argv[0])) + "/lib/grph-1.5.24.jar")
from sikuli import *
from grph.in_memory import InMemoryGrph
from enum import Enum

class Navigator:
    def __init__(self, current_scene = "port"):
        self.graph = InMemoryGrph()
        self.actions = {}
        self.current_scene = current_scene
    def add_path(self, from_scene, to_scene, action):
        pair = from_scene.value, to_scene.value
        self.graph.addDirectedSimpleEdge(from_scene.value, to_scene.value)
        self.actions[pair] = action
    def navigate_to(self, target_scene):
        if current_scene == target_scene:
            return
        path = self.graph.getShortestPath( self.current_scene.value, target_scene.value).toVertexArray()
        for edge in zip(path[:-1], path):
            self.action[edge]()

Scene = Enum("Scene", "hokyu port fixing")

navigator = Navigator()

def scene(scene):
    def decorator(f):
        navigator.navigate_to(scene)
        f()
    return decorator

def click_port_button():
    while exists("1413605460003.png", 0):
        click(Location(10, 10))

for scene in [Scene.hokyu, Scene.fixing]:
    navigator.add_path(scene, Scene.port, click_port_button)

def click_and_wait_sidebar(button):
    def nav():
        click(button)
        wait("1413605460003.png")
    return nav

navigator.add_path(Scene.port, Scene.hokyu, click_and_wait_sidebar("1413617134671.png"))
