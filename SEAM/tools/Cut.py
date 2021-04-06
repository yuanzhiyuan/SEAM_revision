from ..utils import *
from ..settings import *
def Cut(a):
    num_cells = a.shape[0]
    cell_idx = a.uns['cell_idx']
    cell_pos = a.uns['cell_pos']
    cell_pos_list = []


    for i in range(num_cells):
        cur_idx = i + 1
        cur_ind = cell_pos[cell_idx==cur_idx][0]
        cur_ind_list = cell_pos[cell_idx==cur_idx]
        cur_x_list = []
        cur_y_list = []
        for j in cur_ind_list:
            cur_x = ind2ij(cur_ind,IMG_SZ2,1)
            cur_y = ind2ij(cur_ind,IMG_SZ2,0)
            cur_x_list.append(cur_x)
            cur_y_list.append(cur_y)
        cur_x_mean = np.mean(cur_x_list)
        cur_y_mean = np.mean(cur_y_list)

        cell_pos_list.append(np.array([cur_x_mean,cur_y_mean]))


    cell_pos_mat = np.array(cell_pos_list)
    print('setting obsm: spatial')
    a.obsm['spatial'] = cell_pos_mat
    return a


def Cut(a,mode='mean'):
    num_cells = a.shape[0]
    cell_idx = a.uns['cell_idx']
    cell_pos = a.uns['cell_pos']
    cell_pos_list = []

    cell_size_list = []
    for i in range(num_cells):
        cur_idx = i + 1
#         cur_ind = cell_pos[cell_idx==cur_idx][0]
        cur_ind_list = cell_pos[cell_idx==cur_idx]
        cur_x_list = []
        cur_y_list = []
        for cur_ind in cur_ind_list:
            cur_x = ind2ij(cur_ind+1,IMG_SZ2,1)-1
            cur_y = ind2ij(cur_ind+1,IMG_SZ2,0)-1
            cur_x_list.append(cur_x)
            cur_y_list.append(cur_y)
        if mode=='mean':
            cur_x_mean = np.mean(cur_x_list)
            cur_y_mean = np.mean(cur_y_list)
        elif mode=='median':
            cur_x_mean = np.median(cur_x_list)
            cur_y_mean = np.median(cur_y_list)


        cell_size_list.append(len(cur_x_list))
        cell_pos_list.append(np.array([cur_x_mean,cur_y_mean]))


    cell_pos_mat = np.array(cell_pos_list)
    print('setting obsm: spatial')
    a.obsm['spatial'] = cell_pos_mat
    a.obs['cell_size'] = np.array(cell_size_list)
    return a

