import fresh_tomatoes
import media

# Create singular movie options and eventually turn this into an array

Good_Will_Hunting = media.movie("Good Will Hunting",
                                "A story of a misguided mathematical genius",
                                "https://bit.ly/2SUOINy",
                                "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

Vicky_Cristina_Barcelona = media.movie("Vicky Cristina Barcelona",
                                       "A story about love and adventure \
                                        in Barcelona",
                                       "https://bit.ly/2SXvW8e",
                                       "https://bit.ly/2SXvW8e")
Midnight_in_Paris = media.movie("Midnight in Paris",
                                "A fantastical story about \
                                traveling back in time",
                                "https://bit.ly/1LMxGFR",
                                "https://bit.ly/1LMxGFR")

Hitch = media.movie("Hitch",
                    "A romcom about a dating consultant",
                    "https://bit.ly/2rodAiW",
                    "https://bit.ly/2rodAiW")

Billy_Madison = media.movie("Billy Madison",
                            "A story of a childish heir to a hotel fortune",
                            "https://bit.ly/2ECzAkH",
                            "https://www.youtube.com/watch?v=sm0OV5xOjN8")

# group into a list.

movies = [Good_Will_Hunting,
          Vicky_Cristina_Barcelona,
          Midnight_in_Paris,
          Hitch, Billy_Madison]

# call function
fresh_tomatoes.open_movies_page(movies)
