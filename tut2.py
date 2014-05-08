import numpy
class Particles:
    def __init__(self,n=1000,G=1.0):
        self.x=numpy.random.randn(n)
        self.y=numpy.random.randn(n)
        self.m=numpy.ones(n)
        self.vx=numpy.zeros(n)
        self.vy=numpy.zeros(n)
        self.opts={}
        self.opts['n']=n
        self.opts['G']=G
    def get_potential(self):
        pot=numpy.zeros(self.opts['n'])
        for i in range(0,self.opts['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            r=numpy.sqrt(dx*dx+dy*dy)
            rinv=1.0/r
            rinv[i]=0  #make sure we don't get potential from ourself
            pot[i]=self.m[i]+numpy.sum(self.opts['G']*self.m[i]*self.m*rinv)
        return pot

if __name__=='__main__':
    part=Particles()
    pot=part.get_potential()
