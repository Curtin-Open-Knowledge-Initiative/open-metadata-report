
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
COMPARING OPENALEX TO CROSSREF <br>
<br>
DATE: 03 JULY 2022
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

The report currently contains all the graphs comparing metadata coverage of OpenAlex compared to Crossref, and of DOIs vs non-DOIs in OpenAlex, as well as some basic tables. 
More explanatory text and interpretation of findings will be added in a later version.

Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20220703_2](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20220703_2) in this repository.

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

* Crossref: academic-observatory.crossref.crossref_metadata20220507
* OpenAlex: academic-observatory.openalex.Work with date 20220612


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20220703_2](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20220703_2) in this repository. 

<pdf:nextpage> 

# Coverage of OpenAlex vs Crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7a\7a6fdbcf1a8592029a729f8553d0e53a770309e0a413d8ab5f6d96ed0ad8ad23.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d2\d2cf8eb5bf50c2e2c29a909087b75bab0a80cfe7b094e2d866970e77f0c6a6b9.png"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - 2022</td>
  </tr>
 </table>

<br>
### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\92\922368c79714624e528d72ab62a03c6ddbdd5207f00e831a87dce09f08807d5b.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\01\014f8776382896bf5f0003cad273f725214816592b0bd9fb06827f472e6f2656.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Value Add of OpenAlex to Crossref

### Overview

Comparing coverage of metadata types in Crossref and OpenAlex

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\07\07ed41e1f144de95fb67e0830d02ac2624c0fc1971330d7a277b56ba8e5599df.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0c\0c91ee9ab3205d223f94639b48d35a52936d5be4cb8ec7ec08969e8a5040cde0.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\cd\cdd0acbfac3b347c06f90bcec2b8463d9fb67e2baf41d5781e2182046816e3cc.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\11\11f161f0beccadd6a52da96db4dde377452fbe2f7cf3fc92f653f19df44d293e.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage in OpenAlex and Crossref by publication type
<br>




