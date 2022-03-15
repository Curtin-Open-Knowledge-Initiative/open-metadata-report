{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

<!-- Loading JSON data files for access -->
<!-- TODO - these will currently break because they need to be created/added to the precipy index -->
{% set metadata = load_json(save_data_parameters.files["data_parameters.json"].cache_filepath) %}
{% set graph_metadata = load_json(save_data_parameters.files["graph_parameters.json"].cache_filepath) %}
{% set tables = load_json(generate_tables.files["tables.json"].cache_filepath) %}
{% set tablenum = 1 %}

<!-- Title Page -->
<pdf:nexttemplate name="titlepage">
<pdf:nextpage>

<p class="subtitle">OPEN METADATA SOURCES</p>
<p class="titlemeta">
COMPARING OPENALEX TO CROSSREF AND MAG<br>
DATE: {{ helper.created_at()|upper }}</p>

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

This report was run using the following tables as source data:

* Crossref: {{ metadata.TABLES.crossref }}
* Crossref Member Data: {{ metadata.CROSSREF_MEMBER_DATA_TABLE }} with date {{ metadata.CROSSREF_MEMBER_DATE }}
* OpenAlex Native Format {{ metadata.TABLES.openalex.Work }}


<pdf:nextpage>

# Contents

There is actually a way, I think of pulling in a table of contents, but I haven't done that previously. Or it can
be done manually obviously.

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
(with and without DOIs) as well as in coverage of metadata (inlcuding identifiers) for authors, institutions, publication venues 
and disciplines. 


## Data sources

This report was run using the following tables as source data:

* Crossref: {{ metadata.TABLES.crossref }}
* Crossref Member Data: {{ metadata.CROSSREF_MEMBER_DATA_TABLE }} with date {{ metadata.CROSSREF_MEMBER_DATE }}
* OpenAlex Native Format {{ metadata.TABLES.openalex.Work }}

### Crossref Metadata

### Microsoft Academic

### OpenAlex

## Goals of this report

## Limitations

# Coverage of OpenAlex vs Crossref

## Comparing coverage

OpenAlex coverage all time: proportion with and without DOIs, overlap with Crossref.  
OpenAlex coverage of {{ graph_metadata.FOCUS_YEAR }}: smaller proportion publications without DOI, same coverage of Crossref

<table>
  <tr>
    <td valign="top"><img src="{{ overall_comparison.files["openalex_native_crossref_coverage_all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{ overall_comparison.files["openalex_native_crossref_coverage_focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>all time</td>
    <td>{{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>

The proportion of Crossref that is covered in OpenAlex is stable over time, around 75-80%.  
Coverage in OpenAlex of publication types in Crossref [describe]

<table>
  <tr>
    <td valign="top"><img src="{{ source_in_base_by_pubdate.files["crossref_in_openalex_native_by_pubdate.png"].cache_filepath }}"></td>
    <td valign="top"><img src="{{ source_coverage_by_crossref_type.files["openalex_native_coverage_by_crossref_type.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>all time</td>
    <td>all time</td>
  </tr>
 </table>


## Value Add of OpenAlex to Crossref

Comparing coverage of metadata types in Crossref and OpenAlex
Added value of OpenAlex for different metadata types over all publications


<table>
  <tr>
    <td valign="top"><img src="{{ value_add_graphs.files["value_add_sidebyside_openalex_native_all_time.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{ value_add_graphs.files["value_add_stacked_openalex_native_all_time.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>all time</td>
    <td>all time</td>
  </tr>
 </table>

Looking at {{ graph_metadata.FOCUS_YEAR }} only -> describe differences

<table>
  <tr>
    <td valign="top"><img src="{{ value_add_graphs.files["value_add_sidebyside_openalex_native_focus_year.png"].cache_filepath }}"></td>
    <td valign="top">  <img src="{{ value_add_graphs.files["value_add_stacked_openalex_native_focus_year.png"].cache_filepath }}"></td>
  </tr>
  <tr>
    <td>{{ graph_metadata.FOCUS_YEAR }}</td>
    <td>{{ graph_metadata.FOCUS_YEAR }}</td>
  </tr>
 </table>


### Overview

### Details

We can do loops eg over the data elements. But this might be better for a supplementary data section as we will 
presumably want to actually comment on the graphs themselves?

{% for data_element in graph_metadata.SIDEBYSIDE_BAR_SUMMARY_XS %}

<pdf:nextpage>

### {{ data_element }}


{% set filename = "value_add_openalex_native_all_time_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
![]({{ value_add_graphs.files[filename].cache_filepath }})

{% endfor %}

# OpenAlex Coverage Beyond Crossref

## Publication Types

## Metadata Coverage

### Overall

### By publication type

### By field

# Methodology

# Appendices

## Appendix A - Complete Tables

{% for source in metadata.SOURCES %}

### {{ graph_metadata.FORMATTED_SOURCE_NAMES[source] }} Coverage

{% set tablenum = tablenum + loop.index0 %}
{{ helper.tableize(tables[source]["summary_comparison_table"], tablenum) }}

{% endfor %}

{% set tablenum = tablenum + metadata.SOURCES|length %}


## Appendix B - Historical MAG Analysis??

4. OpenAlex - non-Crossref coverage
4a. Publication types - with and without (Crossref?) DOIs
4b. Coverage of 6 main parameters - with /without (Crossref?) DOIs
4c. Coverage of 6 main parameters per publication type 
 - with/without (Crossref?) DOIs
5. Methodology
6. Appendix - tables with AllTheThingsTM

