![hello](https://user-images.githubusercontent.com/32434139/215419654-e8d047aa-1ee7-4845-ad4c-fcda0972101b.gif)

# What can data say about my Netflix habits?
> _A cross data analysis between imdb and my Netflix viewing history_
----

## 1. Libraries and Data used:
1.1 Libraries: <br>
    - plotly <br>
    - matplotlib <br>
    - pandas <br>
    - numpy <br>
    - calendar <br>
    - warnings <br>
    - wordcloud <br>
    - random <br>
    - pillow <br>

2.1 Data sources:<br>
<ol>
    <li> 1. Personal Netflix viewing history, which can be retrieved from this link: https://www.netflix.com/YourAccount </li>
    <li> 2. Web Scrape of this IMDB list: https://www.imdb.com/search/title/?companies=co0144901 </li>
    <ul> 
        <li>list ordered by popularity </li>
        <li>1000/ 250000 instances retieved </li>

 

## 2. Data Cleaning Documentation: 

<ol>
    <li> 1. Personal Netflix viewing history, which can be retrieved from this link: https://www.netflix.com/YourAccount </li>
    <li> 2. Web Scrape of this IMDB list: https://www.imdb.com/search/title/?companies=co0144901 </li>
    <ul> 
        <li>list ordered by popularity </li>
        <li>1000/ 250000 instances retieved </li>

2.1. Check for missing values <br>
2.2. Drop empty rows <br>
2.3. Consistent naming convention: <br>
    - Capitalization <br>
    - Word separation <br>
    - Extra spaces <br>
2.4. Fix inconsistencies in Fatal column <br>
2.5. Fix Year Column <br>
    - Drop NaN <br>
    - Drop Invalid Year format <br>
2.6. Remove duplicates keeping first  <br>
2.7. Export csv for data extraction and visualization

## 3. Data Exploration & Visualization
3.1. Create subset filtering Country data to Brazil <br>
3.2. Count yearly occurencies of attacks <br>
3.3. Found median and average values to stablish baseline. <br>
3.4. define a criteria by which analyse data <br>
3.5. Filter data from 1950 onwards for better visualization <br>
> ANGRYNESS FACTOR: to be relevant angryness factor should be at least 20% above average. <br>


## 4. Plotting

## <span style="color:darkslategrey">Q1: Which genre(s) am I most likely to watch on Netflix?</span>

<img width="808" alt="Shark-attacks_BR_WC-2014" src="images\genre_graph.png">


### <span style="color:darkslategrey"> ### Q2: Which months I have Netflix & Chilled the most recently? </span>

<img width="803" alt="Shark-attacks_BR_WC-history" src="https://user-images.githubusercontent.com/32434139/215419969-23c9c1f9-b973-40b1-9297-eef49dac37f4.png">


### <span style="color:lightslategrey; line-height:1.5em"> **Analysis:** </span>

Data shows that _Brazilian_ sharks do not react negatively when Brazil loses in the World Cup at all, with numbers in those periods being in all time lows. 

In fact, the rise of the 'angryness factor' on the years leading to some World Cups (see 2002, 2006, 2010 and 2018) could indicate that _Brazilian_ _sharks_ are are generally against what some believe to be the Bread and Circus politics surrounding the event. Qualitative data (e.g. interview with the sharks), is needed for further analysis on that subject. 


## <span style="color:darkslateblue"> ### Q3: How do the seasons affect my choices? </span>

<img width="755" alt="Shark-attacks_BR_angryness" src="https://user-images.githubusercontent.com/32434139/215419878-77e69851-ae71-48dd-ab53-ee1463d80820.png">


### <span style="color:lightslategrey; line-height:1.5em"> **Analysis:** </span>

Data shows that most fatal attacks happened when Brazil won the worldcup which is leading this researcher to believe that perhaps this is actually how sharks celebrate the world cup. Further research is required to understand sharks customs regarding sports. 


### <span style="color:lightslategrey; line-height:1.5em"> **Conclusion:** </span> 
There's no direct correlation between World Cup outcomes and the Angryness Factor of the sharks. However, more qualitative analysis is needed in order to better understand sharks views and costumns around the topic. 

![wow](https://user-images.githubusercontent.com/32434139/215419740-5eff78f2-09fd-4ec8-82a7-64a3bbd8f0f6.gif)

## <span style="color:darkslateblue"> ### Q4: What kind of title am I attracted to the most? </span>

![Shark-attacks_global_WC-history](https://user-images.githubusercontent.com/32434139/215450500-2ca025fa-52a8-481b-89d0-7592fb810845.png)

### <span style="color:lightslategrey; line-height:1.5em"> **Analysis:** </span>

None of the countries that made it to the World Cup finals had a significant increase in the number of attacks, regardless of the outcome of the match. 
Note: Netherlands data was not available in the dataset.  

### Thank you!

