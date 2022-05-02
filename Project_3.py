from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=3)
scene.set_floor(-0.02, (1.0, 0.5, 0.5))
scene.set_background_color((1.0, 0.5, 0.5))
scene.set_directional_light((0, 1, 0), 0.1, (1, 1, 1))


@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    for i,j,h in ti.ndrange((-64,63),(-64,63),(0,11)):
        if (i**2 +j**2)**0.5 <= h*0.5:
            scene.set_voxel(vec3(i-h*0.4, h+20, j), 1, vec3(0.6, 0.6, 1))
            scene.set_voxel(vec3(i+h*0.8-12, -h+20+20, j), 1, vec3(0.6, 0.6, 1))

            scene.set_voxel(vec3(i-h*0.4-5, h+20, j-h*0.4+10), 1, vec3(0.6, 0.6, 1))
            scene.set_voxel(vec3(i+h*0.8-12-5, -h+20+20, j+h*0.8-12+10), 1, vec3(0.6, 0.6, 1))

            scene.set_voxel(vec3(i-h*0.4-5, h+20, j+h*0.4-10), 1, vec3(0.6, 0.6, 1))
            scene.set_voxel(vec3(i+h*0.8-12-5, -h+20+20, j-h*0.8+12-10), 1, vec3(0.6, 0.6, 1))
    
    for i,j,k in ti.ndrange((-64,63),(-64,63),(0,21)):
        if (i**2 +j**2)**0.5 <= k*0.3:
            scene.set_voxel(vec3(i-k*0.5-21, j-k+40, k+6), 1, vec3(0.6, 0.6, 1))
            scene.set_voxel(vec3(i-k*0.5-21, j-k+40, -k-6), 1, vec3(0.6, 0.6, 1))
    
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,63)):
        if ((i+19)**2 + (j-6-20)**2 + k**2)**0.5 <= 15:
            scene.set_voxel(vec3(i, j, k), 1, vec3(0.6, 0.6, 1))
        if ((i+17)**2 + (j-4-20)**2 + k**2)**0.5 <= 13:
            scene.set_voxel(vec3(i, j, k), 1, vec3(0.9, 1, 0.5))

    for i,j,k in ti.ndrange((-64,63),(-64,63),(0,21)):
        if (i**2 +j**2)**0.5 <= k*0.3:
            scene.set_voxel(vec3(i+k*0.5-41, j+k*0.6+8, k-46), 1, vec3(0.6, 0.6, 1))
            scene.set_voxel(vec3(i+k*0.5-41, j+k*0.6+8, -k+46), 1, vec3(0.6, 0.6, 1))
    
    for i,j,k in ti.ndrange((0,5),(0,6),(0,3)):
        scene.set_voxel(vec3(i-9, j+18, k+5), 1, vec3(0, 0, 0))
        scene.set_voxel(vec3(i-9, j+18, -k-5), 1, vec3(0, 0, 0))
        if i >= 2:
            scene.set_voxel(vec3(i-9, j+18, k+5), 0, vec3(0, 0, 0))
            scene.set_voxel(vec3(i-9, j+18, -k-5), 0, vec3(0, 0, 0))
    
    for i,j,k in ti.ndrange((-13,-4),(-64,63),(-64,63)):
        if ((j-15)**2 + k**2)**0.5 <= 2 and j <= 15:
            if i > -11:
                scene.set_voxel(vec3(i, j, k), 0, vec3(1, 0, 0))
            else:
                scene.set_voxel(vec3(i, j, k), 1, vec3(1, 0, 0))
    for i,j in ti.ndrange((-1,12),(-1,12)):
        scene.set_voxel(vec3(i-32, j+25, 1+14), 1, vec3(0.3, 0.3, 1))
        scene.set_voxel(vec3(i-32, j+25, 2+14), 1, vec3(0.5, 0.5, 1))
        scene.set_voxel(vec3(i-32, j+25, 3+14), 1, vec3(0.3, 0.3, 1))
        
        scene.set_voxel(vec3(i-32, j+25, -1-14), 1, vec3(0.3, 0.3, 1))
        scene.set_voxel(vec3(i-32, j+25, -2-14), 1, vec3(0.5, 0.5, 1))
        scene.set_voxel(vec3(i-32, j+25, -3-14), 1, vec3(0.3, 0.3, 1))
        if (i >= 2 and i <= 8) and (j >= 2 and j <= 8):
            scene.set_voxel(vec3(i-32, j+25, 1+14), 1, vec3(1, 1, 1))
            scene.set_voxel(vec3(i-32, j+25, 3+14), 1, vec3(1, 1, 1))
            
            scene.set_voxel(vec3(i-32, j+25, -1-14), 1, vec3(1, 1, 1))
            scene.set_voxel(vec3(i-32, j+25, -3-14), 1, vec3(1, 1, 1))
    for i,j,h in ti.ndrange((-64,63),(-64,63),(0,16)):
        if (i**2 +j**2)**0.5 <= h*0.4:
            scene.set_voxel(vec3(i-19, -h+17, j), 1, vec3(0.6, 0.6, 1))
    for i,j,h in ti.ndrange((-64,63),(-64,63),(1,6)):
        if (i**2 +j**2)**0.5 <= h*0.4:
            scene.set_voxel(vec3(i-19, h-3, j+3), 1, vec3(0, 0, 0))
            scene.set_voxel(vec3(i-19, h-3, j-3), 1, vec3(0, 0, 0))
            if h <= 2:
                scene.set_voxel(vec3(i-19, h-3, j+3), 1, vec3(0.9, 1, 0.5))
                scene.set_voxel(vec3(i-19, h-3, j-3), 1, vec3(0.9, 1, 0.5))
    for i,j,h in ti.ndrange((-64,63),(-64,63),(1,8)):
        if (i**2 +j**2)**0.5 <= h*0.2:
            scene.set_voxel(vec3(i-19, j+8, h+2), 1, vec3(0.6, 0.6, 1))
            scene.set_voxel(vec3(i-19, j+8, -h-2), 1, vec3(0.6, 0.6, 1))
    
    scene.set_voxel(vec3(-19, +8, -10), 1, vec3(0.9, 1, 0.5))
    scene.set_voxel(vec3(-19, +8, 10), 1, vec3(0.9, 1, 0.5))
    for i in range(0,4):
        for j in range(-2+i*0.5,3-i*0.5):
            scene.set_voxel(vec3(-16, i+8, j), 1, vec3(0.3, 0.3, 1))
            scene.set_voxel(vec3(i*0.5-16+1, -i-1+8, j), 1, vec3(0.3, 0.3, 1))
initialize_voxels()

scene.finish()
