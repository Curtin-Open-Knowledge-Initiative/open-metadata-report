



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
<br>
COMPARING OPENAIRE TO CROSSREF <br>
<br>
DATE: 30 APRIL 2023
</p>
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

The report currently contains all the graphs comparing metadata coverage of openaire compared to crossref, and of DOIs vs non-DOIs in openaire, as well as some basic tables. 
More explanatory text and interpretation of findings will be added in a later version.

Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230430_crossref_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230430_crossref_openaire_1) in this repository.

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

* crossref: academic-observatory.crossref.crossref_metadata20221207
* openaire: academic-observatory.openaire.publication20221230


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230430_crossref_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230430_crossref_openaire_1) in this repository. 

<pdf:nextpage> 

# Coverage of openaire vs crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a3\a34ec4c81d09301cbd546b029e3a0ab0ea5507742fcef618ed868e279f85b28d.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c0\c0a97a2f4e2ee8b5b87a3839a9d497a79041dbfae935799064b82297c0104e2c.png"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - 2021</td>
  </tr>
 </table>

<br>
### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\98\98708d576d3a1dfd422f368128ec601c9a8046fcfb9eae4d0c42fecd3a15eba4.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\53\53041a164b2d8e361f52e84d45839aeac416de24f4bef7186f6aea6a5ecfba49.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Value Add of openaire to crossref

### Overview

Comparing coverage of metadata types in crossref and openaire

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\16\161a7cf55eaad72656462060e43371b40ea1e9ab277b8516584b6c392c2b6951.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e5\e5d530f712d298e069d6ed76c208171c5f5c9bdf4f5baed644996f3ea4ccb109.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ca\caadc45a11f1cbe83655b9c0e9517a170d54927b8a663f66de7609539953a25a.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b6\b68c8f8435c3123cb42a5ad5fb8fd7de325a852e81e646002dc7b02a8f45e6e0.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage in openaire and crossref by publication type
<br>



### Affiliations






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c6\c6550d152b9f22b71f7e67917bffb9e27a280d010fd56a0505a4318bda19e951.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\15\15aa67890924bb147a8a8cb9799956d0b88c662100d167a470158ebc23112775.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\60aec18933cfa97d106a1a6842369a96261202999772af5c270f74855a524d0f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ef\ef7b371d6ea13584841819f6b11197fa6956a38be56d94121b33bcf016938c15.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Affiliation RORs






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cfb7326f25237898b35aecce5a2f581adebcfb1fcb3b5aa29fd357f1e4d640f1.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a6\a6508628034076d8e23531bf11026f8aa278876c274ae5aa7e917f93d42a4f5c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\25\255b35c6d744af261c1e4348115960e09c0f97445635134ad211a37b5f21ac0e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1d\1d70822d5bf6f356358073ada2315679db5e11469e7b08c8d00a7ccf189a3297.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Authors






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\da\daf8725db8d7d98a650969dc6ccc62416ab9048c36e9ee4056d4708a12859409.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\98\981789a5a931db49dd5c8341d076161cb4d276005fa206f88108c3118520b518.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\46\4673799a49917e20882707ee6cb2487416da11e02c6c63173b1194ca304cbca3.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\87\87103f0aa8de4a8a0a66fe791bd8c08d95437263fa5e0c168b4054fd016f52c8.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Author ORCIDs






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\de\deb23e7a2f3ef711078da27b1ef1fd0ca4de2ba97f6f9e9d331258e2d619d69c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5d\5d641ba614fa47d1de6b6030589ae905859fb7df12b77c638ca2867f07ac11b2.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\66\6664950a1a2153e914a60ed9fee1ee1e9b91985a9e9b07f714fd54d0b807dfba.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\52\52ab255016297ad99755420f5993d5e3669a0c5242e0baa03428bd2c649d982e.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Abstract






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\58\58433c5e279076f630e3e41c86a7434c4f9ea63ef3d509cd9b9971b27afb9f40.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ea\eab7ee81c462aa3525aa281a39e27bec8d6c91b864bdd881ef924b8ce406f845.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\af\afca131a3d5df21236a71d6b7ef1355d7bdf75ba9f4f45e0c4435f5174b698fb.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\41\41a5fcb982eb563f4e55d67a4a93e87f70c785eded32b5fe0f5a7bb37a8f78df.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Citations to






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\21\21196bb8ce7b9118320324e50cb1bc23b95ecd6e45f43bb9e0c88247381ecdba.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\88\88cd4cd97341f372ff536a411c949032502ce63b4fb160c20f543653b39ec3a9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b3\b31401ac3b31a04f4c91d2cb5fde7e338c84123ada377a33a1ace66677685533.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\82\82f1120da6ed1ccb4157e9f819501a635280bbf5d221b29b762dfef67b3398fa.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### References from






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7f\7f19ffc51eb1c9cd0d99da2ea34aa7edbd133def4bfaed18a83a3cc2e3f1107b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\91\91052a114d981a60d09d4a1697f8a78080892939a0e04d0a4dcef63cee636c84.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8f\8f2fe221c4d236c79d235541d1ffdb43e2d0557d96b6773f2a0b638a4c12d91a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\75\753ebd4f1cc83365cd5b15d7e29b8cdccaf39b1a94d53b1d1673bd7ede1f4515.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Venue






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\75\757eaf3f37d6fffa5363ed1951df0a7b8746be3bdc0b4e737446f62e393137f8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c2\c2f2254d5280bdb069c2503adc7da04c53bfbef840fb280fb4e3e1578d6a0cd6.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7d\7d195769a24b7afb3b296fde135f45f5d80871762cc0e7536d528939a2d390b8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\09\090c0360a9167b3a8b880c5bd35969eea6737a33f068256404a15dc343b2871e.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Venue ISSN






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cd\cd253cda1691fe44e138daa5e4a294bc10fc2e29fcde9ba27d0ef135f2d7f8f8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\02\0201c7fa6e79a8612b3707c936ce781b5631351c034a88dbd2f94bcd17366120.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fd\fdddcb44652dd8c696c1cda35947c0bc15d6558a498d919da0c3a096dbbe67f1.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cb\cbbbc4b9c2b3867f12b45d5c8c2b5e9af8a36da52a41d513ac39028fd6a1c16f.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Fields






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e0\e08c8e9abe2012cd5892f71648e76247cc6c020aea475d79c0b927790688ca6b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\70\704b439cfcc3d533f46158ca2cbbecaa26ca14d70763b5e8ac686e6be86e6431.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cfdbc88a7230df6c496e9630f147468da838fe06481d21950665a3076a2873eb.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1b\1b97c792019af8562c5877c920efaf20146bcab8ebb0742660a4a1e0d803945c.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


