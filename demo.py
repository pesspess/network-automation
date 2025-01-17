# from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# import numpy as np

x = np.linspace(0, 20, 100) # create a list of evenly-space numbers over the range
plt.plot(x, np.sin(x))      # plot the sine of each x point
plt.show()                  # display the plot
