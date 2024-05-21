
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
from scipy import signal
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

class Square_graph: 
# Creating 3D figure
      fig = plt.figure(figsize = (8, 8))
      ax = plt.axes(projection = '3d')
# Creating Dataset
      t = np.linspace(0, 1, 1000, endpoint = True)
      ax.plot3D(t, signal.square(2 * np.pi * 5 * t))

class Spiral_graph:
   #Creating 3D figure
   fig = plt.figure(figsize = (8,8))
   ax = plt.axes(projection='3d')
   
   # Creating Dataset
   z = np.linspace(0, 15, 1000)
   x = np.sin(z)
   y = np.cos(z)
   ax.plot3D(x, y, z, 'green')
   
class Parabola_Graph:
   # Creating 3D figure
   fig = plt.figure(figsize = (8,8))
   ax = plt.axes(projection = '3d')
   
   # Creating Dataset
   color_cycle = plt.rcParams['axes.prop_cycle']()
   x = linspace(0, 1, 51)
   a = x*( 1 - x)    
   b = 0.25 - a    
   c = x*x*(1 - x)
   d = 0.25-c    
   
   ax.plot3D(x, a, **next(color_cycle))
  
class Parametric_Graph:
   fig = plt.figure(figsize = (8,8))
   ax = plt.axes(projection='3d')
   ax.grid()
   t = np.arange(0, 10*np.pi, np.pi/50)
   x = np.sin(t)
   y = np.cos(t)

   ax.plot3D(x, y, t)
   ax.set_title('3D Parametric Plot')

   # Set axes label
   ax.set_xlabel('x', labelpad=20)
   ax.set_ylabel('y', labelpad=20)
   ax.set_zlabel('t', labelpad=20)

class Scatter_Graph:
   x = np.random.random(50)
   y = np.random.random(50)
   z = np.random.random(50)

   fig = plt.figure(figsize = (10,10))
   ax = plt.axes(projection='3d')
   ax.grid()

   ax.scatter(x, y, z, c = 'r', s = 50)
   ax.set_title('3D Scatter Plot')

   # Set axes label
   ax.set_xlabel('x', labelpad=20)
   ax.set_ylabel('y', labelpad=20)
   ax.set_zlabel('z', labelpad=20)

class mesh_graph:
   
   fig = plt.figure(figsize = (12,10))
   ax = plt.axes(projection='3d')

   x = np.arange(-5, 5.1, 0.2)
   y = np.arange(-5, 5.1, 0.2)

   X, Y = np.meshgrid(x, y)
   Z = np.sin(X)*np.cos(Y)

   surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

   # Set axes label
   ax.set_xlabel('x', labelpad=20)
   ax.set_ylabel('y', labelpad=20)
   ax.set_zlabel('z', labelpad=20)

   fig.colorbar(surf, shrink=0.5, aspect=8)

class surface_map:
   fig = plt.figure()
   ax = plt.axes(projection='3d')

   # Make data.
   X = np.arange(-5, 5, 0.25)
   Y = np.arange(-5, 5, 0.25)
   X, Y = np.meshgrid(X, Y)
   R = np.sqrt(X**2 + Y**2)
   Z = np.sin(R)

   # Plot the surface.
   surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

   # Customize the z axis.
   ax.set_zlim(-1.01, 1.01)
   ax.zaxis.set_major_locator(LinearLocator(10))
   ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

   # Add a color bar which maps values to colors.
   fig.colorbar(surf, shrink=0.5, aspect=5)

class triangular_mesh_graphs:
   n_radii = 8
   n_angles = 36

   # Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
   radii = np.linspace(0.125, 1.0, n_radii)
   angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

   # Repeat all angles for each radius.
   angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

   # Convert polar (radii, angles) coords to cartesian (x, y) coords.
   # (0, 0) is manually added at this stage,  so there will be no duplicate
   # points in the (x, y) plane.
   x = np.append(0, (radii*np.cos(angles)).flatten())
   y = np.append(0, (radii*np.sin(angles)).flatten())

   # Compute z to make the pringle surface.
   z = np.sin(-x*y)

   fig = plt.figure()
   ax = plt.axes(projection='3d')

   ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

   #subplots
   
   fig = plt.figure(figsize=plt.figaspect(0.5))

   #============
   # First plot
   #============

   # Make a mesh in the space of parameterisation variables u and v
   u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
   v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
   u, v = np.meshgrid(u, v)
   u, v = u.flatten(), v.flatten()

   # This is the Mobius mapping, taking a u, v pair and returning an x, y, z
   # triple
   x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
   y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
   z = 0.5 * v * np.sin(u / 2.0)

   # Triangulate parameter space to determine the triangles
   tri = mtri.Triangulation(u, v)

   # Plot the surface.  The triangles in parameter space determine which x, y, z
   # points are connected by an edge.
   ax = fig.add_subplot(1, 2, 1, projection='3d')
   ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
   ax.set_zlim(-1, 1)


   #============
   # Second plot
   #============

   # Make parameter spaces radii and angles.
   n_angles = 36
   n_radii = 8
   min_radius = 0.25
   radii = np.linspace(min_radius, 0.95, n_radii)

   angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
   angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
   angles[:, 1::2] += np.pi/n_angles

   # Map radius, angle pairs to x, y, z points.
   x = (radii*np.cos(angles)).flatten()
   y = (radii*np.sin(angles)).flatten()
   z = (np.cos(radii)*np.cos(angles*3.0)).flatten()

   # Create the Triangulation; no triangles so Delaunay triangulation created.
   triang = mtri.Triangulation(x, y)

   # Mask off unwanted triangles.
   xmid = x[triang.triangles].mean(axis=1)
   ymid = y[triang.triangles].mean(axis=1)
   mask = np.where(xmid**2 + ymid**2 < min_radius**2, 1, 0)
   triang.set_mask(mask)

   # Plot the surface.
   ax = fig.add_subplot(1, 2, 2, projection='3d')
   ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)

plt.show()