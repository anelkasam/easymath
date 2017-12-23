{% extends "base.tpl" %}

{% block carnel %}
    <div class="col-sm-1 sidenav"> </div>
    <div class="col-sm-10 text-left">
        {% for obj in about %}
            <h1>{{ obj.title }}</h1>
            {{ obj.text | safe }}
            <hr/>
      {% endfor %}
    </div>
    <div class="col-sm-1 sidenav"> </div>
{% endblock %}