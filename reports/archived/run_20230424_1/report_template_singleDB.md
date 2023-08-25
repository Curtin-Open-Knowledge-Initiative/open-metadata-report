
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
DATE: 24 APRIL 2023
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
All images and data belonging to this report are located in the directory [reports\run_20230424_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230424_1) in this repository.

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

* Crossref: academic-observatory.crossref.crossref_metadata20230107
* OpenAlex: 


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20230424_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20230424_1) in this repository. 

<pdf:nextpage> 

# Coverage of OpenAlex vs Crossref
<br>   
## Comparing coverage

### Overview

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1f\1fe5aa0db7a7be7ad8d08eaae0bac152658495a7f21f8afc679d53ff3838b932.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\86\867efbf9fe56766b7130253f2a2ba652093c98d34fce9996a13943f9dbb70882.png"></td>
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
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\90\90963d8e4390e3af2e9c47864dfe37343cce1d20516b2aa0031df7c254dfd4c6.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\28\28842107bb2fa8b1e789ec6192fb16a6429a5b7fe3d33bafa2ebf85dbbe7cec7.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\de\dea6a3388b24bd163b0307f001531a12937892ec681e1c5674e65df4e042ef1f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9b\9bb61f018eed3e12f7a35c3f2c2d272e64bfc32d565517eae5dc8bf514430b40.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6e\6e19f1a6f8923816db46e0f37a2c9b75bb3edd42159b78dd1715df90d4a82f57.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\23\238243a656bf42a65bd5e9643e63ae253516b5ba0295380d7a02e366d9065fb7.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9b\9b460e8b0bbfef29c655d368989e4aebfd4f185e389829b2067031b8ba15213e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\21\21da201b442973265508be0659cb31080e89970232be8543a7119254a05ec6a1.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\de\de4a3dbbb3cfcc12ee137599b3aa9bee1ebd18163b373f5a7cff35bf82038589.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f3\f3932c4da15a1538c19368d3ec538c20a819e6195897b41a7a55c3aa5f8daf81.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ba\ba2522a6bfa540983f5946e36f90c7fe147820c417be50655be2afe789df9e83.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\54\54917721dfbc43fd502202640dad9a01b9595f38b897107758bc89464db4657b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0c0019eafe3050ccaf1e88ef8df13b97dad6a404fd383336b7975d120511d4b0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\99\994963a05728d1681d3359d41b27e89ab30e0fba3f3365046d2e5b44e5173f6c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\06\066819f220671e385a46cdcb8da2c0b5f4c844ba95740ddb11851b5121939377.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8f\8f74a56c802896fb15567d7b563e2c704be19249ec29c0978fb07f23b26b8c95.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9e\9e4963d4312c022c7dd69fbc61fe3f1fbf630312bfa5dc42ff01d9c2b421ecea.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\65\65f630eb3c0e8cd937d48f45422cedb69d76c375d1b8498b932ca72d9f67ab49.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\03\03130a41f29f17039b5718a7731bbdc913e78f15fdd2cca3f51a07c6fc18f4f9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ab\ab80627825c17e551f8151d44b0a315b5f5322819b2dddf762c859711494fb6f.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2d\2d54025034721dc24d9ae7f4eb616697b474f4dd79fb93c04138cdc24fcd2d1b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ee\eef08744899266b5c28b12cf41b348bd30d17ac44410509a5977a5be85f45592.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b1\b13e1c8800f1170b9fb38828c3cd7a70a75e36342f8ab24265b1303f00aeb17f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\97\977af5ff087fa54892f9433ce9876bb4eba4c1d02bb3de41c6d1bf016fbd2ec0.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\83\831fbac475d7675f1f320d76e28749f116e370fb44e68802f158a041d0def9f9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0c5746670726a7926bd64aed9191402458d2592d4a1563701cfc246779b26aa3.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\77\775ac13e864631e9bcc8c31e5ff148723b99b38fc8b16decfdcde6cfde2f3cb1.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\35\35a4d1f078480930ca5380a5039a9a0600720085faa92dc0f67abf4584575325.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\22\22f44f37b8cf322bb82c132a80658963b80fcb22a1503a583bf7c5b274bd41da.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\73\73ae9b6292844ceb1158a9188508198760c01e7cdb30d6c0d3a91fed42b44c89.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\86\8679b105debb5e2216668996e8924cc0438f3db7fe48b37d321676edebd3e20e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\84\8406cceb9458030064960bcc624bee40de7402085d6329d6a656ca5058fcdead.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e4\e40b7aab4fc15d0035c0b6ef41898ceed54143e36db8f2e03c7f5c10d0c21e4b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\50\50f36169ccd157b8ea0a1b506ce147489d2ed4436a66fa3f5151463601abbdf4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b1\b1ab890ee73fa17cfa3f1ca8e153e6b7cbbacf6a9b2704e21edc0c3c23b62f8b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\17\17828c023bde95ed6988776ff46e357afa788d1daa3cc18d5dea05760f5c9b1e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\23\23f30356fa344180beb44ad722ee3a956d338e206de22e76c6a525b78b421d38.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a4\a441a765120bf527b4ea8bb4c86f11c4ac0514b1862399066cffa8282116965f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\71\714ec1fab8df007b987ba3b2dd0764aa18e9c1ea16af089947ff16954f89ddb9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7e\7e95c17901ee2095f5d3be39f9154f997df0aa4ce8b0d4b0c5cc2e263da4d8de.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9d\9d24d938f2bc92b76944f1549a29279087933516153fc72d9c3d673c7969f560.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c0\c001eafa777ceeef58dccfc0c7cdb21e9ee23ba1b29e3c3629386a9492d3a1fa.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9f\9f36fa04e00fbaf093ded0111d9eb6eec0c1110a3409665bc0c94e35885f63e2.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\64\64288047884d253fe4eb3483eeca32310e1cdea2ae50e1d28dd1a9500319b08e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b9\b9907b3b4c6c2a6792c00c82980a02863657832d63f346d0a6de142240629d3f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e9\e96d6ecd17f3d5d8643ceb1102e20356a12831db4702d7c6830fd93c29f10e66.png"></td>
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
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\89\899d68381338f1aa0e13878d5d4451505d0d5010b3c68de616e374a72f844c58.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\40\400774430117c789ac1fa02bf2d5f5633891926fb04c2d0a9b077df6ff1d1d1f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\80\80af643f3540cdf4fdb0b717dd214abb4977e801ecebcd533aa59f79cda336c8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bb\bb0a7662d0ac4f34ea53d4c565efe45e6870725bc6800eea13315e8108ce5c75.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1d\1d1c5d1d36df55532eb22baf700c9f7be72b197747ced88e49680530cc21534d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\76\76f0ada44489331d2e7526b046620dde566e719409bc561e2280e40c5375301b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### Affiliations ROR




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\97\97bc97a69cfc8b619be37f90b9d5dfcde85aac469268d78bf962597cc21bf7be.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\49\49fb2e56f8425d67f3adde3e6abf2d3616f565aba999d3f668b9085b435662d2.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2c\2ce42eb8b2b6b3a90818728025fbb7952505e27a595c89b8198e5d95a619aec5.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0f\0f88c8ac7e5fb99d941008602cd35c3efbaab571927f52166a0dce03c47d7bd4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### Authors ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\20\20c9de35989d2beba62c331b6efa2c11d44be58ed7a287c7220631b521993c6b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a7\a7d3ada8ad36601fedda4dbbe3d542ce7bb9f8e8c54163dd7ba1e7ffa868154f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\70\70f6c564f1b79ffa0230dd50cb28a30fc0358e2aa98e01f641d33000e45a2151.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\36\36d93561015e0f68a3b7fefd8e68c662dc293e1a62c6061475ed37339846995c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4a\4a909e28872cd2a2aac0b8b010baf8f67c1e84cb924185914502ac1a7cb832d0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\05\0554a075d7ad49b2078332a6ac35a83a7898732e802fe443d9338fa014e09bfe.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### References from




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\09\09f29de683d8c62428e62a8565324d6bd33ff19527d6858d25797ed0b13a8db4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d8\d8c9086e853f889aeb3d68026f5e22fdc95d0a96d5254124df5b66d2145bb395.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8a\8a6bb3484ab14017d196b3f422cffd41eee263101d9e579c9254aac8fc4d0231.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e3\e381787e4ca95863207cb97b34a6793b2692a363e2c28d5251218b46b49d94b1.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>