# openaire Coverage Beyond crossref
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\98\98708d576d3a1dfd422f368128ec601c9a8046fcfb9eae4d0c42fecd3a15eba4.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b5\b5b2831dc11de39015341552deb62dba6ea9f1c6b2abd21b402b5c49b0b345b6.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\18\18538019bc64cfa9139c65d0cf87995b2e600864f32edb3cfdc3d5bd77627acf.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1d\1d0f46c49f3554b8afc28e1f2c5082a32e34328d7871a492e29d569d53303517.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage for DOIs and non-DOIs by publication type
<br>



### Affiliations




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cd\cd76c707484a82b7780c2bfb67538325162dd8fd9666b6c4d4b847cce7f5ef0a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\72\72c25d43b7ac7451a026a9514162582c22273899e1d861068502071792b5f797.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Affiliation RORs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c2\c256ed78fe6395ac1e6fde31f7e38393138e077de0f207fe72934b03da978d74.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\81\81f5e6b18f391ba737b11260a09ce47bd3aad323d4263b80e671328b366343f8.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### Authors




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0d\0ddad726a6cbbb9abdf888113655b4db9db8ece0f8ff33846b89601e61880267.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2d\2d5cfd963476271be8920f2414a80ed9f3e6957c541c960c01d733d31441d120.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Author ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\90\90d47b9a5c0a6b77c6dfd252906562e220c0c5be0dcf10384b88eb8d1f6dbc3d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9e\9e1c23bc8dcce82e2219b07f88229af1fe99170036b3ac59d4856e44649f08b2.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### Abstract




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a5\a51a52a1b5e89d2c100e222470b677fc34cb163194d26222aca8727079bb42ad.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\eb\eb444a60d15812434e3cbb65f354691a897338bb90cdce3cc812379a8c17a9be.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\92\925ed4e899c0092b9e046ae3cb467d958b9016add3839d96e190c061e62b643b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7d\7d5186b4e91bc8b4d0931fb6afdc28d62b41b15d44803829bddc6a3383d13733.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\63\63dfaadd2b10013e71511e25272f9b5c36bc9156ac841271ae2af8477486082b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\58\5892625a44c366bb6d6f4849d058fc384aba9535805db7726b27adc9cfa3fa6c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4c\4c7370a8498f8864ce5aa1c83bc1ee0242b148a12b5dc4376b38cc3bb069e88f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c5\c51f82b94615a94d3727fd4f79d8ab8a6dc404aab3b95bd4e0e6ac04a36b9a8d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### Venue ISSN




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6d\6dd6d231b019757631a6f2cb1ed9d5525129f075086ab0434e11f93312aa1d3f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\09\0950a332a1e5b36b56d486198d0e1be7a3bd63c8c9d7dd63e2abc87c1bc6fc0b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue ISSN-L




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\de\deca172c6e0f039e447e088ba3c12a8ed5c57bb07df7572f37f7efe2dec7686d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\19\1965a78ac8136c7e8200e81ae1880919905103a3c0b99f72916ae33ad48b1500.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### Fields




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\91\913b8c58e1f0214b054017a2a47cd5154d9c501c41e008772a7e9e207227de72.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\60df32800fd27e2946b7974176531bcd1415e6bd931bb882a9472c914195e73f.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = 2020-2022  
Focus Year = 2021



