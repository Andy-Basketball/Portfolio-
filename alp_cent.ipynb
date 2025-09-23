# Import necessary libraries
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.io import fits
import matplotlib.pyplot as plt
import zipfile
import os

# Define coordinates for Alpha Centauri (RA ~14h 39m 36s, Dec ~-60° 50' 02")
coord = SkyCoord(ra=219.9*u.deg, dec=-60.8339*u.deg, frame='icrs')

# Specify Sector 3 for the cutout (you can change 'size' for larger/smaller field of view)
dataproducts = Tesscut.get_cutouts(coordinates=coord, sector='3', size=100)

# The result is a list of file paths (usually one ZIP file per camera/CCD)
if dataproducts:
    zip_path = dataproducts[0]  # First (and typically only) file for this sector
    print(f"Downloaded: {zip_path}")
    
    # Extract the ZIP file
    extract_dir = 'tess_cutout_sector3'
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_dir)
    
    # Open the first FITS file (there may be multiple for the time series)
    fits_files = [f for f in os.listdir(extract_dir) if f.endswith('.fits')]
    if fits_files:
        fits_path = os.path.join(extract_dir, fits_files[0])
        with fits.open(fits_path) as hdul:
            # The image data is in the first extension (index 1), first time step (index 0)
            image_data = hdul[1].data[0]  # Shape: (height, width)
            header = hdul[1].header
        
        # Plot the image
        plt.figure(figsize=(8, 8))
        plt.imshow(image_data, cmap='gray', origin='lower', norm='linear')
        plt.colorbar(label='Flux (e-/s)')
        plt.title(f'TESS Sector 3 FFI Cutout: Alpha Centauri\n{header["OBJECT"]} - Exposure: {header["TEXP"]} s')
        plt.xlabel('Pixel Column')
        plt.ylabel('Pixel Row')
        plt.show()
        
        # Optional: Print some header info
        print(f"Target: {header.get('OBJECT', 'Unknown')}")
        print(f"RA/Dec: {header.get('RA_TARG', 'N/A')}, {header.get('DEC_TARG', 'N/A')}")
    else:
        print("No FITS files found in the extraction.")
else:
    print("No data products found for Sector 3.")