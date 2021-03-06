from os import path
from matplotlib import rc
from matplotlib import rcParams

import os

rc('font', **{'family': 'serif', 'serif': ['Times']})
rc('text', usetex=True)
rc('text.latex', unicode=True)
handlelength = 0.8 * rcParams['legend.handlelength']
handletextpad = 0.8 * rcParams['legend.handletextpad']
rc('legend', handlelength=handlelength, handletextpad=handletextpad)

data_dir = 'data'
fig_dir = 'figure'
if not path.exists(fig_dir):
  os.makedirs(fig_dir)

width = 6.4
height = 4.8
legend_size = 25
label_size = 25
line_width = 3.5
dotted_width = 4.0
marker_edge_width = 1.5
marker_size = 12
tick_size = 23
broken_length = 0.015
pad_inches = 0.10
bbox_to_anchor = (-0.22, 1.0, 1.26, 1.0)
line_kwargs = {'linewidth': line_width,
               'markersize': marker_size,
               'fillstyle': 'none',
               'markeredgewidth': marker_edge_width}
markers = ['|', 'v', 'p', 's', 'o']
colors = ['g', 'r', 'b', 'm']
linestyles = ['-', ':', '-.', '--']
mf = 'MF'
nf = 'NF'
ips = 'IPS'
dr = 'DR'
mf_ips = mf + '-' + ips
nf_ips = nf + '-' + ips
mf_dr = mf + '-' + dr
nf_dr = nf + '-' + dr
ltd = '-LTD'

name_linestyles = {'solid': (0, ()),
                   'loosely dotted': (0, (1, 10)),
                   'dotted': (0, (1, 1)),
                   'densely dotted': (0, (1, 1)),
                   'loosely dashed': (0, (5, 10)),
                   'dashed': (0, (5, 5)),
                   'densely dashed': (0, (5, 1)),
                   'loosely dashdotted': (0, (3, 10, 1, 10)),
                   'dashdotted': (0, (3, 5, 1, 5)),
                   'densely dashdotted': (0, (3, 1, 1, 1)),
                   'dashdotdotted': (0, (3, 5, 1, 5, 1, 5)),
                   'loosely dashdotdotted': (0, (3, 10, 1, 10, 1, 10)),
                   'densely dashdotdotted': (0, (3, 1, 1, 1, 1, 1)),
                   'densely dashdotdotdotted': (0, (3, 1, 1, 1, 1, 1, 1, 1))}

def swap_elem(arr_list, pos_i, pos_j):
  elem = arr_list[pos_i]
  arr_list[pos_i] = arr_list[pos_j]
  arr_list[pos_j] = elem
  return arr_list

def report_impr(name, mse_list):
  mse_min = mse_list.min()
  mse_max = mse_list.max()
  impr = (mse_max - mse_min) / mse_max * 100
  print('%-16s %.2f%%' % (name, impr))
