'''
This file rename default dataset "our_dataset"
from char-based naming into int-based naming.
'''
import os

data_dir = "our_dataset_copy/"
img_ext = ".png"

# Loop each person's folder
idx_root = 0
for root_name in os.listdir(data_dir):
    if root_name == ".DS_Store":
        continue

    # rename each person's folder (root_name) first
    new_root_name = str(idx_root)
    # os.rename(root_name, new_root_name)
    os.rename(os.path.join(data_dir, root_name), os.path.join(data_dir, new_root_name))

    idx_root += 1

    # loop each image of every person
    idx_fname = 0
    for file in os.listdir(data_dir + new_root_name):
        new_file = str(idx_fname) + '.jpg'
        # os.rename(os.path.join(new_root_name, file), os.path.join(new_root_name, new_file))
        os.rename(os.path.join((data_dir+new_root_name), file), os.path.join((data_dir+new_root_name), new_file))

        idx_fname += 1

print(" ... DONE ...")