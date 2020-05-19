{"movie_id" : 
{"movie_name" : "", 
"star_cast" : [],
"rating" : }
}

#top 25 movies by rating
rdd = sc.textfile()
rdd.flatmap(lambda movie: (movie.movie_name, movie.rating)).sortbyvalues(lambda x:x[1]).top(10).collect()



