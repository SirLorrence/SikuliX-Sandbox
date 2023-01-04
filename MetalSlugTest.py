# wait x seconds for menu screen - then click to skip intro
# click main mission -> arcade -> one player
# move and shoot left

gamePath="C:\GOG Games\Metal Slug\mslug1.exe"
openApp(gamePath)
wait(10)
click()#skips intro
for i in range(3):
    wait(1.25)
    type(Key.ENTER)

wait(10)
keyDown(Key.ALT + Key.F4)

