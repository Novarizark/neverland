import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

class _sapiens:
    
    def __init__(self, gender):
        self.gender=gender
        self.age=20
        self.single=True

    def try_match(self):
        pass

class _adam(_sapiens):
    
    def __init__(self):
        _sapiens.__init__(self, 'adam')
        self.attract=np.random.randn()
        self.motivite=np.random.rand()

class _eve(_sapiens):
    
    def __init__(self):
        _sapiens.__init__(self, 'eve')
        
        self.attract=np.random.rand()
        self.motivite=np.random.rand()/2.0



adam_list=[]
eve_list=[]

for i in range(0,10):
    adam_list.append(_adam())
    eve_list.append(_eve())

print('Adam Score:')
for adam in adam_list:
    print(adam.attract)

print('Eve Score:')
for eve in eve_list:
    print(eve.attract)
