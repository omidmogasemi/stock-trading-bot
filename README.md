<h1 align="center">
    Python Stock Trading Bot 
</h1>

## About

This is a work in progress bot I am developing that will use a set of popular, well-known trading algorithms to automatically open and close trades on a paper trading account with a starting equity of \$400,000

The bot is built using Python, which is used to perform the algorithm computations and connect to Alpaca's trading API. It also uses WebSockets to stream information from Apaca's API.

## What's inside?

A quick look at the top-level files and directories in this project.

    .
    ├── Algorithms
    ├── AlpacaBot.py
    ├── APITester.py
    ├── Stock.py
    ├── User.py

1.  **`/Algorithms`**: This directory contains all of the possible algorithms that can be used that I have currently implemented in code. This is the bulk of the work in this project, and thus is a constant work in progress with consistent updates.

2.  **`AlpacaBot.py`**: This file is the main driver file for the core program of the bot.

3.  **`APITester.py`**: This file performs a set number of test API calls to Alpaca's service to ensure that the account being used is working correctly.

4.  **`Stock.py`**: This file represents each individual stock being operated on by the bot.

5.  **`User.py`**: This file represents the user running the application.

## Running the Program

If you'd like to run the program yourself, you can! Just create a .env file in the root directory that contains **BASE_URL**, **API_KEY**, and **SECRET_KEY** values. To get these proper values, please [sign up](https://app.alpaca.markets/signup) with an account at Alpaca and use their user dashboard to acquire those needed variables. Once done, please first run the **APITester** to ensure that your account is working and passes all tests. Finally, you can now run the bot by launching the **AlpacaBot** file.
