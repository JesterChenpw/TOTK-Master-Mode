from RESTBL.src.restbl import MergeMods
import os

def generate_restbl(version):

    MergeMods('Mods', 'C://Users//lezen//Desktop//TotK Dump//romfs', version = version)
    os.remove('ResourceSizeTable.Product.110.rsizetable')

generate_restbl(110)