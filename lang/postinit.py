from dataclasses import dataclass, field

# post_init is a feature of dataclass, NOT python syntax.
# But relevant enough to include here :-)

@dataclass()
class Worker:
    name: str
    clss: int # 1 = mgr, 2 = supt, 3 = regular, 4 = casual
    emp_id: int
    hours: []
    tot_hours: float = field(init=False)

    def __post_init__(self):
        self.tot_hours = sum(self.hours)

if __name__ == '__main__':
	w = Worker("Isal Smitee", 3, 2901981, [35, 30, 27, 35])
	print(w)

