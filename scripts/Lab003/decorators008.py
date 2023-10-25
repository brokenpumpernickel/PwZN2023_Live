# class Ising:
#     def calculate_energy(self):
#         print("Calculating energy")
#         self.hamiltonian()

# def hamiltonian():
#     print("Hamiltonian")

# ising = Ising()
# ising.hamiltonian = hamiltonian
# ising.calculate_energy()

class Ising:
    def calculate_energy(self):
        print("Calculating energy")
        self._hamiltonian()
    
    def hamiltonian(self, func):
        print("Hamiltonian DECORATOR")        
        self._hamiltonian = func
        return func

ising = Ising()

@ising.hamiltonian
def hamiltonian():
    print("Hamiltonian")

ising.calculate_energy()