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


{% macro value_add_tableize(name_source, name_base, data_element, focus_year) -%}

{% set filename1 = "value_add_sidebyside_" + name_source + name_base + "all_time_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
{% set filename2 = "value_add_sidebyside_"  + name_source + name_base + "focus_year_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
{% set filename3 = "value_add_stacked_" + name_source + name_base + "all_time_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
{% set filename4 = "value_add_stacked_"  + name_source + name_base + "focus_year_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
{% set filename5 = "value_add_stacked_" + name_base + name_source + "all_time_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
{% set filename6 = "value_add_stacked_"  + name_base + name_source + "focus_year_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}

<table>
  <tr>
    <td valign="top"> <img src="{{ value_add_graphs.files[filename1].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_graphs.files[filename2].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - {{ focus_year }}</td>
  </tr>
<tr>
    <td valign="top"> <img src="{{ value_add_graphs.files[filename3].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_graphs.files[filename4].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - {{ focus_year }}</td>
  </tr>
<tr>
    <td valign="top"> <img src="{{ value_add_graphs.files[filename5].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_graphs.files[filename6].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - {{ focus_year }}</td>
  </tr>
 </table>

{% endmacro -%}


{% macro value_add_self_tableize(name_source, data_element, focus_year) -%}

{% set filename1 = "value_add_self_sidebyside_" + name_source + "all_time_for_" + data_element.lower().replace(' ', '_') + "_by_type.png" %}
{% set filename2 = "value_add_self_sidebyside_"  + name_source + "focus_year_for_" + data_element.lower().replace(' ', '_') + "_by_type.png" %}

<table>
  <tr>
    <td valign="top"> <img src="{{ value_add_self_graphs.files[filename1].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_self_graphs.files[filename2].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - {{ focus_year }}</td>
  </tr>
 </table>

{% endmacro -%}

