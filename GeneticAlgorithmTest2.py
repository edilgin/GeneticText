import random


class Population:
    def __init__(self, pop_size, target):
        self.target = target
        self.target_size = len(target)
        self.pop_size = pop_size
        self.population = []
        self.finished = False
        self.MatingPool = []

        for i in range(self.pop_size):
            gen = Gene(self.target_size)
            gen.randGene()
            self.population.append(gen)

    def calcFitness(self):
        for gen in self.population:
            gen.fitness = 0
            for i in range(self.target_size):
                if gen.genetic[i] == self.target[i]:
                    gen.fitness += 1
                if gen.fitness == self.target_size:
                    self.finished = True
                    print("".join(gen.genetic))
                    exit()

    def naturalSelection(self):
        sortedGenes = sorted(self.population, key=lambda Gene:Gene.fitness, reverse=True)
        best10pct = self.pop_size - int((99 * self.pop_size)/100)
        self.MatingPool = []
        for i in range(best10pct):
            self.MatingPool.append(sortedGenes[-i])
        print("".join(self.population[0].genetic))

    def mutateGene(self):
        char = random.choices([chr(32),chr(46),chr(random.randint(65,90)),chr(random.randint(96,122))], weights=[1,1,15,15])
        return char[0]

    def crossOver(self):
        self.population = []
        for i in range(self.pop_size):
            index1 = random.randint(0,len(self.MatingPool)-1)
            index2 = random.randint(0,len(self.MatingPool)-1)
            parent1 = self.MatingPool[index1]
            parent2 = self.MatingPool[index2]

            child = Gene(self.target_size)

            for i in range(self.target_size):
                randInt = random.randint(0,100)
                if randInt < 50:
                    child.genetic.append(parent1.genetic[i])
                elif randInt < 99:
                    child.genetic.append(parent2.genetic[i])
                else:
                    child.genetic.append(self.mutateGene())
            self.population.append(child)

    def main(self):
        while not self.finished:
            self.calcFitness()
            self.naturalSelection()
            self.crossOver()

class Gene:
    def __init__(self, dnaLen):
        self.dnaLen = dnaLen
        self.genetic = []
        self.fitness = 0

    def randGene(self):
        for i in range(self.dnaLen):
            char = random.choices([chr(32), chr(46), chr(random.randint(65,90)), chr(random.randint(96,122))], weights=[1,1,15,15])
            self.genetic.append(char[0])


target = "It always seems impossible until its done"
pop_size = 100

pop = Population(pop_size, target)
pop.main()