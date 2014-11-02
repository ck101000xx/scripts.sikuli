require 'sikulix'
include Sikulix
require 'util'

class Mission
  def initialize(pattern_space, pattern_mission)
    @pattern_space = pattern_space
    @pattern_mission = pattern_mission
  end

  def select
    click_if @pattern_space until click_if @pattern_mission
  end
end

missions = {
  1 => 1..8,
  2 => 9..16,
  3 => 17..23,
  4 => 25..31,
  5 => 33..39
}.flat_map do |space, range|
  range.map do |mission|
    path = 'images/mission'
    Mission.new("#{path}/space/#{space}.png", "#{path}/#{mission}.png")
  end
end
