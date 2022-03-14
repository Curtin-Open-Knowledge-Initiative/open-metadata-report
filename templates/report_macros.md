{% macro created_at(fmt="%d %B %Y") -%}
{{ datetime.datetime.today().strftime(fmt) }}
{% endmacro -%}

{% macro tableize(table_data, table_number, v_header=false, tiny_header=false) -%}
<table>
    <caption><strong>Table {{table_number}}.</strong> {{ table_data.title }}</caption>
    <thead>
        <tr>
            {% for column in table_data.columns %}
                <th {% if v_header is true %} class=vt_header {% endif %}
                    {% if tiny_header is true %} class=tiny_header {% endif %}
                    text-align={{column.alignment}}>{{ column.name }}
                </th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        {% for row in table_data.rows %}
            <tr style="background-color: {{ loop.cycle("white", "Gainsboro") }};">
                {% for column in table_data.columns %}
                    <td text-align={{column.alignment}}>{{ row[column.name] }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
{% endmacro -%}

{% macro md_tableize(table_data, table_number) -%}
**Table {{ table_number }}.** {{ table_data.title }}

{% for column in table_data.columns -%}
{% if not loop.last -%}{{ column.name }} | {%- else %}{{ column.name }}
{%- endif %}
{%- endfor %}
{% for column in table_data.columns -%}{% if not loop.last -%}------|{%- else %}----
{%- endif %}
{%- endfor %}
{% for row in table_data.rows %}{% for column in table_data.columns -%}{% if not loop.last -%}{{ row[column.name] }} | {%- else %}{{ row[column.name] }}
{%- endif %}
{%- endfor %}
{% endfor %}
{% endmacro -%}