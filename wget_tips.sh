wget (multi purpose download tool)
(cd dir/ && wget -nd -pHEKk http://www.pixel.org/line.html)	
# Store local browsable version of a page to the current dir

wget -c http://www.example.com/large.file			
# Continue downloading a partially downloaded file

wget -r -nd -np -l1 -A '*.jpg' http://www.example.com/dir/	
# Download a set of files to the current directory

echo 'wget url' | at 01:00
# Download url at 1AM to current dir

wget --limit-rate=20k url					
# Do a low priority download (limit to 20KB/s in this case)

wget -nv --spider --force-html -i bookmarks.html
# Check links in a file

wget --mirror http://www.example.com/	
# Efficiently update a local copy of a site (handy from cron)