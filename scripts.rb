require 'sikulix'
include sikulix
require 'navigator'

Settings.MoveMouseDelay = 0
setAutoWaitTimeout FOREVER

class Deck
  def initialize(pattern_selected, pattern_unselected)
    @pattern_selected = pattern_selected
    @pattern_unselected = pattern_unselected
  end

  def selected
    exists @pattern_selected, 0
  end

  def select
    click_if @pattern_unselected until selected
  end
end

class Mission
  def initialize(pattern_space, pattern_mission)
    @pattern_space = pattern_space
    @pattern_mission = pattern_mission
  end

  def select
    click_if @pattern_space until exists @pattern_mission
  end
end

def click_if(pattern)
  click e if e = exists(pattern, 0)
  !!e
end

def mission_result
  return false if click_if '1413631668061.png'
  click wait '1413606152418.png'
  click wait '1413606152418.png'
  true
end

def start_mission(mission, deck)
  scene :mission do
    mission.select
    until exists('1413605794951.png', 0) || exists('1413715679772.png', 0)
      next
    end
    if click_if '1413605794951.png'
      deck.select
      click wait '1413633803249.png'
    end
  end
end

def hokyu(deck)
  scene :hokyu do
    deck.select
    next unless exists(Pattern.new('1413632686156.png').similar(0.95), 0)
    wait 0.5 while click_if(Pattern('1413632686156.png').similar(0.95))
    click wait '1413605362684.png'
    wait '1413605538080.png'
  end
end

def dead
  scene :fixing do
    wait '1413690454984.png'
    click wait '1413690038857.png'
    wait '1413690128632.png'
    exists '1413978749440.png', 0
  end
end

def fix_i8
  scene :fixing do
    wait '1413690454984.png'
    next if exists('1413979036617.png', 0)
    click wait '1413690038857.png'
    wait '1413690128632.png'
    next unless click_if '1413690179720.png'
    wait '1413690300408.png'
    next unless click_if '1413690337256.png'
    click wait '1413690370311.png'
    wait '1413979036617.png'
    waitVanish '1413979036617.png'
  end
end

decks = (1..4).reduce({}) do |hash, index|
  path = "images/deck/#{index}"
  patterns = %w(selected unselected).map { |type| Pattern.new("#{path}/#{type}.png") }
  hash[index] = Deck.new(*patterns.map { |pattern| pattern.similar(0.9) })
end

missions = {
  6 => Mission.new('1413687889991.png', '1413687157384.png'),
  21 => Mission.new('1413687838412.png', '1413687917048.png')
}
battle_map = ARGV[1]
loop do
  first_hokyued = false
  returned_global = false
  loop do
    returned = false
    while mission_result
      wait '1413617134671.png'
      returned = true
      returned_global = true
    end
    break if !returned && first_hokyued
    unless first_hokyued
      hokyu decks[1]
      first_hokyued = true
    end
    decks[2..3].each { |deck| hokyu(deck) } if returned
    if battle_map == '3-2'
      exit if dead
      fix_i8
    end
  end
  if returned_global
    start_mission(missions[6], decks[2])
    start_mission(missions[21], decks[3])
  end
  if battle_map == '3-2'
    click_if '1413693351183.png' until exists '1413693725906.png', 0
    click '1413693725906.png'
    click wait '1413605794951.png'
    click wait '1413605863955.png'
    wait '1413694329127.png'
    while click_if '1413694329127.png'
      next
    end
    click wait Pattern.new('1413715867460.png').similar(0.80)
    click_if '1413615405871.png' until exists '1413606152418.png', 0
    click '1413606152418.png'
    wait 1
    mouseMove Location.new 0, 0
    click wait '1413606152418.png'
    click wait '1413606195311.png'
  elsif battle_map == '1-5'
    click wait '1413605681622.png'
    click wait '1413605771793.png'
    click wait '1413605794951.png'
    click wait '1413605863955.png'
    click_if '1413615405871.png' until exists '1413606152418.png', 0
    click '1413606152418.png'
    wait 1
    mouseMove Location.new(0, 0)
    click wait '1413606152418.png'
    click wait '1413606195311.png'
  else
    wait(5 * 60)
    navigator.navigate_to :port
  end
end
