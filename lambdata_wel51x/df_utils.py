"""
Utility functions for working with DataFrames.
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

def train_validate_test_split(X, y, train_percent=60, validate_percent=20, seed=None):
    np.random.seed(seed)

    if (train_percent + validate_percent) > 100:
        return -1, "Input Percentages > 100"

    test_size = (100 - (train_percent + validate_percent))/100
    val_size = validate_percent / (train_percent + validate_percent)

    temp_x, X_test, temp_y, y_test = train_test_split(X, y, test_size=test_size)

    X_train, X_val, y_train, y_val = train_test_split(temp_x, temp_y, test_size=val_size)

    return X_train, X_test, X_val, y_train, y_test, y_val

states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado",
          "CT":"Connecticut","DC":"District of Columbia","DE":"Delaware","FL":"Florida","GA":"Georgia",
          "HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky",
          "LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota",
          "MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire",
          "NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota",
          "OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","PR":"Puerto Rico","RI":"Rhode Island",
          "SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont",
          "VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

def get_state_abbrev(state):
    return [k for k,v in states.items() if v == state][0]

def get_state_name(abbrev):
    return states[abbrev]
