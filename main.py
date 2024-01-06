 
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def destinations():
    conn = sqlite3.connect('travel_planner.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM destinations")
    destinations = cursor.fetchall()
    conn.close()
    return render_template('destinations.html', destinations=destinations)

@app.route('/activities')
def activities():
    conn = sqlite3.connect('travel_planner.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities")
    activities = cursor.fetchall()
    conn.close()
    return render_template('activities.html', activities=activities)

@app.route('/itinerary')
def itinerary():
    return render_template('itinerary.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-itinerary', methods=['POST'])
def submit_itinerary():
    destination = request.form['destination']
    activities = request.form.getlist('activities')
    dates = request.form['dates']
    conn = sqlite3.connect('travel_planner.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO itineraries (destination, activities, dates) VALUES (?, ?, ?)", (destination, ','.join(activities), dates))
    conn.commit()
    conn.close()
    return redirect(url_for('itinerary'))

@app.route('/get-recommendations')
def get_recommendations():
    conn = sqlite3.connect('travel_planner.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recommendations")
    recommendations = cursor.fetchall()
    conn.close()
    return render_template('recommendations.html', recommendations=recommendations)

@app.route('/save-itinerary')
def save_itinerary():
    return render_template('save_itinerary.html')

if __name__ == '__main__':
    app.run(debug=True)