### Affiliations






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\19\19fbb6b067d0a9ecdad3ecc6e7a5553a4b6bce15b21bd44bb6f9041a38d84e7b.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a4\a4e05685d04e1c7336482d400ec645c8b08c063fd9af5b3a7715426a27647045.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2f\2fdb9b48ae1d7606f0706d42ab4d3fb6733818fbf1af319097ce7e4dffbc1f5e.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\55\55bde9969527077cd380924e7522957322fbeffc671a0adb535ba30a16e10209.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Affiliations ROR






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3a\3abf5675fcec765ceb4e72d5f9034bbdd368ff721e12d213ecee303c8504fc99.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2e\2e4f6df3e6ea6a70f62d522226639ede7e089f09f326d08a888766621cdf02f4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e2\e2a221f48f4650d1e2b845cc1771c637e12489afbedff246f59f672da03e0728.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d9\d98935570c75a30aba92e83cee17db81533bc7c1b7f46245191a29881255de7e.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Authors






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d8\d8b74dff5a12bbd0f54dbd7c442905c334f509b660d7b265c669b42271270615.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1a\1adff52969cd6953e10b1f48f239efe08127355806c6277f0b2579fbe27ad842.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\85\85dc7043292073d24523300fffd36ab9deb523753c0f688f3fb78e809659027a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2f\2f017918125d1c78b688c9dca04fd474dbe01274609b685f0f6f9f44ba74726b.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Authors ORCIDs






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3d\3d6ca733f1919d19939ac62a376e3cf59d34951aa65e3b397646241d0d7498cd.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\50\5045bea2f8e8b34e423ed6e6026518e94e6a3481a2ccf83ecc7f3599f677e24c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7e\7e0110bc4adc0e7dd90508acdc3483d3f98d26a6b6da52174e5933dac93354ab.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a3\a36c039b071d49f41851b70589f9d87b523f3f0b3a0ffe343464a433b00eabd2.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Abstracts






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\19\19a8298883ba9e34247249c421381d3c23ca9d5a40a0fd216be4bcfbaff1df24.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a3\a36a52e58035ef0c26b7fabc5be445e7ff1aabe540478affab47896ff16331fc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\be\be8f7c081e4e606f950238b071ca200d58cb11891b1f02606b912f4a039a7cd3.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1c\1c0097989c774ed16fd5bdd25f7a80c2db4f8b68b4024563ed60f5ea010123f4.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Citations to






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\21\21c947cbeecd93b9fd46ddc216d588a49a4d6aa93bb952ab3b33a3fc9a848895.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f0\f0e6e4bd271dc25dd71718238406225d80713af1ab41430645877679eb10e99d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\81\817afd5794f4bbf64e5e74ff853c32b4c836ffa76bb828f597c9489b1970a5ce.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0e\0e2e871bcf3c5f51ba324e4284355d0c1fed713ace73b02ad444facd992a50e8.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### References from






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b6\b6cf527041118a9e9898fe183888e5d17de902db32c79c1738bba7a74d122b82.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\71\71e0db9130d87f524576161849cf19bfe465e6c994fcc67bf15fb4f0465acdbf.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\73\73e777ea572815aaa439a55e80ea5e8bdafe6cf079bae0e318e5641812a1d880.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7f\7f91f964baa28a4793b1c85466bd2d79bdcf4ec217164bb3a3df9d7f65c8d154.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\68\683d9aace349f5017d973f52fa97cd105fd19a978613eec3fa5574e192692df8.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\cd\cd470968bbabe4be045df342016579b75fd3c56a498b059baec429e8cc7ed9d7.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ce\ce419d416397e67d9ca1c18d1938869ed2409b47997c790357d50066c2588f31.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4d\4dc565626e6d3d33b93dca4590550e4a4043b8e4ad85ad9dd9da7275902159f4.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals ISSN






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\08\08561d8a99dc5bb1481fc6e8286325e086d406853ef577a82095c8b8c1906ac1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\60\60dbf3c59c8391202c4a1be1695f5fbf155a63e7eed149afebd345945065ea44.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\59\59d5efa8cde4bb7a3f09947ef1a07cba6afce35c812b65589f8bfdf3737f2dbc.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\03\03ac4b86f423688b9c0d69a9dd14186f809fdfbcba3073d3897773287aa7b5a2.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Fields






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\66\667c6f65deb94265fa2da54b384fa8e7f8bb87a5bd481d478bdf44cb3f94b96f.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\56\5656864bc7701cb3a5c85f2b25a3134ea94afc2e0ed4e45e9cd261e8aea89dc9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\eb\ebd292da7c7e410e555d9138ece4cd4813705b04eb9d7674450e433d45198830.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\fb\fba1e5367e75791212151832ac48e28d8608381663671de3b27351d635dab30c.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2022</td>
  </tr>
 </table>



<pdf:nextpage>

# OpenAlex Coverage Beyond Crossref
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c8\c84f26b76b82b58cc1ad9a1a7674fa7905d6960b4ddeac5347b51fea14948f71.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6c\6c92d3703af4f67b71e0b94b52d75a1f5cf085dd78a83dfad1f2bd1f4b05ee77.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\04\045a763f7b88b72f8dcb5449bb05a1e11fa7b7ca096f251c734a30c4d1075304.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2b\2bb37e4622745a018f75789ad815e6ee99aec79e759f4f389e80ed6d453f2dd7.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage for DOIs and non-DOIs by publication type
<br>


