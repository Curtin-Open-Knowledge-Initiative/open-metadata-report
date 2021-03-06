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

Here we write some background stuff, probably using the abstracts we have I guess, can also include some
summary statistics and other useful things.

In January 2022, OpenAlex was launched as a source of open bibliographic metadata. Intended both as a replacement of 
and improvement on Microsoft Academic, it provides structured data on publications, authors, institutions and 
publication venues.

Many tools, projects and services relied on Microsoft Academic as source of largely open metadata, and might consider 
switching to OpenAlex. More broadly, the launch of OpenAlex has increased interest in the potential of open metadata 
to enable discovery, linking and integration of data on research processes and outputs.

Unlike metadata from closed sources, open metadata can be combined and enriched to provide a rich open metadata 
landscape. Transparency and provenance allow identifying and addressing existing gaps and biases in coverage and 
quality. 

In this project, we assess and compare the value added by OpenAlex to Crossref metadata, and compare this to 
to Microsoft Academic before it closed. We look both at the coverage of publications and other research output (with and without DOIs) as well as the coverage 
of metadata for authors, institutions and publication venues and disciplines.  


This report was run using the following tables as source data:

* Crossref: {{ metadata.TABLES.crossref }}
* OpenAlex Native Format {{ metadata.TABLES.openalex_native.Work }}
* Microsoft Academic:
    * Papers: {{ metadata.TABLES.mag.Papers }}
    * Authors: {{ metadata.TABLES.mag.Authors }}
    * Affiliations: {{ metadata.TABLES.mag.Affiliations }}
    * Intermediate: {{ metadata.INTERMEDIATE_TABLES.mag }}

<pdf:nextpage>

# Contents

There is actually a way, I think of pulling in a table of contents, but I haven't done that previously. Or it can
be done manually obviously.

# Introduction and Background

Stuff on MAG going away and the motivation for tracking completeness

## Data sources

Do we need a section that gives some brief background on the data sources?

### Crossref Metadata

### Microsoft Academic

### OpenAlex

## Goals of this report

## Limitations

# Coverage of OpenAlex vs Crossref

## Comparing coverage

OpenAlex is based initially on metadata from Microsoft Academic and the overall coverage compared to Crossref is
consistent with for publications over all time. Noting that OpenAlex has made a decision to not cover all the 
content types that MAG did, these two charts show a difference for the non-Crossref materials but very similar
results for the content that has Crossref DOIs.

![]({{ overall_comparison.files["openalex_native_crossref_coverage_all_time.png"].cache_filepath }})

![]({{ overall_comparison.files["mag_crossref_coverage_all_time.png"].cache_filepath }})

Therefore it is of interest to look at a specific recent year, in this case {{ graph_metadata.FOCUS_YEAR }}.

![]({{ overall_comparison.files["openalex_native_crossref_coverage_focus_year.png"].cache_filepath }})

## Value Add of OpenAlex to Crossref

### Overview

### Details

We can do loops eg over the data elements. But this might be better for a supplementary data section as we will 
presumably want to actually comment on the graphs themselves?

{% for data_element in graph_metadata.SIDEBYSIDE_BAR_SUMMARY_XS %}

<pdf:nextpage>

### {{ data_element }}


{% set filename = "value_add_sidebyside_openalex_native_all_time_for_" + data_element.lower().replace(' ', '_') + "_by_cr_type.png" %}
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

