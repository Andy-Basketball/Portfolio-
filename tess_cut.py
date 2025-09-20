import lightkurve as lk
import matplotlib.pyplot as plt

# Use a valid TIC ID
search_result = lk.search_tesscut('TIC 261868510')

# Or a common name for a star
# search_result = lk.search_tesscut('WASP-18')

# Check the search results before downloading
if search_result:
    tpfs = search_result.download_all()
    # Now you can loop through tpfs
    for tpf in tpfs:
        sector = tpf.sector
        tpf.plot(title=f"TESS Sector {sector}")
        plt.show()
else:
    print("No TESS data found for the specified target. Please check the name or ID.
