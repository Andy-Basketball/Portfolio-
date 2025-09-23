# Import necessary libraries
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.io import fits
import matplotlib.pyplot as plt
import zipfile
import os
from astroquery.exceptions import InvalidQueryError

# Define coordinates for Alpha Centauri (RA ~14h 39m 36s, Dec ~-60° 50' 02")
coord = SkyCoord(ra=219.9*u.deg, dec=-60.8339*u.deg, frame='icrs')

# Specify Sector 3 and size (100x100 pixels)
try:
    dataproducts = Tesscut.get_cutouts(coordinates=coord, sector=3, size=100)
except InvalidQueryError as e:
    print(f"Error querying MAST: {e}")
    exit(1)

# Check if data was retrieved
if dataproducts:
    zip_path = dataproducts[0]  # First ZIP file (usually one per sector/camera)
    print(f"Downloaded: {zip_path}")
    
    # Extract the ZIP file
    extract_dir = 'tess_cutout_sector3'
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_dir)
    
    # Find and open the first FITS file
    fits_files = [f for f in os.listdir(extract_dir) if f.endswith('.fits')]
    if fits_files:
        fits_path = os.path.join(extract_dir, fits_files[0])
        with fits.open(fits_path) as hdul:
            # Image data is in the first extension (index 1), first time step (index 0)
            image_data = hdul[1].data[0]  # Shape: (height, width)
            header = hdul[1].header
        
        # Plot the image
        plt.figure(figsize=(8, 8))
        plt.imshow(image_data, cmap='gray', origin='lower', norm='linear')
        plt.colorbar(label='Flux (e-/s)')
        plt.title(f'TESS Sector 3 FFI Cutout: Alpha Centauri\n{header.get("OBJECT", "Unknown")} - Exposure: {header.get("TEXP", "N/A")} s')
        plt.xlabel('Pixel Column')
        plt.ylabel('Pixel Row')
        plt.show()
        
        # Print header info for debugging
        print(f"Target: {header.get('OBJECT', 'Unknown')}")
        print(f"RA/Dec: {header.get('RA_TARG', 'N/A')}, {header.get('DEC_TARG', 'N/A')}")
    else:
        print("No FITS files found in the extracted directory.")
else:
    print("No data products found for Sector 3.")