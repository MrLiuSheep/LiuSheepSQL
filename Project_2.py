from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=3)
scene.set_floor(-1, (1.0, 1.0, 1.0))
scene.set_directional_light((1, 1, 1), 0.1, (0.4, 0.4, 1))
scene.set_background_color((0.5, 0.5, 1))
@ti.func
def hear(x,y,z,length):
    for h in range(0,length+1):
            scene.set_voxel(vec3(x,h+y,h*0.3+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
            for i in range(-2,3):
                scene.set_voxel(vec3(x+i,h-1+y,h*0.3+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
                scene.set_voxel(vec3(x-i,h-1+y,h*0.3+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
                scene.set_voxel(vec3(x,h-1+y,h*0.3+i+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
                scene.set_voxel(vec3(x,h-1+y,h*0.3-i+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
            for j in range(-1,2):
                scene.set_voxel(vec3(x+j,h-1+y,h*0.3+j+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
                scene.set_voxel(vec3(x+j,h-1+y,h*0.3-j+z), 1, vec3(1, 0, 0)*(ti.random()+0.3))
@ti.func
def ball(x,y,z,r):
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,63)):
        if ((i-x)**2 + (j-y)**2 + (k-z)**2)**0.5 <= r:
            scene.set_voxel(vec3(i,j,k), 1, vec3(1, 1, 1))
@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,63)):
        if (i**2 + k**2)/625 + j**2/(0.2*j + 24)**2 <= 1:
            scene.set_voxel(vec3(i, j, k), 1, vec3(1, 0, 0)*(ti.random()+0.3))
            if j <= -5:
                scene.set_voxel(vec3(i, j, k), 1, vec3(0.5, 1, 0.1))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,64)):
        if ((i-21)**2 + (j-5)**2 + (k-7)**2)**0.5 <= 7:
            scene.set_voxel(vec3(i, j, k), 1, vec3(1, 1, 1))
            scene.set_voxel(vec3(i, j, -k), 1, vec3(1, 1, 1))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,63)):
        if ((i-24)**2 + (j-5)**2 + (k-7)**2)**0.5 <= 4:
            scene.set_voxel(vec3(i, j, k), 1, vec3(0, 0, 0))
            scene.set_voxel(vec3(i, j, -k), 1, vec3(0, 0, 0))
    for h,w in ti.ndrange((0,9),(-2,3)):
        scene.set_voxel(vec3(23, h+w+10, h*2), 1, vec3(0, 0, 0))
        scene.set_voxel(vec3(23, h+w+10, h*2-1), 1, vec3(0, 0, 0))
        scene.set_voxel(vec3(23, h+w+10, -h*2), 1, vec3(0, 0, 0))
        scene.set_voxel(vec3(23, h+w+10, -(h-1)*2-1), 1, vec3(0, 0, 0))
    for i,j in ti.ndrange((-5,6),(0,10)):
        for k in range(-5+i+2*j,6-i-2*j):
            scene.set_voxel(vec3(i+28,j-4,k), 1, vec3(0, 1, 0))
            scene.set_voxel(vec3(i+28,-j-4,k), 1, vec3(0, 1, 0))
    hear(0,28,-4,10)
    hear(0,28,2,7)
    for i in range(-11,12):
        for k in range(-3+i*0.3,4-i*0.3):
            scene.set_voxel(vec3(i-28,i/8-5,k*0.5), 1, vec3(0, 0, 0))
            scene.set_voxel(vec3(i-28+2,i/8-5,(k+i)*0.5-5), 1, vec3(0, 0, 0))
            scene.set_voxel(vec3(i-28+2,i/8-5,(k-i)*0.5+5), 1, vec3(0, 0, 0))
    ball(-38,5,0,5)
    ball(-52,3,0,4)
    ball(-62,0,0,2)
initialize_voxels()

scene.finish()
