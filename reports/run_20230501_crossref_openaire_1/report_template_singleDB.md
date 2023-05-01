



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
DATE: 01 MAY 2023
</p>
<br>
<br>
[PRELIMINARY VERSION] 
<!-- switch page templates -->
<pdf:nexttemplate name="report">

<pdf:nextpage>

# Executive Summary

In this project, we assess and compare the value added by OpenAIRE to Crossref metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 

The report currently contains all the graphs comparing metadata coverage of OpenAIRE compared to Crossref, and of DOIs vs non-DOIs in openaire. 
More explanatory text, tables and interpretation of findings will be added in a later version.

Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230501_crossref_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230501_crossref_openaire_1) in this repository.

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

In this project, we assess and compare the value added by OpenAIRE to Crossref metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 


## Data sources

This report was run using the following tables as source data:

* crossref: academic-observatory.crossref.crossref_metadata20221207
* openaire: academic-observatory.openaire.publication20221230


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230501_crossref_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230501_crossref_openaire_1) in this repository. 

<pdf:nextpage> 

# Coverage of openaire vs crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\13\1371feba536c4522fd98bfdd8a03b217b4f7dfe085c4ad5d3809f98714431bba.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8a\8a3d68c683235542109b1c9d5abfd3573cd5a23bb4dcceda66ac8a384d083c20.png"></td>
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
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ed\eda7926b595d17c7eb12c09ad3ab410d78b8014318a80daef131e1cecf29412a.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f4\f4f234bdf05505659a75556b2cd9215a2343c5b95a7fd4138cd612130cfea104.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\87\879615c9814b23f3e4027f58220745368c36e335f18f091afa787edf3724740c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\08\08e5dc64f0560896a445d66069e5b3f6521741629454af51aa653c295fccce83.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4d\4dad2d26c8bb663a971f11fe1f0d4033a4b5080189475c026da554485ac2297c.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\61\61034155e94ff353dd661def0d239ce3d89c2f5b1d1592524665c30698978c83.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\69\69f0c718d5e3f64fe03b104c5d9e3d6938836df628ddf2a5b97cd2e760c3905e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0cb9f32d371b3104752b47fcc44bd1cb1fc3b003c9389854f406f33013898ef4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b4\b440b0f9e92b48ff3cdf69a7ef36160c56b9566742b4d461dccd1cc28b2829b6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\27\277c31fded30c42006ede0824a9339ca8532214a85a6c16ac7ca12ee4b0dfad5.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4d\4daef06f6e25dc9e46707a4f466d84693f3c8874e36fac5b5c043d6cac8f1bfb.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b0\b0888f0919af948605df4a8cccd208f1dfe2497724a5153531e8975b1bacc5fa.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\11\118798263e587b393a6f28cbc1198ff7921d66232947f767ee4c2273f1697238.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6d\6d2873838b68f17f730d191c268ac79b55a376638f5e8300364f4a638bd531c4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5d\5d8ad9dafbef4edc8594b49ad19a3fec2bb87f75287c1d86a9a5bedf978dbac8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f6\f6dc35584dea42e5b835f41d8bb6b4ad1c328a92954b2e2eb7eced97eee9d387.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1e\1eb87afd17746966f9abc9c25393ae2864228283850b5b13245a8781cf96ab79.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\55\556b700e59d26b6d72212f2abd099da9ef56f9da49a6a9fae913d4912b657427.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\70\702f7238271531dc6600ad5b1e3c4126be78519c445bb255a0b17590eb7c6e86.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f2\f2e43515cb0e3f7db5818f720e26a3033f0c0d0af7abf3d46c20858cd5af0d73.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ea\eae20427ba99b633722e0c9b4b55a3a0dc931f7d7b5a6947c84c5d5f8fadd93c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\55\5576cfacd38891f114f8a2e82a2cf946f58c776be53df4e0a8c49320a50dbb3f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4f\4ffcffa5bb7e673eb699f56b4bc0776c49ba81e676562fd387e19baa1fc2a68f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\00\00fc8a900af8d2f4b415e1f4cd58bfc9495b01e024d7d7e19fb67a8065ac32da.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b6\b6fa022845b554aece08d361e76b62fc4f10530f2a009d7a90baffd998aa5c89.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\96\964060d7caa62275f0786597101f2b99d80a92c2d056f2cea09ae6b8ee1654b0.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ec\ecbf19d729ac6cac27feb449b728a23b47d49b85baac7593756bb6cafecb4524.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\58\58368e262b938ae391a24c74482a6f3024b0d3d179e8c4476b775f2204c26228.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2f\2fa567542b72c051358ee44251467f0ee2dd8d44555e8a7fd2d66c228003cc20.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7f\7f4cf032bc1b0594f498dbc0e21a69c0e9de59979884324874bcb7ed08d5a993.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\56\56dca93d53a9c6748716ba95f62b1282243f78c705a96fbf2c81004d553e9e52.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cf831a2dd683dce3eb2d60e63c8ecd0e8838ab544017ecde2aeaac2f4e4db05d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3f\3fdee6869b6b5f22abf51f1b0814ae6d661432ecfeef377415d03854d608732f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e9\e9e7cf8e7f9cbc6596ac5a9e872f0fd1ec8752af143ce914fb484e7731fe5a15.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1a\1a88eabc72ba9223dee17b2b72450a08af33d3ff57d61eb4b360206eecf050a1.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e0\e07b3c76961fb33f55afa0e650173aa3ec338689a7f79324923641f61985d0b2.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4e\4e6b084cf98085fda98d0f83d08c39d18db3a9ba469eb4fa75c8c3590fa84eaa.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\eb\eb0c5f8e444d70d4db17c488486e9b6f9f42e2f2832f61ff69f6761b57139bca.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\99\99366effcd223d81a57308df2521e50fb4f66255dd9c322f08b0fc3d3617d857.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e3\e38723617f36f59357c2789ae8bfd07df82e69dc8b202ed6c443cce99d13ef87.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\26\267bf96804244ee3568b40ee0440424328d982b7a7c2cc722193d6650f135715.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ff\ff6b2b96f2a513c1cf5aa41b2ce50fe3d3aa3d142a0b073651645234aa0a1f0b.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\52\524a620213283bed08860a80b72e8a062cb851f38f1a6755195da15bfe4f9275.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\26\2637b7fc14fb75c6a77dc0be8da6bb26ed7da3190cbb44ef915837627c6774f5.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f2\f26355a2c4396bd1cc2002fe9f191bf5ac46128a5881bba3a1a483e2031d77c9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\53\530d48d1f3e65db99c78f5cb4394c8b47ce59d8a967bc9ad7729b8308c442027.png"></td>
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
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\82\824d33565f136eb98100dcc549eee9f13fe2fc68712a05242989f919f8a55233.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3c\3cb7200b4a0741ec05930a509d720ae69c80734f481bc23e6b7de89cb49b2d90.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\99\99281d5618b28b9c38b1c26212f3007500a9e82ae4df965ced100e1de579a9f8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\67\674150f35475c0eb1dc0ec35b872cb3545c8eb8a3fbc85b1459eb9cacc0a1aa3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0c9c24254561fb552fedb7e06591cc844f1cc2009681d5e83cadccd7d81d1e3e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9a\9acb7274201d68df101d79f902e6dc26da1e86c225e2a98e5cbd97504464360b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Affiliation RORs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d6\d68fe32da923106b58d0804869869fc7f07e40b61be049383cba357527e33ec0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\97\97d0576114ace2c392c7c0d39a3a89963b83a141937480add74dab2c41de3d9d.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\69\6989edc9d4851d1e7bdecaa56559e85ed6de36d87fb8555513465a734060e660.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\30\309652d7d28167d20883cd3e1ce655817ae4a5beb77cf57d8ac2b9b87d131802.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Author ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0c78638a2a1b43723a3a43aedf89d78c94aa36558de70f51c3b805f0668ace9e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\dd\ddbba067fbd51ef007122e665e4942ba84ae9c33b6860987bea357c0830fe258.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a9\a9a12fc3255e60f2de7ae080299c20e817aba87b5642ec5b764128fb224632ee.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c5\c510dfc76ce7eab77b82f829ddc5d2bf5a5ef3d8831fe10d23dc03725a681e83.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9b\9b24bb411cd72d2c3248241f55d9c0d178e4c511f406b21912e3e696e7bae703.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5f\5f30ed99cd9e2e9fda119156cd55b4fda532a84065e5d74269722d0b88b86541.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\79\799b0ed8d67d7b5f7afec2855c180e7960c76e20492b1a13e2f25d7af5d43bee.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5b\5b9de3d875f1471e63fba704489f61800278bc2ccd5719e5e2f3455fbef364ac.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f4\f4d8f9fa08e9b6d6963015e53a05062e4ff7570772c0006b94a1d3162a7c8ca5.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\74\746c986f19649fccb9f1990f3e4e8cec3cd131c2b6a53df876641b591f3fefb4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8c\8c1b159c8c6be2ff0fc7c6dab6c396c7a98acf1c2c4a7d8b17cf256b913f7724.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a0\a0d359ded1e81c659bba874a6ea93bdf02f2f94b686dcf76158f172c15160a5e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue ISSN-L




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7d\7d492be441c571160313d6ee80ff1c40e15394bf1aef960228b3d8d9a1fbcb5f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6b\6b47cd2b8d82fe3f1410a99f30e587391c32c6c546d2a106463566f11c2d8345.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b1\b1a380f2ba839d48398e3dc27958c7f1b61ba1b3ba0025f887f90b1e79e85961.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\80\80b632ec1c251a10e988dedf5a7f8ca2ac719612a9d42bdec502e57b03e6056e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>








