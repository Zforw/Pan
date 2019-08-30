
#least squqre method
import pylab
def getData(fileName):
    dataFile = open(fileName,'r')
    distances = []
    masses = []
    dataFile.readline() #ignore header
    for line in dataFile:
        d,m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses,distances)

def plotData(inputFile):
    masses,distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces,distances,'bo',label = 'Measured displacements')
    pylab.title('Measured Displacements of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')

#plotData('springData.txt')
def fitData(inputFile):
    masses,distances = getData(inputFile)
    distances = pylab.array(distances)
    forces = pylab.array(masses)*9.81
    pylab.plot(forces,distances,'bo',label = 'Measured displacements')
    pylab.title('Measured Displacements of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    #find linear fit
    a,b = pylab.polyfit(forces,distances,1)
    predictedDistances = a*pylab.array(forces) + b
    k = 1.0/a
    pylab.plot(forces,predictedDistances,
               label = 'Displacements predicted by\nlinear fit,k = '
               + str(round(k,5)))
    pylab.legend(loc = 'best')
fitData('springData.txt')