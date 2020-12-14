# conway_game_of_life_2d
A 2D world for Conway's Game of life.

The purpose of this small project was to just explore the Cellular Automata
but in a playful manner :p

Now this repo contains the code for the 2D world which confirms to the most
commonly known rule to create the beautiful gliders and other shapes evolving
over time.

There are various parameters which can be tinkered upon to modify the 
behavior of the animation. Which would be interesting. One can modify the
size of the world (n_world), the probability taken while populating the 
world with active and inactive cells and for visual purposes the frame rates.

Now I've taken help of numpy and matplotlib here. To run this code one just needs
to clone it and run `python3 cgol2d.py` ( If you're someone still using py2...
please evolve!!)

The world here warps around the edges and hence every cell will always have
8 cells as neighbours. So, one can imagine this world as a 2D surface on a 3D
world. ( But still visually it is a 2D world...or is it....)

I guess one can go around the code to understand the logic...it is pretty basic.
So leaving that... Have fun...
