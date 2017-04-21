import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

colors = plt.cm.Dark2

def scatter2d_grouped(x, g):
    n_groups = len(np.unique(g))
    
    for i in range(n_groups):
        plt.scatter(x[g==i, 0], x[g==i, 1], 
                    color = colors(1.*i/n_groups),
                    label = "{}".format(i))
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

class kmeans(object):
    
    def __init__(self, data, k, centers=None, max_iterations=1000, verbose=False):
        self.k = k
        self.data = data
        self.iterations = 0
        self.converged = False
        self.max_iterations = max_iterations
        self.verbose = verbose
        
        if  centers is not None:
            self.centers = centers
        else:
            self.centers = self._init_random_centers()
        self.clusters = -np.ones(data.shape[0])
        self._update_dist()
        
    def _init_random_centers(self):
        """
        Returns k centers by choosing random data points
        """
        nrows = self.data.shape[0]
        randomRows = np.random.choice(nrows, size = self.k, replace = False)
        return self.data[randomRows]
    
    def _update_dist(self):
        """
        Calculates square distances from individual points to centers
        and stores the values in a matrix.
        
        Rows index the points while columns index the centers
        """
        self.dist = np.sum((self.data[:, np.newaxis] - self.centers)**2, axis=2)
        
    def _update_clusters(self):
        """
        Updates cluster assignments using distances.  Ties are broken randomly
        """
        def find_min_center(dists):
            minimizing_clusters = np.where(dists == np.min(dists))[0]
            if len(minimizing_clusters) == 1:
                return(minimizing_clusters)
            else:
                return np.random.choice(minimizing_clusters, size=1)
        
        self.clusters = np.apply_along_axis(find_min_center, 1, self.dist).ravel()
    
    def _update_centers(self):
        """
        Updates the centers by finding the means within clusters
        """
        self.centers = np.array([
            self.data[self.clusters == c].mean(axis=0)
            for c in  range(self.k)
        ])
        self._update_dist()
    
    def _update_sse(self):
        """
        Calculates the within-cluster sum of squares 
        """
        self.css = np.array([
            self.dist[self.clusters == c, c].sum()
            for c in  range(self.k)
        ])
        self.wss = self.css.sum()
    
    def show_sse(self):
        self._update_sse()
        print("Cluster Sum of Squares:")
        for c in range(self.k):
            print("Cluster {}: {}".format(c, self.css[c]))
        print("Total Cluster Sum of Squares: {}".format(self.wss))
        print("\n")
        
    def show_clusters(self):
        print("Assignments:")
        for c in range(self.k):
            members = np.where(self.clusters == c)[0]
            print("Cluster {}: {}".format(c, members))
        print("\n")
    
    def show_centers(self):
        print("Centers:")
        for c in range(self.k):
            print("Cluster {}: {}".format(c, self.centers[c]))
        print("\n")
    
    def summary(self):
        print("Current Iteration: {}".format(self.iterations))
        self.show_clusters()
        self.show_centers()
        self.show_sse()
    
    def plot(self, colored=True):
        if colored:
            scatter2d_grouped(self.data, self.clusters)
        else:
            plt.scatter(self.data[:,0], self.data[:,1],
                        color = colors(.5))
        plt.scatter(self.centers[:,0], self.centers[:,1], 
                    color = 'black', marker = 'x', s = 200)
        
    def step(self):     
        old_clusters = self.clusters.copy()
        
        self._update_clusters()
        self._update_centers()
        
        self.converged = np.all(old_clusters == self.clusters) 
        
        self.iterations += 1
        if self.verbose:
            self.summary()
            
    def run(self):
        if self.converged:
            print("Algorithm converged after {} iterations"
                  .format(self.iterations))
        elif self.iterations == self.max_iterations:
            print("Maximum number of iterations ({}) reached before convergence"
                  .format(self.max_iterations))
        else:
            self.step()
            self.run()
    

        
    