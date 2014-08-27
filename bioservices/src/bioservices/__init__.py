"""BioServices

import bioservices
u = bioservices.uniprot.UniProt()
u.search("ZAP70")

contents
----------

* uniprot
* KEGG
* and much more

see online documentation for details at http://

"""
#from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import pkg_resources
__version__ = "$Id$$, $Rev$"
try:
    version = pkg_resources.require("bioservices")[0].version
    __version__ = version
except:
    version = __version__

try:
    # This is not striclty speaking required to run and use bioservices
    # However, some functions and python notebooks included in bioservices do
    import pandas as pd
except:
    print("BioServices %s warning: pandas is not installed on your system." % version)
    print("Some features requires this library and future version of BioServices may use it.")



import settings
from settings import *

import services
from services import *

import biomodels
from biomodels import *

import chebi
from chebi import *

import geneprof
from geneprof import *

import kegg
from kegg import *

import hgnc
from hgnc import *

import rhea
from rhea import *

import xmltools
from xmltools import *

import wikipathway
from wikipathway import *

import pdb
from pdb import *

import uniprot
from uniprot import *

import unichem
from unichem import *

import wsdbfetch
from wsdbfetch import *

import unicodefix

import xmltools
from xmltools import *

import reactome
from reactome import *

import quickgo
from quickgo import *

import chembldb
from chembldb import *
import chembl
from chembl import *

import picr
from picr import *

import psicquic
from psicquic import *

import ncbiblast
from ncbiblast import *

import biogrid
from biogrid import *

import miriam
from miriam import *

import arrayexpress
from arrayexpress import *

import biomart
from biomart import *

import eutils
from eutils import *

import pathwaycommons
from pathwaycommons import *


import muscle
from muscle import *

import biodbnet
from biodbnet import *
# sub packages inside bioservices.

#import mapping
import apps
#import dev
