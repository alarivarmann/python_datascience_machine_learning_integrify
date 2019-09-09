# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:10:46 2019

@author: alari
"""

import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm # Colormaps
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

sns.set_style('darkgrid')
np.random.seed(42)
#

# Plot of independent Normals


def multivariate_normal_formula(x,mu,cov): 
    d = len(mu)
    return 1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(cov))) * np.exp((-1/2)*mahalanobis_distance_squared(x,mu,cov))

def generate_surface(mean, covariance, grid_size):
    """Helper function to generate density surface."""
    x2s = x1s = np.linspace(-5, 5, num=grid_size)
    x1, x2 = np.meshgrid(x1s, x2s) # Generate grid
    pdf = np.zeros((grid_size, grid_size))
    
    # 2D-gaussian PDF matrix
    for i in range(grid_size):
        for j in range(grid_size):
            pdf[i,j] = multivariate_normal_formula(
                x = np.matrix([[x1[i,j]], [x2[i,j]]]), 
                 mu = mean, cov = covariance)
    return x1, x2, pdf  # x1, x2, pdf(x1,x2)
  
def mahalanobis_distance_squared(x,mu,cov):
    """https://stackoverflow.com/questions/31256252/why-does-numpy-linalg-solve-offer-more-precise-matrix-inversions-than-numpy-li"""
    x_centered = x - mu
    return np.linalg.solve(cov, x_centered).T.dot(x_centered)


def plot_gaussian(cov, mean, ax=None,**kwargs):
    # subplot
    ax = ax or plt.gca()
    label = kwargs.get('label')
    x1, x2, p = generate_surface(
        mean = bivariate_mean, covariance = cov, grid_size = 50)
    # Plot bivariate distribution
    contour_data = ax.contourf(x1, x2, p, 100, cmap=cm.YlGnBu)
    ax.set_xlabel('$x_1$', fontsize=13)
    ax.set_ylabel('$x_2$', fontsize=13)
    ax.axis([-2.5, 2.5, -2.5, 2.5])
    ax.set_aspect('equal')
    ax.set_title(f'{label} variables', fontsize=12)
    return contour_data
    

def finalize_plot(fig,contour_data,supertitle = 'Bivariate normal distributions'):
  # Add colorbar and title
  fig.subplots_adjust(right=0.8)
  cbar_ax = fig.add_axes([0.85, 0.15, 0.02, 0.7])
  cbar = fig.colorbar(contour_data, cax=cbar_ax)
  cbar.ax.set_ylabel('$p(x_1, x_2)$', fontsize=13)
  plt.suptitle(supertitle, fontsize=13, y=0.95)
  


if __name__ == "__main__":
    bivariate_mean = np.matrix([[0.], [0.]])  # Mean
    bivariate_covariance_independent = np.matrix([
        [1., 0.], 
        [0., 1.]])  
    bivariate_covariance_dependent = np.matrix([
        [1., 0.7], 
        [0.7, 1.]])  

    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8,4))
    _ = plot_gaussian(ax = ax1, label="Independent" , mean = bivariate_mean, cov=bivariate_covariance_independent , color='blue',grid_size = 100)
    contour_data = plot_gaussian(ax = ax2, cov=bivariate_covariance_dependent, label="Correlated", color='blue',grid_size = 100)
    finalize_plot(fig,contour_data)
    plt.show()