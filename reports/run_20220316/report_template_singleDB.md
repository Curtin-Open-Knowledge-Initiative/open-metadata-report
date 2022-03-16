
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
COMPARING OPENALEX TO CROSSREF AND MAG<br>
DATE: 16 MARCH 2022
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

### Crossref Metadata

### Microsoft Academic

### OpenAlex

## Goals of this report

## Limitations

# Coverage of OpenAlex vs Crossref

## Comparing coverage

OpenAlex coverage all time: proportion with and without DOIs, overlap with Crossref.  
OpenAlex coverage of 2020: smaller proportion publications without DOI, same coverage of Crossref

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\e7\e785cd2286a38369964fd2fd70e83cd59d031b7c59cf32411b0d921834b2ba12.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c2\c2d4d7fa56d4c5a60eb86bcf01323506206c22eb4955f4ce0d74e9b63db0397b.png"></td>
  </tr>
  <tr>
    <td>all time</td>
    <td>2020</td>
  </tr>
 </table>

The proportion of Crossref that is covered in OpenAlex is stable over time, around 75-80%.  
Coverage in OpenAlex of publication types in Crossref [describe]

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\76\76689ea74242c8ed6ddcd20cc9166ebec90335874614d8d40cd50c97876d3cb5.png"></td>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\76\769f42c0d17112cf07c035325ace95d1c6f08e2e6f4e45d00ef2b9d2fd7e0985.png"></td>
  </tr>
  <tr>
    <td>all time</td>
    <td>all time</td>
  </tr>
 </table>


## Value Add of OpenAlex to Crossref

Comparing coverage of metadata types in Crossref and OpenAlex
Added value of OpenAlex for different metadata types over all publications


<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ec\ec4717e1a7786bd064dad030c57ac9f09c9e3375f1e45b8c24bee9ca75e8d177.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\75\75414313727eeb5099f20c3499cb37d99b772308bc5b10a404329806a6c8569d.png"></td>
  </tr>
  <tr>
    <td>all time</td>
    <td>all time</td>
  </tr>
 </table>

Looking at 2020 only -> describe differences

<table>
  <tr>
    <td valign="top"><img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9c\9c243e29dbc03f875903a4d98bc2ecfd6eda90afb35b2d9099e6e8e47a531b83.png"></td>
    <td valign="top">  <img src="C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\99\994698c81c1dc32a76602f81344749e7b19927329387e87f3c23cec80e693dfe.png"></td>
  </tr>
  <tr>
    <td>2020</td>
    <td>2020</td>
  </tr>
 </table>


### Overview

### Details

We can do loops eg over the data elements. But this might be better for a supplementary data section as we will 
presumably want to actually comment on the graphs themselves?



<pdf:nextpage>

### Affiliation strings



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\87\876bb62815844dd1bda0c7ad36577b2ceda020b79c35dea99b9ecb84e5a1d7a3.png)



<pdf:nextpage>

### Authors



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\89\89a0a57153dedb447d4a6a14bebd6386d2856526ecb29847a8fc9a05e38cac74.png)



<pdf:nextpage>

### Abstracts



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\2f\2fb047103aad3a1ecf60d4624652784242358ec47822a89c61c6060b217365a0.png)



<pdf:nextpage>

### Citations to



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\9d\9dbf120c23706f8948c105d28e929a5662af355edbc188d1e0956df7ab4cc8d2.png)



<pdf:nextpage>

### References from



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\5d\5d46122118d223819ef499cc97c29629ba6fa49e94a157996eda7ef751f9d741.png)



<pdf:nextpage>

### Journals



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\ba\ba1d73b285089ef1999882e999984f51a87114dbd9e47356a50cbd0f2032c3f6.png)



<pdf:nextpage>

### Fields



![](C:\Users\Krame117\AppData\Local\Temp\precipy\output_cache\c2\c2a09f69f70e785ddb441e3d4f4a6a824ab62218d63bcada4db3d995dea84a81.png)



# OpenAlex Coverage Beyond Crossref

## Publication Types

## Metadata Coverage

### Overall

### By publication type

### By field

# Methodology

# Appendices

## Appendix A - Complete Tables



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
                
                    <td text-align=center>120141465</td>
                
                    <td text-align=center>91604073</td>
                
                    <td text-align=center>91604073</td>
                
                    <td text-align=center>nan</td>
                
                    <td text-align=center>61757635</td>
                
                    <td text-align=center>62222493</td>
                
                    <td text-align=center>57167548</td>
                
                    <td text-align=center>83255485</td>
                
                    <td text-align=center>68014618</td>
                
                    <td text-align=center>62899573</td>
                
            </tr>
        
            <tr style="background-color: Gainsboro;">
                
                    <td text-align=center>Crossref Current</td>
                
                    <td text-align=center>20058172</td>
                
                    <td text-align=center>15351173</td>
                
                    <td text-align=center>15351173</td>
                
                    <td text-align=center>nan</td>
                
                    <td text-align=center>10670101</td>
                
                    <td text-align=center>10022562</td>
                
                    <td text-align=center>9361893</td>
                
                    <td text-align=center>13582180</td>
                
                    <td text-align=center>9297507</td>
                
                    <td text-align=center>8488171</td>
                
            </tr>
        
            <tr style="background-color: white;">
                
                    <td text-align=center>Focus Year</td>
                
                    <td text-align=center>7012560</td>
                
                    <td text-align=center>5413872</td>
                
                    <td text-align=center>5413872</td>
                
                    <td text-align=center>nan</td>
                
                    <td text-align=center>3770219</td>
                
                    <td text-align=center>3523628</td>
                
                    <td text-align=center>3269285</td>
                
                    <td text-align=center>4767469</td>
                
                    <td text-align=center>3219642</td>
                
                    <td text-align=center>2922199</td>
                
            </tr>
        
    </tbody>
</table>




### OpenAlex Coverage


<table>
    <caption><strong>Table 2.</strong> OpenAlex Metadata Coverage of Crossref DOIs</caption>
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
    <caption><strong>Table 3.</strong> Crossref Metadata Coverage of Crossref DOIs</caption>
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
