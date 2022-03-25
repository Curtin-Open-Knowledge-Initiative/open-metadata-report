
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











<!-- This is a stopgap measure as will not correctly display for first run w/o suffix -->



<!-- Title Page -->
<pdf:nexttemplate name="titlepage">
<pdf:nextpage>

<p class="subtitle">OPEN METADATA SOURCES</p>
<p class="titlemeta">
<br>
COMPARING OPENALEX TO CROSSREF <br>
<br>
DATE: 25 MARCH 2022
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

Complete data and code are available at:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
with all images and data belonging to this report located in [/reports/run_20220325_3](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20220325_3)

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

* Crossref: academic-observatory.crossref.crossref_metadata20220107 
* Crossref Member Data: utrecht-university.crossref.member_data with date 20220311
* OpenAlex: utrecht-university.OpenAlex_native.Work with date 20220130


Complete data and code are available at:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
with all images and data belonging to this report located in [/reports/run_20220325_3](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20220325_3)

<pdf:nextpage> 

# Coverage of OpenAlex vs Crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ca\ca105e61f98c8798a0c31a0a9e0f79b45c123cb01310cdd17f03d8aab0d3c252.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\52\526d88d6ae2f042c478209ca5709afd66cc01bf4ef5825db44d46848ab7ef7b3.png"></td>
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
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9a\9a7af9f93ed972840ad0557e66de0da6bc95ea1a38063d4c663a69a34e08ed53.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\dd\dd19a6d6bbd2277f5d3830a144684d105ee143004a8ff8763fbdb73025c51b52.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\73\73803d2e36110697d1f393a4c8938ca35440e64799f340189ff2fd621c005655.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ab\abd91ee536576c6afe167eb0b82b20bfc24e0912babcc559cf3cdcc34ca631a5.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a9\a985d4ad85d574f626dbe7d9b6a69a68871aeca47f52b698c8a026cddc1c432f.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\50\503f1e14a7b85ca0ca61c086e7c14c1c6927acdea7ea8ce3a82b379ddb9fe5e6.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\49\49c8681deab64400dd8472a694d2bd4365a9262a95a9b3c14df4ff67dd37c016.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a4\a410000528afb7ce9ceb3020577c30a5d70556c579acb79920cb1ebb13c9594a.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\33\33fb35fe92d0dec72de9b1bb8bbc027fcc91f5164629ada8b4f34395a5cab252.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\95\95435cd9a94845125f8553bed6d06bd590a9100fd1b902a0ec944d3b87ed61e7.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\aa\aa28ca26a3e7b2807bdb681cee5354608c86866d4ebc0a827903ef6a5e0f1f8e.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\06\061a915dba5f52af798a1aae2a715fcd6ec70b3b89b66cca9405f9964a3f5d35.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7d\7d023c18b3ed4bf5d607099bb4706d09924121e5df02cf2ae3a6f67ef84a6b49.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6e\6e953363713707bddf0ce006ea44153570bcd94a7ea3253ca08bca844947cdb4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6e\6ec1eda616efc5ec5938cb4a37187007ae1c65f2455ccf53b6ce4c0a4904c079.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\30\306f70326594e6d4e2a9ef73ce5ec1a547aa5c63e4fb122f15d74abe3b76c4dc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\12\12a6c28797205058be221c1567c3ddac600484c29693552d9e24a85ea856555e.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\93\9376b72401352da0b6220e3eb1692e7f3069b21da36cbd651187879a27bf8d49.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8f\8ff5ccf26448ff3ebba26e1ed0b7644f5d0f0aaa56cbc1a5687503af94739bff.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5e\5ea2ed0fc3e46af9be877f1375f02e28384e8c394b1eaf7f33e334fbd4fead5c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d7\d72e364e993b001a5f5a9f50bf3ae8360b8bb40e1412da33b967bbfd35db8de1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9e\9e52b3d5ff14e9255051e5275a72b6dd55193abd3e54ee06821e6a3103e9f2b2.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0a\0a8c3a6911582c5c3975b9b949588e24b1d3d46c83deed49fa8eb32deb80114c.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\70\703345e1f361525cb2514b3d5bf4ae3f4caa0d4d99cea1817a9a1806b463a13e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\98\98d7549131c515393c7b297e8f24597d2b75411401977204d53ee1b5a529eed5.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\66\6693ac710cf6d4518f4f543b7ba607b9bf5af2b955bc23990f30f4b05c41bb7b.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\91\91788d6320ba46b93f953d36a5ef4273da09bad6031ee21e73bc50c24436340d.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\95\959c9665a61ebfc2adf64472e674c126d7a95e91fda7ac0cdcd303c96e327325.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5e\5e2ae63d3961e12e0f1d17b099f02f9cefb08f6929445861c0cd077906bde764.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1c\1c2627e1f6caf98505a0e49571fe8e4784f9585f9facc1457c374790e422efb7.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\32\3250c877fce1522f51a5d89d0ad10f2fc79eaa096ac53bf7fdb7e238fefafa15.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c7\c79f2f90f6b486a153d667ccffbdae7e8fd98c605628cccdb8f10d2aafc9b13c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\33\3340c00ba74ed78221bb96b55ba45701594aa84f2b8af8a27a0638cd6eb09824.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\16\165e187e2a88f051d421af1c9a3fde922cbd3afb48cfd678b2fe0999547e19fb.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Open References from






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\76\76b9b5b4bd5e21ef6d38bebe95470b92eb5c80690ff4198d422cdab5d4658f8f.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6b\6b26985e6fd61b5c9d926564c1949472aff409c1169a1fac3bd6d2a4a20505a2.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\39\391b5163325ceb03e620a203b9dcc716c6d8f0df288665dfa88e3c46f02ae4b2.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\25\253d759b1f66f80434394cbf22dc6e090c0a4381c327e84371f980212ff70ad6.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\20\20b3d12b53e08f1f8139bd462f7a9f8a47bdc314b9631f08b054bce5bdba2304.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\74\7412314bdad48749e59f2b18e76506acd51ba2d37ce6f60cbed3517909c35ea6.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\80\809fd048c725276a9375288e9f2370c1be46bbddd820d4d56a1b0a1e1eb8f75b.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d2\d2e40981a8e4ed43eeca5a9a62ea4c5ef6e87b59ef2c37f851809285e30326f1.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4c\4c13f2eb53e36de08f3dce3f05074436b3ea0470c0b7619fe24dd3b9e58b6e29.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a5\a5f4fe921d1c0c7be6a26b718a98a92d09d35739657802999bede5d03f32ab1c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3c\3c34b1f51f4ef9552580203785f5ee862eb3879d38b381e99526f7413f4da767.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9c\9c17f51bd84caafe63ad237874bc6f24bafdd040fdba70bf9ac8ba16f74e4443.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\44\44ee1b7f55dacbcc01bb61e6984f735b582962b46b89b0232ec5f066c94e5ff0.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b9\b91be6b92aa06f051720c6d7dbbb38cd7ef8adfcb580bd807452f74b03dc9d68.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d3\d3efbdedf00588a144ac9c76d6ab1a0e67f51e32c8e9e86996f30384ad00af22.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\50\50763c3ab5f08c3540125123019b4b41007d41e5bdfb23ed5e65387f09e1406a.png"></td>
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
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4a\4a2d86b424e17ad456e02e7bfca89a6c7e0c36edf8b72edc90f57aec3d03eda3.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\cb\cbd41035cac1d187684914546fe0468f5a8938cf3c05a9c3504d561df28e1263.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\dc\dcb1933dcb54f79aedec712dd024e131b73d79a5e3d21e28a061dabf7a374fae.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\cf\cf609307e876443b83ffa247e48277451dd06a86b2c8c59dc9dd712d0357e6d3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\20\20f4a5f14bf60fbc6cc683b8a410fa23fe35f68ca5125f1fc440fbb6f8294616.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\02\023ca22bdf7bbf8c9af3163cb5b6d4bfe16e66c5873029e0ae5d269ba88913b4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### Affiliations ROR




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\11\11b999d85b2573adc18287c802b5e946b6c9a4a6f1e57e7e7c65665d638ccda9.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\63\631f8ff035b5102e55ffdd3b111d496b8863b84a7f12d60a4aead46281a540ac.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\30\301a9d3f04d8920b85eaec936c93909cc29f37978b90f0114243adda4116be24.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\39\39747afe45aa1d1d0e24198cc9559be0cd79dd875ad139ccc37e9815dfda028b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### Authors ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\aa\aaa0bd310ff97ad8f7275179d6b666101e0a280e39638bb71f648fa6badb0bd2.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\17\172457137f8bc5eade0b1f8e69dd75d8a75b411589d2aeb04a20d982583d9cd4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\54\541db97cb8b385c94cee17f1210840b21595f324e5635a0f378f33b6ff4275a3.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\78\78fea4de7a96aec5a52c3c7145226755ea414b517408f42e9750845aecd7f975.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b3\b3cfbaa36c78b759ffe05c11ed472d3418cb0ed7da978ce52aed9cb8487b72ec.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8f\8f8ebd981309d2046a41855871be5d8ad79a73607eaf45b881170c15d86fa23d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2d\2d6fbba0ecfcc5a5ddbc7855f5290e20b64c7f4422e124308acd92d21868b4e1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e4\e4048500a92f5a32b9be7c2da521e1162cb10c8c823f8a6948ad9d9a869b6d81.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\51\51640267292577110e9bb204bea43043fd57d610cdc5d6fdbf0e511c3b3b8ca4.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\38\383652e4acd9f3854539ce73c1bb79580e941aa7c8aff92bdbabb911eb01c49e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





