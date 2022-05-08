from scene import Scene
import taichi as ti
from taichi.math import *
scene = Scene(voxel_edges=0, exposure=3)
scene.set_floor(-1, (0.5, 0.5, 1))
scene.set_background_color((0.5, 0.5, 1))
scene.set_directional_light((1, 1, 0), 0.1, (0.3, 0.3, 0.3))
@ti.func
def cloud(x,y,z):
    for i in range(0,21):
        for j,k in ti.ndrange((-25+i,26-i),(-1,2)):
            scene.set_voxel(vec3(0.5*i*ti.cos(15.0+i*360*10)+x,0.5*i*ti.sin(15.0+i*360*10)*0.5+y,j*0.1+k+z), 1, vec3(1,1,1))
            scene.set_voxel(vec3(0.5*i*ti.cos(15.0+i*360*10)+x,0.5*i*ti.sin(15.0+i*360*10)*0.5+k+y,j*0.1+z), 1, vec3(1,1,1))
            scene.set_voxel(vec3(0.5*i*ti.cos(15.0+i*360*10)+k+x,0.5*i*ti.sin(15.0+i*360*10)*0.5+y,j*0.1+z), 1, vec3(1,1,1))
@ti.kernel
def initialize_voxels():
    for i,j in ti.ndrange((0,11),(-3,4)):
        if j > -3 and j < 3 and i >= 1:
            scene.set_voxel(vec3(-i+60,i*0.1+1+10,j-1), 1, vec3(0.9, 0.1, 0.1))
            scene.set_voxel(vec3(-i+60,i*0.1+2+10,j-1), 1, vec3(0.9, 0.1, 0.1))
        else:
            scene.set_voxel(vec3(-i+60,i*0.1+10,j-1), 1, vec3(0.9, 0.1, 0.1))
            scene.set_voxel(vec3(-i+60,i*0.1+1+10,j-1), 1, vec3(0.9, 0.1, 0.1))
    for i,j in ti.ndrange((-2,10),(-3,4)):
        if j > -3 and j < 3 and i >= 0:
            scene.set_voxel(vec3(-i-4+60,i*0.7-6-1+10,j-1), 1, vec3(0.9, 0.1, 0.1))
            scene.set_voxel(vec3(-i-4+60,i*0.7-6+10,j-1), 1, vec3(0.9, 0.1, 0.1))
        else:
            scene.set_voxel(vec3(-i-4+60,i*0.7-6+10,j-1), 1, vec3(0.9, 0.1, 0.1))
            scene.set_voxel(vec3(-i-4+60,i*0.7-6+1+10,j-1), 1, vec3(0.9, 0.1, 0.1))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,63)):
        if (i**2 + j**2 + k**2)**0.5 <= 2:
            scene.set_voxel(vec3(i-10+60,j+4+10,k+2-1), 2, vec3(1, 1, 1))
            scene.set_voxel(vec3(i-10+60,j+4+10,k-2-1), 2, vec3(1, 1, 1))
    for i,j in ti.ndrange((-64,63),(-64,63)):
        if (i**2 + j**2)**0.5 <= 3:
            scene.set_voxel(vec3(i-10+60,(j+i)*0.5+5+10,j+2-1), 1, vec3(0.9, 0.1, 0.1))
            scene.set_voxel(vec3(i-10+60,(-j+i)*0.5+5+10,j-2-1), 1, vec3(0.9, 0.1, 0.1))
        if (i**2 + j**2)**0.5 <= 2:
            scene.set_voxel(vec3(i-10+60,(j+i)*0.5+6+10,j+2-1), 1, vec3(0.9, 0.1, 0.1))
            scene.set_voxel(vec3(i-10+60,(-j+i)*0.5+6+10,j-2-1), 1, vec3(0.9, 0.1, 0.1))
    for x,y in ti.ndrange((-64,63),(-64,63)):
        if (x**2 + y**2)**0.5 == 5:
            for i,j,k in ti.ndrange((-64,63),(-64,63),(0,11)):
                if ((i-x)**2 + (j-y)**2)**0.5 <= k**0.1:
                    scene.set_voxel(vec3(-k-13+60,j-k*x*0.1+3+10,i+k*y*0.1-1), 1, vec3(1, 0.4, 0.1))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(0,16)):
        if (i**2 + j**2)**0.5 <= k*0.2:
            scene.set_voxel(vec3(k-27+60,j-k+20+10,i-k*0.2+5-1), 1, vec3(0.1, 1, 0.1))
            scene.set_voxel(vec3(k-27+60,j-k+20+10,i+k*0.2-5-1), 1, vec3(0.1, 1, 0.1))
    for i in range(16):
            scene.set_voxel(vec3(-i+60,ti.sin(0.5*i)+12,i+2), 1, vec3(1, 0.4, 0.1))
            scene.set_voxel(vec3(-i+60,ti.sin(0.5*i)+12,-i-4), 1, vec3(1, 0.4, 0.1))
    for i,x,y in ti.ndrange((-55,21),(-64,63),(-64,63)):
        if (x**2 + y**2)**0.5 <= 5:
            scene.set_voxel(vec3(i+22,x+ti.sin(0.1*i)*13,y+ti.cos(0.1*i)*5), 1, vec3(1, 0.1, 0.1))
            for l in range(10):scene.set_voxel(vec3(i+22,l+ti.sin(0.1*i)*13,ti.cos(0.1*i)*5), 2, vec3(1, 0.4, 0.3))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(0,18)):
        if (i**2 + j**2)**0.5 <= k*0.3:scene.set_voxel(vec3(k-51,k*0.6+i-2,-k*0.4+j+10), 1, vec3(1, 0.1, 0.1))
    for i in range(0,20):
        for j in range(-10+i*0.5,11-i*0.5):
            scene.set_voxel(vec3(i-40,i*0.6+j+6,-i*0.4+6),2,vec3(1,0.4,0.3))
            scene.set_voxel(vec3(-i-40,-i*0.6+j+6,i*0.4+6),2,vec3(1,0.4,0.3))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(2,11)):
        if (i**2 + j**2)**0.5 <= k*0.5:
            scene.set_voxel(vec3(k+i+2,k+j-20,k-10), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(-k+i+22,k+j-20,-k+17), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(k*2+i-25,k+j-15,k-18), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(k*2+i-25,k+j-15,-k+9), 1, vec3(1, 0.1, 0.1))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(0,6)):
        if (i**2 + j**2)**0.5 <= 1:
            scene.set_voxel(vec3(-k+i+8+2,k-24,k*0.4+j-10), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(-k+i+8+18,-k-15,-k*0.4+j+18), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(k+i+8-35,-k-8,k*0.2+j-17), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(k+i+8-35,-k-8,-k*0.2+j+8), 1, vec3(1, 0.1, 0.1))
    for i,j,k in ti.ndrange((-64,63),(-64,63),(0,11)):
        if (i**2 + j**2)**0.5 <= k*0.2:
            scene.set_voxel(vec3(-k+20,k*0.5+i-30,j-10), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(-k+20,k*0.5+i-30,k*0.5+j-5-10), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(-k+20,k*0.5+i-30,-k*0.5+j+5-10), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k-20+20,k*0.5+i-30,j-10), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(-k*0.5+i+32,-k-5,j+17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(-k*0.5+i+32, -k-5,k*0.5+j-5+17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(-k*0.5+i+32, -k-5,-k*0.5+j+5+17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(-k*0.5+i+32, k-20-5,j+17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33 ,k-20,j-17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33,k-20,k*0.5+j-5-17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5-33,k-20,-k*0.5+j+5-17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33,-k+20-20,j-17), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33 ,k-20,j+8), 1, vec3(1, 0.1, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33 ,k-20,k*0.5+j-5+8), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33 ,k-20,-k*0.5+j+5+8), 1, vec3(1, 0.5, 0.1))
            scene.set_voxel(vec3(k*0.5+i-33,-k+20-20,j+8), 1, vec3(1, 0.5, 0.1))
    cloud(10,20,10);cloud(-10,-10,-20);cloud(40,-20,10);cloud(-40,15,-10);cloud(-10,-30,10)
    for i,j,k in ti.ndrange((-64,63),(-64,63),(-64,63)):
        if ((i-10)**2 + (j+34)**2 + (k+10)**2)**0.5 <= 5:
            scene.set_voxel(vec3(i,j,k), 2, vec3(0.9, 1, 0.1))
initialize_voxels()
scene.finish()
