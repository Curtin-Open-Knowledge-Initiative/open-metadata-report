{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

<!-- Loading JSON data files for access -->
<!-- TODO - these will currently break because they need to be created/added to the precipy index -->
{% set metadata = load_json(save_data_parameters.files["data_parameters.json"].cache_filepath) %}
{% set graphs_metadata = load_json(save_data_parameters.files["graph_parameters.json"].cache_filepath) %}
{# set tables = load_json(generate_tables.files["tables.json"].cache_filepath #}

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

This report was run using the following tables as source data:
Crossref: {{ metadata.TABLES.crossref }}
Crossref Member Data: {{ metadata.CROSSREF_MEMBER_DATA_TABLE }} with date {{ metadata.CROSSREF_MEMBER_DATE }}
OpenAlex Native Format {{ metadata.TABLES.openalex.Work }}
Microsoft Academic:

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

![](openalex_native_crossref_coverage_all_time.png)

![](mag_crossref_coverage_all_time.png)

Therefore it is of interest to look at a specific recent year, in this case {{ graphs_metadata.FOCUS_YEAR }}.

![](openalex_native_crossref_coverage_focus_year.png)

## Value Add of OpenAlex to Crossref

### Overview

### Details

We can do loops eg over the data elements. But this might be better for a supplementary data section as we will 
presumably want to actually comment on the graphs themselves? 

TODO:
There is a bug in the xhtml2pdf package which means it
only works with complete paths on windows. This creates an issue as we would need to use precipy to give us the full
path but I'm not sure whether we can use a variable inside that full path declaration. Some experimentation required.

{% for data_element in graphs_metadata.SIDEBYSIDE_BAR_SUMMARY_XS %}

### {{ data_element }}

![](value_add_openalex_native_all_time_for_{{ data_element.lower().replace(' ', '_') }}_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that

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

## Appendix B - Historical MAG Analysis??

4. OpenAlex - non-Crossref coverage
4a. Publication types - with and without (Crossref?) DOIs
4b. Coverage of 6 main parameters - with /without (Crossref?) DOIs
4c. Coverage of 6 main parameters per publication type 
 - with/without (Crossref?) DOIs
5. Methodology
6. Appendix - tables with AllTheThingsTM

