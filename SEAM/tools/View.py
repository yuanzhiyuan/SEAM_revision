from sklearn.manifold import TSNE
import umap
import numpy as np
from sklearn.preprocessing import *
from sklearn.decomposition import PCA
def View(a,method='Umap'):
    
    data_all = a.uns['IMS']
    pseudo_count=1
    data_all_norm = (data_all+pseudo_count)/(np.percentile(data_all,50,axis=1,keepdims=True)+pseudo_count)
    data_all_norm = MinMaxScaler().fit_transform(data_all_norm)
    if method=='Umap':
        fg_umap = umap.UMAP(n_components=3,n_neighbors=50).fit_transform(data_all_norm)
        a.uns['IMS_Umap'] = fg_umap
    elif method=='Tsne':
        fg_tsne = TSNE(n_components=3).fit_transform(data_all_norm)
        a.uns['IMS_Tsne'] = fg_tsne
    elif method=='PCA':
        fg_pca = PCA(n_components=3).fit_transform(data_all_norm)
        a.uns['IMS_PCA'] = fg_pca
    return a

def View(a,method='Umap',bg_threshold=0):

    data_all = a.uns['IMS']
    if 'adenine' not in a.uns:
        data_134=np.sum(np.array(data_all),axis=1)
    else:
        data_134 = np.array(data_all)[:,a.var_names==a.uns['adenine']][:,0]
    fg_condition = (data_134>=bg_threshold)
    print(fg_condition.shape)
    fg_idx = np.where(fg_condition)[0]
    a.uns['View_fg_idx'] = fg_idx
    pseudo_count=1
    data_all_norm = (data_all+pseudo_count)/(np.percentile(data_all,50,axis=1,keepdims=True)+pseudo_count)
    data_all_norm = MinMaxScaler().fit_transform(data_all_norm)
    if method=='Umap':
        fg_umap = umap.UMAP(n_components=3,n_neighbors=50).fit_transform(data_all_norm[fg_condition,:])
        a.uns['IMS_Umap'] = fg_umap
    elif method=='Tsne':
        fg_tsne = TSNE(n_components=3).fit_transform(data_all_norm[fg_condition,:])
        a.uns['IMS_Tsne'] = fg_tsne
    elif method=='PCA':
        fg_pca = PCA(n_components=3).fit_transform(data_all_norm[fg_condition,:])
        a.uns['IMS_PCA'] = fg_pca
    elif method=='PCAUmap':
        fg_pca = PCA(n_components=50).fit_transform(data_all_norm[fg_condition,:])
        fg_pcaumap = umap.UMAP(n_components=3,n_neighbors=50).fit_transform(fg_pca)
        a.uns['IMS_PCAUmap'] = fg_pcaumap
    elif method=='PCATsne':
        fg_pca = PCA(n_components=50).fit_transform(data_all_norm[fg_condition,:])
        fg_pcatsne = TSNE(n_components=3).fit_transform(fg_pca)
        a.uns['IMS_PCATsne'] = fg_pcatsne
    return a

