# Holiday Plans
### Get me out of here!

Cass has just finished school for the year, and is ready to take a break and relax somewhere. Anywhere. But maybe not at school. In fact, it would probably be best to be as far away from school as possible. As far away from *ANY* school as possible.

Where would Cass have to go in Australia to be as far away as possible from any school? How would you help her find out where that is?

#### Looking for information

First we need to know just where in Australia every school is, and for that we're going to need some data. Data comes in all shapes and sizes, and from all kinds of places, so actually finding the data can be tricky as well. Luckily, lots of people have built search engines to help us find all sorts of data.

One spot we can look for data is Google's dataset search tool, at [https://toolbox.google.com/datasetsearch](https://toolbox.google.com/datasetsearch)

The Australian Government has also built a search tool for data, at [https://search.data.gov.au/](https://search.data.gov.au/)

Cass lives in Sydney, so she decided to look for data about NSW schools first. She searched the search.data.gov.au site for "nsw school locations" and found some data from 2016 called "NSW government school locations and enrolment". Can you find it?


#### Understanding the data
This data is stored in a .csv file, which stands for comma separated values. The data is stored in a table format where each row of the table represents a school and each column is a piece of information about that school. Each piece of data is separated by a comma, which is where the name comes from, and each row is put on a new line.

Lot's of different programs can be used for looking at this kind of data. Try opening the file in a text editor, and in excel to see what it looks like.

It's for Cass to work out where she should go for her holiday just by looking at the table. Each school's address is listed in the table, so she can look them up on a map very easily. What she needs, however, is a way to look them all up at the same time.

#### Map Pins
In order to find her holiday destination, Cass took this list of schools and a big map of NSW, and started sticking pins into it for each one of the schools. Next she was going to draw circles around each school ruling out any places that were close to a school. By drawing bigger and bigger and bigger circles she would eventually find out the part of NSW farthest from any school.

As she started putting the pins into place she checked the list and saw that there are over 2000 different schools in NSW, so drawing those circles one by one would take a very long time.

Luckily, she had just learnt an easier way!

She could get the computer to draw the circles on a map for her, and the computer could do it a lot faster than she would ever be able to. All she needs is the data set she downloaded, a map, and a way to tell the computer how to draw the circles.


#### Drawing on a Map
We're going to use a computer programming language called python to tell the computer how to draw our map. Luckily, lots of other people have wanted to draw maps in the past, so most of the work to do this is already done for us.

Computers are really good at following instructions, and really fast, but we have to tell them exactly what to do in each step. So let's think about the process we would use.

First, we have to get the location of each school. We have this in our data file, so we can open the file and go through line by line looking at the address. In fact, in order to draw a point on a map we actually need the latitude and longitude of school, which happens to be in this data set too.

We then have to have a map, and draw a circle on the map for each school.

Once we have the map, we need to save it to a file we can look at.
```
from gmplot import gmplot
gmap = gmplot.GoogleMapPlotter.from_geocode("New South Wales")
gmap.draw("my_map.html")
```
