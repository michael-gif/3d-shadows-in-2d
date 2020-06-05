# 3d-shadows-in-2d
Generates shadows from 3d objects in a 2d image

### Usage
In the shadows.py file, you can change the 3d position of the wall, and light.
Each pixel's color is determined by how far away it is from the light, and wether the ray from the light to itself is blocked by the wall.
The wall's shadow is the black square. All the pixels around the wall aren't blocked by the wall, so they have color.
