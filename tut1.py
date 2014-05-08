class cc:
    def __init__(self,r=0,c=0):
        self.r=r
        self.i=c
    def copy(self):
        return cc(self.r,self.i)

    def __add__(self,val):
        ans=self.copy()
        if isinstance(val,cc):
            ans.r=ans.r+val.r
            ans.c=ans.i+val.i
        else:
            ans.r=ans.r+val
        return ans
    def __mul__(self,val):
        ans=self.copy()
        if isinstance(val,cc):
            ans.r=self.r*val.r-self.i*val.i
            ans.i=self.r*val.i+self.i*val.r
        else:
            ans.r=ans.r*val
            ans.i=ans.i*val
        return ans
    def __sub__(self,val):
        ans=self.copy()
        if isinstance(val,cc):
            ans.r=ans.r+val.r
            ans.c=ans.i-val.i
        else:
            ans.r=ans.r-val
        return ans

    def __div__(self,val):

        if isinstance(val,cc):
            val=val.copy()
            val.i=-1*val.i
            ans=self*val
            myabs=val.r**2+val.i**2
            ans=ans*(1.0/myabs)
        else:
            ans=self*(1.0/val)
        return ans
        
    def __repr__(self):
        if (self.i<0):
            return repr(self.r)+' - '+repr(-1*self.i) +'i'
        else:
            return repr(self.r)+' + '+repr(self.i) +'i'
    def __lshift__(self,crud):
        self.i=-1*self.i

        

