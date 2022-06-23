import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import os
import imageio


class KMeans:
    def __init__(self, nCluster=3, randomState=721):
        self.nCluster = nCluster
        self.randomState = randomState

    def fit(self, dataset):
        self.X = dataset.iloc[:, [0, 1]]  
        self.m = self.X.shape[0] 
        self.n = self.X.shape[1]  
        initialCentroids = self.initializeCentroids()
        self.plot_initialCentroids(initialCentroids)
        self.clustering(initialCentroids)

    def initializeCentroids(self):
        initialCentroids = []
        random.seed(self.randomState)

        for i in range(self.nCluster):
            initialCentroids.append(np.ravel(self.X.iloc[(random.randint(0, self.m - 1)), :]))

        return np.array(initialCentroids)

    def plot_initialCentroids(self, initialCentroids):

        plt.scatter(self.X.iloc[:,0], self.X.iloc[:,1], c='#000000', s=7, label='Data Points')
        plt.scatter(initialCentroids[:, 0], initialCentroids[:, 1], marker='*', s=120, c='r', label='Initial Centroids')
        plt.title('Initial Random Cluster Centers')
        plt.legend()
        plt.draw()

    def clustering(self, centroids):

        oldCentroids = np.zeros(centroids.shape)
        stoppingCriteria = 0.0001
        self.iterating_count = 0
        self.objectiveFuncValues = []

        while self.euclideanDistance(oldCentroids, centroids) > stoppingCriteria:
            clusters = np.zeros(len(self.X))
            # Assign each value to its closest cluster
            for i in range(self.m):
                distances = []
                for j in range(len(centroids)):
                    distances.append(self.euclideanDistance(self.X.iloc[i, :], centroids[j]))
                cluster = np.argmin(distances)
                clusters[i] = cluster

            # Store the old centroid values to compare centroid moves
            oldCentroids = copy.deepcopy(centroids)

            # Find the new centroids
            for i in range(self.nCluster):
                points = [self.X.iloc[j, :] for j in range(len(self.X)) if clusters[j] == i]
                centroids[i] = np.mean(points, axis=0)

            # Calculate the objective function value for the current cluster centroids
            self.objectiveFuncValues.append([self.iterating_count, self.objectiveFuncCalculate(clusters, centroids)])
            self.plotCentroids(centroids, clusters)
            self.iterating_count += 1

        self.plotObjectiveFunctionValues()


    def plotCentroids(self, centroids, clusters):
        colors = ["#0061ff", "#ff5d03", "#03ff3c", "#fc0009", "#3d03ff",
          "#937860", "#fa00b1", "#8C8C8C", "#fcc603", "#03c3fc"]
        fig, ax = plt.subplots()
        for i in range(self.nCluster):
            points = np.array([self.X.iloc[j, :] for j in range(len(self.X)) if clusters[j] == i])
            ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i], label='Cluster {}'.format(i + 1))
        ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=120, c='#000000', label='Centroids')

        plt.title('k-Means Clustering\n( Iteration count = {} Objective Function value = {:.2f} )'
                  .format((self.iterating_count + 1), np.array(self.objectiveFuncValues)[self.iterating_count, 1]))
        plt.legend()
        plt.draw()

    def euclideanDistance(self, a, b):
        return np.sqrt(np.sum((np.array(a) - np.array(b))**2))
    
    # Calculate the objective function value for the current centroids
    def objectiveFuncCalculate(self, clusters, centroids):
        
        # Calculate the objective function value
        distancesFromCentroids = []
        for i in range(self.nCluster):
            points = np.array([self.X.iloc[j, :] for j in range(len(self.X)) if clusters[j] == i])
            for k in range(len(points)):
                distancesFromCentroids.append(self.euclideanDistance(points[k, :], centroids[i]))
        return sum(distancesFromCentroids)

    # Plot graph of objective function value for each iteration 
    def plotObjectiveFunctionValues(self):
        
        plt.figure()
        plt.plot((np.array(self.objectiveFuncValues)[:, 0] + 1),  np.array(self.objectiveFuncValues)[:, 1], 'bo')
        plt.plot((np.array(self.objectiveFuncValues)[:, 0] + 1), np.array(self.objectiveFuncValues)[:, 1], 'k')
        plt.title('Objective Function')
        plt.xlabel('Iteration Number')
        plt.ylabel('Objective Function Value')
        plt.draw()

    # Save all the figures plotted with matplotlib to path directory
    def saveFigures(self, path):

        # Create folder to store the png files
        if not os.path.isdir(path):
            os.makedirs(path)

        # plt.get_fignums returns a list of existing figure numbers.
        # then save all the existing figures
        for i in plt.get_fignums():
            plt.figure(i)
            plt.savefig(os.path.join(path, "figure_{}.png".format(i)), format='png')

        # Close all figures to clear figure numbers
        plt.close("all")
        print("Figures saved in {}".format(path))

    def createGif(self,path):
        """Scan path folder, create list from file names in folder,
        sort these png file names in list, add each png file to images list
        and create animation from these png files in images list """

        # Create folder to store the gif files
        if not os.path.isdir(os.path.join(path, "animation")):
            os.makedirs(os.path.join(path, "animation"))

        pngDir = path
        images = []
        fileNames = []

        # Add each png file name in path fileNames list
        for fileName in os.listdir(pngDir):
            if fileName.endswith('.png'):
                fileNames.append(fileName)

        # Sort filenames according to last digits
        sortedFileNames = sorted(fileNames, key=lambda y: int((y.split('_')[1]).split('.')[0]))

        # Add each file in sorted filenames to images list
        for i in range(len(sortedFileNames)):
            filePath = os.path.join(pngDir, sortedFileNames[i])
            images.append(imageio.imread(filePath))

        # Remove the last png file (objective function figure) from the images list
        images.pop()

        # Save the gif file to the animation folder
        imageio.mimsave(os.path.join(path,'animation/animation.gif'), images, duration=0.5)

        print("Animation of figures saved in {} directory.".format(os.path.join(path,'animation')))