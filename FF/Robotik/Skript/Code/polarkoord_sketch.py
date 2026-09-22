import matplotlib.pyplot as plt
import numpy as np

angles = [
    0,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
    210,
    220,
    230,
    240,
    250,
    260,
    270,
    280,
    290,
    300,
    310,
    320,
    330,
    340,
    350,
]

#####################
### Fügen Sie in die folgende Liste Ihre 36 Messwerte ein ###
#####################

distances = [
    8,
    7,
    7,
    8,
    9,
    10,
    13,
    10,
    8,
    7,
    6,
    6,
    5,
    8,
    7,
    9,
    10,
    10,
    10,
    11,
    11,
    11,
    12,
    14,
    10,
    8,
    8,
    8,
    9,
    9,
    8,
    7,
    6,
    6,
    6,
    6,
]

angles_rad = np.radians(angles)

ax = plt.subplot(projection="polar")
ax.plot(angles_rad, distances, marker="o")

plt.show()
