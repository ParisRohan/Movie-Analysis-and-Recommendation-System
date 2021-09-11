# Movie-Analysis-and-Recommendation-System
Performing analysis and basic recommendations based on similar genres and movies which users prefer.

1. Data Cleaning
	a. Dropped columns not required for analysis
	b. Checked percentage of missing values in each columns and dropped missing values from gross and budget because they had comparitvely high percent of missing values.
	c. Checked count of missing values column wise and dropped row with missing count < 2
	d. imputed missing values -> used mean for numerical, used mode for categorical and 'Unknown Actor' for missing actor names

2. Feature Engineering
	a. Converted gross and budget from $ to Million $
	b. calculated Profit
	
3. Found top 10 profitable movies

4. Categorized movies as English and Foreign Language because out of 3853 movies, 3673 are in english language

5. Categorized movies as Long and Short duration

6. Extracted movie genre

7. Social_Media_Popularity = num_user_for_reviews/num_voted_users * movie_facebook_likes

8. Most bankable movie genre and The Most Profitable Movie from each Genre

9. Profit and loss analysis by plotting 'Most Profitable Box Office Years', 'Time Series for Box Office Profit for English vs Foreign Movies' and 'Movies that made huge losses'

10. Gross comparison of long and short duration movies 

11. Association between IMDB Rating and movie duration 
	a. Highest Rated Long Duration Movie - The Shawshank Redemption
	b. Highest Rated Short Duration Movie - The Usual Suspects

12. Comparing critically acclaimed actors and generating report showing their carreer

13. Top movies based on gross and imdb rating using interactive widgets

14. Recommending movies based on language

15. Recommending movies based on actor

16. Recommending similar genres

17. Recommending similar movies 
