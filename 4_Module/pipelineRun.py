class PipeObj():
    def __init__(self,start,exit_code,end=None):
        self.start=start
        self.end = end
        self.exit_code = exit_code
        possible_types = (int,float,None)
        possible_exits = [0,1,2]

        if not isinstance(self.start,(int,float)):
            raise TypeError

        if self.end != None:
            if not isinstance(self.end,(int,float)):
                raise TypeError
            if self.start>self.end:
                raise ValueError
        if self.end is None:
            self.status = 'RUNNING'
        if not isinstance(self.exit_code,int):
            raise TypeError
        if self.exit_code not in possible_exits:
            raise ValueError 
        if self.exit_code == 0 and self.end:
            self.status = 'DONE' 

        if self.exit_code == 1 or self.exit_code == 2:
            self.status = 'FAILED'



    def pipeline_duration(self):
        if self.status == 'RUNNING':
            return 'Pipeline is still running!'

        if self.end != None:
            if self.start == self.end:
                return 0
            return self.end - self.start

    def pipeline_run_summary(self):
        results = {
            'duration':self.pipeline_duration(),
            'is_success':self.status
        }
        return results

if __name__=='__main__':
    p = PipeObj(1,1,None)
    print(p.status)
    print(p.pipeline_duration())
    print(p.pipeline_run_summary())