title:
headline:
author:
date:

{% extends "post.html" %}
{% block body %}

{% filter markdown:"fenced-code-blocks" %}
{% verbatim %}

{% endverbatim %}
{% endfilter %}
{% endblock body %}
