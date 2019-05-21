from flask import request, redirect, url_for, render_template, flash
from sensai import app, db
from sensai.models import Game
import random

@app.route('/')
def show_menus():
    return render_template('show_menus.html')

@app.route('/get', methods=['GET'])
def get_menus():

    # params
    menus = []
    budget = 2000
    text = "ゲムマ2000円ガチャの結果！" + "\n" + "\n"
    money = 2000
    budget = money

    # select first food
    while not menus:
        rand = random.randrange(0, db.session.query(Game.id).count()) + 1
        menus = db.session.query(Game).filter(Game.id==rand, Game.price <= budget).all()

    # calc
    budget -= int(menus[0].price)

    #add text for tweet
    text += str(menus[0].name) + "\n"

    while budget > 0:

        # avalable food candidate
        candidate = db.session.query(Game).filter(Game.price <= budget).all()

        # no candidate break
        if not candidate:
            break

        # select food
        rand = random.randrange(0, len(candidate))

        # add to list
        menus.append(candidate[rand])

        #add text for tweet
        text += str(candidate[rand].name) + "\n"

        #calc
        budget -= int(candidate[rand].price)

    # tweet result
    budget = money - budget
    text += "\n"
    text += "計 " + str(budget) + "円 " + "\n" + "\n"
    return render_template('show_menus.html', menus=menus, budget=budget, text=text)

import random
