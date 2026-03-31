# We are using db sample_mflix so must specify that we want to look at movies, ie db.movies
## Query 1
### We want to specify the movie came out in 1983 so, specify that it must match exactly. We also want movies longer than 200 minutes we use built in greater than: $gt. For selection we care about runtime, title, year in that order. Self explanatory. Finally we add a sort by runtime and use 1 to specify ascending.
<img width="822" height="628" alt="Screenshot 2026-03-31 at 6 01 37 PM" src="https://github.com/user-attachments/assets/1c881acf-a061-49f4-b0ad-ed53515d3c81" />

## Query 2
### We want movies after 2014 so again use $gt. We also want IMDB rating. This is embedded in the imdb document as imdb.rating, so use dot notation, putting the text in quotes. For selection we care about title, year, imdb rating. Again using dot notation to get this value. We don't sort this query by anything
<img width="777" height="431" alt="Screenshot 2026-03-31 at 6 03 26 PM" src="https://github.com/user-attachments/assets/e62c3397-844a-402f-a9a0-18b722aa61f1" />
