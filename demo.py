# from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# import numpy as np
#import General.Plotting.auxiliary_plotting_functions as aux_plot  
# pylint: disable=import-error
import General.Misc.general_tools as tools  # type: ignore

x = np.linspace(0, 20, 100) # create a list of evenly-space numbers over the range
plt.plot(x, np.sin(x))      # plot the sine of each x point
plt.show()                  # display the plot
