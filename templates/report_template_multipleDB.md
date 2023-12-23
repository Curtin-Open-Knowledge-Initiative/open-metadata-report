<!-- {% set source_a = "openalex" %} -->
<!-- {% set source_b = "openaire" %} -->

{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

<!-- Loading JSON data files for access -->
<!-- TODO - these will currently break because they need to be created/added to the precipy index -->
{% set metadata = load_json(save_data_parameters.files["data_parameters.json"].cache_filepath) %}
{% set graph_metadata = load_json(save_data_parameters.files["graph_parameters.json"].cache_filepath) %}
{% set tables = load_json(generate_tables.files["tables.json"].cache_filepath) %}

{% set source_a = metadata.COMPARISON[0] %}
{% set source_b = metadata.COMPARISON[1] %}

{% set name_source_print = metadata.SOURCE_JSON[source_b].SOURCE_PRINT_NAME %}
{% set name_base_print = metadata.SOURCE_JSON[source_a].SOURCE_PRINT_NAME %}
{% set name_source_full = metadata.SOURCE_JSON[source_b].SOURCE_NAME %}
{% set name_base_full = metadata.SOURCE_JSON[source_a].SOURCE_NAME %}
{% set name_source = name_source_full  + "_" %}
{% set name_base = name_base_full + "_" %}

{% set focus_year = graph_metadata.FOCUS_YEAR %}
{% set crossref_current = graph_metadata.CROSSREF_CURRENT %}
{% set tablenum = 1 %}


<!-- Title Page -->
<pdf:nexttemplate name="titlepage">
<pdf:nextpage>

<p class="subtitle">OPEN METADATA SOURCES</p>
<p class="titlemeta">
<br>
COMPARING {{ name_base_print|upper }} TO {{ name_source_print|upper }} <br>
<br>
DATE: {{ helper.created_at()|upper }}</p>
<br>
<br>
[PRELIMINARY VERSION] 
<!-- switch page templates -->
<pdf:nexttemplate name="report">

<pdf:nextpage>

# Executive Summary

In this project, we assess and compare {{ name_base_print }} to {{ name_source_print }} metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 

The report currently contains all the graphs comparing metadata coverage of {{ name_base_print }} compared to {{ name_source_print }}, and of DOIs vs non-DOIs in {{ name_source_full }}. 
More explanatory text, tables and interpretation of findings will be added in a later version.

Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [{{ metadata.ARCHIVE_REPORT_DIR }}](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/{{ metadata.ARCHIVE_REPORT_NAME }}) in this repository.

<pdf:nextpage> 


# Introduction and Background

In January 2022, OpenAlex was launched as a source of open bibliographic metadata. Intended both as a replacement of 
and improvement on Microsoft Academic, it provides structured data on publications, authors, institutions and 
publication venues.

Many tools, projects and services relied on Microsoft Academic as source of largely open metadata, and might consider 
switching to OpenAlex. More broadly, the launch of OpenAlex has increased interest in the potential of open metadata 
to enable discovery, linking and integration of data on research processes and outputs.

Unlike metadata from closed sources, open metadata can be combined and enriched to provide a rich open metadata 
landscape. Transparency and provenance allow identifying and addressing existing gaps and biases in coverage and 
quality. 

In this project, we assess and compare {{ name_base_print }} to {{ name_source_print }} metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 


## Data sources

This report was run using the following tables as source data:

* {{ name_base_print }}: {{ metadata.TABLES[source_a] }}
* {{ name_source_print }}: {{ metadata.TABLES[source_b] }}


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [{{ metadata.ARCHIVE_REPORT_DIR }}](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/{{ metadata.ARCHIVE_REPORT_NAME }}) in this repository. 

<pdf:nextpage> 

# Coverage of {{ name_base_print }} and {{ name_source_print }}
<br>   
## Comparing coverage

### Overview - {{ name_base_print }}

<table>
  <tr>
    <td valign="top"><img src="{{ overall_comparison.files[name_base + "crossref_coverage_all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{overall_comparison.files[name_base + "crossref_coverage_focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<br>

### Overview - {{ name_source_print }}

<table>
  <tr>
    <td valign="top"><img src="{{ overall_comparison.files[name_source + "crossref_coverage_all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{overall_comparison.files[name_source + "crossref_coverage_focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<pdf:nextpage>


### By year and publication type - {{ name_base_print }}

<table>
  <tr>
    <td valign="top"><img src="{{ source_in_base_by_pubdate.files[name_base + "in_crossref_by_pubdate.png"].cache_filepath }}"></td>
    <td valign="top"><img src="{{ source_coverage_by_crossref_type.files[name_base + "coverage_of_crossref_by_crossref_type.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<br>

### By year and publication type - {{ name_source_print }}

<table>
  <tr>
    <td valign="top"><img src="{{ source_in_base_by_pubdate.files[name_source + "in_crossref_by_pubdate.png"].cache_filepath }}"></td>
    <td valign="top"><img src="{{ source_coverage_by_crossref_type.files[name_source + "coverage_of_crossref_by_crossref_type.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Comparing {{ name_base_print }} and {{ name_source_print }} 

### Overview 

Coverage of metadata types in {{ name_base_print }} and {{ name_source_print }} (for Crossref DOIs)

<table>
  <tr>
    <td valign="top"> <img src="{{ value_add_graphs.files["value_add_sidebyside_" + name_source + name_base + "all_time.png"].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_graphs.files["value_add_sidebyside_" + name_source + name_base + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
<tr>
    <td valign="top"><img src="{{ value_add_graphs.files["value_add_stacked_" + name_source + name_base + "all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{ value_add_graphs.files["value_add_stacked_" + name_source + name_base + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
<tr>
    <td valign="top"><img src="{{ value_add_graphs.files["value_add_stacked_" + name_base + name_source + "all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{ value_add_graphs.files["value_add_stacked_" + name_base + name_source + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<pdf:nextpage>

### Details 

Metadata coverage in {{ name_base_print }} and {{ name_source_print }} by publication type (for Crossref DOIs)
<br>

{% set data_element_array = graph_metadata.VALUE_ADD_META[source_a][source_b]['xs'] %}
{% for data_element in data_element_array %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, name_base, graph_metadata.GRAPH_PRINT_NAMES[data_element], focus_year) }}

<pdf:nextpage>
{% endfor %}

# {{ name_base_print }} Coverage Beyond DOIs
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="{{ crdois_in_source_by_pubdate.files["crdois_in_" + name_base + "by_pubdate.png"].cache_filepath }}"></td>
    <td valign="top"><img src="{{ source_coverage_self_by_type.files[name_base + "coverage_self_by_type.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Metadata Coverage

### Overview

Comparing coverage of metadata types for DOIs and non-DOIs in {{ name_base_print }}

<table>
  <tr>
    <td valign="top"> <img src="{{ value_add_self_graphs.files["value_add_self_sidebyside_" + name_base + "all_time.png"].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_self_graphs.files["value_add_self_sidebyside_" + name_base + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage for DOIs and non-DOIs by publication type
<br>

{% set data_element_array = graph_metadata.INTERNAL_COMPARISON_META[source_a]['xs'] %}
{% for data_element in data_element_array %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_base, graph_metadata.GRAPH_PRINT_NAMES[data_element],focus_year) }}
{{ loop.cycle("", "<pdf:nextpage>") }}
{% endfor %}

<pdf:nextpage>

# {{ name_source_print }} Coverage Beyond DOIs
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="{{ crdois_in_source_by_pubdate.files["crdois_in_" + name_source + "by_pubdate.png"].cache_filepath }}"></td>
    <td valign="top"><img src="{{ source_coverage_self_by_type.files[name_source + "coverage_self_by_type.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Metadata Coverage

### Overview

Comparing coverage of metadata types for DOIs and non-DOIs in {{ name_source }}

<table>
  <tr>
    <td valign="top"> <img src="{{ value_add_self_graphs.files["value_add_self_sidebyside_" + name_source + "all_time.png"].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_self_graphs.files["value_add_self_sidebyside_" + name_source + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage for DOIs and non-DOIs by publication type
<br>

{% set data_element_array = graph_metadata.INTERNAL_COMPARISON_META[source_b]['xs'] %}
{% for data_element in data_element_array %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, graph_metadata.GRAPH_PRINT_NAMES[data_element],focus_year) }}
{{ loop.cycle("", "<pdf:nextpage>") }}
{% endfor %}



{# Lines below are not currently run pending refactoring (2023-04-25)
## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = {{ crossref_current[0] }}-{{ crossref_current[2] }}  
Focus Year = {{ focus_year }}

{% for source in metadata.SOURCES %}
`
### {{ graph_metadata.FORMATTED_SOURCE_NAMES[source] }} Coverage

{% set tablenum = tablenum + loop.index0 %}
{{ helper.tableize(tables[source]["summary_comparison_table"], tablenum) }}


{% endfor %}

{% set tablenum = tablenum + metadata.SOURCES|length %}
#}


