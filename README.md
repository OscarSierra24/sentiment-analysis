# Sentiment-Analysis

This project serves to gather tweets from the most popular trending topics in twitter through the day and do sentiment analysis with them for later proper data analysis.

# Technologies used

- MongoDB hosted on [MLab](https://mlab.com/)

- Twitter API [Twitter Developer](https://developer.twitter.com/)

- Azure Cognitive Services [Azure](https://azure.microsoft.com/es-es/)

# How to use

## Get your keys for each technology and set them in an .env file

### Example
    #.env run with sh .env if python dotenv not working
    DB_USER='val1'
    DB_PASS='val2'
    CONSUMER_KEY='val3'
    CONSUMER_SECRET='val4'
    OAUTH_TOKEN='val5'
    OAUTH_TOKEN_SECRET='val6'
    AZURE_KEY='val7'


### MLab
- DB_USER
- DB_PASS

### Twitter API
- CONSUMER_KEY
- CONSUMER_SECRET
- OAUTH_TOKEN
- OAUTH_TOKEN_SECRET

### Azure
- AZURE_KEY

