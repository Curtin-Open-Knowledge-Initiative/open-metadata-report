<!--  -->
<!--  -->


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
        height: 24.7cm;
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
COMPARING OPENALEX TO OPENAIRE <br>
<br>
DATE: 11 OCTOBER 2023
</p>
<br>
<br>
[PRELIMINARY VERSION] 
<!-- switch page templates -->
<pdf:nexttemplate name="report">

<pdf:nextpage>

# Executive Summary

In this project, we assess and compare OpenAlex to OpenAIRE metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 

The report currently contains all the graphs comparing metadata coverage of OpenAlex compared to OpenAIRE, and of DOIs vs non-DOIs in openaire. 
More explanatory text, tables and interpretation of findings will be added in a later version.

Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20231011_crossref_openalex_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20231011_crossref_openalex_openaire_1) in this repository.

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

In this project, we assess and compare OpenAlex to OpenAIRE metadata, both in coverage of publications and other research output 
(with and without DOIs) as well as in coverage of metadata (including identifiers) for authors, institutions, publication venues 
and disciplines. 


## Data sources

This report was run using the following tables as source data:

* OpenAlex: academic-observatory.openalex.works20231002
* OpenAIRE: academic-observatory.openaire.publication20230817


Complete data and code are available on Github:
[https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report)  
All images and data belonging to this report are located in the directory [reports\run_20231011_crossref_openalex_openaire_1](https://github.com/Curtin-Open-Knowledge-Initiative/open-metadata-report/tree/main/reports/run_20231011_crossref_openalex_openaire_1) in this repository. 

<pdf:nextpage> 

# Coverage of OpenAlex and OpenAIRE
<br>   
## Comparing coverage

### Overview - OpenAlex

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4f\4f697afe04ebefe589ea29a4d9de0f01aaccc9520a0b2fada1d142a18afc2c55.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e8\e8b4ef8a0bdd7e4ec5eca557e317d98c5f65e181d81e35391b33c63b10f4d046.png"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - 2021</td>
  </tr>
 </table>

<br>

### Overview - OpenAIRE

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\df\df909946f28055faa587cc9f12c1a73255c02f0f2ff2de7ca2950b60d626da64.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\be\be057585a850ccd00d45cd3af83389d8643a24aeb5eb87723627b74a525a82ec.png"></td>
  </tr>
  <tr>
    <td>overall comparison - all time</td>
    <td>overall comparison - 2021</td>
  </tr>
 </table>

<pdf:nextpage>


### By year and publication type - OpenAlex

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\87\87c89da23d1590379b53bbb49df95e6af8a0627a55972810536fa9e3387f44ec.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bf\bf783e244c0494f1f820e2ba4c05173b341afaa31932716ea8d0ba688ac52b75.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<br>

### By year and publication type - OpenAIRE

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0c7d906716602b4e3c98859761e4e49eb3ae77ea947d0c5337a23eba62a4411a.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\14\1404073deeb766310406a3b79885ca7e20466b7d7b774c8ad896897e7c5be1be.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Comparing OpenAlex and OpenAIRE 

### Overview 

Coverage of metadata types in OpenAlex and OpenAIRE (for Crossref DOIs)

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\06\06fb03a1d0120913596fb30bd8180d545286e6ac3aaab4d6b03b018642b7e4c8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b8\b84eed0485e88037f0acd4f597e76b551584a7ef85ef2c1bdf1a7d5fa6f2c17e.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\36\36abd194f64906e05c19f8b4eb2a08df0c5534ba1f1bae587646205cf11fcd52.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\77\77d13fdba958d4123cd6d735ba5d95935b90b3d5cd57f8302595baddeeb5d84b.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\01\0114ab44d66372301fc556fcfe516b44120b1ea0a174896ca2711ea265438e49.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c8\c85ecce45e32f9114c1c4db376a9d27a2d3e1f84c111657c2c2921f92a6c7100.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details 

Metadata coverage in OpenAlex and OpenAIRE by publication type (for Crossref DOIs)
<br>



### Affiliations








<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\cf\cf8ca7b9a5138ef16e4c8e63cecc2590919c2a0ab471119f482407165405c7e0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e0\e01fca8b0b4d8ed86efbe12fa62d01e4e8f8ba049fa9ae12f51f89124621a9e9.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ee\ee99c43289371c99b496733af983fb88842ff96f76cceaf709b78f9de429e2bd.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e8\e8d419298fcaa9df067c6ae68903cbbc5eb0e3c5ce6d5aa25a0607c1ac489e4b.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\77\77acb21ddf5ac3961e230ca4e6a006824f1d6557662c0ed9f7bf5fe93d3f4fb8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fa\fac3994959871fcbf4115b70d9b539a545ed992e524ea2fc502876609e859c0c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\85\855ab0104696f4d0f7c273dde0bd702f8af529d50df4a3862a4767f83c369a34.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0e\0e13e1cfbb7f1cf49a4ab242b0699dac5aeeff75e0b54f44295e6655ba980801.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ea\ea3fae1a7e1eba62effbf9762ce4a0c960ebe58d6604ed35053e85ac79c65b9e.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d0\d0bb3552b5df0c057ce1b88be710799fffd1adeaf6861addf367eac504f1695c.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5c\5c6270af6f43007275d43148a1b8572e9d626614bacc17d385f01e6ae802e3d0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7f\7f9a24bdd130b62ce37419425e307533b1248a804855051c1607262ba72efc66.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\27\27e46c8b056cb3dcc5a0d281475363a741154af0661202f54282ddc65465241d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bd\bd3472fa56a8eb5059e5ded751e82d34b7f503e5e52e5c2fffc0496ccd4e34a8.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4c\4ca418ae52e9c776e1c360922a957f113811d350705dba0a9c4f75253597e0f4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d2\d24f2478926a972205f6765a3341ade6924df78b2c5ae612ac2b0b5db684deeb.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4e\4ef25b64769115b9cb81a97f3e8ee8d56e0f6029e4f8785d02c1527d8c0200fe.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\da\da83376bbd24ac8458ef9e9898a68fdce660d0f6441266cfffc95b2f1017473c.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\33\33d6695917270ad0fb70b26071be20d6ca6c65302ee1b53b49d6e1395ff8d937.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\df\df7414785f69161e12e2b21beb2f3b1e84311c2635e3f755e9f091b2596e1fc6.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\13\13fed8938f323a86ce6db914e34ed56b2fe241c330780d9628fe5f56c390bd82.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\67\671e78258e8cef66b8c9ba89bbe970fb83fb954e8e4887f335788d33aef3768f.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d6\d6b1169a248165eadbbd5a8fc4cab6461812dc606aff784f1f787d0b08773ae9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5a\5a63db942345467783847e79051edcbbe00e17ae659793e6255304c93ce7e0d2.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\74\7416aed9aaf10a2d71e2073bde66c7bcf9d723e414d6a6a517e6a6ef08bbd755.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5e\5e492df3c173191d49a1cf3a4eddb2c25341cf2c0e8ab67625ce73c52860f999.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c0\c025d0dd2a81fd1da44e72caaaa40a0d51e509e7f78e9476e47af683bc025186.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\dc\dccb552d9f0bcf9c8902eafae3cd8f06dfdb931cb9252589d37e21fc2ddd113d.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\44\44f2dabaf8f234a663ac5a0d1de7a39bb25dee55c163228e907df93722546246.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9c\9c47bc3ab62b2510f0c27fd8450b9572b1dbfe6b761b6518b62171e39df8fb13.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c1\c1708c53324478c9b03a927fd1b231aa7ce841b78edf200a97a2872748886ad2.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\eb\eb59b9ced850542e85ed509b6d6df5f45321284a615bd73ae8981489d1049640.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\91\91bb82802957765a73375db4caa79e7a2797ecddf3b4e0d1ec590462d68ba6b4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\98\98267510bffcf9f8f2c05ccc543846956c280dcc7ce41863315f51c824515f88.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\28\285eda7f4d8a40dc2469089d5744a1ff4783b2bbd9a87435db4a10efa1b60ec4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bf\bf764f1cff96c0cbfe1f479078d921fa87025eca2fa73df4916c08cbb11cbfea.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a7\a7db85881d7f94d9ac4a9d96c63a6477adf3efcecbafd02ac9cc2e0ebf6a1e73.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ec\ec3904b0b177d617b86f68de83da0132e73e85389d584f791213f7c5ab6c5df0.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\88\88cecca806c9de96e3fac7872952ce54e64dfa509366619aee9ebebaf4eca165.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6a\6ada8de4035f90e9ebb3f865e250566b3763e4a7e440027eb58c90e535a4557f.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d9\d90221ac8289832722c449065109c9fcf13954b118c00d478aaf121a47df22dd.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d1\d125209db664364c8ea2f607c8a3ab93d04cda851f9df8f8b507ee9e1050f7d7.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ee\ee24ac45e1549746f3244ac73355b13278ba7633cfd85fc796586ceae391c843.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9c\9c9c6ad7492e9a15986ab68d3066bcd13c2da7886c1a59feb2886e5d1a935515.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a6\a60bab696faff9adb9293fcb54477330c5fa8a5f347741dbfb273b3d1e25b0cc.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\98\98478f6ac57665dd846d823b968c288fec240f105d1cc562d6e2249cab341fe7.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0f\0fad091e923b6e07b5ac2c43c3b138ed30b0c569a6d162857e9a12dfb43aec39.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e7\e791c8a8c2056f5b6f93fa43b5839cc0c8566a88eda9119e407808d8c5e3f013.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Funders








<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b3\b32b8abb66179ec1d3713da4b44b7732d60e85d21762c9f3222a888cf06a4ff9.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\04\0439106c7b613cac9c360e3216f99a331000a27ed6c1c82f865ebf70651142e3.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8c\8cecd59dbf54507f8f008dd763a284a33d95f02c67dfd4aadf99d3caa0bef190.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\70\70f54e241cfe7abaf76a0417362b055524034ca8c1d465d57065b866cae65d93.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\36\3640d69122d0c392f6b98b9f44157dd740db3f0b807583ea2d093c81bb45f282.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6f\6fe8f76c300e94991603e2088b7f9a27941247468fae5b83c1fa3b86f499d68a.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Funder Strings








<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\74\745979f74b29a58443ede7f528d1f298f9fa1ac01ac54aea51cd931cdf6a2ac6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\90\9022211102efefdc558d3d1bf54e6d1a678ecb6d8be16afebcd4a42f013f1375.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\07\07ea57ba78f4a1780fb59fd39d928169db31449d27361e520376afa441c893f3.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d5\d534d24fbd7a3e868db4a9777efb98da51bdbc9228016df558ed9f42ab67da06.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ae\ae75d09ec2b8a6aaec8ea84d8a4167c1508a602bacae2328452cda42e25c47d5.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\53\530571cc0f28e5e5a28ae385140b65fd8bbeec5fbf77003da092a2e1e75efd0b.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Funder Source IDs








<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6d\6d2f91b3c9d4fd62349a184447101b917dc4a74da871e7539af680288afb6537.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\94\94e21613e693951fd253b052b36ee666609cdd83171dcc40fc70a49ad01c1950.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\dc\dcf800e84e8a123695042f12cde79b45edd911510ec30e675a1fd042ba3f3628.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\78\78e5dad969ff0a9753f11985652c1023f7e41d6ed0454530ffc51d63365067b1.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1c\1c067a1bdd36fb441646bb52a25f28d6246e44eb984b48a5849f9396704e6af8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b8\b87791c4629b333616ad6643cd8cb955d051f0dfc8481a3036dfbbe49e1d16f4.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


## Comparing OpenAlex and OpenAIRE (overlap)

### Overview 

Coverage of metadata types in OpenAlex and OpenAIRE (overlap only)

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c0\c0afbe307e87b64cb8d57dc3c68ee4a0e980efe6b2a2aa5799a3530999d69446.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\29\2926527469b55ad80b10e5bad60ec27a14a047e61aa73b44a8d248e709bff7ff.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\76\76e7ddb19fb6d1defb78547c7ea4f5a7e5f61648c1bc44dc190e5c351f3234b9.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8c\8cd6f57c92db3bf9cff9c145be3a5fa5ee41d7ec4d7f23adb6c8c8ae387cd491.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\27\27b4c47908194f623763e25c69e0889a3bae42d19ed35d23b22554c53f29e079.png"></td>
    <td valign="top">  <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4e\4e1ef3c1f0ca62f8894087d784474e9bc46819e8d2c91bcd52b9dd277dbec80b.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>

<pdf:nextpage>

### Details 

Metadata coverage in OpenAlex and OpenAIRE by publication type (overlap only)
<br>



### Affiliations







<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\55\55be1aefc307fda606a32c05dfc04396d91c368ad935daffdb98696492f63e49.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ec\ecac6109f303a027a88c34f2f33eb75ae40f4665d5da1c6322a9856d4eb59ab4.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\07\07210be6f609e7d6a2916a4a6320646e1cc2be15e5e18383dc7bd3358d153aef.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\56\567993337f7d0f61bb65c379cb477dbf86fa6ba41e428c4f1b47f4c1acc34a73.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d2\d2cee56c37bb3238b68128846855721e6a3385a98e4fa70783ba1c0f78e9b5b6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\68\685ff94de6cc3efd2c31e1630166a9899d91f8ce5555f387d3a27680f058c86d.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\16\160617197029b468693a12c64131cd12fd66fe5f6bb5b0dd1db2fa10ec8951ba.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\15\153e5c7b5043c53a6b6281ccce054795e6099033f4edb4e7212cda780b8f68ff.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\72\7280760ceb2d66d79fe1f2f06ccc498b0c5bcf5a7f102ac2b84e17d68e4fa107.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\23\232f67376d6d31909f8530a65ccecb64047240161da8d4a2536b16f3c4956a8c.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\31\311f8eaf1bd62af2c8b709536bbcf83a8856ac73f77a993a229ec734fd310d4c.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\70\701037bf35e152b2f9bde8fc878cbf9fdf022246c71299b347b1cc2b742ee94e.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fa\fa60d091b6a35ab175fe9b264e7659805a0ad8f7410e9ca73a5fb102c191f78a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\23\231982f280174a7a8c29f39d4984ef5a924fae046dcdca2292d75f6d26f0ef3c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\aa\aa24dc438ec3af429208f0d69a422cf4e1055e9b495f099bd2d0ebbcdbe37312.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\34\347272144a0cc1025aa292f5735a4561503cd704c8badf136a1983d6e58404a0.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0e\0ee801371c4aa1cf3f82784ed96f773b0bd06b34ee39a7274e127dad79207687.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ac\ac488325ad2fcbc22ce80feffe8b3d9931770d54efb04c766577a2f6b6a2adea.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\85\85e07ffedf6b80fc8619645b3e0ec84d9aad5e5e0ffe7c33fb21d914fed545ff.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ba\bab9bccc6dedd2f1f8bcf3be1bb5f0eec8d812658e7f7f7e2245d949804a0505.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\23\2337d1a4062de57dcb5db53cc8189326e673dfdfce442067bfc5fcc7f604d54a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\27\27da4de0f48842565b11030991d99eb4abeb0521647fd3fa0c3a3489a04998f6.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\34\3498777d5bd78daeb6c0dcb58910f9e4e9db3e3da0a9d6567a73ab089b029f3b.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2e\2e943bfe915edaf13d91c03b7a2202661a36cd15e48bfbe91defce9a1cb8f8f1.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\12\126e05c6851e0ae4a08ff248bcc6a53da272b26bab4c902ca7e45a38f53d3d01.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b5\b58921354f175be7f361ba2f4acc8cd63ccff7b76d66976b9c19a6462f25e1d2.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4f\4f9dd148def7b95894c9c66e20c4c84107cfc6ac0be4a3f8bd1300147ce1d2f8.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8e\8e80cb7d73b17e7c5c2a8c8f56b04c4abfbf67c30ca78c7f1a1ae1615a574a48.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e8\e83f1febead6e6b48eead3d9b593d20100256483940a6ba201842f6253636771.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\34\34de516cded8591a84ad33bcb1db9f42af751098510890e44889a26d5c7c5b0d.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d4\d47cdf765a16c65eb5eb17382472b75a27646d3cff09bb0e0b8bc817cb49019a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\46\46f399ed321d6ca903b7520933f896eae1b9e1d60766953c77ff36bc2a6805ea.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ae\ae962b2546cebd95a245479057a2baca881fba7d0eb74c172f298bde2ca01d5f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\dc\dcc2d0562c13de0309bba475851d472e0ccd6089bd1ef17b7a75d0b3bd869c55.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a8\a8147cc4d8662a6a85603b5fd0e6752079f16810fc0be0d9a032c226d9a4d250.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\26\26affb08804ef21063bf33439c17ad5aaeaa9b41206466cf2b8f8b0219616fbc.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9d\9d581a8eaa58b603538bfbbcd1fb1d5d49301a1fb2ebe4681748bbfbc42ee270.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7e\7e21928e7ff8c12b9ae42df8a2866f71631fb43fc65105ecec0f3faafc73edfc.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\23\23487e7415c69f99c2c302c0db9fafa3f144b33c197ea61fcd6a748c08aea3a7.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\31\316c385abceff40acbd6a2dd155192f4646a4643a2de904695a34fa6cc8fd1e6.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\47\47f87c797ff0b872b354b03cee9e04345c53eb7ebc9b0eb67a00a97c67e27614.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2d\2d17463716d98e13280ea2bc2117fa71bfc9ed81ddff901a43746cdccfcfb3a1.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\9c\9c03d4883618540ef412fa94bd75eec77f9ca7bd21ac501155fde42dd6e027db.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d6\d6b735d8d0a9eb48cb845d88d003a60a4cd254d1b2dc6799da1a97eec8415539.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e1\e11e1f1f9b5742b5811bd519a39db461bf3966c08b5f191519f58e02f6b0c8d6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\48\48d0d6c0a1f217fdfe8be97a918bd98a3f387e522eeddc8f9fcb8303928e1289.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c0\c098e603e2f8c1aafe1c7162ec1fcb06ff1d90dedbd9a7cf581b93d65370fadd.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\92\92878e831894d0d02ce6f3d3f4801a475d56877089c869a6308936b0b70695d3.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Funders







<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6c\6c197b2033c51a474757af9cf1c4bf036a12a2d601ddb17dc68ef7360c383003.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bd\bd93c36cd050a257b89a1403a730c899edc6d4553374efe7f392f303aca76fea.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5d\5d5a1074cb88dfd69cc53c43fcd19ab2c0fe4947f09e881fc8c1e6be3c436d05.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\3f\3ff8ba62f42013cfa7318d016ea5947cabd60a6abbb066b3d2df34324d7af698.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a9\a96ed81a69d187bcd8cded35711b09ef6eb38624f13ad86665d9dd25a054091f.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\14\14a6a7571e400f90f548331eec26feefa16f5685f493c7b4738bf22b8ad735e3.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Funder Strings







<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\90\90f9d3da78d150cf6c3fc23a6f98ed88bfc930b151f464c62ef81e3938057c19.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a8\a8b81a85287fc4345b0719ccac3d0244eaada2b508ddef149ef07ed90426a32f.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\71\71d575360b56ad3cdb850a2c420ac133e1d6691e4edbc0569c3adfbd00c26845.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d4\d42809c0f091b66ee7eb9d00feb40134d718159da7c4cb734ae13b7fd0ac6cbd.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a3\a35efe30394dda69d709cf8352142b972836b1c817a6bc19fcc6633388964d43.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ee\ee3817f4f4b51ee68f9e68497155b67ae85cf570da77e111049a2d6d2560ee23.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>

### Funder Source IDs







<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\58\58deb9eab6ad3ce948b5e8325fb3fcc8982e95f7e08adae75b831f7e39f5d291.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\37\372233492ce696e6fbe21f07716ae69cf1aad13305026a1a7ba2e1374f72134d.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ce\cec894a9c7826bf79d247e0776487d32b5cd9260495f3ff6367038915ea3ae4a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7a\7afdb48bf8e5780e6e19179786f67a0d38e75aed783cbb15ec9f5c6215fd8811.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
<tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\61\6104b0027f65bcbd46f0555a2178e90ea27877ab4c5294f27829c7c909a37227.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\14\14f0205e16a6a195af02e4aadd235942b62edf9c9c6cbc09a6259a2d232971f3.png"></td>
  </tr>
  <tr>
    <td>coverage added value - all time</td>
    <td>coverage added value - 2021</td>
  </tr>
 </table>



<pdf:nextpage>


# OpenAlex Coverage Beyond DOIs
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\fd\fd630678749b732048bc903e2723307f9daea4d5689c511b260a3e55555a5d0b.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\13\13c0459cbc1a0e6a10958d217279290dc2cc67a558a18a1d0d93e4bb9ff60868.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\2e\2e6499dd8b12e9dd4d6c4946d0d7d66899bd890d170546c540bd8b45db833530.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\36\3691e0bb1dae7b243be398ee252cb8c68c92e30ea5762739981c107e8c72a1f0.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1e\1e029d5afccf0423bfe7a52938e231e912acfa36f737e12c87566ed712a20281.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ff\ffbae669fdb46cc228f268e3c3a4798273d3927b916c2df1928921cee1f514f3.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Affiliation RORs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\61\61ef07b48356b6fd675bd7d684a094c7b7dacbe51ddd49311da0a52809257462.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a6\a6c20e50bdec641348986babcb8053e70485cdd0141ad282dd2062be56892ef7.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\e4\e4ed02cd193f752f75afd9e3c890c9c807a3bd2d24812b7ebeeae8f047bd8825.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\17\178bd6c80a9b149aba2b6b56ab86bba3961b11189ae10d5237539636bd1bedb8.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Author ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\75\75154fde07e74062b5cc9a1e5fccf5cdc180084f79e6932d734a4d0941e8c0d0.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1e\1eff4a1ad2fb221eea62a310f737498050fa2abd334e6c0741f5a1bb131eeb3f.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\85\85053add20c0230fa3dc120ec2cebd6d6393a3af194be21412d9c50687886343.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\62\629a63ddda4d1a5f79bb01e52921f7e004a5595bd6d50b5469c0d204a8f848d7.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Citations to




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\5f\5f7dc6e585d23291e50b8c8f2a14888126a3f79f30a7208e388e1e985e6a76c6.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\22\22396f88bfe92d7a4080fbf0b9f200ce69de84c84d69bb9f8cfc6e64fa4289fa.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6c\6c738112a92eef89a0dbdcf2baadca17905ac50dd2efb9c538a0a1ace65cdeb5.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\57\57e28ac8dba970f1ea7b8935f0818044a34722d7bf4b3113f5801d53b60b1813.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ed\ed4c80e93d1e88f197af0aa1fff70cb8d1e1623c8accabdacfc05e2882eec825.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bd\bdcfa17a2a71309bbebe96ef362c19e47ba4bb9a7e60df20bd45228704d603e8.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\96\96f6bbd582429304e11dfbfba4ce27d6d3b13c55341eda928ce7f8adc1d70e95.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\f5\f574008235d07227c682687aec62244ab6a5e8f2438406b10fce3f8a5f582466.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue ISSN-L




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\bd\bd5e03c503131b3f02c58888e2df9a756f93a0afe783fbcd79e58010490e2356.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\85\858f5d4a3ab421c8b2e4beae30945d9b3ae3182b46eeae368f7cd9876e5352fb.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1a\1a4a3c54fb3b03718b9613fb1268ff7563510444c454950e83efdb844d3eaf58.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7b\7b5d893774817895689ae3be2a33b5eba83e52555ac38eb0f9a6c4907af71958.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Funders




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\6005febdb77a214d73fdff09dcdf5f5e5ef5bf49c56145372ed33cc5701cba20.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\86\861db73c3da50eeb14ab796f7c56a841884feab0f3c7e72e2e092d1ab04cab2c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### Funder Source IDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\6a\6a37c895f80c06346ce983fbda9001fbb269913a7a584e8f89ea1bddade7f96a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7f\7f6465457b48622468fe106e6d312890154eba0813428e2186c74dd1d8fee017.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>





<pdf:nextpage>

# OpenAIRE Coverage Beyond DOIs
<br>
## DOIs vs non-DOIs

### By year and publication type

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\52\5215c332a79a19c1ea4b808a00d4a26245b26481811de262a2fe0ab783707a4e.png"></td>
    <td valign="top"><img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\da\da88debf60bfdd9768ee3e4f8718c37414e35f1365a83264d46e43f9c61e2816.png"></td>
  </tr>
  <tr>
    <td>coverage by publication date - all time</td>
    <td>coverage by publication type  - all time</td>
  </tr>
 </table>

<pdf:nextpage>

## Metadata Coverage

### Overview

Comparing coverage of metadata types for DOIs and non-DOIs in openaire_

<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\df\df40d93543760e9f10cef722fc87f47be32a1f63fa0b7b796ce131310209f687.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0f\0f58ea5fea9c6b39cde6c7145bc2060d7ee9ae37dc845a822f7befa5c4dc9faf.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\1a\1a4fae2a119ce25c6bb76be5d40cf7822dbe0c6dbbeb5f6e036faafa22c597e3.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\04\048d8495c00dc29449ea32a4e29cf263ff3a91cc45fdcc48e22468c1f22da661.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Affiliation RORs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c9\c92fa318265e67d6a80363b4e2509f94b76a2cc225578addfe9bcedb43b24a99.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b8\b8f022f25d2fd928d13bcce07a27787b4c85041d0ce11be137c7a7c5fe1ac8a1.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\4e\4eaf69bca5fe8768c83af1bf95e96d26d6fc32d953e41186a2e2781effae65e4.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7d\7d93f2a02818be84963df66c80bdaa15a7bf511dd4a739fafa83204a3a23805c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Author ORCIDs




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\58\58c03c87a94053b37670fb38ccc5de4eabbdd15679450e20eab1497304453020.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\b4\b4d2ff7562b35cad3c3945d004eb4911f687bacf5916b1043d42f5f965f71b09.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\7d\7dcca0b3f69d9b9f2141163720dbbcf688408b0ff14d15f0c2979c9733d4192a.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\c9\c94d770e5d45454e0c32e333c41a9af66c9f742b2c17e31084ffb10b88ac3a75.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\8f\8ff066779d03a19107e82a86f836e1991218daf180054ceedd3e0090396c4269.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\d8\d81f433f834da86342976c6173adb3cf3e4e272a6ae579bde4503e29e51e16ad.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\72\726436daad0f694a5a294b82ab03fcb306d33eee6eab951f99dc3e6aa74de324.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\ec\ec631195018a2af3e1e11621653ab2b6a7211ef09643be334d08107d21b4ce3c.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Venue ISSN-L




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\47\4701020e0ef11781d6b7e971c5accb6137d7278cd0981cc63748d496147e378d.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\63\633868e38ceaae088304fa5aa7d091300bb77441a2e125dbe76cad928c0d2fd4.png"></td>
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
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\01\0131e72ed9e0f13548862ce35ceb934f9f0d80a454300f8086d4b4ec1e8b7d53.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\0c\0cbf4bf2213a7ca1c95e79a6012c435dc59ff30c2af8e027d5c4ad8b8e3c60d1.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>




### Funders




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\72\722b173f316bf9523b766e3e260261802579306962383c986f77b516645930e3.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\60\601ecfceebcdb0c88cc13f5ade9cf44ac40dfe87a01a2772b09108a2d56c98d5.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>


<pdf:nextpage>

### Funder Strings




<table>
  <tr>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\a4\a4ea150c57639ff5817e4f14bb8bdc48e7f480b8a650bd27db8e9aa3e0e9b3cc.png"></td>
    <td valign="top"> <img src="C:\Users\Bianca\AppData\Local\Temp\precipy\output_cache\88\88f95301421af63e41f9450afc76f3f7d0f13074f0a1d64380509c2b41e4c86b.png"></td>
  </tr>
  <tr>
    <td>coverage comparison - all time</td>
    <td>coverage comparison - 2021</td>
  </tr>
 </table>









