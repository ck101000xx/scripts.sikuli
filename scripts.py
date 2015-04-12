from sikuli import *
Settings.MoveMouseDelay = 0
setAutoWaitTimeout(FOREVER)


class Deck:

    def __init__(self, pattern_selected, pattern_unselected):
        self.pattern_selected = pattern_selected
        self.pattern_unselected = pattern_unselected

    @property
    def selected(self):
        return exists(self.pattern_selected, 0)

    def select(self):
        while not self.selected:
            click_if(self.pattern_unselected)


class Mission:

    def __init__(self, pattern_space, pattern_mission):
        self.pattern_space = pattern_space
        self.pattern_mission = pattern_mission

    def select(self):
        while not click_if(self.pattern_mission):
            click_if(self.pattern_space)


def click_if(pattern):
    e = exists(pattern, 0)
    if not e:
        return False
    click(e)
    return True


def go_port():
    while exists("1413605460003.png", 1):
        click(Location(10, 10))
    if not exists("1413605597225.png", 2):
        click(Location(10, 10))


def mission_result():
    if not click_if("1413631668061.png"):
        return False
    click(wait("1413606152418.png"))
    click(wait("1413606152418.png"))
    return True


def start_mission(mission, deck):
    mission.select()
    while not exists("1413605794951.png", 0) and not exists("1413715679772.png", 0):
        pass
    if click_if("1413605794951.png"):
        deck.select()
        click(wait("1413633803249.png"))


def hokyu(deck):
    deck.select()
    if exists(Pattern("1413632686156.png").similar(0.95), 0):
        while click_if(Pattern("1413632686156.png").similar(0.95)):
            wait(0.5)
        click(wait("1413605362684.png"))
        wait("1413605538080.png")
        return True
    else:
        return False


def fix_akashi():
    wait("1413690454984.png")
    click(wait("1413690038857.png"))
    wait("1413690128632.png")
    if not click_if("1414757939751.png"):
        return
    wait("1413690300408.png")
    if exists("1414834140414.png", 0):
        return
    click(Pattern("1413690300408.png").targetOffset(52,0))
    if not click_if("1413690337256.png"):
        return
    reg = Region(550, 380, 130, 40)
    reg.click(reg.wait("1413690370311.png"))

def fixing_i8():
    wait("1413690454984.png")
    if exists("1413690572298.png", 0):
        return True
    click(wait("1413690038857.png"))
    wait("1413690128632.png")
    if click_if("1413690179720.png"):
        wait("1413690300408.png")
        if click_if("1413690337256.png"):
            click(wait("1413690370311.png"))
            wait("1413690572298.png")
            return True
    return False

decks = {}
for deck_index in [1, 2, 3, 4]:
    path = "images/deck/" + str(deck_index)
    decks[deck_index] = Deck(
        Pattern(
            path +
            "/selected.png").similar(0.9),
        Pattern(
            path +
            "/unselected.png").similar(0.9))

missions = {}
for space, mission in [(1,2), (1, 5), (1, 6), (3, 21)]:
    path_space = "images/mission/space/" + str(space) + ".png"
    path_mission = "images/mission/" + str(mission) + ".png"
    missions[mission] = Mission(path_space, path_mission)

try:
    battle_map = sys.argv[1]
except:
    battle_map = None
while True:
    wait("1413617134671.png")
    first_hokyued = False
    returned_global = False
    while True:
        returned = False
        while mission_result():
            wait("1413617134671.png")
            returned = True
            returned_global = True
        if not returned and first_hokyued:
            print('hokyued all')
            break
        if battle_map == "1-1":
            click(wait("1413690676832.png"))
            fix_akashi()
            while not exists("1413605538080.png", 0):
                click_if("1414835147219.png")
        else:
            click(wait("1413617134671.png"))
            mouseMove(Location(10, 10))
            wait("1413605460003.png")
        if not first_hokyued:
            hokyu(decks[1])
            first_hokyued = True
        if returned:
            for deck in [decks[2], decks[3], decks[4]]:
                hokyu(deck)
        if battle_map == "3-2":
            while not exists("1413690454984.png", 0):
                click_if("1414759360717.png")
            if fixing_i8():
                waitVanish("1413690572298.png")
        go_port()

    click(wait("1413605597225.png"))
    if returned_global:
        click(wait("1413633517841.png"))
	wait("1414842642178.png")
        start_mission(missions[5], decks[2])
        start_mission(missions[21], decks[3])
        start_mission(missions[2], decks[4])
        while not exists("1413635164833.png", 0):
            click("1413635231796.png")
    else:
        click(wait("1413636959019.png"))
    if battle_map == "3-2":
        while not exists("1413693725906.png", 0):
            click_if("1413693351183.png")
        click("1413693725906.png")
        click(wait("1413605794951.png"))
        click(wait("1413605863955.png"))
        wait("1413694329127.png")
        while click_if("1413694329127.png"):
            pass
        click(wait(Pattern("1413715867460.png").similar(0.80)))
        while not exists("1413606152418.png", 0):
            click_if("1413615405871.png")
        click("1413606152418.png")
        wait(1)
        mouseMove(Location(0, 0))
        click(wait("1413606152418.png"))
        click(wait("1413606195311.png"))
    elif battle_map == "1-1":
        mouseMove(Location(10, 10))
        wait("1413605681622.png")
        click(wait(Pattern("images/battle/field/1-1.png").exact()))
        reg = Region(630, 420, 110, 45)
        reg.click(reg.wait("1413605794951.png"))
        click(wait("1413605863955.png"))
        while not exists("1413606152418.png", 0):
            click_if("1413615405871.png")
        click("1413606152418.png")
        wait(1)
        mouseMove(Location(0, 0))
        click(wait("1413606152418.png"))
        click(wait("1413606195311.png"))
    elif battle_map == "1-5":
        click(wait("1413605681622.png"))
        click(wait("1413605771793.png"))
        click(wait("1413605794951.png"))
        click(wait("1413605863955.png"))
        while not exists("1413606152418.png", 0):
            click_if("1413615405871.png")
        click("1413606152418.png")
        wait(1)
        mouseMove(Location(0, 0))
        click(wait("1413606152418.png"))
        click(wait("1413606195311.png"))
    else:
        wait(5 * 60)
        go_port()
