
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
DATE: 24 MARCH 2022
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
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9e\9e28d4a4755ef67e4c2cda215ce5e164a9cbb22cba6484528e10ac4fdb354733.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3c\3c1d89d5c6edf97f0b64d3149ecf3a352f79c6a51263f639d547dbe9be4ecf72.png"></td>
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
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b2\b2baa6f6e85acd1219004822067945a8134863c1c4833bd5688928810742a63a.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d6\d6075ffd5259e63b9e1b205b03f8b4a22554b0d5d1ac9c5d6795bda5a40fd7a3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e6\e6b2bc8a4b5944360c8475115da1297ccf73c3711e5e161de8045a21afdb24ad.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\fc\fcc1a5a14e4c03a500ee1401d72cf0f07d6357d07bf2a65a756ee0ca6f6685f4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ee\eeed9ed92b3799461b28406513c80f9fafebf90ec7a725023de43425bea44955.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ca\ca192e6fa6b7e92174e55cd5ffe76310dfd321794e77b39520aff6d22da74791.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\94\94b5af9662845050ff824eefa64192ae45191dadc3e23d7a18196bef21d0ebbb.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bb\bb013dde263703ceea5a298b4bcde18c0ac5e1f3f79a667f0f57566e07c321cd.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bf\bfdb08ef3377ab5c0ca11e744b75ce46d32685577051aaf3f566d8e46807a3d9.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b9\b969e428c7f52e014cc60f532b4aca8bed01ee48212103becc0d2deb107378f5.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ab\ab86813f36e1a48c0793ee70d3f94f127cb5241920ac42deb64af4cce39ac66f.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5c\5cd3354a8a0798e6ad5ddbd356468306c127ea95aff4f33aa8f26faba61795c6.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bf\bf6fc56d2e1b26913d2dead837c6944c7b25abd190372163fd33d6f641c1f259.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c8\c8f9b0261f64633eeb11f8b176dcd4c32a8c78a2e4a62527a27dc812407c8120.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\22\227a5c77bb3635ecf93a4cf152ca0c0917240133d8b5da11e5530c8820da1bf6.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a5\a58796020f562c4000df9db80587a87f26d2d5531120e48743904f2025d3eca0.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\57\57a7fc275690bcc25570db3a3897794f2162f3e4354e0491f7c5e41f46fcef3d.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5b\5b7d26f59b81ca9cf3d2db1bfa97525281b4dd35ce4574afb7e5c65587f618f9.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d1\d189362826c6b4aa9f65d328d441d9c3f355ce750d8036891ce0686a53415072.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a4\a4af60183cb6f6547d3fae357b5b7b943c65465271fe7ea20738237d20851e97.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\17\17e6a7926e3cdd5a480fda130e65788f6b6e0cb0b5a1ab199f4093a03ddd13c5.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\03\03cf3d20b77580f8624af9fa9a532e85346958dcffbee15c2fc966fe651cb073.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\89\899c75d91c4563ecd16ca299d32212e9c63569aba376f9de8185e103342660c8.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\fe\fe479170a72c16eb216d2bed0bb5ac5a8f52cb3292ed0aa17890105f57cee1b0.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\87\875c5b517c2d0ed93c2cc829878e70286af173a52450470be3c4ef34dc6651f4.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d4\d4d7c9cdf7632b7aad6cbe7dc89cbb299297c7f37a8f87fef6c8be6958f5e638.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\01\01ec96c18ad69d634f7cfcc6ac91b96782672baf5899cc7282fb5dc54dbd5ef2.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\14\142a39d3e4fa58f643f65b404cbe0e4ce865aee8e98ef42b085a0bfab4737109.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\19\194e772e333a6b4ae45e1931e4419c85d14904d91757c3425b7f794cff179964.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\32\32b8a6928adcb0274118fdc63a612356f9ec4db1f55308c93a02d31d21d122e9.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0c\0c0c96fc89cabb98db2d11254e1fe65fcc9dd39e479e193cf605ab7a420130d4.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2a\2a92330df6bb48614d642cb1760f627e8ebdfbb6d6f7e5d3881f65cd08482e61.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\35\354c0a6ebf698879046cb8d88720c9196b27fc2dc705e99da2688aa4b40e5178.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0f\0f0ba380f5c572e2123ac8de82b65c4dc41204db84fe4110e2a0cc455712311e.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\62\62a6ce5a40919ab43a0178b171889e2316d1ad11b6307b4f2ab316e8906f6e7a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9f\9fa8b0b0a780eb61be702ff1bdb81aefaaab3eda577faa9099a9ab89df644080.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5c\5cebf02da00a719e4265027a4927d995355a062562d50f3782a3d621ceffd872.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\84\84097957102cd4d73e4e100f01d23d9c74f276af77aab4a6afbb40403a0fc05c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\25\25d563c0eb9a234ecf4726aa6005f7c6fa957e497a035e7b94c4b3c843edfef1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\af\af20ccb2cf11eb0d18ef43260d5d6ab6d2bed81655a5a14971f485cce1d4ea68.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\cb\cbb95629bbc785c3f16ffdcc1993d88748bbddd24bb5e5fcf568cf341f59dbca.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ed\ed9baf18af70b096c205cebf50248609841b08a8ddbddda27fd8807ff956a1b3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4b\4bde06b3be231980c1754b3500d6a242479f18c8f2d03ca56d04264d128c58e5.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\62\6231f73a79906773dca1e54263c0b4da5a2505ab1c3cc47e0c7a75c9988309df.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3e\3e50cca89db77b84ba71c4280d48a738870648c64f6719beecd143e51c417cd2.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8c\8c3550fbdc0870a64b2e69ccd33a5d1bae734e1bbd020474668535fd8375029f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b9\b943e009fda9018a09e238a8fa41b937f8ec6cbd6f74e5ff4d7d2c0703088942.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0c\0c7b96652a52bccdd34e3c55970d4be94ab231d228511d21c23ad705b5750e14.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4c\4cb1d60f25010a94ed7bba0d532f590dbe90e9c19a635b661d9c0589fa016516.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b4\b43fdf10d17e816660280a6d97da290b79da02597884a9001e6cb39a72a1e33c.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2020</td>
  </tr>
 </table>



