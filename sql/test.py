
import numpy as np
# array([[23,  5],
#        [ 3, 638]])

cf_matrix = np.array([[638,  10735],
       [ 20, 35128]])

import seaborn as sns


group_names = ["True Pos","False Pos","False Neg","True Neg"]
group_counts = ["{0:0.0f}".format(value) for value in
                cf_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in  zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
heatmap = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')

heatmap.figure.savefig("output.png")
