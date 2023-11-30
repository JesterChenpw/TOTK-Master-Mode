from RESTBL.src.restbl import MergeMods
import os

def generate_restbl(version):

    MergeMods('Mods', 'C://Users//lezen//Desktop//TotK Dump//romfs', version = version, smart_analysis = False, checksum = True)
    os.remove(f'ResourceSizeTable.Product.{version}.rsizetable')

generate_restbl(110)