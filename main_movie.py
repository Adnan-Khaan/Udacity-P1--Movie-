import monty_python
import movie


'''Initialing the objects and assigning the values'''
madmax = movie.Movie(
    'Mad Max Fury Road',
    "In a stark desert landscape where humanity is broken, two rebels\
     just might be able to restore order",
    'http://ecx.images-amazon.com/images/I/91xy4RlK98L._SL1425_.jpg',
    'https://www.youtube.com/watch?v=hEJnMQG9ev8',
    5,
    ' Tom Hardy, Charlize Theron, Nicholas Hoult',
    '15 May 2015',
    )
'''Initialing the objects and assigning the values'''
inception = movie.Movie(
    'Inception',
    'A thief who steals corporate secrets through use of \
    dream-sharing technology is given the inverse task of\
     planting an idea into the mind of a CEO.',
    'http://www.hdwallpapers.in/walls/2010_inception_movie-wide.jpg',
    'https://www.youtube.com/watch?v=66TuSJo4dZM',
    5,
    ' Leonardo DiCaprio, Joseph.',
    '10 June 2010',
    )
'''Initialing the objects and assigning the values'''
bourn_identity = movie.Movie(
    'Bourne Identity',
    'A man is picked up by a fishing boat, bullet-riddled and \
    suffering from amnesia, before racing to elude assassins \
     and regain his memory.',
    'http://img.soundtrackcollector.com/cd/large/Bourne_Identity_VSD6367.jpg',
    'https://www.youtube.com/watch?v=F8-deZCXEig',
    4,
    ' Franka Potente, Matt Damon',
    '15 September 2002',
    )
'''Initialing the objects and assigning the values'''
beautiful_mind = movie.Movie(
    'Beautiful Mind ',
    'After a brilliant but asocial mathematician accepts secret \
    work in cryptography, his life takes a turn for the nightmarish.',
    'http://goo.gl/wZDMSz',
    'https://www.youtube.com/watch?v=2d_dtTZQyUM',
    4,
    'Russell Crowe, Ed Harris, Jennifer Connelly',
    '4 June 2001',
    )
'''Initialing the objects and assigning the values'''
avengers = movie.Movie(
    'The Avengers',
    "Earth's mightiest heroes must come together and learn to\
    fight as a team, to defeat Loki .",
    'http://media.comicbook.com/wp-content/uploads/2013/06/avengers.jpg',
    'https://www.youtube.com/watch?v=JAUoeqvedMo',
    3,
    ' Robert Downey Jr., Chris Evans, Scarlett Johansson',
    '24 May 2012',
    )
iron_man = movie.Movie(
    'Iron man',
    'After being held captive in an Afghan cave, an industrialist\
     creates a unique weaponized suit of armor to fight evil.',
    'http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
    'https://www.youtube.com/watch?v=uy6zdEbxjuU',
    4, ' Robert Downey Jr., Gwyneth Paltrow', '12 July 2008',
     )
'''Initialing the objects and assigning the values'''
batman = movie.Movie(
    'Bat-man',
    'Eight years after the Joker s reign of anarchy, the Dark\
     Knight is forced to return from his imposed exile to save Gotham City. ',
    'http://www.wired.com/images_blogs/underwire/2012/07/TDK_P3_1280.jpg', 
    'https://www.youtube.com/watch?v=GokKUqLcvD8',
    4,
    'Christian Bale, Tom Hardy ',
    '05 June 2012',
     )
'''Initialing the objects and assigning the values'''
departed = movie.Movie(
    'The Departed',
    'An undercover cop and a mole in the police attempt to identify\
     each other while infiltrating an Irish gang in South Boston.',
    'http://www.thedeparted.net/images/the_departed_poster.jpg',
    'https://www.youtube.com/watch?v=RqWJho4zSFc',
    4,
    'Leonardo DiCaprio, Matt Damon, Jack Nicholson',
    '03 September 2006',
    )
'''Creating an Array and assigning the values'''  
movies = [
    madmax,
    bourn_identity,
    iron_man,
    departed,
    avengers,
    beautiful_mind,
    batman,
    inception,
    ]
'''Call a method of class monty_python'''    
monty_python.open_movies_page(movies)
