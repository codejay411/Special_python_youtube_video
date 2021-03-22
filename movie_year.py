import imdb

s = imdb.IMDb()
search = s.search_movie("Titanic")
# print(search)
year = search[0]['year']
print("titanic: ",year)