
<style>

    @page {
        size: a4 portrait;
        @frame null {
        left: 1cm;
        width: 18cm;
        top: 7cm;
        height: 20cm;
    }}

    @page titlepage {
        size: a4 portrait;
        background-image: url("/Users/266883j/PycharmProjects/es_reports/assets/title_image.png");
        @frame title {
        left: 2cm;
        width: 16cm;
        top: 8.9cm;
        height: 19cm;
    }}

    @page report {
        size: a4 portrait;
        @frame content_frame {
        left: 2cm;
        width: 17cm;
        top: 2.5cm;
        height: 24.2cm;
    }}

     @page landscape-report {
        size: a4 landscape;
        @frame content_frame {
        left: 2cm;
        width: 24.7cm;
        top: 2cm;
        height: 17.5cm;
    }}

        @page lastpage {
        size: a4 portrait;
        background-image: url("/Users/266883j/PycharmProjects/es_reports/assets/final_page.png");
        @frame content_frame {
        left: 2cm;
        width: 17cm;
        top: 2.5cm;
        height: 24.2cm;
    }}

    body {
        font-family: brandon-grotesque, sans-serif;
        font-size: 10pt;
        font-weight: 300;
        font-style: normal;
        line-height: 140%;
    }

    .titleface {
        text-transform: uppercase;
        font-family: brandon-grotesque, sans-serif;
        font-weight: 900;
        font-style: normal;
        font-size: 53pt;
        color: black;
        margin: 0;
        padding-top: 0pt;
        line-height: 100%;
    }

    .subtitle {
        text-transform: uppercase;
        font-family: brandon-grotesque, sans-serif;
        font-weight: 900;
        font-style: normal;
        font-size: 53pt;
        color: #F26E3B;
        margin: 0;
        padding-top: 0pt;
        line-height: 100%;
    }

    .titlemeta {
        text-transform: uppercase;
        font-family: brandon-grotesque, sans-serif;
        font-weight: 300;
        font-style: normal;
        font-size: 24pt;
        color: black;
        margin: 0;
        padding-top: 0pt;
        line-height: 100%;
    }

    h1 {
        text-transform: uppercase;
        font-family: brandon-grotesque, sans-serif;
        font-weight: 900;
        font-style: normal;
        font-size: 24pt;
        color: #F26E3B;
        margin: 0;
        padding-top: 0pt;
        line-height: 120%;
    }

    h2 {
        text-transform: uppercase;
        font-family: brandon-grotesque, sans-serif;
        font-weight: 300;
        font-style: normal;
        font-size: 24pt;
        color: #F26E3B;
        margin: 0;
        padding-top: 0pt;
        line-height: 120%;
    }

    p {
        font-family: brandon-grotesque, sans-serif;
        font-size: 10pt;
        font-weight: 300;
        font-style: normal;
    }

    table {
        font-size: 9pt;

    }

    th {
        table-layout: auto;
        padding-top: 4pt;
        padding-left: 2pt;
        padding-right: 0pt;
        text-align: center;
        font-weight: bold;
        border-bottom-color: black;
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-top-color: black;
        border-top-width: 1px;
        border-top-style: black;
        word-wrap: break-word;
    }

    td {
        padding-top: 4pt;
        padding-left: 2pt;
        padding-right: 0pt;
        text-align: center;
    }

    img {
        vertical-align: top;
    }

    ul {
        list-style-position: outside;
        font-size: 11pt;
        padding-left: 5pt;
        padding-top: 0;
    }

    figcaption {
        font-size: 9pt;
    }

    caption {
        font-size: 9pt;
    }

    .footer {
        font-size: 10pt;
    }

    .vt_header {
        writing-mode: sideways-rl;
        }

    .tiny_header {
        font-size: 7px;
        }

</style>

<!-- Loading JSON data files for access -->
<!-- TODO - these will currently break because they need to be created/added to the precipy index -->




<!-- Title Page -->
<pdf:nexttemplate name="titlepage">
<pdf:nextpage>

<p class="subtitle">OPEN METADATA SOURCES</p>
<p class="titlemeta">
COMPARING OPENALEX TO CROSSREF AND MAG<br>
DATE: 22 FEBRUARY 2022
</p>

<!-- switch page templates -->
<pdf:nexttemplate name="report">

<pdf:nextpage>

# Executive Summary

Here we write some background stuff, probably using the abstracts we have I guess, can also include some
summary statistics and other useful things.

This report was run using the following tables as source data:
Crossref: academic-observatory.crossref.crossref_metadata20220107
Crossref Member Data: utrecht-university.crossref.member_data with date 2022-02-14
OpenAlex Native Format utrecht-university.OpenAlex.Work20220130
Microsoft Academic:

* Papers: academic-observatory.mag.Papers20211206
* Authors: academic-observatory.mag.Authors20211206
* Affiliations: academic-observatory.mag.Affiliations20211206
* Intermediate: utrecht-university.mag.mag_intermediate20211206


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

Therefore it is of interest to look at a specific recent year, in this case 2020.

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



### Affiliation strings

![](value_add_openalex_native_all_time_for_affiliation_strings_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



### Authors

![](value_add_openalex_native_all_time_for_authors_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



### Abstracts

![](value_add_openalex_native_all_time_for_abstracts_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



### Citations to

![](value_add_openalex_native_all_time_for_citations_to_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



### References from

![](value_add_openalex_native_all_time_for_references_from_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



### Journals

![](value_add_openalex_native_all_time_for_journals_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



### Fields

![](value_add_openalex_native_all_time_for_fields_by_cr_type.png)

The above will not work on windows...may need to figure a work around for that



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