<pdf:nextpage>

# OpenAlex Coverage Beyond Crossref

## DOIs vs non-DOIs

The proportion of OpenAlex that has DOIs is stable/not stable* over time, around xx%.  
Proportion of DOIs vs non-DOIs by publication type in OpenAlex [describe]

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\07\07a4fda35eb36e1951289f071d04666394e9eb57007fb81250224516da7199fd.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\87\8714e9a6e031677966f8588407678f963ea95be0f6d53fb31fd69758fe9d11f6.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Metadata Coverage

### Overview

Comparing coverage of metadata types for DOIs and non-DOIs in OpenAlex (all time and 2020) -> describe differences

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\31\31208ffd7bc53c6b359526674a510da5254ccc8abb8c5d2b1f7a490100ee2871.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ec\ec52278dc8162819781aa391bca7211ffb9d2d00cd60ccf0567fc11cdd881ea8.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage for DOIs and non-DOIs by publication type



### Affiliations




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\76\76359418f0f5e3bfb934cb4b7c462c6436271448535a6ef15168eda930bb727a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c1\c1b359a6408dcf0cd6cad0f6e275a0237f61e2fc8ebb5d012e3d2690aa9d9fa5.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Affiliations ROR




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\37\37fa188664f3f0ef4eeba3c3e1b6a7e184c638211b0d67dd510f4d32bfdb30d0.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e3\e3bc188b8a6e25d03890ac4f862cdc9b21434662dc3baadbe69bc003690e2b40.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### Authors




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bf\bf88dda7c10de72bcebc9fee20505563844fe7e8d841667c96c481cc5a70aa36.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b6\b6a5090a9aa526af4dccafd97c743b65cdab94abf6b4b9d96232f5840544483c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Authors ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\39\39c22b6c113d39e772d8a7fa7dc0cf547139aad30d6d96f77040df493fafbbd3.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\09\09dc46bf4b5062b2ec89f4d1e46bf410da13eb49085b4c161fd3b11ec685685a.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### Abstracts




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\82\823d645a38b43cd77d8ddf28d904af8c5f34b4073923f677a38526f347127d36.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0d\0dd74896e9c2731d44fd9c6b418fdd3c23863ded030dd401f8b6a5dec47cbbee.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\36\360ec9bccb2a36c06a0dab5732af439b3447ad2164afe880e80147ba824e2428.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9f\9fc47670ff34ba858a1ebeec1753dbfe3bbb5ba81cb839571633c8f19ff8234f.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\59\599be25fa3a9a2b94acf35305ceb6b11d16b7cf9bbe78248ce13b4786756eea0.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5e\5ed6b686573013fc0e76bf2b330296e7a63577769ede773e90ce8345c5e24574.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### Journals




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\01\017e73b0ad661bb525e62b712d45199a4d3e85d2b569f7cc2ac500298ede3c5e.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\24\24141afe153199621b023c3c907f7dafc77f710d561e12d445f079c88dd4ddbf.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Journals ISSN




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8a\8a509a0075c2ec4f9e0d0f8e0c944167cea2e2c3442d1736dad11c26e301eeb3.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ae\ae0947271b631bdc59f872ac2a206542ae066cdc8c27c4e122a5b37b05020980.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### Fields




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\74\74d0e46dd74c9468e407630b3fa315750d9a099d9e274290fb515e5aafb18198.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d4\d46e4619c4e8ccea2685541a16dea2619a9499181a1d51a8ee091836ea0b6430.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>




<pdf:nextpage>

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