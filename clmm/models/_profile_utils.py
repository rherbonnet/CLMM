'''profile utilities including sigma crit functionality and get cosmology function'''

import astropy.cosmology as apycosmo
from astropy import constants
import numpy as np


class sigma_crit():
    """
    This calculates a sigma crit for a given cosmology, mass definition, source and lens redshifts.
    
    Attributes
    ----------

    z_lens : float
        Redshift of the lensing object

    z_source : 

    mass_definition : str
        Definition of mass, e.g. 'm200c'
 
    cosmology : str
        Label of cosmology

    """
    

    def __init__(self, z_lens, z_source, mass_definition, cosmology) :

        """ 
        Parameters
        ----------

        z_lens : float
            Redshift of the lensing object

        z_source : 

        mass_definition : str
            Definition of mass, e.g. 'm200c'

        cosmology : str
            Label of cosmology

        Methods
        -------

        calculate_sigma_crit

        beta_function

        beta_discrete_mean
        
        beta_square_discrete_mean


        """ 
        self.cosmology = _get_cosmology( cosmology ) 

    def calculate_sigma_crit(self) :
        
        return constants.c.to('Mpc/s') * constants.c.to('Mpc/s') / \
            (4. * np.pi *  constants.G.to('Mpc3 / (Msun  s2)') * \
             self.cosmo.angular_diameter_distance(self.z_lens) * self.beta_function(z_source) )



    def beta_function(self, z_source) :
        
        return self.angular_diameter_distnce_two_objects(z_lens, z_source, cosmology) / self.cosmo.angular_diameter_distance( self.z_source )

        pass

    def beta_discrete_mean(self, z_source ) :
        """
        Arithmetic mean for discrete lensing efficiency <beta> for given source redshift or redshifts
        
        Parameters
        ----------

        z_source : float or array-like of floats
            Source redshift or redshifts
        
        """

        if np.iterable(z_source) and all(isinstance(z_s, float) for z_s in z_source) :
            return np.mean(self.beta_function(z_source))

        elif isinstance(z_source, float) :
            return self.beta_function(z_source)

        else :
            raise TypeError("z_source must be float or array-like of floats ")
            


    def beta_square_discrete_mean( z_source ) :
        """
        Mean of the square of the discrete lensing efficiency <beta^2>
        
        Parameters
        ----------

        z_source : float or array-like of floats
            Source redshift or redshifts

        """

        if np.iterable(z_source) and all(isinstance(z_s, float) for z_s in z_source) :
            return np.mean(self.beta_function(z_source*z_source))

        elif isinstance(z_source, float) :
            return self.beta_function(z_source*z_source)

        else :
            raise TypeError("z_source must be float or array-like of floats ")
            



def _angular_diameter_distance_two_objects(z_lens, z_source, cosmology) :
    """
    Hogg+00 Eqn (19)

    """
    hubble_radius= constants.c.to('Mpc/s')/cosmo.H(0).to.('/s')                      
    ang_diameter_lens = self.cosmo.angular_diameter_distance(self.z_lens)
    ang_diameter_source = self.cosmo.angular_diameter_distance(self.z_source)
    return (ang_diameter_source*np.sqrt(1.+ ang_diameter_lens**2/hubble_radius**2) \
            - ang_diameter_lens*np.sqrt(1.+ ang_diameter_source**2/hubble_radius**2))/(1.+z_source)
    


def _get_cosmology( cosmology ) :
    """
    Currently only can parse for astropy cosmology options
    
    cosmology : str
        Label of cosmology


    """

    pass

    