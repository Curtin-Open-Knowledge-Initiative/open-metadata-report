
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
COMPARING MAG TO CROSSREF <br>
<br>
DATE: 27 MARCH 2022
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

The report currently contains all the graphs comparing metadata coverage of MAG compared to Crossref, and of DOIs vs non-DOIs in MAG, as well as some basic tables. 
More explanatory text and interpretation of findings will be added in a later version.

Complete data and code are available at:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
with all images and data belonging to this report located in [/reports/run_20220327_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20220327_1)

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

* Crossref: academic-observatory.crossref.crossref_metadata20211007 
* Crossref Member Data: utrecht-university.crossref.member_data with date 20220311
* MAG: {'Papers': 'academic-observatory.mag.Papers20211011', 'Affiliations': 'academic-observatory.mag.Affiliations20211011', 'Authors': 'academic-observatory.mag.Authors20211011', 'Journals': 'academic-observatory.mag.Journals20211011', 'ConferenceInstances': 'academic-observatory.mag.ConferenceInstances20211011', 'ConferenceSeries': 'academic-observatory.mag.ConferenceSeries20211011', 'PaperAuthorAffiliations': 'academic-observatory.mag.PaperAuthorAffiliations20211011', 'FieldsOfStudy': 'academic-observatory.mag.FieldsOfStudy20211011', 'FieldOfStudyExtendedAttributes': 'academic-observatory.mag.FieldOfStudyExtendedAttributes20211011', 'PaperAbstractsInvertedIndex': 'academic-observatory.mag.PaperAbstractsInvertedIndex20211011', 'PaperFieldsOfStudy': 'academic-observatory.mag.PaperFieldsOfStudy20211011', 'PaperExtendedAttributes': 'academic-observatory.mag.PaperExtendedAttributes20211011', 'PaperResources': 'academic-observatory.mag.PaperResources20211011', 'PaperUrls': 'academic-observatory.mag.PaperUrls20211011', 'PaperMeSH': 'academic-observatory.mag.PaperMeSH20211011', 'doi': 'academic-observatory.mag.doi20211011', 'Author': 'academic-observatory.mag.Author20211011', 'Concept': 'academic-observatory.mag.Concept20211011', 'Institution,Venue': 'academic-observatory.mag.Institution,Venue20211011', 'Work': 'academic-observatory.mag.Work20211011', 'additional_source_journal_fields': '', 'additional_source_org_fields': '', 'additional_truthtable_fields': '\n    , CASE\n        WHEN CHAR_LENGTH(journal.Issn) > 0\n        THEN TRUE\n        ELSE FALSE\n        END\n    as has_venue_issn,\n    CASE\n        WHEN CHAR_LENGTH(journal.Issn) > 0\n        THEN 0\n        ELSE 1\n        END\n    as count_venue_issn\n    '} 


Complete data and code are available at:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
with all images and data belonging to this report located in [/reports/run_20220327_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20220327_1)


<pdf:nextpage> 

# Coverage of MAG vs Crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\39\39c53f20194c2c7dee0a1d1b7e06aa9c8020decb32c7891d37435bcfbb8b2ca3.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7f\7f27298e004d52657132c1cfd12760cc73b4ebe2a93a877ba64ffcede1ae02aa.png"></td>
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
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\20\20048b3465b93e9483ec2764b8f8ed84275a4470fa61575c390427561f8b3b14.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\fc\fc313fc317ebbd5e7541eb9a863f5a843682e8b2dd57fc31a306693075c4b3d6.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Value Add of MAG to Crossref

### Overview

Comparing coverage of metadata types in Crossref and MAG

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a2\a2c451abfc448aaf8e0bea05aec25bc2476230f1a05e8f3bc6738e02318bcf98.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\49\49e1f86634c3332318b2bbfff692c9f8b562b9562c8a068b09d614183dbfb3f0.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5f\5faf8c233d051734d1e5161380c9440c93d57f40dc996b7b8b1a4aef622ee72b.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c8\c834c3d64fc5e01ef1dbfb6ec045a370f995e7a62b790e9655a896293ca39d6a.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage in MAG and Crossref by publication type
<br>




