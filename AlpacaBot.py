import os
import sys
import time
from dotenv import load_dotenv
from User import User

# initialize minute clock system
seconds_elapsed = time.perf_counter()
goal_time = 0

# load environment variables
load_dotenv()
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

user = User(api_key, secret_key, base_url, "ICLN,QQQ,SPY")


try:
    while user.clock.is_open:
        user.get_bars("ICLN")
        user.purchase_shares("ICLN")
        user.print_portfolio()
        goal_time += 60.001
        seconds_elapsed = time.perf_counter()
        print("Time left until next market check: ", end="")
        print(goal_time - seconds_elapsed)
        time.sleep(goal_time - seconds_elapsed)
except KeyboardInterrupt:
    print("You have closed the application. Your portfolio is as follows: ")
    print(user.list_positions)
    sys.exit()

print("The market is now closed. Your portfolio is as follows: ")
print(user.list_positions)
