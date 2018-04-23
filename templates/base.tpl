<html>
<head>
  <title>{% block title %}{% endblock %}</title>
  <link rel="stylesheet" href="/static/css/menus-min.css">
  <link rel="stylesheet" href="/static/css/skeleton.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
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
  <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">
    <img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" />
  </a>
  <br />このページの書籍情報は<a href="http://ja.dbpedia.org/">DBpedia Japan</a>または<a href="https://ja.wikipedia.org/">Wikipedia 日本語版</a>から抽出したデータを使用しているため、 <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">クリエイティブ・コモンズ 表示 - 継承 3.0 非移植 ライセンス</a>の下に提供されています。
  <br />
  <a href="/">Back to Home</a>
  <p><small>&copy;2018 <a href="https://twitter.com/intent/user?user_id=3503112972">Studio 4単位/Eniehack</a> </small></p><br>
</body>
</html>