
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
COMPARING OPENALEX TO CROSSREF <br>
DATE: 17 MARCH 2022
</p>

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

* Crossref: academic-observatory.crossref.crossref_metadata20220107
* Crossref Member Data: utrecht-university.crossref.member_data with date recent
* OpenAlex Native Format utrecht-university.OpenAlex_native.Work


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

* Crossref: academic-observatory.crossref.crossref_metadata20220107
* Crossref Member Data: utrecht-university.crossref.member_data with date recent
* OpenAlex Native Format: utrecht-university.OpenAlex_native.Work

### Crossref Metadata

### OpenAlex

## Goals of this report

## Limitations

# Coverage of OpenAlex vs Crossref

## Comparing coverage

OpenAlex coverage all time: proportion with and without DOIs, overlap with Crossref.  
OpenAlex coverage of 2020: smaller proportion publications without DOI, same coverage of Crossref

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\86\861c7d0605e2fc37d15c80987bec37cce3903799e01d045c4eadc0769bf5a553.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\46\46e06d8f9c163903386f00bdfaaf6f6480f091c3ffff458dc1ec752a22306a66.png"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - 2020</td>
  </tr>
 </table>

The proportion of Crossref that is covered in OpenAlex is stable over time, around 75-80%.  
Coverage in OpenAlex of publication types in Crossref [describe]

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ed\ed7f91c75af0f9ea56ab80295417c5b56541fdd61fe48cce5111b42bbcfb863a.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\58\58cef39b1ea5ad1f54cd3ad459bf6296d7d8fb6af87e12220fe5f0eb9505b3f5.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Value Add of OpenAlex to Crossref


### Overview

Comparing coverage of metadata types in Crossref and OpenAlex (all time and 2020) -> describe differences
Added value of OpenAlex for different metadata types over all publications (all time and 2020) -> describe differences

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6d\6d94935a4a39af3ee86956ae4503bc37b828fcfcc65039f00d4f4177790a810f.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\66\66b5042917b308b1dd4b23fa34b49fed66b455394459f9f1b876dd6229548a43.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\43\438f543c9f1cb8ba97264d131e83a2a159d514271b32029c456a2ed6d9409752.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1a\1a41ecb04562198f28299b89e0be874f5194f907f7b09ef65654844d9401d89c.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

We can do loops eg over the data elements. But this might be better for a supplementary data section as we will 
presumably want to actually comment on the graphs themselves?




