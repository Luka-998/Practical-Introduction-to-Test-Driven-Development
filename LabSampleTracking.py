
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
        if self.amount <= 0:
            raise ValueError('Volume must be > 0!')
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
        if self._volume -amount_ml >0:
            self._volume -=amount_ml
            return self._volume
        else:
            print(f"Volume can't be {self._volume - amount_ml}")
            raise ValueError("Volume is 0!")


class DNASample(Sample):
    def __init__(self,sample_id,concetration,status):
        super().__init__(sample_id,status)
        update_status = super().update_status()
        self.concetration = concetration
        assert self.concetration > 0, "Concetration must be > 0!"


sample1=Sample(1,12.2,'collected')
print(sample1)
dna1 = DNASample(2,14.2,'supported')