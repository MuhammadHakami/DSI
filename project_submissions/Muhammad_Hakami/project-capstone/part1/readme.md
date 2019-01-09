## 1- The hunt for exoplanets.
   - Problem Statement.
   
Exoplanets(planets not orbiting our sun) are really hard to spot using telescope due to the light of each star, but scientist can detect it by looking at the decrease in flux(light intensity) due to a planet blocking part of the flux to our point of view, so to gather data NASA launched kepler a space telescope back in 2009. 

The mission was a success and it brought back 14 billion data points with some being noisy unrealistic for a human to go through, so thats where Machine Learning can help, taking part of the data i want to use ML to find the point where a scientist can then confirm it, i will try other filtering method to handle the noise like ICA and cluster the data to find the stars with highest number of exoplanets.

If i manage to finish all that and found time, then i will proceed to see if i can classify planets as habitable or not with other features.

   - Potential Audience.
   
Astronomers looking for faster way to parse through data to find exoplanets.

   - Goals.
   
Classify if star has planet or not, then cluster to find the highest number of planets in a star.

   - Success Metrics.
   
Accuracy, Recall and f1 score.

   - Data Source(s).
   
NASA open data's database.

--

## 2- Search for dark matter hints at CERN experiment.
   - Problem Statement
   
Dark matter is considered to be one of most puzzling phenomena about space, weather it exist or not and if it does exists, is it the reason for the universe's expansion?, while these questions are interesting im clustering to search for a specific pattern not trying to answer the privous questions.

   - Potential Audience 
   
physicist, Astronomers and ML enthusiasts.

   - Goals
   
To find a spicific pattern in a 3D plot using clustering methods.

   - Success Metrics.
   
The Silhouette Coefficient.

   - Data Source(s).
   
CERN's kaggle competition.