### Affiliations






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c4\c4e9b126515ff895eeaa26e43363413bcd14d54a5c34e7869a2e3e0fd22f2d27.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c1\c18dc1c0b173ead3315b899f0eed117ba74e78b3352a285c721afa1aeb804491.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\55\55d8cb2765430d5b2401b91a0d5ff229da80673e072c6738d8fd6f36d1aafde9.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\03\03403761f45a945305d809136a492a3773973c8074744d099c2ca54761090fd3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3b\3b2e95363608485a7253fd31eef0a44ae27a7f592dee552aac8d14a37fa05665.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\40\40b84c7d0ad8bf19c52fcdba9ecda66f640a221d08849ab623c5510a1941a8fc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\3a\3aabf65122bcc20dee9fec9012147ce6b7fd0fd2293f67256026d31287e0023a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\29\2984eaf167b5e6fd18be076c59a0af1ee989aa43ff44287606245d1f6582a203.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6c\6c9f717db80b13156f8eb6bf11384453115c44cb662c1c87c6062618dad850c6.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ee\ee33f0b235b055965db384776359b04e31686b868860c848a69b8e7f538f55bd.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\38\38268a00c57f03abcfff81b158ecc3d0c11b963831317034750ab5bd7050791c.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a0\a0c1a7dc512ff44e7c76dffb48d29bc00844b298ff7124840f5b4938b7def8ae.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\1c\1c4b3352c002fbb4ed602fbb4e22b30cb56711914d4d8c6f977c0b202142b072.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\7a\7accb9d273a6ac8aeca2f65932bdfd2c1f3cc6574404bc50c66891f571342e09.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\dc\dc5340be3c8078763154952810ecfa2931d50fd06a771cbdaaaae630b270fc99.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\4c\4c32c1a7416966978d5dc4122c62aef534a60fa37f88896c5d7e4783018553b4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\25\255d144bf2d927fdc24ec5ab42bc18464cd9d1faf64c22adffa2e5a888bb7bfc.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c3\c3a54429af3d1399fdfe4b50ae04ebbdfe4c3ff0f73b7a18698e33d2b5d0ec62.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\17\17482e582adbcb1c351677220cfc79b72ee68332ef21d9f8dbd42b2cfc280712.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\cf\cf0aad30e1c7e19cd0d1a1c09812a165a097f4b047e5a317099a8b0b3e40c1e1.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f9\f95c07b583475a16d70d85f4c6fb6e9d516330a8ab6124a249745b3349479dd6.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f0\f085011fab0f4781ad9d03facf205652e3b3e9eba01e6fd4f14ab550e38e8cfe.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bc\bcb78a1992aa612ec64c76ef101494e6bfe5d75dc2f841a0ee2476fd6c2e6169.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\23\231a525a9ff899b294495eb12ac9d6d637057489de931c6516bdf1c99cb72ccd.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\21\210a46d6e545940a7f840dc435f569b80bfd41a4f003e6e690bbcc4ab09aa8fb.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\b5\b5ceb179a97746167ddfe886a242695fe4dbb1fe9cb631e3cf753eaeeec37602.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\67\6774ad948d09b6c3f3b9272b49b66a719db0c9d18dda65d2eb81fa554cc3f0ef.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\6d\6dfc72609097c28f0d3f7ec5c1f81eac51f853e2e9a74a47812ac6781daf2bf0.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\09\092b09123d0fa868ebcb8b696031b4e9837caede58a2c3f343598a726c675bd2.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\58\58abdb6167ee66b1077aa1cda4b5633e08cb73891d0f17ef7960d4a83f37bebf.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\db\dbad40cdef229fec5c496696cca63f1f31913cb143786f29dc0c3cc83142bcf1.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\63\63df5474ed85802df7719ad131a7c20571a89b010e9d22c0455f2af234f4c8c6.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\f2\f2e50195879d74d1960e336322ec6246f362ccd1a4c19c68e8f010dbe035dc1a.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c6\c612b18eb65bc3298cc5707632458fa929b691f3092fe6fdb579823c7496ffa8.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\bf\bf4151a755cfddb147f85b813a9980c9dd81f5d953a797522439dc6e16734c03.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\a1\a181a4f24cdea6fcac6b45b8c0c2df0eb58685bc9f2a0f38cffc7ac0588c7a28.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


