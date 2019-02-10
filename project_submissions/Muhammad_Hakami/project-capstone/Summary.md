## 1- Market Prediction in FFXIV.

   - Problem Statement.
   
Final Fantasy 14 is a very famous game being the second most played Massive Multiplayer Online(MMO) game. the trading system in-game is very competitive and the currency earned thier can be sold with real world value and it has a strong weight.<br/>
The market changes by the second so i need to make a model that predict by the secound and constantly check the market.


   - Potential Audience.
   
-In-game traders who wish to gather money in game.

-The Community in-game.

-People who trades the currancy in game with real world money.


   - Goals.
   
Predict the price of an item.


   - Success Metrics.
   
R2 score and RMSE.


   - Data Source(s).
   
Website for tracking the in-game market(ffxivmb.com).


   - Overall Approach.
   
-I cleaned the data, removed outliers, and resampled it to have 49 minuates prediction for each interval.

-Then extracted information about the past of the signal(prices) to predict the future with it.

-After that i bult many models and compared the performance.


   - Basic description of models.
   
-ARIMA: this model says the future values equals the nearest past value plus the average of the nearest past values.

-Linear Regression: draws the data points of the past and current then tries to fit a line in middle of the points(best fit).

-Random Forest: tries to segment the points into tree like structure then map the points where it best fit by conditions.

-Long-short Term Memory(LSTM): this is a deep learning model essentially it creates two memories short and long memory, the long memory keeps the important even far in past information, while the short memory keeps the most important not to far in past information, then based on the long and short memories the model make a decision in what to predict.


   -Findings.

-I found out the prediction of 49 minuates is not hard to predict essenitaly since the data deosn't change much in between.

-So making an auto trading bot using Reinforcment Learning is the most effective method which i included in future work.


   -Risks/Limitations.
   
-I resampled my data to have the interval i want, but it doesn't mean that people will buy every interval, the players may buy many time in a single secound while may take secounds in other time and maybe minuates to buy, so while i predicted the prices and it has effect in how active people are i didn't predict how active or when people are most active which can be good to include in my buying habits.
   
-My models can predict 49 minuates in future so i may want to prioritise near future in prediction for that i may need to resample.


   -Impact, Next Steps, Conclusions.
   
-Impact: the model gave great results and can infact be used to increase profit.

-Next Steps: built a Reinforcement agent that auto-trade and continue learning with reward function as the time goes.

-Conclusion: The model gave great results but it has some limitations, and it can be improved giving more data. while i believe the best solution to the problem exist in Reinforcment Learning specificly Actor-Critic method.