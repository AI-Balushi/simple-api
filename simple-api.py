from fastapi import FastAPI
import random

app = FastAPI()

# List of side hustles
side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell products without holding inventory.",
    "Affiliate Marketing - Promote products and earn commissions.",
    "Tutoring - Teach subjects you’re good at online.",
    "Print on Demand - Sell custom designs on products.",
    "Content Creation - Start a YouTube channel or blog.",
    "Stock Photography - Sell your photos online.",
    "Handmade Crafts - Sell handmade items on Etsy.",
    "App Development - Build and sell mobile apps.",
    "Online Courses - Create and sell educational content.",
    "Podcasting - Monetize your niche podcast."
]

# List of money-related quotes
money_quotes = [
    "Don't work for money, make money work for you. - Robert Kiyosaki",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing. - Philip Fisher",
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "If you don’t find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "A penny saved is a penny earned. - Benjamin Franklin",
    "Rich people have small TVs and big libraries, poor people have small libraries and big TVs. - Zig Ziglar",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "Time is more valuable than money. You can get more money, but you cannot get more time. - Jim Rohn",
    "It’s not your salary that makes you rich, it’s your spending habits. - Charles A. Jaffe"
]

@app.get("/side_hustles")
def get_side_hustle():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quote():
    """Returns a random money-related quote"""
    return {"money_quote": random.choice(money_quotes)}
