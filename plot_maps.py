import matplotlib
matplotlib.use('Agg')

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import pandas as pd
import numpy as np
import yaml
import os
import sys
import json


# new colormap
cmap = plt.get_cmap('jet')
my_cmap = cmap(np.arange(cmap.N))
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)
my_cmap = ListedColormap(my_cmap)

sns.set(style="whitegrid")

path = sys.argv[1]

dirs = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]

for dir in dirs:
################################################################################

    if not os.path.exists(path+'/'+dir+"/maps/"):
        os.mkdir(path+'/'+dir+"/maps/")

    # if not os.path.exists(path+'/'+dir+"/error/"):
    #     os.mkdir(path+'/'+dir+"/error/")

    if not os.path.exists(path+'/'+dir+"/factor/"):
        os.mkdir(path+'/'+dir+"/factor/")

    result= pd.read_csv(path+'/'+dir+'/result.csv')
    params = yaml.load(open(path+'/'+dir+'/params.yaml', "r"))
    # localization_error = json.loads(open(path+'/'+dir+'/localization_error.json').read())
    factor = json.loads(open(path+'/'+dir+'/real_time_factor.json').read())
    path_min_x = json.loads(open(path+'/'+dir+'/path_plan_x.json').read())
    path_min_y = json.loads(open(path+'/'+dir+'/path_plan_y.json').read())
    path_elapsed_x = json.loads(open(path+'/'+dir+'/path_executed_x.json').read())
    path_elapsed_y = json.loads(open(path+'/'+dir+'/path_executed_y.json').read())

################################################################################

    img = mpimg.imread(path+'/map.pgm')
    img = np.flipud(img.T)

    robot_vel = params['robot_vel']
    max_experiments = params['max_experiments']

    s = result['status']=='SUCCESS'
    success = s.sum()/s.size

################################################################################

    for experiment_id in range(0,max_experiments):

        a = img.shape[0]
        b = img.shape[1]
        path_min = np.zeros((a,b,4))
        path_elapsed = np.zeros((a,b,4))

        # values_le = localization_error[str(experiment_id)]
        values_fa = factor[str(experiment_id)]

        values_pmx = path_min_x[str(experiment_id)]
        values_pmy = path_min_y[str(experiment_id)]

        values_pex = path_elapsed_x[str(experiment_id)]
        values_pey = path_elapsed_y[str(experiment_id)]

        for i in range(1,len(values_pmx)):
            x = a/2 + int(float(values_pmx[i])/0.05)*-1
            y = b/2 + int(float(values_pmy[i])/0.05)*-1
            try:
                path_min[int(x),int(y),0] = 255
                path_min[int(x),int(y),1] = 255
                path_min[int(x),int(y),2] = 255
                path_min[int(x),int(y),3] = 1
            except Exception as e:
                print (e)
        for i in range(1,len(values_pey)):
            x = a/2 + int(float(values_pex[i])/0.05)*-1
            y = b/2 + int(float(values_pey[i])/0.05)*-1
            try:
                path_elapsed[int(x),int(y),0] = 255
                path_elapsed[int(x),int(y),1] = 255
                path_elapsed[int(x),int(y),2] = 255
                path_elapsed[int(x),int(y),3] = 1
            except Exception as e:
                print (e)

        img=img[int(a/2-150):int(a/2+150), int(b/2-150):int(b/2+150)]
        path_min=path_min[int(a/2-150):int(a/2+150), int(b/2-150):int(b/2+150)]
        path_elapsed=path_elapsed[int(a/2-150):int(a/2+150), int(b/2-150):int(b/2+150)]

        #######################################################

        plt.figure(figsize=(10, 10))

        plt.subplot(2, 1, 1)
        plt.imshow(img, cmap='gray')
        plt.imshow(path_min, cmap=my_cmap, interpolation='bicubic')

        plt.subplot(2, 1, 2)
        plt.imshow(img, cmap='gray')
        plt.imshow(path_elapsed)

        plt.savefig(path+'/'+dir+"/maps/"+str(experiment_id)+".png")
        plt.close()


        # plt.clf()
        # sns.lineplot(x=range(0,len(values_le)), y=values_le, palette="tab10", linewidth=2.5)
        # plt.savefig(path+'/'+dir+"/error/"+str(experiment_id)+".png")

        plt.clf()
        sns.lineplot(x=range(0,len(values_fa)), y=values_fa, palette="tab10", linewidth=2.5)
        plt.savefig(path+'/'+dir+"/factor/"+str(experiment_id)+".png")
