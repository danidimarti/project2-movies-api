
![intro](https://user-images.githubusercontent.com/32434139/217019138-d6393f5e-d4b2-4552-a3f6-ba587c41438b.gif)

# What can data say about my Netflix habits?
> _A cross data analysis between imdb and my Netflix viewing history_
----

## 1. Libraries:
<ol>
    <li> 1. Libraries: </li>
    <ul> 
        <li>plotly</li>
        <li>matplotlib </li>
        <li>numpy </li>
        <li>pandas </li>
        <li>calendar </li>
        <li>warnings </li>
        <li>wordloud </li>
        <li>random </li>
        <li>pillow </li>
    </ul>
</ol> 

## 2. Data Sources: 
<ol>
    <li> 1. Personal Netflix viewing history, which can be retrieved from this link: https://www.netflix.com/YourAccount </li>
        <ul> 
        <li>Columns: Title, Date </li>
        <li>832 values / 544 unique</li>
    </ul>
    <li> 2. Web Scrape of this IMDB list: https://www.imdb.com/search/title/?companies=co0144901 </li>
    <ul> 
        <li>list ordered by popularity </li>
        <li>1000/ 250000 instances retieved </li>
        <li>996 values / 986 unique </li>
        <li>Columns: title, ratings and genre </li>
    </ul>
</ol>       
        > Note: IMDB offers two API options: official (paid), unoficial (free). An attempt to retrieve data via a unofficial IMDB API was made. However, the free API possess limited options. The above list would allow more possiblities for analysis. 
 

## 3. Data Extraction and Cleaning Documentation: 
<ol>
    <li> Scrape data from IMDB list </li>
    <li>Indefy tag and classes of Title, Ratings, and Genres</li>
    <li>Consistent naming convention for joining tables later: word separation, removed subtitles and episode names(anything after :), removed line break tags, etc</li>
    <li>Review need for dropping NaN</li>
    <li>Remove duplicates</li>
    <li>LEFT JOIN df_netflix to df_imdb based on Title name</li>
    <li>Drop duplicates</li>
    <li>Export CSV for extraction and visualization</li>
    
</ol> 


## 4. Analysis & Visualization

## <span style="color:darkslategrey">Q1: Which genre(s) am I most likely to watch on Netflix?</span>

<img width="808" alt="genre-graph" src="images\genre_graph.png">


## <span style="color:darkslategrey">Q2: Which months I have Netflix & Chilled the most recently? </span>

<img width="803" alt="seasons" src="images\seasons.png">


## <span style="color:darkslategrey">Q3: How picky am I when chosing a movie of a certain genre?  </span>


![ratings](https://user-images.githubusercontent.com/32434139/217028373-883ffa3b-dbc9-4819-8e07-4ad8de96f4b0.png)


## <span style="color:darkslategrey">Q4: How do the seasons affect my choices? </span>


![genre-and-season](https://user-images.githubusercontent.com/32434139/217028412-f9113711-9cce-480a-aca2-d2134c6f49b3.png)


## <span style="color:darkslategrey">Q5: What kind of title attracks me the most? </span>

<img width="600" alt="wordcloud" src="images\wordcloud.png">

![popcorn](https://user-images.githubusercontent.com/32434139/217019247-f28a71e5-bc78-4d19-bfec-8102ea08be54.gif)

### Thank you!

