from ursina import *
from random import randint, uniform
from random import choice
from ursina.shaders import basic_lighting_shader
from ursina.prefabs.first_person_controller import FirstPersonController
import threading
from playsound import *


def play(sound):
    threading.Thread(target=playsound, args=(sound,), daemon=True).start()

#dev
efficientmode = False
hyperefficientmode = False





play('Space Ambience.mp3')

spedometer = 1

gassies = ['satrn.jpg', 'jupitr.jpg']
icies = ['urnas2.jpg', 'nptun2.jpeg']
terrestries = ['mrs.jpeg', 'mrcy.jpg', 'vens.jpg']
dwarfes = ['pto.jpg', 'crs']
moonse = ['encla.jpg', 'erpa.jpg', 'mun.jpg']


def update():
    global spedometer
    if not hyperefficientmode:
        for sun in entities:
            sun.rotation_z += time.dt*0.025 * spedometer * sun.sped
        for anchor in anchors:
            anchor.rotation_z += time.dt*0.025 * spedometer * anchor.sped
        #for planet in planets:
        #    planet.rotation_z += time.dt*planet.scale_x * 0.00325  * spedometer
        if efficientmode == False and hyperefficientmode == False:
            for moon in moons:
                moon.rotation_z += time.dt*1 * spedometer
    if held_keys['shift'] == 1:
        player.speed = 100
    if held_keys['control'] == 1:
        player.speed = 1000
    elif not held_keys['shift'] == 1 and not held_keys['control'] == 1:
        player.speed = 1
    if held_keys['z'] == 1:
        player.y -= 0.0025 * time.dt * 100
        if held_keys['shift'] == 1:
            player.y -= 2.5 * time.dt * 20
        if held_keys['control'] == 1:
            player.y -= 2.5 * time.dt * 200
    if held_keys['x'] == 1:
        player.y += 0.0025 * time.dt * 100
        if held_keys['shift'] == 1:
            player.y += 2.5 * time.dt * 20
        if held_keys['control'] == 1:
            player.y += 2.5 * time.dt * 200
    if held_keys['r'] == 1:
        spedometer = 100000
    if held_keys['e'] == 1:
        spedometer = 10000
    #if held_keys['e'] != 1:
    #    spedometer = 1
    if held_keys['r'] != 1:
        spedometer = 1
        

def input(key):
    if key=='escape':
        exit()

app = Ursina()



entities = []
anchors = []
planets = []
moons = []
rings = []

#r = choice((0, 1555))
#g = choice((0, 1555))
#b = choice((0, 1555))

if hyperefficientmode:
    Helper = AmbientLight(color=color.rgb(50, 50, 50))
    rang = 500
    xyz = 40000
else:
    rang = 25
    xyz = 2000


for i in range(rang):

    spacepositionx = randint(-xyz, xyz)
    spacepositiony = randint(-xyz, xyz)
    spacepositionz = randint(-xyz, xyz)

    if not hyperefficientmode:
        skel = uniform(7.5, 15.0)
    else:
        skel = uniform(75, 150)

    if hyperefficientmode == False:
        Sun2 = PointLight(color=color.rgb(1555 / 100, 1555 / 100, 1555 / 100), x=spacepositionx, y=spacepositiony, z=spacepositionz)#shadows=True)
        Sun = Entity(model='sphere', parent=Sun2, scale=(skel, skel, skel), color=color.rgb(15555,15555,15555), shader=None, sped=randint(10, 15) / 100)
        entities.append(Sun)
    else:
        Sun = Entity(model='sphere', scale=(skel, skel, skel), rotation_x=90, color=color.rgb(15555,15555,15555), shader=None, sped=randint(10, 15) / 100, x=spacepositionx, y=spacepositiony, z=spacepositionz)

    if not hyperefficientmode:
        planetypes = {
            'dwarf':0.125,
            'terra':0.25,
            'gassy':2.0,
            'iceys':1.05,
        }
        prevx = 4
    else:
        planetypes = {
            'dwarf':0.125,
            'terra':0.25,
            'gassy':2.0,
            'iceys':1.05,
        }
        prevx = 20



    for i in range(randint(2, 7)):
        anchore = Entity(model='cube', parent=Sun, color=color.rgba(0, 0, 0, 0), sped=randint(10, 150) / 1000)
        anchors.append(anchore)
        scrap, siz = choice(list(planetypes.items()))
        skel = uniform(siz - (siz // 3), siz + (siz // 3))
        r = randint(0, 200)
        g = randint(0, 200)
        b = randint(0, 200)
        if scrap == 'dwarf':
            texta = choice(dwarfes)
        if scrap == 'terra':
            texta = choice(terrestries)
        if scrap == 'iceys':
            texta = choice(icies)
        if scrap == 'gassy':
            texta = choice(gassies)
        if not hyperefficientmode:
            i = Entity(parent=anchore, model='sphere', subdivisions=3, x=prevx * 1.3, y=0, z=0, scale=(skel, skel, skel), color=color.rgb(r,g,b), shader=basic_lighting_shader, texture=texta)
        else:
            i = Entity(parent=anchore, model='sphere', subdivisions=3, x=prevx * 1.3, y=0, z=0, scale=(skel, skel, skel), color=color.rgb(r,g,b))
        i.rotation_x = 90

        if not hyperefficientmode:
            print("XYZ: " + str(i.x) + " " + str(i.y) + " " + str(i.z))
            print("COLOR: " + str(r) + " " + str(g) + " " + str(b))
            planets.append(i)
        e = randint(0, 1)
        if efficientmode == False and hyperefficientmode == False:
            if skel > 1:
                r = randint(0, 4)
                if r == 2:
                    #r = uniform(0.0, 1.0)
                    r = 0
                    ring = Entity(parent=anchore, x=i.x, y=i.y, z=i.z, model='plane', scale=(i.scale_x + 2, i.scale_x + 2, i.scale_y + 2), color=color.rgba(255, 255, 255, 255), texture='ring.png', double_sided = True)
                    ring.rotation_x = 90
                    rings.append(ring)
                    #ring.rotation_x = 90
                    print("HAS RING: TRUE")
                else:
                    print("HAS RING: FALSE")
            if e == 1 or skel > 0.5:
                print("HAS MOON: TRUE")
                prevd = 0.75
                muns = randint(0, 8)
                print("NUMBER OF MOONS: " + str(muns))
                for j in range(muns):
                    print("WOO")
                    scrap, siz = choice(list(planetypes.items()))
                    skel = uniform(siz - (siz // 3), siz + (siz // 3))
                    skel /= 10
                    r = randint(0, 200)
                    g = randint(0, 200)
                    b = randint(0, 200)
                    texta = choice(moonse)
                    mun = Entity(parent=i, model='sphere', x=uniform(prevd + 2, prevd * 2), y=0, z=choice((-prevd, prevd, 0)), scale=(skel, skel, skel), color=color.rgb(r,g,b), shader=basic_lighting_shader, texture=texta)
                    moons.append(mun)
        prevx *= 1.7

    #for i in range(randint(2, 7)):
    #    planit(i)

window.color = color.rgb(0, 0, 0)

player = FirstPersonController(gravity=0, speed=10)
#EditorCamera()
camera.rotation_x = 0

#player.add_script(NoclipMode())

app.run()