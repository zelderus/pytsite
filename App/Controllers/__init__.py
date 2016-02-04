#from os.path import dirname, basename, isfile
#import glob
#modules = glob.glob(dirname(__file__)+"/Controllers"+"/*.py")
#__all__ = [ "Controllers."+basename(f)[:-3] for f in modules if isfile(f)]


#import Controllers.BaseController
from Controllers.BaseController import BaseController
from Controllers.TestController import TestController