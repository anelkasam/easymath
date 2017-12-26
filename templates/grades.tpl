{#<div class="'sidebar-header">#}
{#    <h3>Групи матеріалів</h3>#}
{#</div>#}

<ul class="list-unstyled components">
<li><a href="#">Означення</a></li>
<li>
    <a href="#subjectSubmenu" data-toggle="collapse" aria-expanded="false">Предмети</a>
    <ul class="collapse list-unstyled" id="subjectSubmenu">
        {% for subject in subjects %}
            <li><a href="#">{{ subject.title }}</a></li>
        {% endfor %}
    </ul>
</li>

<li>
    <a href="#gradeSubmenu" data-toggle="collapse" aria-expanded="false">Класи</a>
    <ul class="collapse list-unstyled" id="gradeSubmenu">
        {% for grade in grades %}
            <li><a href="#">{{ grade.title }} клас</a></li>
        {% endfor %}
    </ul>
</li>
</ul>
