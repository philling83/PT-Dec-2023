# `S3W35D1`

## [Jinja Docs](https://jinja.palletsprojects.com/en/3.1.x/)
## [Flask Docs](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

## Templating

Main reasons to use templating

- "Easier"
  - If you understand the template language very well, it's easier
  - A complex React App's JSX can be messier than using templates
- Lightweight
  - Much easier to run than a React App
  - Generally used for internal tools, in development, etc
    - You wouldn't book a flight to a place you can walk to
    - You shouldn't build a React App for a task you can template
- You might see it somewhere in the real world
  - Might not be Jinja, but templating is very similar across many implementations
- Not really any other reasons to use templates
  - If the above cases don't apply, use React

## Works with Flask right out the box

`render_template` built-in function in Flask package

```py
from flask import render_template
from flask import Flask, render_template
```

Expects that all templates are in a "templates" folder

Pass filename to function to render that template

- Will automatically look in your "templates" folder

```py
@app.route('/')
def index():
    return render_template('index.html')
```

## Variables

We can use variables through double curly braces `{{ variable_name }}`

Pass as kwarg (similar to props} to `render_template` and used inside your templates

```py
res = # Pretend database stuff happens here
return render_template('index.html', user=res.first_name)
```

```html
<!-- /app/templates/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <h1>Hello {{ user }}!</h1>
  </head>
</html>
```

## Conditionals

Put conditionals right into html

```html
{% if not logged_in %}
  <a href="/login">Log in</a>
{% endif %}
```

## Iteration

```py
nav = [
  { 'href': 'https://appacademy.io', 'caption': 'App Academy' },
  { 'href': 'https://youtube.com', 'caption': 'YouTube' },
]

render_template("page.html", nav=nav)
```

```html
<ul>
  {% for el in nav %}
    <li>
      <a href="{{ el.href }}">{{ el.caption }}</a>
    </li>
  {% endfor %}
</ul>
```

## Components

You can break your templates into React-like "components" by simply making more template files

Then, combine using the `include` keyword

```html
<!-- /app/templates/other_page.html -->
<h2>This sure is some other page!</h2>

<!---->
<!---->
<!---->

<!-- /app/templates/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <h1>Hello {{ user }}!</h1>
    {% include 'other_page.html' %}
  </head>
</html>
```

---

## Flask Blueprints

Blueprints are extremely similar to `Router` from Express

Blueprint takes 3 arguments

- String to set the name of the blueprint
- `__name__` to specify the file name this blueprint is in
- `url_prefix=` set to the url path

Like with Express Router, any requests that start with `/spots` would go here

```py
# /app/routes/spots.py
from flask import Blueprint

bp = Blueprint('spots', __name__, url_prefix='/spots')

@bp.route('/pet-friendly')
def my_route():
    return render_template('pet_spots.html')
```

And any requests starting with `/reviews` will go here

```py
# /app/reviews/reviews.py
from flask import Blueprint

bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@bp.route('/5-star')
def my_route():
    return render_template('bribed-reviews.html')
```

All of your blueprints need to be connected to your app

`register_blueprint()` takes your blueprint, access through your module

```py
app.register_blueprint(routes.spots.bp)
app.register_blueprint(routes.reviews.bp)
```