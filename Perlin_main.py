# With this script, we can generate Perlin and simplex noise images

""" Command: python Perlin_main.py shape num_images resolution octaves persistence folder_out
"""

import perlin2d
from perlin2d import generate_perlin_noise_2d
from perlin2d import generate_fractal_noise_2d
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
import imageio

options = sys.argv[1:]
# Check that we have the necessary input
if len(options) != 6:
    print('The input syntax is:\n'
    'python Perlin_main.py shape num_images resolution octaves persistence folder_out\n'
    'Please check your input string')
    sys.exit()

shape = int(options[0])     # This is the size in px of the generate image
num_imgs = int(options[1])  # How many images do we want?
res = int(options[2])       # The lower the res, the less features we see
oct = int(options[3])       # Number of octaves. if 1, we have the basic Perlin noise
pers = float(options[4])    # The persistence values determines how rough a
                            # terrain is. The value should be between 0 and 1
                            # (see http://libnoise.sourceforge.net/tutorials/tutorial4.html)
                            # Recommended value: 0.5
folder_out = options[5]     # Folder where to save the combined images

# If necessary, make the output folder
if not os.path.exists(folder_out):
    os.makedirs(folder_out)

for ii in range(num_imgs):
    #A = generate_perlin_noise_2d([shape, shape], [res, res])
    A = generate_fractal_noise_2d([shape, shape], [res, res], oct, pers)
    # Rescale the images

    #plt.imshow(A)
    #plt.show()
    #sys.exit()

    A_resc = (((A - A.min()) / (A.max() - A.min())) * 255.9).astype(np.uint8)

    filename = os.path.join(folder_out + "/noise" + "_" + str("%02i_%02i" % (res, oct)) + "_" + str("%04i" % ii) + ".png")
    imageio.imwrite(filename, A_resc)

    indicator = num_imgs/10
    if (ii/indicator).is_integer() == True:
        print("We're at %02i%% of the total for resolution %01i, octaves %01i" % ((ii/num_imgs)*100, res,oct) )