### Journals ISSN




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6b\6b44673ffc5c0af1f74737939db83e9dff5a37bd0a4925f43c06af68e600f1a0.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3e\3ec255457bf18bb509c7dcdc6ea1f516609481db9b8dd481515fe0a9e6becf25.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\73\73b497db7e08e7f4ae44257da350ea2b8f3ae3fb76a703faa78bb791caf840f4.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6e\6e0ae141884e652001b265a977a74da075c866da51957b26a4cc0daf39c82e1d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




<pdf:nextpage>



## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = 2019-2021  
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
                
                    <td text-align=center>120141465</td>
                
                    <td text-align=center>93393648</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>20058172</td>
                
                    <td text-align=center>16016838</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>6845252</td>
                
                    <td text-align=center>5535386</td>
                
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
                    
                    text-align=center>Abstracts
                </th>
            
                <th 
                    
                    text-align=center>Open Abstracts
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
                
                    <td text-align=center>120141465</td>
                
                    <td text-align=center>101589631</td>
                
                    <td text-align=center>7654447</td>
                
                    <td text-align=center>15929784</td>
                
                    <td text-align=center>14187606</td>
                
                    <td text-align=center>51699495</td>
                
                    <td text-align=center>74432176</td>
                
                    <td text-align=center>116534739</td>
                
                    <td text-align=center>95732822</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>20058172</td>
                
                    <td text-align=center>17496450</td>
                
                    <td text-align=center>5173497</td>
                
                    <td text-align=center>3936403</td>
                
                    <td text-align=center>5518678</td>
                
                    <td text-align=center>9249685</td>
                
                    <td text-align=center>9862613</td>
                
                    <td text-align=center>18832104</td>
                
                    <td text-align=center>14626037</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>6845252</td>
                
                    <td text-align=center>6101054</td>
                
                    <td text-align=center>2084965</td>
                
                    <td text-align=center>1369435</td>
                
                    <td text-align=center>2271715</td>
                
                    <td text-align=center>3270231</td>
                
                    <td text-align=center>3510576</td>
                
                    <td text-align=center>6366601</td>
                
                    <td text-align=center>5131324</td>
                
            </tr>
        
    </tbody>
</table>







