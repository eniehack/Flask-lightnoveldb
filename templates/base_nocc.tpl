<html>
<head>
  <title>{% block title %}{% endblock %}</title>
  <link rel="stylesheet" href="/static/css/pure-min.css">
  <link rel="stylesheet" href="/static/css/skeleton.css">
  <link rel="stylesheet" href="/static/css/style.css">

  {% block header %}
  {% endblock %}

</head>
<body>
<header class="header">
  <h1>名作ライトノベル作品データベース</h1>
</header>
<main>

  {% block contents %}
  {% endblock %}

</main>
  <br />
  <a href="/">Back to Home</a>
  <p><small>&copy;2018 <a href="https://twitter.com/intent/user?user_id=3503112972">Studio 4単位/Eniehack</a> </small></p><br>
</body>
</html>