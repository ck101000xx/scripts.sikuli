java_import 'grph.in_memory.InMemoryGrph'
require 'sikulix'
include Sikulix
require 'set'

class Navigator
  def initialize(current_scene = :port)
    @graph = InMemoryGrph.new
    @handlers = Set.new
    @actions = Hash.new { |hash, key| hash[key] =  Hash.new(Proc.new) }
    @current_scene = current_scene
  end

  def on_move(&handler)
    @handlers.add handler
  end

  def set_action(*edge, &action)
    source_id, target_id = ids = edge.map(&:object_id)
    @graph.addDirectedSimpleEdge(*ids) unless @graph.isDirectedSimpleEdge(*ids)
    @actions[source_id][target_id] = action
  end

  def navigate_to(target_scene)
    current_scene_id = @current_scene.object_id
    target_scene_id = target_scene.object_id
    if current_scene_id == target_scene_id
      @actions[current_scene_id][target_scene_id].call
    elsif path = @graph.getShortestPath(current_scene_id, target_scene_id)
      path[1..-1].zip(path) do |(target, source)|
        @actions[source][target].call
        @handlers.each do |handler|
          handler.call(ObjectSpace._id2ref source, ObjectSpace._id2ref target)
        end
      end
      @current_scene = target_scene
    else
      fail "Cannot find a path from #{@current_scene} to #{target_scene}"
    end
  end
end

navigator = Navigator.new

def scene(scene)
  navigator.navigate_to scene
  result = yield
  navigator.navigate_to scene
  result
end

[:hokyu, :fixing, :shutsugeki].each do |scene|
  navigator.set_action scene, :port do
    click Location.new(10, 10) while exists 'images/sidebar/port.png', 0
  end
end

[:hokyu, :fixing, :shutsugeki].each do |scene|
  navigator.set_action :port, scene do
    click "images/port/menu/#{scene}.png"
    wait 'images/sidebar/port.png'
  end
end