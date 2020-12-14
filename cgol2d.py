"""
This is a simple Conway's game of life representation.
The grid's edges wraps around, so one can imagine this
as a 2D surface on a 3D object ( or world ).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ACTIVE = 255
INACTIVE = 0
vals = [ACTIVE, INACTIVE]

def random_grid(n_world):
    """
    Just generating a random grid to play with.
    """
    return np.random.choice(vals, n_world*n_world,
                            p=[0.2, 0.8]).reshape(n_world, n_world)

def update(_, img, grid, n_world):
    """
    Updates the world state based on the present state.
    """
    new_grid = grid.copy()
    for i in range(n_world):
        for j in range(n_world):
            n_state = int((grid[i, (j-1)%n_world] + grid[i, (j+1)%n_world] +
                           grid[(i-1)%n_world, j] + grid[(i+1)%n_world, j] +
                           grid[(i-1)%n_world, (j-1)%n_world] +
                           grid[(i-1)%n_world, (j+1)%n_world] +
                           grid[(i+1)%n_world, (j-1)%n_world] +
                           grid[(i+1)%n_world, (j+1)%n_world])/255)
            if grid[i, j] == ACTIVE:
                if (n_state < 2) or (n_state > 3):
                    new_grid[i, j] = INACTIVE
            else:
                if n_state == 3:
                    new_grid[i, j] = ACTIVE

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

def main():
    """
    TBH adding this line just because pylint is pretty serious about it.
    """
    n_world = 10 # Size of the world.
    grid = random_grid(n_world)
    update_interval = 500

    fig, a_x = plt.subplots()
    img = a_x.imshow(grid, interpolation='nearest')
    _ = animation.FuncAnimation(fig, update, fargs=(img, grid, n_world, ),
                                frames=100,
                                interval=update_interval,
                                save_count=50)

    plt.show()

if __name__ == '__main__':
    main()
