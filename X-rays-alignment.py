
# coding: utf-8

## Ray tracing test for the X-rays alignment:¶

# In[1]:

import foxsisim
from foxsisim.module import Module
from foxsisim.detector import Detector
from foxsisim.source import Source
from foxsisim.plotting import scatterHist
import matplotlib.pyplot as plt
from foxsisim.plotting import plot
import numpy as np
get_ipython().magic(u'matplotlib inline')


# After make a complete alignment using the X-rays generator yesterday (November 10, 2014), today we are  ready to do an analysis of the how off-axis are the optical modules mounted over the foxsi meter-tube.
# 
# 

# In[2]:

# create module of 7 shells
#module = Module(radii=[5.151,4.9,4.659,4.429,4.21,4.0,3.799],
module = Module(radii=[5.151, 3.799],
                seglen=30.0,
                base=[0,0,0],
                focal=200,
                angles=None,
                conic=False)

detector = Detector(width=2, 
                    height=2,
                    normal=[0,0,1],
                    center=[0,0,200.0+30.0],
                    reso =[256,256])


# In[3]:

source_distance = -2187.5
offaxis_angle_arcmin = 0.0
source = Source(type='point',          
                center=[ source_distance * np.sin(np.deg2rad(offaxis_angle_arcmin/60.0)) , 0.0 , source_distance ],
                color=[0,1,1])


# In[4]:

rays = source.generateRays(module.targetFront, 10)
module.passRays(rays, robust=True)
detector.catchRays(rays)


# In[5]:

plot(detector)


# In[6]:

scatterHist(rays)


# In[7]:

for ray in rays:
    print("x=%f, y=%f, bounce=%i, dead=%i" % (ray.des[0], ray.des[1], ray.bounces, ray.dead))


# In[8]:

np.sum([ray.dead for ray in rays])


# In[9]:

fig = plt.figure(figsize=(7,7), dpi=100)

x = np.array([ray.des[0] for ray in rays])
y = np.array([ray.des[1] for ray in rays])

# Defining colors:
colors = []
for ray in rays:
        if ray.bounces == 1: col = 'r' # red
        elif ray.bounces == 2: col = 'g' # green
        elif ray.bounces == 3: col = 'b' # blue
        else: col = 'k' # black
        colors.append(col)

# definitions for the axes 
left, width = 0.1, 0.8
bottom, height = 0.1, 0.8
rect_scatter = [left, bottom, width, height]
axScatter = fig.add_axes(rect_scatter)
        
axScatter.scatter(x,y,c=colors)

plt.title('X-rays alignment - simulation')
plt.grid()
plt.show()


## Testing Straight Through Flux Shield

# In[10]:

module = Module(radii=[5.151, 3.799],
                seglen=30.0,
                base=[0,0,0],
                focal=200,
                angles=None,
                conic=False,
                core_radius=1.0)

detector = Detector(width=2, 
                    height=2,
                    normal=[0,0,1],
                    center=[0,0,210.0],
                    reso =[256,256])
source_distance = -2187.5
offaxis_angle_arcmin = 0.0
source = Source(type='atinf',          
                center=[ source_distance * np.sin(np.deg2rad(offaxis_angle_arcmin/60.0)) , 0.0 , -10 ],
                color=[0,1,1],
                width=15,
                height=15)
rays = source.generateRays(module.targetFront, 1000)
module.passRays(rays, robust=True)
detector.catchRays(rays)


# In[11]:

scatterHist(detector.rays)


# In[18]:

detector.rays[4].pos


# In[21]:

detector.rays[5].hist


# In[22]:

detector.rays[5].bounces


# In[14]:



