
<ul class="nav navbar-nav sidenav">
    <li>
        <a href="#">Означення</a>
    </li>
    <li>
        <a href="#" data-toggle="collapse" data-target="#submenu-subjects">Предмети</a>
        <ul class="collapse list-unstyled" id="submenu-subjects">
            {% for subject in subjects %}
                <li><a href="#">{{ subject.title }}</a></li>
            {% endfor %}
        </ul>
    </li>
    <li>
        <a href="#" data-toggle="collapse" data-target="#submenu-grades">Класи</a>
        <ul class="collapse list-unstyled" id="submenu-grades">
            {% for grade in grades %}
                <li><a href="#">{{ grade.title }} клас</a></li>
            {% endfor %}
        </ul>
    </li>
</ul>
