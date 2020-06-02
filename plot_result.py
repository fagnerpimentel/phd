from __future__ import division

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
import os
import re

path = sys.argv[1]
space_factor_tolerance = 5
time_factor_tolerance = 5

dirs = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]

v_xlabels = []

v_space_mean = []
v_space_std = []
v_time_mean = []
v_time_std = []

v_SUCCESS = []
v_SPACE_EXCEEDED = []
v_TIME_EXCEEDED = []
v_ABORTION = []
v_COLLISION = []

for dir in dirs:
    result=pd.read_csv(path+'/'+dir+'/result.csv')
    max_experiments = result.i.count()

    SUCCESS = result.status.tolist().count('SUCCESS') / max_experiments
    SPACE_EXCEEDED = result.status.tolist().count('SPACE_EXCEEDED') / max_experiments
    TIME_EXCEEDED = result.status.tolist().count('TIME_EXCEEDED') / max_experiments
    ABORTION = result.status.tolist().count('ABORTION') / max_experiments
    COLLISION = result.status.tolist().count('COLLISION') / max_experiments

    space_elapsed = np.array(result.space_elapsed.tolist())
    space_min = np.array(result.space_min.tolist())
    time_min = np.array(result.time_min.tolist())
    time_elapsed = np.array(result.time_elapsed.tolist())

    space_max = space_factor_tolerance*space_min
    space_coef = 1-(space_elapsed-space_min)/(space_max-space_min);

    time_max = time_factor_tolerance*time_min;
    time_coef = 1-(time_elapsed-time_min)/(time_max-time_min);

    success_indexes = [index for index in range(len(result.status.tolist())) if result.status.tolist()[index] == 'SUCCESS']
    space_coef_success = np.array([space_coef[ind] for ind in success_indexes])
    time_coef_success =  np.array([time_coef[ind] for ind in success_indexes])


    v_xlabels.append(dir.replace('_', '\n') + '\n (' + format(SUCCESS*100, '.2f') + '%)')

    v_space_mean.append(space_coef_success.mean() if(len(space_coef_success) > 0) else 0)
    v_space_std.append(space_coef_success.std() if(len(space_coef_success) > 0) else 0)
    v_time_mean.append(time_coef_success.mean() if(len(time_coef_success) > 0) else 0)
    v_time_std.append(time_coef_success.std() if(len(time_coef_success) > 0) else 0)

    v_SUCCESS.append(SUCCESS)
    v_SPACE_EXCEEDED.append(SPACE_EXCEEDED)
    v_TIME_EXCEEDED.append(TIME_EXCEEDED)
    v_ABORTION.append(ABORTION)
    v_COLLISION.append(COLLISION)

    result = result.replace('SUCCESS', 'SUCCESS:              ' + format(SUCCESS*100, '.2f') + '%')
    result = result.replace('SPACE_EXCEEDED', 'SPACE_EXCEEDED:' + format(SPACE_EXCEEDED*100, '.2f') + '%')
    result = result.replace('TIME_EXCEEDED', 'TIME_EXCEEDED:  ' + format(TIME_EXCEEDED*100, '.2f') + '%')
    result = result.replace('ABORTION', 'ABORTION:            ' + format(ABORTION*100, '.2f') + '%')
    result = result.replace('COLLISION', 'COLLISION:          ' + format(COLLISION*100, '.2f') + '%')

    sns.set(style="whitegrid")
    # plt.suptitle('Accuracy: ' + str(SUCCESS) + '%')

    ax0 = plt.subplot(2, 1, 1)
    plt.ylim(-0.05, 1.2)
    sns.swarmplot(x=result.i, y=time_coef, hue='status', data=result)
    t_mean = time_coef_success.mean() if(len(time_coef_success) > 0) else 0
    sns.lineplot(x=result.i, y=t_mean, dashes=True)
    ax0.set(ylabel='Time coeficience')
    ax0.set(xlabel='')
    ax0.get_legend().remove()
    ax0.set(xticklabels=[])

    ax1 = plt.subplot(2, 1, 2)
    plt.ylim(-0.05, 1.2)
    sns.swarmplot(x=result.i, y=space_coef, hue='status', data=result)
    s_mean = space_coef_success.mean() if(len(space_coef_success) > 0) else 0
    sns.lineplot(x=result.i, y=s_mean, linestyle='--')
    ax1.set(ylabel='Space coeficience')
    ax1.set(xlabel='Experiment ID')
    plt.legend(loc='lower center')

    plt.savefig(path+'/'+dir+'/result.png')
    plt.close()


ax0 = plt.subplot(2, 1, 1)
plt.ylim(0, 1.2)
sns.barplot(x=dirs, y=v_time_mean, yerr=v_time_std)
ax0.set(ylabel='Time coeficience')
ax0.set(xticklabels=[])
ax0.set(xlabel='')

ax1 = plt.subplot(2, 1, 2)
plt.ylim(0, 1.2)
sns.barplot(x=dirs, y=v_space_mean, yerr=v_space_std)
ax1.set(ylabel='Space coeficience')
ax1.set(xticklabels=v_xlabels)
ax1.set(xlabel='')
plt.xticks(rotation=90)

fig = plt.gcf()
DPI = fig.get_dpi()
fig.set_size_inches(1626.0/float(DPI),887.0/float(DPI))

plt.savefig(path+'/all.png')
# plt.show()



# generate latex
set = path.split('/')[-1]
tex = open(path+'/'+set+'.tex','w+')
tex.write('%% '+set+' results %%\n')
s_set = re.sub('[_|-]','',set)
for x in range(0,len(dirs)):
    s_dir = re.sub('[_|-]','',dirs[x])
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'S'  +'}{'+ str(v_SUCCESS[x]) +'}\n')
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'SE' +'}{'+ str(v_SPACE_EXCEEDED[x]) +'}\n')
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'TE' +'}{'+ str(v_TIME_EXCEEDED[x]) +'}\n')
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'A'  +'}{'+ str(v_ABORTION[x]) +'}\n')
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'C'  +'}{'+ str(v_COLLISION[x]) +'}\n')
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'SC' +'}{'+ str(v_space_mean[x]) +'}\n')
    tex.write('\\newcommand{\\'+ s_set + s_dir + 'TC' +'}{'+ str(v_time_mean[x]) +'}\n')
    tex.write('\n')
# tex.close()
