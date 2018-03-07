from flask import render_template, flash, redirect
from app import app
from .forms import *
from .League import *
from .Summoner2 import *


@app.route('/', methods=['GET', 'POST'])
# Run the simulations by calling the appropriate functions, and return the value to display
def index():
    full_form = FullForm()
    abridged_form = AbridgedForm()
    games = 0
    game = 0
    goal = ""
    # Called if the user uses the manual mode
    if full_form.rank.data and full_form.validate_on_submit():
        sim = Player(full_form.rank.data, full_form.current_gain.data, full_form.current_loss.data, full_form.current_LP.data, full_form.in_series.data, full_form.series_wins.data, full_form.series_losses.data)
        index = 0
        goal = full_form.goal.data
        # Run 1000 simulations to calculate the average results
        while index < 1000:
            games += sim.Ranked_calculate(full_form.goal.data, full_form.winrate.data)
            index += 1
    # Called if the user uses the automated mode
    elif abridged_form.username.data and abridged_form.validate_on_submit():
        info = get_info(abridged_form.username.data)
        if len(info) > 2:
            sim = Player(info[0], int(info[3]), 40 - int(info[3]), info[1], info[1] >= 100, 0, 0)
            goal = abridged_form.goal.data
            index = 0
            while index < 1000:
                games += sim.Ranked_calculate(abridged_form.goal.data, abridged_form.winrate.data)
                index += 1
        else:
            games = 2000 * 1000
    return render_template('login.html', games=games / 1000, fform=full_form, aform=abridged_form, goal=goal)
