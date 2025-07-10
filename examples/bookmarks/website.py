#!/usr/bin/env python3

# Main program to display bookmark results via web using Flask

import sqlite3;
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main page, getting data from a SQL query
    and passing it to the template.
    """
    c = sqlite3.connect("bookmarks.db");
    cur = c.cursor();
    sql_query_results = cur.execute("select text,url from bookmark order by text");

    # Render the 'results.html' template, passing the query results to it.
    # The template will access this data via the 'results' variable.
    return render_template('results.html', results=sql_query_results)

if __name__ == '__main__':
    # Run the Flask development server.
    app.run(debug=True)


