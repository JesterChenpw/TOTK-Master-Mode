from RESTBL.src.restbl import MergeMods
import os

def generate_restbl(version):

    MergeMods('Mods/' + str(version), 'C://Users//lezen//Desktop//TotK Dump//' + str(version) + '//romfs', version = version, smart_analysis = False, checksum = True)
    os.remove(f'ResourceSizeTable.Product.{version}.rsizetable')

generate_restbl(110)