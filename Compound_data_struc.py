
Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
    
def most_prolific(dictionary_of_album_releaseyear):
    #function most_prolific counts the year in which the most album releases
    #returns year with max album releases
        
    #create dict with year as key and freq of year as value
    album_year_counts = {}
    
    # creates a var holding the maximum value (count) and which key (year) it is associated with
    max_count = 0
    max_year = 0
    
    # a single for loop starts with creating dictionary album_year_counts
    for album in dictionary_of_album_releaseyear:
        year = dictionary_of_album_releaseyear[album]
        
    #a series of if conditions go through orig. dict input for the function
    # updating the dictionary of album_year_counts
        if dictionary_of_album_releaseyear[album] in album_year_counts:
            album_year_counts[year] += 1
        else:
            album_year_counts[year] = 1
    
    # if loop that tracks which year(s) has max_count
        if album_year_counts[year] > max_count:
            max_count += 1
            max_year = [year]
        elif album_year_counts[year] == max_count:
            max_year.append(year)
    
    print ("Dictionary: {}, Max-year; {}, Max-count; {}".format(album_year_counts, max_year, max_count))
    
    # if loop to provide one year if single year otherwise provides a list of years
    if len(max_year) > 1:
        return max_year
    else:
        return max_year[0]


most_prolific(Beatles_Discography)



