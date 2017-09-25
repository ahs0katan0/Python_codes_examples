
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
   
    
    #STEP 1 convert scores to numbers
    def convert_to_numeric(score):
        score = float(score)
        print (score)
        return (score) 

    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)
    print (score1,score2, score3,score4, score5)
        
    
    #STEP 2 and STEP 3 find the average of the middle three scores
    def sum_of_middle_three(score1, score2, score3, score4, score5):
        min_score = min(score1, score2, score3, score4, score5)
        max_score = max(score1, score2, score3, score4, score5)
        sum_middle_three = ((score1 + score2 + score3 + score4 + score5) - min_score - max_score)
        print (float(sum_middle_three))
        return (float(sum_middle_three))
    
    sum_middle_three = sum_of_middle_three(score1, score2, score3, score4, score5)
    print ("sum_middle_three = ", sum_middle_three)
        
    
    average_score = sum_middle_three / 3
    print ("average_score = ", average_score)
    
    
    #STEP 4 turn average score into a rating
    
    def score_to_rating_string(average_score):
        average_score = float(average_score)
        score_rating = None
        if average_score >= 0 and average_score < 1:
            score_rating = "Terrible"
        elif average_score >= 1 and average_score < 2:
            score_rating = "Bad"
        elif average_score >= 2 and average_score < 3:
            score_rating = "OK"
        elif average_score >= 3 and average_score < 4:
            score_rating = "Good"
        elif average_score >= 4 and average_score <= 5:
            score_rating = "Excellent"
        print (score_rating)
        return score_rating
    
    score_rating = score_to_rating_string(average_score)
    
    print ("score_rating = ", score_rating)
    return score_rating

scores_to_rating(3,4,2,1,3)