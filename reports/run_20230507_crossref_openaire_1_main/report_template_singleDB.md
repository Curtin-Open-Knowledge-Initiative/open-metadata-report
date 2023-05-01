



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
DATE: 07 MAY 2023
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
All images and data belonging to this report are located in the directory [reports\run_20230507_crossref_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230507_crossref_openaire_1) in this repository.

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

* Crossref: academic-observatory.crossref.crossref_metadata20221207
* OpenAIRE: academic-observatory.openaire.publication20221230


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230507_crossref_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230507_crossref_openaire_1) in this repository. 

<pdf:nextpage> 

# Coverage of OpenAIRE vs Crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\90\909b74eca20b74bd3224e6bfcece4809bdd8cd2affdb056de6f7da442b753aa2.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\02\027ae7fe95e8ebf1d54b7cd9613d5c41efa60b1de7212f0439cef0f4aa035b41.png"></td>
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
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\da\da776a9e0ebe7e485e7ba84f18b8834ae68271d2a84e31b63b5b0b2d51a97328.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ff\ff68a30873e5b1294eaa900eee7f4b43536a67186e1b00a3bf4729494fe140a6.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Value Add of OpenAIRE to Crossref

### Overview

Comparing coverage of metadata types in Crossref and OpenAIRE

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cf1fcb29fc8f2fc59f2610b994675a5585d3674ae498ee811255e3e7361c7f6a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3e\3e7c66a8dc6465d6ea525541f44597830a8688d53715ce85bdf37a6bfdeba2cd.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cfb8b8bab7afd6afbb04ce6e7abfda9bb872838fd133e6b1b6433e5bfdd98631.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f0\f09adab166958e0eb6df84e2783e09511927b1c589c755d5407956c96f8a2edd.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details

Metadata coverage in OpenAIRE and Crossref by publication type
<br>



### Affiliations






<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ab\ab6dd0c0b3543071f4603f0331adf5111fcc15f796036897f9e3a3a0de9e03d7.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\96\961f46d2e8214359a22cac1a1a1e0b27b4eb74bbce76a5b5cef47c1b031e22da.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\98\98b553f935e4bce5398e7ec870332ad0d8df4690572e809f8758d2152478dae8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\25\259d8547045bbda3dc1625d3b7d98c4c763b5a886b1260425537efcfdcdfa92f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ca\ca210a34afd0095a25c0b633a5ce597421962e6ae194971c3f9e22b7f6dec3e4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\83\8352e13f0d149435bb85d706a3ee31d2c93d0006e648913496b006f9577a9f96.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d3\d3d19888f8ecb96bdd17302ad8b54bd62a865c4a729f0335e7b6711261c69a80.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\78\7820e88378d08a5b7a96ebcb4297611519af9fc9da18d3fdab15da5b4f0512cf.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\38\38b04f779b9f2a0d7e2a433f7d49bbafbdeef0ca721419bf886c6d4779c02fd4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\60f69c0f7ceea091bb8b9c892eed4542b3b4c8079541253316b91210f66ef781.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b9\b99e6d6dda83d8cb9738430b3559251c64530746c9e2a0927698e0a55f20aaaf.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9c\9cc240163c3c90ec9b85c132442442b89cfa105454dc87908aa1c39281a1195f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ab\ab1daf1b7614dfe2e458ca435f55e6ad307addd0b14898c3eeed688d956bca63.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\52\5298d1871b811574041a8fb88f4682f016e7413ba0582712445db8bcaa33591f.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6d\6dc0b87d4dce2c7eeac8ddbbb7c10bf2fe9707c7ece3f1744d322e51664584b0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\21\2124fdab51c67f5dbeca475de32e037af348d13e8ab3e24854dbd12640f2f838.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\92\92b05ebc1a75629896a5e1f6e12ceeb9c9ca091fb72b682df475eab2e24683cb.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3c\3c2719dcc390632fafe90d1d9f2d61c383e7d6777ed7dc8c9e6a16ccde942f68.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\85\8533c4bf1fac67e077946d7905d880357019e3ba5eb0a7ce046ff86b67c0ccd3.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8e\8e7124203926ac37ead344233045d41a2720f19caf0525da6328e14444d0945f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ba\ba97cfc6e93b3d2254f0bbb991f9e038c131866c3986275096c0231eec1c3851.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bb\bbe792a772288f19d89336bd17a98042445f516123af5d2d99d9aeb6dcc2c8ef.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\80\807ae674097af82b3e30dd9cd4c8645cd683875c5112c15eaa0c84cc31917218.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\31\31d398d8c75c3e87a5a3692149914cf386315ffc4c841920c7c53edd11bfa324.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\20\20d5325f8cef82728ded7079051d0780a9609360c870e30cafd1ebbaa8575a2c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3f\3f98680b338a7cbe5849470201b57ff3ad7b693ec2cb41d1afa2e880dd3dca8e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\05\0562d087812fcfa541a3a0b0b8c7523c2b3c5333300381490e205df8bffe61d0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\61\61d867f22e7b551ef24a0f1c47080cf1bb654c2c64c9c4687c47d4bf9320fb48.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\12\121c9be3a0791e95261a07eb34df229bf03074b1d78eafbc5aa1e6e0f091e98e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b1\b12a47d3615016c5f1cbd7d27e7f7130a1f0cade9dcfe535c2c90e1fc5406afc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e1\e1c3a793bb249e79995dd80f61f868a12aab473ab18f5ecc1aeb232eb853a9a5.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8f\8fe486b6f6ac83a757cb468e67ad8839633a9d9f3a60163c9e3a0d2e37ab34cc.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\6097994a39a44afd06d7775c4a5abd57a54740ce61d5f67b36fdfdc63714cc8b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6b\6b673877a451f55f19677fcede8761ecc2fbf10d25d638e3f7769272f3b69fb3.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6f\6f709e3b23f8273e6a21fa01b31f04b036b024c0a5b4ecf249ad1fcedfd31535.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8a\8a1e7e7efc4bd3f98ac8d31b08617dd8876a439202e0b12d72d827b1d564339a.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\74\744a26eb77a6969136b933a37d32a25ea4c0a7f1615939062ecf9f4e976ffd83.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ae\ae28490f3177b04853833b18abeafda8b55c86cf958c7456555ba7690928ffca.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\55\55619674a6f97e056be21b2fe57cd6c6edd5c23f68890a7a370146573ec6e127.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fa\fa8424fa318fab8984c5e335fb1e0d43a8efe07579bfc21fe21440cda758cfe3.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


