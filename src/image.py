from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):

        im_bin = Image()

        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        for y in range(self.H):
            for x in range(self.W):
                if self.pixels[y][x] > S :
                    im_bin.pixels[y][x] = 255
                if self.pixels[y][x] < S :
                    im_bin.pixels[y][x] = 0
                if self.pixels[y][x] == S:
                    im_bin.pixels[y][x] = 0
        
        return im_bin

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        
        im_loc = Image()
        c_min=0
        c_max=0
        l_min=0
        l_max=0
        
        im_loc.set_pixels(self.pixels)
        for y in range (self.H):
            for x in range (self.W):
                if self.pixels[y][x] == 0:
                    l_max=y+1
                    
        for x in range (self.W):  
            for y in range (self.H,):
                if self.pixels[y][x] == 0:
                    c_max=x+1
                 
        for y in range (self.H-1,0,-1):
            for x in range (self.W-1,0,-1):
                if self.pixels[y][x] == 0:
                    l_min=y
                  
        for x in range (self.W-1,0,-1):
            for y in range (self.H-1,0,-1):
                if self.pixels[y][x] == 0:
                    c_min=x
        
        im_loc.pixels=im_loc.pixels[l_min:l_max,c_min:c_max]
        return im_loc

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        
        im_res= Image()
        im_res.pixels=resize(self.pixels,(new_H,new_W),0)
        im_res.pixels=np.uint8(im_res.pixels*255)
        im_res.H= new_H
        im_res.W= new_W
        return im_res

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
       k = 0
       n = 0
       im_sim = Image()
       im_sim.set_pixels(self.pixels)
       im.set_pixels(im.pixels)
       for y in range (self.H) :
           for x in range (self.W):
               n = n+1
               if self.pixels[y][x]==im.pixels[y][x]:
                   k = k+1
       return k/n
       

