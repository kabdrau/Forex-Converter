### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
> **Python** is used to develop back-end of web applications, also it is being used in deifferent areas like data science, machine learning, artificial intelligence, image processing and many more. Python is simple to read and maintain code. To run python code usually interprete is required. Python is commonly used for server side scripting.
>
> **JavaScript** can be used to develop both front-end and back-end sides of web applications. JS doesn't provide easy code readability or maintainability. JS code can be run on most web browsers. JS is commonly used for user side scripting.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

> `my_dict = {"a": 1, "b": 2}`
> `my_dict.get('c', 'not found')`
> `my_dict.setdefault('c', '3')`

- What is a unit test?

> Test one “unit” of functionality, typically, one function or method

- What is an integration test?

> Test that components work together

- What is the role of web application framework, like Flask?

> Flask is a small and lightweight web framework built in Python that provides useful tools and features to develop server side of web applications

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

> URL Parameter `shop/<toy>` feels more like “subject of page”
> Query Parameter `/shop?toy=elmo` feels more like “extra info about page”, often used when coming from form

- How do you collect data from a URL placeholder parameter using Flask?

> You can add variable sections to a URL by marking sections with `home/<variable_name>`
> Your function then receives the `<variable_name>` as a keyword argument
> Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

- How do you collect data from the query string using Flask?

> Let's say we have following url with query parameter: `home/query?arg1=something1&arg2=something2`
> In order to retrieve data from query string we need define function with request module and call `arg1 = request.args['arg1']` and `arg2 = request.args['arg2']`
> **request.args** is a dict-like object of query parameters.

- How do you collect data from the body of the request using Flask?

> By default, a route only responds to GET requests
> To accept POST requests, we must specify `@app.route("/my/route", methods=["POST"])`
> To get data from the body of request you need to initiate POST request for example `data = request.form["data"]`
> **request.form** is a dict-like object of POST parameters.

- What is a cookie and what kinds of things are they commonly used for?

> Cookies are name/string-value pair stored by the client (browser). Cookies are very small (4KB). The data is sent back to the server for every HTTP request. The aim is to remember and track data that is relevant to customer usage for better visitor experience and website statistics.

- What is the session object in Flask?

> Flask-Session is an extension for Flask that supports Server-side Session to your application. The Session is the time between the client logs in to the server and logs out of the server. The data in the Session is stored on the top of cookies and signed by the server cryptographically.

- What does Flask's `jsonify()` do?

> `jsonify()` is a helper method provided by Flask to properly return JSON data