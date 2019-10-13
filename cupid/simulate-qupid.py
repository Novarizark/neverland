import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

class _sapiens:
    
    def __init__(self, id0):
        self.age=20
        self.id0 = id0
        self.single=True
    def gen_expect(self, n_sample):
        """
            generate adam/eve's lower bound of expectated lover's rank
        """
        if self.gender=='adam':
            self.exp_lowerbnd=np.random.randint(int(self.rank-0.05*n_sample),int(self.rank+0.2*n_sample))
        else:
            self.exp_lowerbnd=np.random.randint(int(self.rank-0.2*n_sample),int(self.rank+0.05*n_sample))

    def try_match(self, n_net, tgt_sort_list):
        """
            as the motivated one, now he/she will try to match the one in his/her networking circle
        """
        tgt_upperbnd=np.random.randint(int(self.rank-n_net), int(self.rank+n_net))
        
        if tgt_upperbnd < 0:
            tgt_upperbnd=0
        
        # pick the one
        tgt_num=np.random.randint(tgt_upperbnd, tgt_upperbnd+n_net)
        if tgt_num>len(tgt_sort_list)-1:
            tgt_num=len(tgt_sort_list)-1
        tgt_obj=tgt_sort_list[tgt_num]

        if (self.exp_lowerbnd>tgt_num) and (tgt_obj.exp_lowerbnd>self.rank) and (self.single) and (tgt_obj.single):
            # match done!
            self.single=False
            tgt_obj.single=False
            self.mate_id=tgt_obj.id0
            tgt_obj.mate_id=self.id0
            return 1
        return 0
class _adam(_sapiens):
    
    def __init__(self, id0):
        _sapiens.__init__(self, id0)
        
        self.gender='adam'
        self.attract=np.random.rand()
#        self.motivite=np.random.rand()

class _eve(_sapiens):
    
    def __init__(self, id0):
        _sapiens.__init__(self, id0)
        
        self.gender='eve'
        self.attract=np.random.rand()
        self.motivite=np.random.rand()/2.0


# set init paras

N_ADAM=100
N_EVE=100

# individual networking circle volumn
N_NETWORK=20

adam_dic={}
eve_dic={}

# init adam and eve
for i in range(0,N_ADAM):
    adam_dic[i]=_adam(i)
for i in range(0,N_EVE):
    eve_dic[i]=_eve(i)

# sort adam and eve by their attractive values
adam_sort_list=sorted(adam_dic.values(), key=lambda adam: adam.attract)
eve_sort_list=sorted(eve_dic.values(), key=lambda eve: eve.attract)

# allocate rank #; generate lower bound of each adam or eve's expected lover's rank
ii=0
for adam in adam_sort_list:
    adam.rank=ii
    adam.gen_expect(N_ADAM)
    ii=ii+1

ii=0
for eve in eve_sort_list:
    eve.rank=ii
    eve.gen_expect(N_EVE)
    ii=ii+1

# try to match one round, adam is motivated!
match_n=0
for ii in range(0,50):
    for adam in adam_dic.values():
        match_n=match_n+adam.try_match(N_NETWORK, eve_sort_list)
    print(match_n)
