import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#import the inputscript file used to analyze the URL
import inputScript
#load model
app = Flask(__name__)
model = pickle.load(open('Phishing_website.pkl'))
