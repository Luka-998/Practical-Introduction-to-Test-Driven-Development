
class Sample():
    def __init__(self,sample_id:int,volume_ml:float,status: str):
        self.sample_id = sample_id
        self._volume = volume_ml
        self.current_status = status
        self.possible_status = ['collected','archived','processing','discarded']

        if self.current_status not in self.possible_status:
            raise ValueError(f"{self.current_status} not in possible status!")

    def __repr__(self):
        return f"Sample id: {self.sample_id}, volume {self._volume} and current status: {self.current_status}"
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self,amount):
        if amount<= 0:
            raise ValueError('Volume increase must be > 0!')
        self._volume = amount

    def update_status(self,new_status):
        if new_status not in self.possible_status:
            raise ValueError(f"{new_status} not in {self.possible_status}!")
        elif self.current_status in ['archived','discarded']:
            raise ValueError(f"Can't change status of item when the item is :{self.current_status}")
        elif new_status == self.current_status:
            return self.current_status
        else:
            self.current_status = new_status

    def use_volume(self,amount_ml):
        if self._volume -amount_ml >=0:
            self._volume -=amount_ml
            return self._volume
        else:
            print(f"Volume can't be {self._volume - amount_ml}")
            raise ValueError("Volume is 0!")


class DNASample(Sample):
    def __init__(self,sample_id,volume_ml,concentration,status,type_dna):
        super().__init__(sample_id,volume_ml,status)
        self.concetration = concentration
        self.type_dna = type_dna
    def __repr__(self):
        return f"Dna sample: {self.sample_id}, volume_ml: {self._volume} concetration : {self.concetration} , status: {self.current_status} and type: {self.type_dna}"

class RNASample(Sample):
    def __init__(self,sample_id,volume_ml,concetration,status,integrity_score):
        super().__init__(sample_id,volume_ml,status)
        self.concetration = concetration
        self.integrity_score = integrity_score

    def __repr__(self):
        return f"RNA sample_id {self.sample_id}, volume: {self._volume}, concetration : {self.concetration} and ig score: {self.integrity_score}"

    @property
    def integrity_score(self):
        return self._integrity_score
    

    @integrity_score.setter
    def integrity_score(self,score):
        if 0<=score<=10 and isinstance(score,float):
            self._integrity_score = score
        else:
            raise ValueError("Score must be float type between 0-10!")
    def is_degraded(self):
        if self._integrity_score < 4:
            return True
        else:
            return False
sample1=Sample(1,12.2,'collected')
print(sample1)
print(sample1.volume)
sample1.volume = 2
print(sample1.volume)
dna1 = DNASample(2,14.2,24,'collected','human')
dna1.update_status('processing')
print(dna1)

rna1 = RNASample(1,2.2,99.1,"collected",2.0)
print(rna1)
print(rna1.is_degraded())