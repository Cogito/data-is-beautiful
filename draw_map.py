from gmplot import gmplot
import csv
gmap = gmplot.GoogleMapPlotter.from_geocode("New South Wales")
with open("nsw-public-schools-master-dataset-07032017.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["latitude"],row["longitude"])
        try:
            gmap.marker(float(row["latitude"]),float(row["longitude"]))
        except ValueError: continue
gmap.draw("my_map.html")
