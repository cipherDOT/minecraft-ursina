from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.rgb(0, 255, 0),
            highlight_color=color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            # if a voxel at y = 0 is destroyed it causes a bug
            elif key == 'left mouse down' and self.position.y != 0:
                destroy(self)


app = Ursina()

player = FirstPersonController()

voxels = []


def update():
    for z in range(int(player.z - 5), int(player.z + 5)):
        for x in range(int(player.x - 5), int(player.x + 5)):
            # optimizing by not making any voxels where there are already voxels
            if (x, z) not in [(voxel.x, voxel.z) for voxel in voxels if len(voxels) != 0]:
                voxel = Voxel((x, 0, z))
                voxels.append(voxel)

    if player.y <= -10:
        player.x = 0
        player.z = 0
        player.y = 0


app.run()
