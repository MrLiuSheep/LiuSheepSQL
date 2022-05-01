from scene import Scene
import taichi as ti
from taichi.math import *
scene = Scene(voxel_edges=0.01,exposure=3);scene.set_floor(-0.05, (1.0, 1.0, 1.0))
@ti.func
def arroung(x,y,h,h_start):
    for a,b,c in ti.ndrange((0-x,0+x+1),(0-y,0+y+1),(h_start-h,h_start+h+1)):
        ran = ti.random()*1.05;scene.set_voxel(vec3(a,c,b), ran, vec3(1,1,ti.random()+0.5))
        if ran > 1:scene.set_voxel(vec3(a,c,b), 2, vec3(ti.random(),ti.random(),1))
    for l,m,n in ti.ndrange((0-x+1,0+x),(0-x+1,0+x),(0-x+1,0+x)):scene.set_voxel(vec3(l,n,m), 0, vec3(0,0,0))
@ti.func
def lightning(x,y,a1,a2,h_start):
    for h,b in ti.ndrange((h_start,63),(-1,2)):
        if h >= 10:
            scene.set_voxel(vec3(b+x+a1*(-h+2*10)*0.5,h,y+a2*(-h+2*10)*0.5), 2, vec3(0.6,0.6,1))
            scene.set_voxel(vec3(x+a1*(-h+2*10)*0.5,h,b+y+a2*(-h+2*10)*0.5), 2, vec3(0.6,0.6,1))
        else:
            scene.set_voxel(vec3(b+x+a1*h*0.5,h,y+a2*h*0.5), 2, vec3(0.6,0.6,1))
            scene.set_voxel(vec3(x+a1*h*0.5,h,b+y+a2*h*0.5), 2, vec3(0.6,0.6,1))
        if h <= 3:
            scene.set_voxel(vec3((h+3)+x+a1*h*0.5,h,y+a2*h*0.5), 2, vec3(1-(ti.random()*h),1-(ti.random()*h),1))
            scene.set_voxel(vec3(-(h+3)+x+a1*h*0.5,h,y+a2*h*0.5), 2, vec3(1-(ti.random()*h),1-(ti.random()*h),1))
            scene.set_voxel(vec3(x+a1*h*0.5,h,(h+3)+y+a2*h*0.5), 2, vec3(1-(ti.random()*h),1-(ti.random()*h),1))
            scene.set_voxel(vec3(x+a1*h*0.5,h,-(h+3)+y+a2*h*0.5), 2, vec3(1-(ti.random()*h),1-(ti.random()*h),1))
@ti.func
def lightning_b(ran1,ran2,ran3):
    for h in range(20):scene.set_voxel(vec3(h*ran1+15,h*ran2+25,h*ran3-20), 2, vec3(1-(0.07*h),1-(0.07*h),1))
@ti.kernel
def initialize_voxels():
    arroung(6,7,4,17);arroung(6,6,3,1);arroung(5,5,8,5)
    for i, j, k in ti.ndrange((-4, 5), (-4, 5), (0, 3)):
        if not (j == 0 or i == 0):
            if k == 0:scene.set_voxel(vec3(i,k,j), 1, vec3(0,ti.random()/10,0))
            else:scene.set_voxel(vec3(i,k,j), 1, vec3(0,ti.random(),0))
    for i, j, k in ti.ndrange((-2, 3), (-2, 3), (3, 14)):scene.set_voxel(vec3(i,k,j), 1, vec3(0,ti.random(),0))
    for i, j, k in ti.ndrange((-3, 4), (-4, 5), (13, 20)):scene.set_voxel(vec3(i,k,j), 1, vec3(0,ti.random(),0))
    scene.set_voxel(vec3(-1,14,4), 0, vec3(0,0,0));scene.set_voxel(vec3(0,15,4), 0, vec3(0,0,0))
    scene.set_voxel(vec3(1,14,4), 0, vec3(0,0,0));scene.set_voxel(vec3(-1,14,3), 2, vec3(1,1,0.1))
    scene.set_voxel(vec3(0,15,3), 2, vec3(1,1,0.1));scene.set_voxel(vec3(1,14,3), 2, vec3(1,1,0.1))
    for i,j in ti.ndrange((-2,0),(16,18)):scene.set_voxel(vec3(i,j,4), 0, vec3(0,0,0))
    for i,j in ti.ndrange((1,3),(16,18)):scene.set_voxel(vec3(i,j,4), 0, vec3(0,0,0))
    for i,j in ti.ndrange((-2,0),(16,18)):scene.set_voxel(vec3(i,j,3), 2, vec3((j-15)*i**2*0.1,(j-15)*i**2*0.1,0.1))
    for i,j in ti.ndrange((1,3),(16,18)):scene.set_voxel(vec3(i,j,3), 2, vec3((j-15)*i**2*0.1,(j-15)*i**2*0.1,0.1))
    for i,j in ti.ndrange((-50,50),(-50,50)):
        if i%42 == 0 and j%42 == 0:lightning(i+ti.random()*50,j+ti.random()*50,ti.random()-0.5,ti.random()-0.5,-2)
    for i,j in ti.ndrange((-64,63),(-64,63)):
        scene.set_voxel(vec3(i,-3,j), 1, vec3(ti.random()*0.3,1,ti.random()*0.3))
        if (i**2+j**2)**0.5 <= 32:scene.set_voxel(vec3(i,-2,j), 1, vec3(ti.random()*0.3,1,ti.random()*0.3))
        if (i**2+j**2)**0.5 <= 10:scene.set_voxel(vec3(i,-1,j), 1, vec3(ti.random()*0.3,1,ti.random()*0.3))
    for h in range(-1,6):
        scene.set_voxel(vec3(15,h,-20), 2, vec3(1,1,1));scene.set_voxel(vec3(17,h+1,-18), 2, vec3(1,1,1))
        scene.set_voxel(vec3(13,h+1,-22), 2, vec3(1,1,1))
    for h in range(6,25):scene.set_voxel(vec3(15,h,-20), 1, vec3(0.5,0.5,0.5))
    for h in range(5,8):
        scene.set_voxel(vec3(17,h,-18),1,vec3(0.5,0.5,0.5));scene.set_voxel(vec3(13,h,-22),1,vec3(0.5,0.5,0.5))
        scene.set_voxel(vec3(16,h+1,-19),1,vec3(0.5,0.5,0.5));scene.set_voxel(vec3(14,h+1,-21),1,vec3(0.5,0.5,0.5))
    lightning(15,-20,ti.random(),ti.random(),25)
    for i,j,k in ti.ndrange((10,21),(20,31),(-25,-14)):
        if ((i-15)**2 + (j-25)**2 + (k-(-20))**2)**0.5 <= 3:scene.set_voxel(vec3(i,j,k), 2, vec3(0.3,0.3,1))
    for i in range(15):ran1,ran2,ran3 = ti.random()-0.5,ti.random()-0.5,ti.random()-0.5;lightning_b(ran1,ran2,ran3)
initialize_voxels()
scene.finish()