### Fields




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c0\c06e77857224bf478278cb25c4605ae267e30e255dc4f088b6bfe980f1422f90.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f7\f7a8d584149abab48aa0db1d3eb0a36c8bedc699ebb580e6664554f275656634.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2022</td>
  </tr>
 </table>




<pdf:nextpage>



## Appendix A - Tables

This section contains tables with summary counts. More tables will be added in a later version. 

Crossref Current = 2021-2023  
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
                
                    <td text-align=center>114106963</td>
                
                    <td text-align=center>111589895</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>15457212</td>
                
                    <td text-align=center>13331614</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>7557737</td>
                
                    <td text-align=center>6154438</td>
                
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
                
                    <td text-align=center>114106963</td>
                
                    <td text-align=center>97534520</td>
                
                    <td text-align=center>9714590</td>
                
                    <td text-align=center>17712873</td>
                
                    <td text-align=center>15184</td>
                
                    <td text-align=center>17605618</td>
                
                    <td text-align=center>71539736</td>
                
                    <td text-align=center>110293918</td>
                
                    <td text-align=center>88013738</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>15457212</td>
                
                    <td text-align=center>13708888</td>
                
                    <td text-align=center>4574846</td>
                
                    <td text-align=center>3670579</td>
                
                    <td text-align=center>14112</td>
                
                    <td text-align=center>5309811</td>
                
                    <td text-align=center>8365274</td>
                
                    <td text-align=center>14443911</td>
                
                    <td text-align=center>11311113</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>7557737</td>
                
                    <td text-align=center>6717850</td>
                
                    <td text-align=center>2229979</td>
                
                    <td text-align=center>2031355</td>
                
                    <td text-align=center>10972</td>
                
                    <td text-align=center>2638456</td>
                
                    <td text-align=center>4076912</td>
                
                    <td text-align=center>7090980</td>
                
                    <td text-align=center>5446969</td>
                
            </tr>
        
    </tbody>
</table>







