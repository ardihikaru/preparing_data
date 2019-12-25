import os
import random


class PairGenerator:
    def __init__(self, data_dir, pairs_filepath, img_ext):
        """
        Parameter data_dir, is your data directory.
        Parameter pairs_filepath, where is the pairs.txt that belongs to.
        Parameter img_ext, is the image data extension for all of your image data.
        """
        self.data_dir = data_dir
        self.pairs_filepath = pairs_filepath
        self.img_ext = img_ext

    def write_similar(self, lst):
        f = open(self.pairs_filepath, 'a+')
        for i in range(20):
            left = random.choice(lst)
            right = random.choice(lst)
            # f.write(left + ' ' + right + ' 1\n')

            # Ardi: Modification to fit example: pairs-sample.txt
            label = left.split('/')[0]
            # left_img_id = (left.split(".")[0]).split("/")[1]
            # right_img_id = (right.split(".")[0]).split("/")[1]
            left_img_id = int(((left.split(".")[0]).split("/")[1]).split("_")[1])
            right_img_id = int(((right.split(".")[0]).split("/")[1]).split("_")[1])
            f.write(label + ' ' + str(left_img_id) + ' ' + str(right_img_id) + '\n')

    def write_different(self, lst1, lst2):
        f = open(self.pairs_filepath, 'a+')
        for i in range(500):
            left = random.choice(lst1)
            right = random.choice(lst2)
            f.write(left + ' ' + right + ' 0\n')
        f.close()

    # def write_simple(self, lst1, lst2):
    #     f = open(self.pairs_filepath, 'a+')
    #     for i in range(500):
    #         left = random.choice(lst1)
    #         right = random.choice(lst2)
    #         f.write(left + ' ' + right + ' 0\n')
    #     f.close()

    def generate_pairs(self):
        # Initial phase: put the common information
        f = open(self.pairs_filepath, 'a+')
        f.write("25 2323\n")
        f.close()

        for name in os.listdir(self.data_dir):
            if name == ".DS_Store":
                continue

            a = []
            for file in os.listdir(self.data_dir + name):
                if file == ".DS_Store":
                    continue
                a.append(name + '/' + file)

            generatePairs.write_similar(a)

    # added by ardi
    def generate_lst(self):
        label = 0
        for name in os.listdir(self.data_dir):
            if name == ".DS_Store":
                continue

            f = open(self.pairs_filepath, 'a+')
            # a = []
            for file in os.listdir(self.data_dir + name):
                if file == ".DS_Store":
                    continue
                file_path = name + '/' + file
                # file_int = file.split('.')[0]
                dataset_dir = "faces112x112" # folder naming used in the future
                # dataset_dir = "mlsp_dataset_int/faces112x112" # folder naming used in the future
                f.write("1" + '\t' + dataset_dir+file_path + '\t' + str(label) + '\n')
                # f.write("1" + '\t' + file_path + '\t' + str(label) + '\n')
                # f.write("1" + ' ' + file_path + ' ' + str(label) + '\n')
                # f.write("1" + ' ' + file_int + ' ' + str(label) + '\n')
            f.close()

            label += 1

            # generatePairs.write_similar(a)

    def generate_non_pairs(self):
        folder_list = []
        for folder in os.listdir(self.data_dir):
            folder_list.append(folder)
        folder_list.sort(reverse=True)
        # print(folder_list)
        i = 0
        a = []
        for dir in os.listdir(self.data_dir):
            if dir == ".DS_Store":
                continue

            for file in os.listdir(self.data_dir + dir):
                if file == ".DS_Store":
                    continue
                a.append(dir + '/' + file)
            # print(a)
        b = []
        for dir in os.listdir(self.data_dir):
            if dir == ".DS_Store":
                continue

            for file in os.listdir(self.data_dir + folder_list[i]):
                if file == ".DS_Store":
                    continue
                b.append(folder_list[i] + '/' + file)
            # print(b)
            i = i + 1

        generatePairs.write_different(a, b)


if __name__ == '__main__':
    data_dir = "our_dataset_lagi/"
    pairs_filepath = "pairs.txt" # output of new pair
    # pairs_filepath = "pairs.lst" # output of new pair
    # pairs_filepath = "pairs_ardi.txt" # output of new pair
    # img_ext = ".png"
    img_ext = ".jpg"
    generatePairs = PairGenerator(data_dir, pairs_filepath, img_ext)
    # generatePairs.generate_lst() # to use, please uncomment this line
    generatePairs.generate_pairs() # to use, please uncomment this line
    # generatePairs.generate_non_pairs() # to use, please uncomment this line
