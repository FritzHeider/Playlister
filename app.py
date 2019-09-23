from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists


app = Flask(__name__)


# OUR MOCK ARRAY OF PROJECTS
# playlists = [
#     { 'title': 'Doggo Videos', 'description': 'Doggoss acting weird'},
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing! '},
#     { 'title': '70\'s Music', 'description': 'All wrapped up in Blue! '},
#
#
#     { 'title': '60\'s Music', 'description': 'Lay lady lay '}
# ]

@app.route('/')
def playlists_index():
    """Show all playlits."""
    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():
    """Show new playlist."""
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    playlists.insert_one(playlist)
    #print(request.form.to_dict())
    return redirect(url_for('playlists_index'))


if __name__ == '__main__':
    app.run(debug=True)