# OpenAIRE Coverage Beyond DOIs
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d9\d951ceea83cb2f2fefae71b8ac16593ac4b2307d3e092880b45edddffd7882d9.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cd\cd1a9a02208aa8959fdecf8f007b8f23cd38af3f790cee162fdf4f43ff0efad2.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Metadata Coverage

### Overview

Comparing coverage of metadata types for DOIs and non-DOIs in OpenAIRE

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\33\33693c3c1a73ebbf501beef07cce40b3a0cdb4057fd662f4c5f28e438e2dbaa5.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7c\7c92cd0999496b3e1076afb1b54056c75811b2c98871849aaaebdc0db0e84ad0.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\31\31108c114af10e16bbc887592d70942b627a494458eb796bbe9a9cb27f727d0e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8d\8d9e28390a81f8a94645a06e073396fbc6c3bcc30a3e61e1ba758ed116e21b7c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Affiliation RORs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\88\88fe36f7b8001daa5dc5244dcef40617ade349541a99cc782de284fb9d3dc77d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\07\0721ad92f79dbae03d970a352342c3ae51bf56e2b64eabeb0f280f53cce5d30f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cfff659b53c4bba4618f29c024bdac329cf9d239a77f4a8d8847df4a5df34401.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\43\4383d0ef6b80da682427e0e7a7bd9bdb0166005a9886e428505c124f102e0dd3.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Author ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\29\29ff18b92d072e803eaa7f45426cf3c14c2acc260066d09099a680c046547789.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7b\7bec0fe7d57b1a751c6e2b16050be1c208716f99b23a17dafbe07729ca8c0d77.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d1\d17cc8f7f4d24f7420ae6bc85493d21c4fb90995799b1351fe19a6ae5b3743b9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f3\f361ac8934bfe4fa7cf6e627ef9e819ae9f25924c466e0b08f157349251a7587.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\97\9749973575dc14617a2e35acee68a21db9d9c809f78d21b0717bcd74cefe61a8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a9\a9af10ee50e18b96513d36770a3ac04b4452b8cc739462966cc2d36dcd1d43fe.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2b\2b391fa9fd58abf98728c546f704d324c540cf75ea077dcfadb2d1e32c2fa16d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\76\76cbbe532c69569bb9ed8b9788c6cff107c8557b78f0b21192c6313a304e1a86.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\80\806d96fd1019caa13d2d6336262cfab9031a68ff87bad7e16ba41c30db958146.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3f\3fa85059a4f1cdd609a5e017e538c1dcc5ea0f809f20fb66c9234e8d11000f33.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\59\594ca102dfadac6ee525d28850241e118a73b833524a35da95fc786207d2c03a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c2\c20941ae80d7a210ab0b305166c26117949beaa9f84682fe2f3d52dfd73a547b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue ISSN-L




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cf2d8834c12ea621d781190ebbf307d57d02a9bbde6fedcf0d6833d045d3b3b9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e0\e074a24af8d1cba0c995e63b47cb98035fdc1eabc89c424c1f2c1de7f683160a.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c3\c37a7a17d81d411b00f5f6b4e89e84c10efaf9c08f449d83f071fc06ab4e6e8b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c1\c10665d5ee8a187cbb80c89bfcda8eeafa45e5e088f933705443559b7bed78a9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>







