
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
DATE: 21 MARCH 2022
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
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b1\b1937a9a5ec2593029c4c97888f7d3ac8ff340c86796243e9132cdd51be02c41.png"></td>
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

## Publication Types

To add

## Metadata Coverage

### Overview

Comparing coverage of metadata types for DOIs and non-DOIs in OpenAlex (all time and 2020) -> describe differences

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4c\4cd75aeb5e5320d3fdbae76080d60083d6aca371963dad2cb5a436d4e6a5f5b8.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e8\e8dc5dc0cc020368fb7c52bb4ca1cc5ede44cdedd3082a724cbe010d25ba623d.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\46\465a6dab03ec16443fef91392e5d3cacd21ae2740d1200d86f80b0ab89245978.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7e\7ef82904acd64b4b1093a4355f2a9f1ce5e3911bf3ffca8c78835fc0bc2719a9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### Affiliations




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\46\465a6dab03ec16443fef91392e5d3cacd21ae2740d1200d86f80b0ab89245978.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7e\7ef82904acd64b4b1093a4355f2a9f1ce5e3911bf3ffca8c78835fc0bc2719a9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Affiliations ROR




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a5\a568e6f5a592e5d2c686bbc0670587cd484a4e6a27d3c6e0a63c81b0d5c035d1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ed\ed49247b3dd104a2da3d19207ec11d38ba8640a7dbce02b3c09c827871d9c230.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c6\c6b3b38cd952293464cc6569256b3c2c9526fb14e5a776d44cd68fa939bb1993.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6f\6f3469dc5688b90dfe0c11bf9c7eba25697155df43b80ca2ba5285f1ae58748b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Authors ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\25\257d0607301b5cb5e9d4c783ffb0fcdacd1a9546d86506b9b7dc2becdade0cda.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f8\f8b8fcac3effafe7e502a61f7d8c135d51ccf144dd9ad7562b6d36b62b82a94a.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7f\7f8b99dc6c3774bb78e1e1b806804a3c503fa871ed3d7e277638111f671217c7.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d4\d47d24967ea99bdc5e13ac445d4979fe499e87fcd51daa0a70fab8af69b9bb92.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\25\254b99c4f2a6354d6065a59ff422af81ac5854cd9796e4f1f6d00ac5868a5ac4.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8e\8ed53b8940e4378d8ebc354879203fa666f89e5c932b4aa80705e6c6720a5899.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>



<pdf:nextpage>


### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a6\a6b2d66e519b6566d3e3e6da84091ccb709aeb51ef0f55871bf03dcfcd1d99b8.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7b\7bd0ea8380edebaba45914be7dafc7226f0595bac4742eeac5895ac9dc161e51.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Open References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4b\4b673a1328965a9de8e04dfb105ed22869c37568aff3cc4284a398d9e4867b2d.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\38\382d83dedf36816863bfe98433ea5c8f19327ff578b8bf1c7fb950e56aeaf6de.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d6\d61aacf69a917ca753505cc4f4ee02952ad049394386712fe499fdc9f304caac.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\d5\d5d51cdfb581ed5d358c49b3b41d4dc47d73318aa8fd449300e387f07beda404.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2020</td>
  </tr>
 </table>





### Journals ISSN




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\8d\8d564bef867df824b7d51dd1a45e74eddce4e0efa262cc163fcb9ff0f7b0e96f.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\0b\0b7fe71120d34bcc4fc7b700d9099d9ee451009e54f0d5e2223a97ea2a16ced9.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\aa\aacfcba5a7fe84da1e140e0fed351b35d6caf31e329c92d402a1606d491bb3a5.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\57\57abf19df266b84c94bef48b8fb15a0e8cf396357ee656e452e5dffa3718bc23.png"></td>
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