# MAG Coverage Beyond Crossref
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e3\e39a186dfa72e62e1ca7021ebaaba5360a50149ba92e6163536e862048438a67.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\80\80b1b3aa1b338fc13ffd559dcb43316212758320a47c3c1b81cc555772dc8d53.png"></td>
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
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\51\514acd8992f3cec43fae20d13e13bac120a937fd84f56aaf2419d35159846b68.png"></td>
    <td valign="top"> <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\52\52498e3f86acbc3f48c704dd6fde824cc0c0422d52f0df98227e1e2892602455.png"></td>
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



### MAG Coverage


<table>
    <caption><strong>Table 1.</strong> MAG Metadata Coverage of Crossref DOIs</caption>
    <thead>
        <tr>
            
                <th 
                    
                    text-align=center>Time Frame
                </th>
            
                <th 
                    
                    text-align=center>Crossref DOIs
                </th>
            
                <th 
                    
                    text-align=center>MAG Coverage of DOIs
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
                    
                    text-align=center>References
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
                
                    <td text-align=center>117531122</td>
                
                    <td text-align=center>90414430</td>
                
                    <td text-align=center>90414430</td>
                
                    <td text-align=center>nan</td>
                
                    <td text-align=center>60833634</td>
                
                    <td text-align=center>61318453</td>
                
                    <td text-align=center>56388851</td>
                
                    <td text-align=center>82244295</td>
                
                    <td text-align=center>67402491</td>
                
                    <td text-align=center>62354538</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>18635169</td>
                
                    <td text-align=center>14454604</td>
                
                    <td text-align=center>14454604</td>
                
                    <td text-align=center>nan</td>
                
                    <td text-align=center>10023041</td>
                
                    <td text-align=center>9357977</td>
                
                    <td text-align=center>8790541</td>
                
                    <td text-align=center>12807403</td>
                
                    <td text-align=center>8834471</td>
                
                    <td text-align=center>8079414</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>5522198</td>
                
                    <td text-align=center>4155213</td>
                
                    <td text-align=center>4155213</td>
                
                    <td text-align=center>nan</td>
                
                    <td text-align=center>2896950</td>
                
                    <td text-align=center>2690078</td>
                
                    <td text-align=center>2662976</td>
                
                    <td text-align=center>3730973</td>
                
                    <td text-align=center>2675796</td>
                
                    <td text-align=center>2464455</td>
                
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
                
                    <td text-align=center>117531122</td>
                
                    <td text-align=center>99409110</td>
                
                    <td text-align=center>7077220</td>
                
                    <td text-align=center>15322758</td>
                
                    <td text-align=center>12826809</td>
                
                    <td text-align=center>50680820</td>
                
                    <td text-align=center>72386377</td>
                
                    <td text-align=center>113910712</td>
                
                    <td text-align=center>93033865</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>18635169</td>
                
                    <td text-align=center>16243253</td>
                
                    <td text-align=center>4820308</td>
                
                    <td text-align=center>3665413</td>
                
                    <td text-align=center>4723238</td>
                
                    <td text-align=center>8729021</td>
                
                    <td text-align=center>9099790</td>
                
                    <td text-align=center>17469644</td>
                
                    <td text-align=center>13507289</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>5522198</td>
                
                    <td text-align=center>4929884</td>
                
                    <td text-align=center>1740246</td>
                
                    <td text-align=center>1117559</td>
                
                    <td text-align=center>1679994</td>
                
                    <td text-align=center>2776749</td>
                
                    <td text-align=center>2970744</td>
                
                    <td text-align=center>5122257</td>
                
                    <td text-align=center>4170845</td>
                
            </tr>
        
    </tbody>
</table>







