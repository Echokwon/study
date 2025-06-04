from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

todo_items = []

TEMPLATE = """
<!doctype html>
<title>Todo App</title>
<h1>Todo List</h1>
<ul>
  {% for item in items %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>
<form method="post" action="/add">
  <input type="text" name="item" required>
  <input type="submit" value="Add">
</form>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, items=todo_items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item', '').strip()
    if item:
        todo_items.append(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
