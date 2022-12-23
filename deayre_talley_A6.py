from ast import Delete


movies = [[1939, 'Gone With the Wind', 'drama'],
 [1943, 'Casablanca', 'drama'],
 [1960, 'The Apartment', 'drama'],
 [1965, 'The Sound of Music', 'musical'],
 [1970, 'Patton', 'historical'],
 [1972, 'The Godfather', 'drama'],
 [1973, 'The Sting', 'comedy'],
 [1977, 'Annie Hall', 'comedy'],
 [1981, 'Chariots of Fire', 'drama'],
 [1984, 'Amadeus', 'historical'],
 [1986, 'Platoon', 'action'],
 [1990, 'Dances with Wolves', 'western'],
 [1991, 'The Silence of the Lambs', 'drama'],
 [1992, 'Unforgiven', 'western'],
 [1993, 'Schindler s List', 'historical'],
 [1994, 'Forrest Gump', 'comedy'],
 [1995, 'Braveheart', 'historical'],
 [1997, 'Titanic', 'historical'],
 [1998, 'Shakespeare in Love', 'comedy'],
 [2001, 'A Beautiful Mind','historical'],
 [2002, 'Chicago', 'musical'],
 [2009, 'The Hurt Locker', 'action'],
 [2011, 'The Artist', 'comedy'],
 [2012, 'Argo', 'historical'],
 [2013, '12 Years a Slave', 'drama'],
 [2014, 'Birdman', 'comedy'],
 [2016, 'Moonlight', 'drama'],
 [2017, 'The Shape of Water', 'fantasy'],
 [2018, 'Green Book', 'drama'] ,
 [2019, 'Parasite', 'comedy'],
 [2020, 'Nomadland', 'drama'],
 [2021, 'CODA', 'drama '] ]

md = {}

menu = """
 yr - display winning movie for a selected year
 dlist - display entire movie list - year, title, category
 cat - display movies in a selected category - year and title
 a  - add movie title and category for a selected year
 q - quit
 Select one of the menu options above
"""
while True:
    
    print(menu)
    count = 0
    menu_options = input("Choose an option from the menu above: ")
    for m in movies:
        md[m[0]] = [m[1],m[2]]

    if menu_options  != 'q':
        #displays the "yr" menu options
        if menu_options == 'yr':
            
            year = int(input('Type in a year: '))
            #gives a limit for the year during the oscars 
            if year >= 1927 and year <= 2021:
                print('\n')
                for keys, value in md.items():
                    if keys == year:
                        print(keys, value[0], value[1], sep=", ")
                        print("\n")
                    else: 
                        count += 1
                        continue
                if count == 32:
                    #Gives the user another chance at the program. 
                    print("Error!!! Not an option")
                    continue
                continue
            else:
                print("Re- enter a valid yeardlist")
                continue
            
    
            #displays the "dlist" menu options. 
        if menu_options == "dlist":
            for keys, value in md.items():
                print(keys, value[0], value[1], sep=', ')
                #prints the individual text within movies. 
            menu_options = " "
            continue
        if menu_options == 'a':
                year = int(input("Input  an integer between 1927 and 2021, inclusive: "))     
                if year in md:
                    print ('Hey there already is a movie for this year..')
                    update = input('Would you like to replace this movie y/n ?')
                    if update not in 'y':
                        continue    #  this will redisplay the menu
                title = input("Input a title less than 40 characters: ")
                category = input("Input the fallowing values: ('drama', 'western', 'historical', 'musical', 'comedy', 'action','fantasy', 'scifi': ")
                md[year]=[title, category]
                #for loop for the simular year value
                #found = False
                #for keys, value in md.items():
                    #if keys == year:
                            #print('\nHey there is already a movie like this')
                           #update = input("Would you like to replace movie year with new one, y or n?: ")
                            #if update == 'y':
                               # del md[keys, value]
                            #elif update == 'n':
                               #continue
                            
                
                #for i in sorted(md.keys()):
                    #print(i, end=" ")
                for keys, value in sorted(md.items()):
                    print(keys, value[0], value[1], sep=', ') 
                continue
            
       
        while True:
            
            
            #displays the "cat" menu options
            if menu_options == 'cat':
                category = input("Input a Category: ")
                print('\n')
                counter2 = 0
                for keys, value in md.items():
                    #prints off each individual text within movies.
                    if value[1] == category:
                        print(keys, value[0], value[1])
                        print('\n')
                    else:
                        counter2 += 1
                if counter2 != 32:
                    break
                if counter2 == 32:
                    print("Not an option on the menu. Please Try again: ")
                    continue
            continue
           
    else: 
        break
print("End of the program.\n\n Good-Bye\n\n Here is your Movie list: \n ")


print(movies)
        
        

                    
        
                    
            
