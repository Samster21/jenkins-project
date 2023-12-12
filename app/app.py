import sqlite3
import os, logging
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort




def get_db_connection():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con

def get_post(post_id):
    con = get_db_connection()
    post = con.execute("SELECT * FROM posts WHERE id=?",(post_id,)).fetchone()
    con.close()
    
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'YURI'

@app.route('/')
def index():
    con = get_db_connection()
    posts = con.execute('SELECT * FROM posts').fetchall()
    con.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
    
#         if not title:
#             flash('Title is required!!!')
    
#         else:
#             con = get_db_connection()
#             con.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#                         (title, content))
#             con.commit()
#             con.close()
#             return redirect(url_for('index'))
    
#     return render_template('create.html')

# @app.route('/<int:id>/edit', methods=('GET', 'POST'))
# def edit(id):
#     post = get_post(id)
    
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
        
#         if not title:
#             flash('Title is Empty!!!')
            
#         else:
#             con = get_db_connection()
#             con.execute('UPDATE posts SET title=? , content=?  WHERE id=?', (title, content,id))
#             con.commit()
#             con.close()
            
#             return redirect(url_for('index'))
        
#     return render_template('edit.html', post=post)


# @app.route("/<int:id>/delete", methods=('POST',))
# def delete(id):
#     post = get_post(id)
#     con = get_db_connection()
#     con.execute("DELETE FROM posts WHERE id=?", (id,))
#     con.commit()
#     con.close()
#     flash("{} was successfully deleted!".format(post['title']))
#     return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
