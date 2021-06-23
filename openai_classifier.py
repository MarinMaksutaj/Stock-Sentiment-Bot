import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def make_single_request(tweet):
    result = openai.Classification.create(
        search_model="davinci",
        model="davinci",
        examples=[
            ["Great moment to buy some stock", "Positive"],
            ["Huge sell signal, warning", "Negative"],
            ["Time to buy some more stock", "Positive"],
            ["Crash is coming, sell now", "Negative"],
            ["Amazing run this week, markets seem bullish", "Positive"],
            ["We are headed into a bear market, prices are falling", "Negative"]
        ],
        query=tweet,
        labels=["Positive", "Negative"],
    )
    print(result)
    return result["label"]

