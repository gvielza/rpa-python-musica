import pyautogui as robot
import time
#pyautogui.moveTo(X, Y, Seconds)

lista_canciones=['eamon','vocales']
google=123,44
max=1308,13
direccion=179,52
buscar=372,130
cancion=467,290
exit=1347,11



#función para abrir
def abrir(pos,click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

#abrir chrome
abrir(google,click=2)

#configurar tamaño de pantalla
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(0.5)
robot.typewrite("x")

#ubicarme en el buscador
time.sleep(4)
abrir(direccion)
robot.typewrite("www.youtube.com")
robot.hotkey("enter")
time.sleep(4)

#elegir cancion

for i in range(len(lista_canciones)):
    abrir(buscar,click=3)
    robot.typewrite(lista_canciones[i])
    robot.hotkey("enter")
    time.sleep(2)
    abrir(cancion)
    time.sleep(5)

abrir(exit)
print("Finish")









