Settings.MoveMouseDelay = 0
setAutoWaitTimeout(FOREVER)
decks = [("1413632300064.png", "1413632333979.png"), ("1413632425193.png", "1413632400432.png"), ("1413632475923.png", "1413632448473.png")]
def click_if(pattern):
    e = exists(pattern, 0)
    if not e: return False
    click(e)
    return True
       
def mission_result():
    if not click_if("1413631668061.png"):
        return False
    click(wait("1413606152418.png"))
    click(wait("1413606152418.png"))
    return True

def hokyu(active, inactive):
    active = Pattern(active).similar(0.9)
    inactive = Pattern(inactive).similar(0.9)
    if not exists(active, 0):
        click(inactive)
        wait(active)
    if click_if(Pattern("1413632686156.png").exact()):
        click(wait("1413605362684.png"))
        wait("1413605538080.png")
        return True
    else:
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
        print('wait to hokyu')
        wait("1413605460003.png")
        print('start hokyu')
        if not first_hokyued:
            hokyu(*decks[0])
            first_hokyued = True
        if returned:
            for pair in decks[1:]: hokyu(*pair)
        while exists("1413605460003.png", 0):
            click(Location(10, 10))
    if not exists("1413605597225.png", 2):
        click(Location(10, 10))
    click(wait("1413605597225.png"))
    if returned_global:
        click(wait("1413633517841.png"))
        click("1413633439897.png")
        if click_if("1413605794951.png"):
            wait(decks[1][0])
            click(wait("1413633803249.png"))
        while not exists("1413633736745.png", 0):
            click("1413633644536.png")
        click("1413633736745.png")
        if click_if("1413605794951.png"):
            click(wait(decks[2][1]))
            click(wait("1413633803249.png"))
        while not exists("1413635164833.png", 0):
            click("1413635231796.png")
    else:
        click(wait("1413636959019.png"))
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
