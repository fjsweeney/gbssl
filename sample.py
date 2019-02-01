import numpy as np
from scipy import sparse
from gbssl import LGC,HMN,PARW,MAD,OMNIProp,CAMLP

G = sparse.lil_matrix((5,5))
G[0,1]=1
G[1,0]=1
G[1,2]=1
G[2,1]=1
G[2,3]=1
G[3,2]=1
G[2,0]=1
G[0,2]=1
G[3,4]=1
G[4,3]=1
G.tocsr()

## sources is going to be from infosieve
compressed = "dummys/dummy_compressed.csv"
sources = numpy.loadtxt(open(compressed, "rb"), delimiter=",", skiprows=1)

#shape=row,column????
p_corr_mtx = np.empty(shape=(len(sources), len(sources)))
s_corr_mtx = np.empty(shape=(len(sources), len(sources)))
for i, src_a in enumerate(sources):
    for j, src_b in enumerate(sources):
        p_corr_mtx[i][j] = stats.pearsonr(sources[src_a], sources[src_b])[0]
        s_corr_mtx[i][j] = stats.spearmanr(sources[src_a], sources[src_b])[0]

#lgc = LGC(graph=G,alpha=0.50)
#hmn = HMN(graph=G)
#parw = PARW(graph=G,lamb=10)
#mad = MAD(graph=G)
#omni = OMNIProp(graph=G)
camlp = CAMLP(graph=G)

x = np.array([1,2,3])
y = np.array([0,0,1])

#lgc.fit(x,y)
#hmn.fit(x,y)
#parw.fit(x,y)
#mad.fit(x,y)
#omni.fit(x,y)
camlp.fit(x,y)

#print lgc.predict_proba(np.arange(5))
#print hmn.predict_proba(np.arange(5))
#print parw.predict_proba(np.arange(5))
#print mad.predict_proba(np.arange(5))
#print omni.predict_proba(np.arange(5))
print camlp.predict_proba(np.arange(5))
#save to file
