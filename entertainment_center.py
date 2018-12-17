import fresh_tomatoes
import media

#Create singular movie options

Good_Will_Hunting = media.movie("Good Will Hunting",
                        "A story of a misguided mathematical genius",
                        "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
                        "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

Vicky_Cristina_Barcelona = media.movie("Vicky Cristina Barcelona",
                        "A story about love and adventure in Barcelona",
                        "https://upload.wikimedia.org/wikipedia/en/0/05/Vicky_Cristina_Barcelona_film_poster.png",
                        "https://www.youtube.com/watch?v=B-RdUcXAKiw")
Midnight_in_Paris = media.movie("Midnight in Paris",
                        "A fantastical story about traveling back in time",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=BYRWfS2s2v4")

Hitch = media.movie("Hitch",
                        "A romcom about a dating consultant",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Hitch_poster.JPG",
                        "https://www.youtube.com/watch?v=pYrrEUgnT6s")

Billy_Madison = media.movie("Billy Madison",
                        "A story of a childish heir to a hotel fortune",
                        "https://upload.wikimedia.org/wikipedia/en/0/07/Billy_madison_poster.jpg",
                        "https://www.youtube.com/watch?v=sm0OV5xOjN8")



#group into a list.

movies = [Good_Will_Hunting, Vicky_Cristina_Barcelona, Midnight_in_Paris, Hitch, Billy_Madison]

#call function from fresh_tomatoes

fresh_tomatoes.open_movies_page(movies)
