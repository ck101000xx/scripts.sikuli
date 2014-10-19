Settings.MoveMouseDelay = 0
setAutoWaitTimeout(FOREVER)
decks = map(lambda pair: map(lambda pattern: Pattern(pattern).similar(0.9), pair)
    , [("1413632300064.png", "1413632333979.png"), ("1413632425193.png", "1413632400432.png"), ("1413632475923.png", "1413632448473.png")])

def click_if(pattern):
    e = exists(pattern, 0)
    if not e: return False
    click(e)
    return True
def go_port():
    while exists("1413605460003.png", 0):
        click(Location(10, 10))
    if not exists("1413605597225.png", 2):
        click(Location(10, 10))
def mission_result():
    if not click_if("1413631668061.png"):
        return False
    click(wait("1413606152418.png"))
    click(wait("1413606152418.png"))
    return True

def start_mission(space, mission, deck):
    active, inactive = deck
    while not exists(mission, 0):
        click(space)
    if click_if("1413605794951.png"):
        while not exists(active):
            click_if(inactive)            
        click(wait("1413633803249.png"))

def hokyu(active, inactive):
    if not exists(active, 0):
        click(inactive)
        wait(active)
    if click_if(Pattern("1413632686156.png").similar(0.90)):
        click(wait("1413605362684.png"))
        wait("1413605538080.png")
        return True
    else:
        return False

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
            return True
    return False
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
        click(wait("1413617134671.png"))
        wait("1413605460003.png")
        if not first_hokyued:
            hokyu(*decks[0])
            first_hokyued = True
        if returned:
            for pair in decks[1:]: hokyu(*pair)
        go_port()
    while True:
        click(wait("1413690676832.png"))
        if not fixing_i8():
            go_port()
            break
        wait(10)
        go_port()
    click(wait("1413605597225.png"))
    if returned_global:
        click(wait("1413633517841.png"))
        start_mission("1413687889991.png", "1413687157384.png", decks[1])
        start_mission("1413687838412.png", "1413687917048.png", decks[2])

        while not exists("1413635164833.png", 0):
            click("1413635231796.png")
    else:
        click(wait("1413636959019.png"))
    while not exists("1413693725906.png", 0):
        click_if("1413693351183.png")
    click("1413693725906.png")
    
    
#    click(wait("1413605681622.png"))
#    click(wait("1413605771793.png"))
    click(wait("1413605794951.png"))
    click(wait("1413605863955.png"))
    click(wait("1413694329127.png"))
    click(wait(Pattern("1413694559796.png").similar(0.9)))
    while not exists("1413606152418.png", 0):
        click_if("1413615405871.png")
    click("1413606152418.png")
    wait(1)
    mouseMove(Location(0, 0))
    click(wait("1413606152418.png"))
    click(wait("1413606195311.png"))
