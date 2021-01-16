## Two-dimensional wave simulation

This python code uses Finite Volume Method to obtain a simulation of a sound wave propagation. Plot in end of the program shows the motion of a sound wave with sound source in center of environment

![Alt Text](wave_propagation_2d.gif)

For this example, the following conditions are considered:

### Boundary Conditions
<p>
<img src="https://render.githubusercontent.com/render/math?math=u(0,0,t) = 0">
</p>
<p>
<img src="https://render.githubusercontent.com/render/math?math=u(L, W, t) = 0">
</p>
<p>
<img src="https://render.githubusercontent.com/render/math?math=u(L, 0, t) = 0">
</p>
<p>
<img src="https://render.githubusercontent.com/render/math?math=u(0, W, t) = 0">
</p>

### Initial Conditions

<p>
<img src="https://render.githubusercontent.com/render/math?math=u(x,0) = 100.000, L/2 - dx\le x \le \L/2 %2B dx, W/2 - dy\le y \le \W/2 %2B dy">
</p>
<p>
<img src="https://render.githubusercontent.com/render/math?math=\left.\frac{\partial u}{\partial t}\right|_{t = 0} = 0">
</p>

Changing boundary and initial conditions, allows to obtain waves with different shapes.