{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

<!-- Loading JSON data files for access -->
<!-- TODO - these will currently break because they need to be created/added to the precipy index -->
{% set metadata = load_json(save_data_parameters.files["data_parameters.json"].cache_filepath) %}
{% set graph_metadata = load_json(save_data_parameters.files["graph_parameters.json"].cache_filepath) %}
{% set tables = load_json(generate_tables.files["tables.json"].cache_filepath) %}
{% set name_source = metadata.NON_BASE_SOURCES[0] + "_" %}
{% set name_base = metadata.BASE_COMPARISON + "_" %}
{% set name_source_full = graph_metadata.FORMATTED_SOURCE_NAMES[metadata.NON_BASE_SOURCES[0]] %}
{% set name_base_full = graph_metadata.FORMATTED_SOURCE_NAMES[metadata.BASE_COMPARISON] %}
{% set focus_year = graph_metadata.FOCUS_YEAR %}
{% set crossref_current = graph_metadata.CROSSREF_CURRENT %}
{% set tablenum = 1 %}

<!-- This is a stopgap measure as will not correctly display for first run w/o suffix -->
{% set report_run_date = metadata.TODAY_STR %}
{% set report_run_n = 1 %}
TEST PATH TO ARCHIVE: {{ metadata.ARCHIVE_REPORT_DIR }}
TEST NAME OF ARCHIVE DIR: {{ metadata.ARCHIVE_REPORT_NAME }}
<!-- Title Page -->
<pdf:nexttemplate name="titlepage">
<pdf:nextpage>

<p class="subtitle">OPEN METADATA SOURCES</p>
<p class="titlemeta">
<br>
COMPARING {{ name_source_full|upper }} TO {{ name_base_full|upper }} <br>
<br>
DATE: {{ helper.created_at()|upper }}</p>
<br>
<br>
[PRELIMINARY VERSION] 
<!-- switch page templates -->
<pdf:nexttemplate name="report">

<pdf:nextpage>

# Executive Summary

In January 2022, OpenAlex was launched as a source of open bibliographic metadata. Intended both as a replacement of 
and improvement on Microsoft Academic, it provides structured data on publications, authors, institutions and 
publication venues.

In this project, we assess and compare the value added by OpenAlex to Crossref metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 

The report currently contains all the graphs comparing metadata coverage of {{ name_source_full }} compared to {{ name_base_full }}, and of DOIs vs non-DOIs in {{ name_source_full }}, as well as some basic tables. 
More explanatory text and interpretation of findings will be added in a later version.

Complete data and code are available at:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
with all images and data belonging to this report located in [/reports/run_{{ report_run_date }}_{{ report_run_n }}](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_{{ report_run_date }}_{{ report_run_n }})

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

In this project, we assess and compare the value added by OpenAlex to Crossref metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 


## Data sources

This report was run using the following tables as source data:

* {{ name_base_full }}: {{ metadata.TABLES.crossref }} 
* Crossref Member Data: {{ metadata.CROSSREF_MEMBER_DATA_TABLE }} with date 20220311
* {{ name_source_full }}: {{ metadata.TABLES.openalex_native.Work }} with date 20220313


Complete data and code are available at:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
with all images and data belonging to this report located in [/reports/run_{{ report_run_date }}_{{ report_run_n }}](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_{{ report_run_date }}_{{ report_run_n }})

<pdf:nextpage> 

# Coverage of {{ name_source_full }} vs {{ name_base_full }}
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="{{ overall_comparison.files[name_source + name_base + "coverage_all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{overall_comparison.files[name_source + name_base + "coverage_focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<br>
### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="{{ source_in_base_by_pubdate.files[name_base + "in_" + name_source + "by_pubdate.png"].cache_filepath }}"></td>
    <td valign="top"><img src="{{ source_coverage_by_crossref_type.files[name_source + "coverage_by_" + name_base + "type.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Value Add of {{ name_source_full }} to {{ name_base_full }}

### Overview

Comparing coverage of metadata types in {{ name_base_full }} and {{ name_source_full }}

<table>
  <tr>
    <td valign="top"> <img src="{{ value_add_graphs.files["value_add_sidebyside_" + name_source + "all_time.png"].cache_filepath }}"></td>
    <td valign="top"> <img src="{{ value_add_graphs.files["value_add_sidebyside_" + name_source + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
<tr>
    <td valign="top"><img src="{{ value_add_graphs.files["value_add_stacked_" + name_source + "all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{ value_add_graphs.files["value_add_stacked_" + name_source + "focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - {{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage in {{ name_source_full }} and {{ name_base_full }} by publication type
<br>

{% set data_element_array = graph_metadata.VALUE_ADD_META[metadata.BASE_COMPARISON][metadata.NON_BASE_SOURCES[0]]['xs'] %}

{% set data_element = data_element_array[0] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[1] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[2] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[3] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[4] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[5] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[6] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[7] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[8] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[9] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[10] %}
### {{ data_element }}

{{ helper.value_add_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

# {{ name_source_full }} Coverage Beyond {{ name_base_full }}
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="{{ dois_in_source_by_pubdate.files["dois_in_" + name_source + "by_pubdate.png"].cache_filepath }}"></td>
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

Comparing coverage of metadata types for DOIs and non-DOIs in OpenAlex

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

{% set data_element = data_element_array[0] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}


{% set data_element = data_element_array[1] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[2] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}


{% set data_element = data_element_array[3] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[4] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[5] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}


{% set data_element = data_element_array[6] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[8] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}


{% set data_element = data_element_array[9] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}

<pdf:nextpage>

{% set data_element = data_element_array[10] %}
### {{ data_element }}

{{ helper.value_add_self_tableize(name_source, data_element, focus_year) }}


<pdf:nextpage>



## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = {{ crossref_current[0] }}-{{ crossref_current[2] }}  
Focus Year = {{ focus_year }}

{% for source in metadata.SOURCES %}

### {{ graph_metadata.FORMATTED_SOURCE_NAMES[source] }} Coverage

{% set tablenum = tablenum + loop.index0 %}
{{ helper.tableize(tables[source]["summary_comparison_table"], tablenum) }}

{% endfor %}

{% set tablenum = tablenum + metadata.SOURCES|length %}



