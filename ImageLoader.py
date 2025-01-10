import numpy as np
import pandas as pd
def load():
    images_txt = np.load("images_final_intersected.npy")
    images_ids = np.load("images_final_intersected_ids.npy")
    dataImage = pd.DataFrame(images_txt)
    dataImage["id"] = images_ids
    dataImage.set_index("id", inplace=True)
    return dataImage