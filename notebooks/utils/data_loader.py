import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
import os
import sys
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from utils import ransac_fit

def parse_topaz_coordinates(path_to_topaz, path_to_helix):
    f = open(path_to_topaz, "r")
    f.readline()  # skip one line
    o = None

    current_title = ""

    for x in f:
        line = x.split("\t")
        if line[0] != current_title:
            current_title = line[0]
            o = open(path_to_helix + "/" + line[0] + ".txt", "w")

            o.write("x_coord\ty_coord\tscore\n")
            o.write(line[1] + "\t" + line[2] + "\t" + line[3])
        else:
            o.write(line[1] + "\t" + line[2] + "\t" + line[3])
    return 1

def parse_helix_coordinates(path, threshold=-2.5):
    #parse each file
    file_library = {}
    threshold_score = -2.5

    for file in os.listdir(path)[1:]:
        df = pd.read_csv(path+"/"+file, sep="\t")
        df = df.drop(df[df.score<threshold_score].index)
        x = df["x_coord"].to_numpy()
        y = df["y_coord"].to_numpy()
        tup = (x,y)
        file_library.update({file: tup})

    return file_library

def visualize_file(name, file_library):
    img = file_library[name]
    plt.scatter(img[0], img[1], marker=".")


def DBSCAN_fit(img, eps=15, min_samples=5):
    # #############################################################################

    # provide a m * 2 coordinate array for the data points on xy plane
    X = np.concatenate((img[0][..., np.newaxis], img[1][..., np.newaxis]), axis=1)

    # #############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps, min_samples).fit(X)
    # obtain a mask for the useful data points, as defined by "core samples",
    # they contain sufficient number of neighbours within the eps distance
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True

    # obtain the classification labels mapped from each point
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    # #############################################################################
    # Plot result
    import matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    # create a set of labels
    unique_labels = set(labels)
    # create a corresponding set of colours for bijection to the the set of labels
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]

    list_of_clusters = []

    # for each class label and its colour
    for k, col in zip(unique_labels, colors):
        # set the colour to black if the class is assigned to -1 (noise)
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        # obtain a boolean vector to select for coordinates in X of the current k only
        class_member_mask = (labels == k)

        # obtain a list of coordinates from X if they belong to the current k(class) and they are "core samples"
        xy = X[class_member_mask & core_samples_mask]

        # plot the core samples as large dots
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        # plot the non-core samples as smaller dots using a mask for: current k, not "core samples"
        xy_not_core = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy_not_core[:, 0], xy_not_core[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

        cluster = np.concatenate((xy, xy_not_core))
        list_of_clusters.append(cluster)

    plt.title('Estimated number of clusters: %d' % n_clusters_)

    return list_of_clusters



def filament_fit(list_of_clusters, save_path):
    for cluster in list_of_clusters:
        poly_o = ransac_fit.polyfit(cluster, 2, 1, disable_linear=True, directory_mode=False)
        arclength_o = ransac_fit.arclength(poly_o)
        x = ransac_fit.spacing(arclength_o, 60.218)

        y = poly_o["model"].predict(x)

        plt.scatter(x, y, color="purple")
    plt.savefig(save_path)