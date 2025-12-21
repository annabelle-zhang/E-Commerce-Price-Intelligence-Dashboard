# E-Commerce-Price-Intelligence-Dashboard
hoping to figure out some secrets about online shopping (electronics-focused)


Week 1-2: Scraping + Data Collection
- Learning requests and BeautifulSoup to scrape Best Buy, Amazon, Walmart, Target
Goals: Scrape 50-100 products daily for 2 weeks
Store in SQL/postgreSQL database

Week 3: EDA + Visualization
- Basic pandas and matplotlib work
- Going to try to do some feature engineering for the models I'm going to make later
Goals: Create visualizations/find answers to these questions
Which retailer has lowest average prices?
How often do prices change?
What's the price range for each product category?
Correlation between rating and price?
Decide on what features to engineer after preliminary data cleaning/inspection

Week 4: ML Model
- Build price prediction model that uses features of a product to determine its price (linear regression, random forest, XGBoost)
- Other predictions: price drop (binary classification, logistic regression/random forest classifier), pricing recommendation (regression to find ideal prices)
- Evaluate with RMSE/MAE/R-Squared, explain findings in business context

Week 5: A/B Testing
- Test feature engineering - does accuracy improve with engineered features?
- Test business strategy - how does my model hold up against simply pricing 5% below competitors?
- Could backtest too

Week 6: Frontend/Backend
- Flask/FastAPI backend
- Streamlit frontend
- Display predictions and insights