### Affiliations




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\64\6454eded104f20739b1977ea63e233f7052d5ce25567c2043cd8dd638725b36e.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\52\525e342abafb8f6400e70b007930daf518604bce4d9dda830e42ccf8117a96a9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### Affiliations ROR




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9e\9e2ebcd5cd6b27a8e2980b002d344b62df4adb173ae0cca196626a6d37963500.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\81\81ac080e0eef9a96c2afc23e7738a576c424d29e21512b2ee8f68b18559f635b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Authors




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\59\5906ac8e61688d2d53193d242a5dd034982755d3efb7077ce107bdc8723c584b.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1d\1d5fdba946763a49e366cd13f46284cefb49c1c24acd8ca63f02a5230a4af435.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### Authors ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c6\c684596051c2d3a928f270d3e9521f465faeac9994d1018cec2980dd623dbe99.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\fc\fc9713eac01129f4d2664b571c51475686a06381d6fdc3c2997173529bf7c0b3.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Abstracts




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a9\a990429fe40dc2f4196c3b1e0ba3c280b9de73866e949308a9a60482ef67e590.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b7\b7c89f24621993e65d87b1d467c68110ae9242333a7489ba2c538297f9eb48db.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\56\567ae9fa61a326ff35e0b816191a6f04be13ddf04ff48162c21644c6253d501a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ec\ec2c76ef6ca95f2a5e3ca6e3d53316d472228fbcca6a214c1bd703fc022f57bf.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1c\1c00459d51d6814e98694191f89a423c70767c9000890098d147eaea1acc438c.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\73\73c91fa90c373373243df7903198d7b88b0287e4f366ac61332089e4c9d50288.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals ISSN




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0d\0d047877f1ab49917c86aa772e557da8dd3ffef27757b0bfead90a2edcef1636.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\58\5862dbd20f9dc3e505e106e84ff7cded0ae71020eb58389db629d106b27a70dc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### Fields




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bf\bfe747f60fd17041ac70c7126531a0fe48830cf5d69b75ce1c2259d0836bbde1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b7\b7efa00a0dc3523688f93ce904fd1928f39b02e92b5bbcd016721b02f2e4cde7.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>




<pdf:nextpage>



## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = 2020-2022  
Focus Year = 2022



### OpenAlex Coverage


<table>
    <caption><strong>Table 1.</strong> OpenAlex Metadata Coverage of Crossref DOIs</caption>
    <thead>
        <tr>
            
                <th 
                    
                    text-align=center>Time Frame
                </th>
            
                <th 
                    
                    text-align=center>Crossref DOIs
                </th>
            
                <th 
                    
                    text-align=center>OpenAlex Coverage of DOIs
                </th>
            
        </tr>
    </thead>
    <tbody>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>All Time</td>
                
                    <td text-align=center>123390682</td>
                
                    <td text-align=center>121006622</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>17003593</td>
                
                    <td text-align=center>16210017</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>2829867</td>
                
                    <td text-align=center>2517291</td>
                
            </tr>
        
    </tbody>
</table>




### Crossref Coverage


<table>
    <caption><strong>Table 2.</strong> Crossref Metadata Coverage of Crossref DOIs</caption>
    <thead>
        <tr>
            
                <th 
                    
                    text-align=center>Time Frame
                </th>
            
                <th 
                    
                    text-align=center>Crossref DOIs
                </th>
            
                <th 
                    
                    text-align=center>Author Strings
                </th>
            
                <th 
                    
                    text-align=center>Author ORCIDs
                </th>
            
                <th 
                    
                    text-align=center>Affiliation Strings
                </th>
            
                <th 
                    
                    text-align=center>Affiliation RORs
                </th>
            
                <th 
                    
                    text-align=center>Abstracts
                </th>
            
                <th 
                    
                    text-align=center>Field Classification
                </th>
            
                <th 
                    
                    text-align=center>Venue Names
                </th>
            
                <th 
                    
                    text-align=center>ISSNs
                </th>
            
        </tr>
    </thead>
    <tbody>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>All Time</td>
                
                    <td text-align=center>123390682</td>
                
                    <td text-align=center>104214913</td>
                
                    <td text-align=center>8375904</td>
                
                    <td text-align=center>16858936</td>
                
                    <td text-align=center>4061</td>
                
                    <td text-align=center>15598258</td>
                
                    <td text-align=center>80453587</td>
                
                    <td text-align=center>119578458</td>
                
                    <td text-align=center>97790273</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>17003593</td>
                
                    <td text-align=center>14939285</td>
                
                    <td text-align=center>4784710</td>
                
                    <td text-align=center>3546363</td>
                
                    <td text-align=center>3086</td>
                
                    <td text-align=center>5209761</td>
                
                    <td text-align=center>9004200</td>
                
                    <td text-align=center>15853385</td>
                
                    <td text-align=center>12373221</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>2829867</td>
                
                    <td text-align=center>2565941</td>
                
                    <td text-align=center>921938</td>
                
                    <td text-align=center>702269</td>
                
                    <td text-align=center>1869</td>
                
                    <td text-align=center>884343</td>
                
                    <td text-align=center>1636961</td>
                
                    <td text-align=center>2652599</td>
                
                    <td text-align=center>2134995</td>
                
            </tr>
        
    </tbody>
</table>







