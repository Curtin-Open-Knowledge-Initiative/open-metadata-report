
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
DATE: 04 FEBRUARY 2023
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
All images and data belonging to this report are located in the directory [reports\run_20230204_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230204_1) in this repository.

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

* Crossref: academic-observatory.crossref.crossref_metadata20221207
* OpenAlex: academic-observatory.openalex.Work_snapshots20230122


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230204_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230204_1) in this repository. 

<pdf:nextpage> 

# Coverage of OpenAlex vs Crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\71\718f9fab28b1f5ff53973472e44e57a43fb8ae5bbf7fab7c45757ba2353e1a24.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1b\1ba6e68d5371f76e5e9fdbdbd49b72b6e36abaa77e16df0438acc5caf81bfa19.png"></td>
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
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f0\f03b8ed50c2a344918fcab1c3dcce9f496ac680f7812ba897c4df007a8dde51b.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\03\03e32818425de684823273167574b3f8ae709ba89d9ab3d93b5b16f96f051945.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\51\514a15ea4bdb33f4f63a141f2a586c320d950f4329e8dc35765157abdc07ee84.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f2\f252e0417a644f3241c737be42a10fbe50129253630251cdf01c8459f12c016d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\58\583953bce13e092d4691f688850fcff1f14716328f13c510a8d92464667e6cd4.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2d\2dd804d7c2e86b93973c3a8bc21829b4942e2f6517daf1f789da77db2283de7e.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage in OpenAlex and Crossref by publication type
<br>




### Affiliations






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ff\ff7b4485d2b2716305b9386ef6030481dfdb6ac79ff6dee36d54a4af74ad4ac0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2b\2b2e9e07af3d99c9337c20c457cfc7a9bd20853c8aff52775d1e0c16abea8c28.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e3\e372b43d5e3c6c1ceeedb03c325554066306421b7d2ad4f17efcccaf0ff83e86.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5e\5e1bd1fd78774cbfccce04eb21dd5529c7c15dec042b1411bec5b7959b21a145.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Affiliations ROR






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e9\e944399e421295cbcc4469c486806754403acecab4c41279c3649584270b70f6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\aa\aad06f1b7d00fd244094726798915e400577b90356b8c15b8ccea49f8aa6f878.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fa\faecb0520e434de1c212c422531530330cb139ccdadf35ae9a2f61c57423c2ce.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\86\861805ee301c01d28c127343b693d0c09c0341395ca41914938377b9a98bb5c3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\30\30cffe0bd346d0ad4a5eccc1ac485b3ba3a2e6300cf199e5f8626075c5fec6e8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4b\4bd4d8c8b082c891c9377f31dfd54c064225804e7fcbb333fc41c12351f56699.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\76\76320f2e91354b57bd32166b3eca44a58323868dc632be45e6b1dc947cead5e4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4c\4ccbbcac0267c73e5558acbfee348d67e2635af199d52c3a0742a3b76e845c32.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Authors ORCIDs






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ee\eea4b66aada74be0dd0dd0036c90c602e1e7fe98c3b4784ec83b006fcfb920a2.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9f\9f88537b703bf0877f54c6ad035a1af6060f1d4d849e798459ea925cb9cc335b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2e\2eb0aad864a5da0643c3f0a83c090ee5e789ec54c9d3e68ac4545675ca05108e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\78\786525e45f5c1fbdc6ec0040fd9366674bb56ac492a17eeef94c51a6b87c3573.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Abstracts






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e0\e07f3e96309e72454a733368277b317cac3c712ae761a81ce971ec41210d1945.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b6\b604b6c8806623d433f484ad04c9c05a7f4610ddf5b1fb2a2715cd3a4bfc49f3.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f7\f7ea1a64accba3babe78cb83b76fbeaaf32172965a38c16db1a951cdeefa9f1b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3f\3f5828f52c2d50845316699a71b42b3f417119eb3fb88be56df2d0842ba2afa5.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6b\6b40a0ca0c1ed56e052134e4b4fe345846155042e84c5c040e70400d1d9f393b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\59\5971ca6c88681e34c30bb4de2fc3ac517b5c7507b1b6cc1a78a863d7135fd41d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c8\c8588461342c1a6103850ed37175c1cfff11b74bf21ad605d82ef044527abebd.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\34\3445805e28319f0683734e57c21a49c74af8f099e5b2f21e7063d4108f41c499.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9a\9ab912f8c43e330dbb0934ffb9a6044e63c801558767fb5fedf04f791208273c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c3\c3734b256e6f5d88de2358b98f206d2b1a7aa835b46a232a96a907942d118630.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1e\1e112b7a5af3c128813ae616c9ab2e464c29c05667d84da842f73e5f77d11c3b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7a\7a22700bf5a803542cafe363b9e38276bae45a6ccc72b6aa9f3fd54544ef7c87.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3d\3d7e97afa4c9b449195098e58cd998a2d0d2954318af87812bc8cb9a2944ddc8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\83\839c527907115b28d98c791916d701d9ed08995763fe3debc81ae333ccdbaa35.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d2\d28bfbe8863ee4fc3002ab69883af89e31f1bf9992716a8cc686017c11dc71c1.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c7\c79496d712919ff64338ed94951129af8a9587a7dfbb6c923bac255d67f50406.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals ISSN






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f7\f7a14de468a80e384ef62f8fa1a8f8b94c62087a44a6ddf86aaf707fbbaabb36.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\17\17c98269fb45b492e859b6790579aa90b56998ac27e851303194a95be8791261.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f2\f2601cbba2d84ce09f330489fe2df509ce2ea4808769f39b8e9adcceba8864f9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\94\94647c23d26577a0b838dcc0c7da359719209fb40c8ee1e228974c71e2432e7c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\42\42a46dd877601d4ab5ad51ccf2c3bbe9cc938e5a40cdc03047133a2cd185c082.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fd\fd9a16d9a7b6343b65f9a80bc4a9b0287b7828830d76e6eb83e3025b1e7534fe.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f2\f2382c9159cbcfb5fc919dbf289edb3321b6f762ef2f602cd4a168d7bf2a8945.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\33\33e0d83d0b45433a4917719936507e5329e1951571ce52fe458ccdb2642a1fd1.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

