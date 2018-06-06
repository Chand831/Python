import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to his life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQc4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar", "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
mahanati = media.Movie("Mahanati",
                       "The life story of South Indian actress Mahanati Savitri.", 
                       "https://upload.wikimedia.org/wikipedia/en/1/1d/Mahanati_poster.jpg", 
                       "https://www.youtube.com/watch?v=OrnYMmWBuV4")
#mahanati.show_trailer()

bharath_ane_nenu = media.Movie("Bharath Ane Nenu",
                               "To make good on a promise he made to his mother, a university graduate returns to India and becomes disillusioned by the government corruption he encounters.",
                               "https://www.behindwoods.com/telugu-movies/bharat-ane-nenu/stills-photos-pictures/bharat-ane-nenu-stills-photos-pictures-33.jpg",
                               "https://www.youtube.com/watch?v=KMWS5y2gZ6E")

bahubali = media.Movie("Bahubali-The Beginning",
                       "In the kingdom of Mahishmati, while pursuing his love, Shivudu learns about the conflict ridden past of his family and his legacy. He must now prepare himself to face his newfound arch-enemy.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=3NQRhE772b0")
bahubali2 = media.Movie("Bahubali-The Conclusion",
                        "When Bhallaladeva conspires against his brother to become the king of Mahishmati, he has him killed by Katappa and imprisons his wife. Years later, his brother's son returns to avenge his father's death.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                        "https://www.youtube.com/watch?v=qD-6d8Wo3do")
janatha_garage = media.Movie("Janatha Garage",
                             "Sathyam learns about the rape and murder of his friend's daughter at the hands of local hooligans. When the police fail to take action, Sathyam and his garage workers decide to punish the culprits.",
                             "https://upload.wikimedia.org/wikipedia/en/2/2c/Janatha_Garage_poster.jpg",
                             "https://www.youtube.com/watch?v=7O4Hm070Bc8")

#janatha_garage.show_trailer()

movies = [toy_story, avatar, mahanati, bharath_ane_nenu, bahubali, bahubali2, janatha_garage]
fresh_tomatoes.open_movies_page(movies)