### Affiliations






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1c\1ce2cf5959fed7e0ce71e35579844e19e442dc3ae7a797dd4cdf0b372abf5025.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f8\f8d848d30f91e8eadb136713bc1683e469dfc61bae90a613f8dd0dc20af3b023.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d0\d07e1a201303cac90d0f7945580a1362d0a4097d5ddf634dc57866591e5f15ad.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\94\94e9644ec3b5d33833f5dab4081a3322a714d2cdbbb5dd421881f6c942d20e17.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Affiliations ROR






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\35\35e0668796bc438924e05d271699882a2960fc482783a60cbd2767f95958b7b0.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8d\8d23a4425de4f4793d3f88309629f2ee1d0839d4c9ac043553c82074cef6c328.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\28\288635b47c174e0d0fb350a1d8b8a65338b490e00c97cf41e690d95eea7b36dc.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\da\da629a9526dc892bf912fc32df0aafe53e2a21fb6c151e925e17a40d0f75deb1.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Authors






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\35\35cb9f11e618283af76baa5c2af38bd1859b96aa665e41e4ab1c4971e9e916d2.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\53\53cfbabeb4d1b098cbbd27b6aa902241d39d16da733e272e37c3169b5552becc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\17\17a71656d5174185cb697785eaf1d0489c492548dd21a9922ccecb6bf3baceeb.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\95\95846fec1c7febaf1bb9bd74b8994d18934901194f6e237dba4c9d4006152095.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Authors ORCIDs






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\db\db67120d5168b0459afe4812eb5945b9871f05c6cf6dd7779e2df3a6ccade8f3.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\19\19b3dcb23e7c5e396d947e5f0536439479e46eafa6c0b2ebd567e3a9f4d40fd4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\20\20f52e36fc7bd239ee3893dcc1fbe4e3f4bb905a06ad780111debdd3ebb6f2a7.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\da\daf86ad5701830e53a26f77a01c58e5beee11a9c1babdcc8aa8dbd1ee1b39cac.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Abstracts






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\da\daa0e6135f3427d95d2ea9135f45c1a5c0cb38608d826a07ba3307b07c21e557.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\37\37f481f77868629253223ebb61ed9d55bea989647e4c816a5f737c722e712619.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ae\ae4b94ce68f5f28307066cfe7410d445977d1566f3b708102c28473076a3559a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4f\4fbda3e2f1748de38f3cfaa920e2a1a41c8e340fd814d385dd6a48d547143a59.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Citations to






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7f\7fa3713a8e22e61a2d5004ed31578530ebe19433179971998c0d3415bc0087e7.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\87\87c2dbbb15d35952d970bdd5de053b6d5af493e6c4e81ae3a15a8d7103f3f29e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\49\4991e387828ac80226239018d0d14f44deb7ced44708102d65c09434dd79d015.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ec\ec6257ef6169c6b54c7b26b15e01dd73a1ace50d7d300eb3312379081fc4c523.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### References from






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0c\0c424ba352b1da8c0b2db571f040ab220091b851a09333588b885d402d243287.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f0\f0029572ab1b0e95b695c658cac81b5a9125623e9b4fac8b596ecbe634e558f1.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d4\d4ed0b0a133f0cadfaf59cf405a1a638edaa6a016bb68d541df82f74aa5927f8.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\77\77c35c24b1bf2e634b70b5ce90bedfcf0d99e8b4bfd65f590412a40184b035a1.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Open References from






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c1\c102e28bc8785553a39c016d2ab8881766c39ec89789012fad4f9761ed34a6e5.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c7\c7376779b49feb2ab519983c6c6c4591c1f009fe867ae5ccbedc5a3d97fc8aec.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5c\5ca7cd987a339f30e864f1d04e9952b82e348f3c9c4049f084d23e72964b8cbf.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\09\09b9fdad189b5325ae754a3b46f0d35465f4b1fe8c34e1480ba83e649685e216.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Journals






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8a\8af03f5b1bff59ddec200f021120c3a0254dd08e34d126da6992afb929be0691.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ef\efe7470b7a005073638d8d5b17fcaa542adc732f658ae171a516b70b8b3db31e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\03\03c5b7150d19cb602c2fdc0e6ce32bc3ea8b928243a11506bd08f872faf60743.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\90\9019e626381abbbedebda5788a8e458718e45223db6752bc89a3b349e385e726.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Journals ISSN






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\21\21243bd6ade749c3c8d6a91fa61996aaf13061a05ac94d63fabb9bc84666b503.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2f\2fb8feb864a43533b1d879667f3c248461279e119f06c8da914f51353a1b0210.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c7\c72d2cbec4d6a909af7632ee8340980c3ac5218f1eeffe36dc4bde6464198aa3.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\af\afd5f0168e79157029d330825f5d25593f3f6a51b672e30bc73ffbf7772bce12.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


### Fields






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\42\42d8020649610acbb149979b5a7eee2795fec91482834b962d20a041cefeb085.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\03\036bf621bbc79b3d2f47156becdd20fd40139d9daedf4f0ace0b4501ec1fd84d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\45\457a3e8a6ca6fef9d6d5f78873ddb7c692377d9df7014ae8c0b737599b230956.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e5\e5e991ff7786089b967162acca3a7794744132ef6790e883752bdaf11ed8b779.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>

<pdf:nextpage>


# OpenAlex Coverage Beyond Crossref

## Publication Types

## Metadata Coverage

### Overall

### By publication type

### By field

# Methodology

# Appendices

## Appendix A - Complete Tables



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
                
                    <td text-align=center>7012560</td>
                
                    <td text-align=center>5514414</td>
                
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
                
                    <td text-align=center>7012560</td>
                
                    <td text-align=center>6031297</td>
                
                    <td text-align=center>1764980</td>
                
                    <td text-align=center>1399557</td>
                
                    <td text-align=center>1914610</td>
                
                    <td text-align=center>3229854</td>
                
                    <td text-align=center>3315446</td>
                
                    <td text-align=center>6542494</td>
                
                    <td text-align=center>4951558</td>
                
            </tr>
        
    </tbody>
</table>







## Appendix B - Historical MAG Analysis??

4. OpenAlex - non-Crossref coverage
4a. Publication types - with and without (Crossref?) DOIs
4b. Coverage of 6 main parameters - with /without (Crossref?) DOIs
4c. Coverage of 6 main parameters per publication type 
 - with/without (Crossref?) DOIs
5. Methodology
6. Appendix - tables with AllTheThingsTM