# OpenAlex Coverage Beyond Crossref
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d4\d469034fe0f19aa30d9d330d38672b0e4527966daa6bb7c20bef1e4b57481be1.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b4\b4b344819d1efef56b75f989250ee7f1881314f421160f0326e3fb44d985751c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a5\a5892d673c50335fd5b56d26203f1428fe57c6864c8027861487f5ccf7da746d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\97\9708b921c50e5c842d6944dce4251de656019601b87319c08de15cefefc13fdb.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\81\81150ff3f11496337875f3150edb0bdb0f7befa20927f0747c8742c8f2c23ed6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\99\99c4011dff368c012e83337353aebe753008e5ca48371ee5e412bc3fe3a409ba.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### Affiliations ROR




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\39\39e428b79545b6fceb8d933c7e7e7012f032dce037c9e3ee27c662ba53d709db.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c5\c54aa371dee168454157c769d8d1aeb387c1e42a65143531578c4db392887af6.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\12\1245fbf6e73ac89b7570bedb6438db1886774ad44d086435f65375f1dab552ec.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2e\2e2ea449ee7cf0671146646ebfeff3328fbf04aa1a5168b2e27960f164d337f8.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### Authors ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\59\59df2839db0b9b30d49002643ecbc358d2f18fda9efd8d13dada790dd6e3a9ad.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\37\37a04699493d90bb6acac6fd68eec86b3e76a772e98fe8fd3793fe7e3eed3a51.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Abstracts




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5e\5ee87d5ee83ab65b4bc22bcf6a219339490e2f83656df8fb22ca97374882b69c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0a\0a73ade0581db052c1c7f41be98189ebd791aa08b3243c9b073786be98e14453.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\53\53f8f925aa2a93737335ad39ea16bebc3e941b36e885b1a77e3f9bf89a555919.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\78\785ba01e66803bdb527086b20de3b2fd0a26da271d4d70aaf16de64aecc7d9b1.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ee\ee693425a951fabf764ca5ef1b6845f137162c3acbf3a7b4e55db89489a7ed5f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\60ca968f73fbc7be5ee328afe551b719d34a3be91787eba9b411a5ffb7149a19.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals ISSN




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9b\9bdc34462e53292e8f83aca7062b7db39756872c7bedaa57ab19e48ac1c3e88a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3c\3c97d06e6949d75fd26502b4fa96721a8dd77c84dcc0142dbc8330197940abfa.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### Fields




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\49\497e1fb904c8cc86f73f6e5f19829907b15d7587ed5810e5d0a065c02b97aa91.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a4\a476263cf865c17cff49c45bd0005d1b78111d0d3039f02b311f29d9d3908675.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




<pdf:nextpage>



## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = 2020-2022  
Focus Year = 2021



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
                
                    <td text-align=center>129435800</td>
                
                    <td text-align=center>127122982</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>21818007</td>
                
                    <td text-align=center>20268736</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>7270754</td>
                
                    <td text-align=center>7050725</td>
                
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
                
                    <td text-align=center>129435800</td>
                
                    <td text-align=center>109134489</td>
                
                    <td text-align=center>9755547</td>
                
                    <td text-align=center>18632165</td>
                
                    <td text-align=center>14709</td>
                
                    <td text-align=center>18122552</td>
                
                    <td text-align=center>83600137</td>
                
                    <td text-align=center>125281452</td>
                
                    <td text-align=center>101821880</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>21818007</td>
                
                    <td text-align=center>19122384</td>
                
                    <td text-align=center>6091456</td>
                
                    <td text-align=center>4929911</td>
                
                    <td text-align=center>12866</td>
                
                    <td text-align=center>7047401</td>
                
                    <td text-align=center>11499642</td>
                
                    <td text-align=center>20368713</td>
                
                    <td text-align=center>15732833</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>7270754</td>
                
                    <td text-align=center>6423035</td>
                
                    <td text-align=center>2104021</td>
                
                    <td text-align=center>1502626</td>
                
                    <td text-align=center>1965</td>
                
                    <td text-align=center>2484769</td>
                
                    <td text-align=center>3823965</td>
                
                    <td text-align=center>6762677</td>
                
                    <td text-align=center>5358417</td>
                
            </tr>
        
    </tbody>
</table>







