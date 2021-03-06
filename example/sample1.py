from IMDBAPI import IMDB
#import IMDB
def main():
	while 1:
		imdb = IMDB()
		
		#print("Movie Rated: "+imdb.getRating("dark night rises")+" out Of 10") #get ratings for "The Dark night rises"
		#print("Movie Rated: "+imdb.getRatingByImdbId("tt1345836")+" out Of 10") #get ratings for "The Dark night rises" using its IMDB ID
		
		movie = input("Enter a movie: ").strip();
		if movie:
			
			print("Movie Rated: "+imdb.getRating(movie)+" out Of 10")
			#print("Movie Rated: "+imdb.getRatingByImdbId(movie)+" out Of 10")
			
			print("Summary: "+ imdb.getSummary(movie))
			#print("Summary: "+ imdb.getSummaryByImdbId(movie))
			
			print("Director: "+ imdb.getDirector(movie))
			#print("Director: "+ imdb.getDirectorByImdbId(movie))
			
			castList = imdb.getCasting(movie) # default no cast returned will be 10
			#castList = imdb.getCasting(movie, length=20) # setting the length of cast list to 20 to get top 20 peopeple in the cast
			#castList = imdb.getCasting(movie, all=True) #print all of the cast List
			
			#castList = imdb.getCastingByImdbId(movie, all=True) #print all of the cast List
			
			print("Cast_list size: "+str(len(castList)))
			for cast in castList:
				print(cast)
			
			print("Movie Details: ")
			print(imdb.getMovie(movie))
			#print(imdb.getMovieByImdbId(movie))
		else:
			print("enter a valid movie name")
main()