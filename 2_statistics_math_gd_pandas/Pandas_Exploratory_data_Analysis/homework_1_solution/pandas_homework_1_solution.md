

```python
import pandas as pd
```

## Basic info

Read the data-file (a 10 000 row subset of most rated IMDB-movies) into Pandas DataFrame and name the DataFrame-variable to `df` (use tab-character (`\t`) as the separator)

1. Use the following column-names: `ID, title, year, rating, votes, duration, genres`
2. Index the `df` with `ID`-column (either on reading the file or after it.)
3. Display first 5 rows of the `df`
4. Display last 11 rows of the `df`
5. Display the `df`-info


```python
# 1.
names = ['ID', 'title', 'year', 'rating', 'votes', 'duration', 'genres']
df = pd.read_csv('movie_data.txt', sep='\t', names=names)
```


```python
# 2.
df.set_index('ID', inplace=True)
# or
# df = pd.read_csv('data.txt', sep='\t', names=names, index_col='ID')
```


```python
# 3.
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption (1994)</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>142 mins.</td>
      <td>Crime|Drama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tt0110912</td>
      <td>Pulp Fiction (1994)</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>154 mins.</td>
      <td>Crime|Thriller</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tt0137523</td>
      <td>Fight Club (1999)</td>
      <td>1999</td>
      <td>8.8</td>
      <td>458173</td>
      <td>139 mins.</td>
      <td>Drama|Mystery|Thriller</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tt0133093</td>
      <td>The Matrix (1999)</td>
      <td>1999</td>
      <td>8.7</td>
      <td>448114</td>
      <td>136 mins.</td>
      <td>Action|Adventure|Sci-Fi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt1375666</td>
      <td>Inception (2010)</td>
      <td>2010</td>
      <td>8.9</td>
      <td>385149</td>
      <td>148 mins.</td>
      <td>Action|Adventure|Sci-Fi|Thriller</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 4.
df.tail(11)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9989</th>
      <td>tt0101356</td>
      <td>Another You (1991)</td>
      <td>1991</td>
      <td>4.9</td>
      <td>1359</td>
      <td>98 mins.</td>
      <td>Comedy|Crime</td>
    </tr>
    <tr>
      <th>9990</th>
      <td>tt0421090</td>
      <td>Zerophilia (2005)</td>
      <td>2005</td>
      <td>6.3</td>
      <td>1359</td>
      <td>90 mins.</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>9991</th>
      <td>tt0067227</td>
      <td>The Merchant of Four Seasons (1971)</td>
      <td>1971</td>
      <td>7.6</td>
      <td>1359</td>
      <td>88 mins.</td>
      <td>Drama</td>
    </tr>
    <tr>
      <th>9992</th>
      <td>tt0339727</td>
      <td>Stateside (2004)</td>
      <td>2004</td>
      <td>5.8</td>
      <td>1358</td>
      <td>97 mins.</td>
      <td>Drama|Music|Romance</td>
    </tr>
    <tr>
      <th>9993</th>
      <td>tt0218581</td>
      <td>Scarlet Diva (2000)</td>
      <td>2000</td>
      <td>5.2</td>
      <td>1358</td>
      <td>91 mins.</td>
      <td>Drama</td>
    </tr>
    <tr>
      <th>9994</th>
      <td>tt0118635</td>
      <td>Aprile (1998)</td>
      <td>1998</td>
      <td>6.7</td>
      <td>1358</td>
      <td>78 mins.</td>
      <td>Comedy</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>tt0807721</td>
      <td>Meduzot (2007)</td>
      <td>2007</td>
      <td>7.0</td>
      <td>1357</td>
      <td>78 mins.</td>
      <td>Drama</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>tt0339642</td>
      <td>Daltry Calhoun (2005)</td>
      <td>2005</td>
      <td>5.2</td>
      <td>1357</td>
      <td>100 mins.</td>
      <td>Comedy|Drama|Music|Romance</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>tt0060880</td>
      <td>The Quiller Memorandum (1966)</td>
      <td>1966</td>
      <td>6.5</td>
      <td>1356</td>
      <td>104 mins.</td>
      <td>Drama|Mystery|Thriller</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>tt0152836</td>
      <td>Taal (1999)</td>
      <td>1999</td>
      <td>6.5</td>
      <td>1356</td>
      <td>179 mins.</td>
      <td>Musical|Romance</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>tt0279977</td>
      <td>The Navigators (2001)</td>
      <td>2001</td>
      <td>6.9</td>
      <td>1356</td>
      <td>96 mins.</td>
      <td>Comedy|Drama</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 5.
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 7 columns):
    ID          10000 non-null object
    title       10000 non-null object
    year        10000 non-null int64
    rating      10000 non-null float64
    votes       10000 non-null int64
    duration    10000 non-null object
    genres      9999 non-null object
    dtypes: float64(1), int64(2), object(4)
    memory usage: 547.0+ KB


## Cleaning

1. Drop all the missing rows which contain _any_ column with missing data
2. Convert the `duration` column to numerical representation of seconds
3. Remove the year from `title` column


```python
# 1.
df.dropna(inplace=True)
```


```python
# 2.
df['duration'] = df['duration'].map(lambda s: int(s.replace(" mins.", "")) * 60)
```


```python
# 3.
df['title'] = [i[:-7] for i in df['title']]

df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>8520</td>
      <td>Crime|Drama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tt0110912</td>
      <td>Pulp Fiction</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>9240</td>
      <td>Crime|Thriller</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tt0137523</td>
      <td>Fight Club</td>
      <td>1999</td>
      <td>8.8</td>
      <td>458173</td>
      <td>8340</td>
      <td>Drama|Mystery|Thriller</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tt0133093</td>
      <td>The Matrix</td>
      <td>1999</td>
      <td>8.7</td>
      <td>448114</td>
      <td>8160</td>
      <td>Action|Adventure|Sci-Fi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt1375666</td>
      <td>Inception</td>
      <td>2010</td>
      <td>8.9</td>
      <td>385149</td>
      <td>8880</td>
      <td>Action|Adventure|Sci-Fi|Thriller</td>
    </tr>
  </tbody>
</table>
</div>



## Concatenating

1. Read `crew_data.tsv.gz` to DataFrame named `movie_crew_df` with columns `ID, director_ids` indexed by `ID` (forget the rest of the columns)
2. Read `person_data.tsv.gz` to DataFrame named `person_df` with columns `person_ID, name` indexed by `person_ID` (forget the rest of the columns)
3. Merge `movie_crew_df` into `df` with `ID`s and drop the columns without necessary data (hint `outer`-join)
4. Remove movies with more than one director and rename `director_ids` => `director_id`
5. Merge `df` with `person_df` on `director_id`, remove `director_id` and `person_ID` columns, rename `name` => `director`


```python
# 1.
movie_crew_df = pd.read_csv('crew_data.tsv.gz', sep="\t", usecols=[0, 1], names=['ID', 'director_ids'], index_col=['ID'], header=0).dropna()
```


```python
# 2.
person_df = pd.read_csv('name_data.tsv.gz', sep="\t", usecols=[0, 1], names=['person_ID', 'name'], header=0).dropna()
```


```python
# 3.
df = df.merge(movie_crew_df, how='inner', left_on='ID', right_on='ID')
df.dropna(inplace=True)
```


```python
# 4.
df = df.loc[df['director_ids'].str.len() == 9]
df.rename(columns={'director_ids': 'director_id'}, inplace=True)
```


```python
# 5.
df = df.merge(person_df, how='inner', left_on='director_id', right_on='person_ID')
df.rename(columns={'name': 'director'}, inplace=True)
df.drop(['director_id', 'person_ID'], inplace=True, axis=1)
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
      <th>director</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>8520</td>
      <td>Crime|Drama</td>
      <td>Frank Darabont</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tt0120689</td>
      <td>The Green Mile</td>
      <td>1999</td>
      <td>8.4</td>
      <td>243660</td>
      <td>11340</td>
      <td>Crime|Drama|Fantasy|Mystery</td>
      <td>Frank Darabont</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tt0884328</td>
      <td>The Mist</td>
      <td>2007</td>
      <td>7.4</td>
      <td>90987</td>
      <td>7560</td>
      <td>Horror|Sci-Fi|Thriller</td>
      <td>Frank Darabont</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tt0268995</td>
      <td>The Majestic</td>
      <td>2001</td>
      <td>6.8</td>
      <td>27241</td>
      <td>9120</td>
      <td>Drama|Romance</td>
      <td>Frank Darabont</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt0110912</td>
      <td>Pulp Fiction</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>9240</td>
      <td>Crime|Thriller</td>
      <td>Quentin Tarantino</td>
    </tr>
  </tbody>
</table>
</div>



## Exploration

1. Find ten most longest movies
2. Find Best rated movies ordered by rating DESC and Title ASC
3. What is the average duration (in minutes) of a movie?
4. Get ten most productive directors
5. How many movie has been made in the 2000's?
6. Get all the movies directed by Akira Kurosawa ordered by year DESC


```python
# 1.
df.nlargest(10, 'duration')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
      <th>director</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8059</th>
      <td>tt0111341</td>
      <td>Satantango</td>
      <td>1994</td>
      <td>8.5</td>
      <td>2698</td>
      <td>27000</td>
      <td>Comedy|Drama|Mystery</td>
      <td>Béla Tarr</td>
    </tr>
    <tr>
      <th>7958</th>
      <td>tt0063794</td>
      <td>War and Peace</td>
      <td>1967</td>
      <td>7.8</td>
      <td>2833</td>
      <td>25620</td>
      <td>Drama|History|Romance|War</td>
      <td>Sergey Bondarchuk</td>
    </tr>
    <tr>
      <th>5230</th>
      <td>tt0107007</td>
      <td>Gettysburg</td>
      <td>1993</td>
      <td>7.7</td>
      <td>12093</td>
      <td>15660</td>
      <td>Drama|History|War</td>
      <td>Ron Maxwell</td>
    </tr>
    <tr>
      <th>1941</th>
      <td>tt0116477</td>
      <td>Hamlet</td>
      <td>1996</td>
      <td>7.7</td>
      <td>19698</td>
      <td>14520</td>
      <td>Crime|Drama|Romance|Thriller</td>
      <td>Kenneth Branagh</td>
    </tr>
    <tr>
      <th>6246</th>
      <td>tt1128075</td>
      <td>Love Exposure</td>
      <td>2008</td>
      <td>8.0</td>
      <td>1922</td>
      <td>14220</td>
      <td>Action|Comedy|Drama|Romance</td>
      <td>Sion Sono</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 2.
df.sort_values(by=['rating', 'title'], ascending=[False, True]).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
      <th>director</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>145</th>
      <td>tt0068646</td>
      <td>The Godfather</td>
      <td>1972</td>
      <td>9.2</td>
      <td>474189</td>
      <td>10500</td>
      <td>Crime|Drama</td>
      <td>Francis Ford Coppola</td>
    </tr>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>8520</td>
      <td>Crime|Drama</td>
      <td>Frank Darabont</td>
    </tr>
    <tr>
      <th>5636</th>
      <td>tt0252487</td>
      <td>Outrageous Class</td>
      <td>1975</td>
      <td>9.0</td>
      <td>9823</td>
      <td>5220</td>
      <td>Comedy|Drama</td>
      <td>Ertem Egilmez</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt0110912</td>
      <td>Pulp Fiction</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>9240</td>
      <td>Crime|Thriller</td>
      <td>Quentin Tarantino</td>
    </tr>
    <tr>
      <th>146</th>
      <td>tt0071562</td>
      <td>The Godfather: Part II</td>
      <td>1974</td>
      <td>9.0</td>
      <td>291169</td>
      <td>12000</td>
      <td>Crime|Drama</td>
      <td>Francis Ford Coppola</td>
    </tr>
    <tr>
      <th>339</th>
      <td>tt0060196</td>
      <td>The Good, the Bad and the Ugly</td>
      <td>1966</td>
      <td>9.0</td>
      <td>195238</td>
      <td>9660</td>
      <td>Western</td>
      <td>Sergio Leone</td>
    </tr>
    <tr>
      <th>631</th>
      <td>tt0050083</td>
      <td>12 Angry Men</td>
      <td>1957</td>
      <td>8.9</td>
      <td>148155</td>
      <td>5760</td>
      <td>Drama|Mystery</td>
      <td>Sidney Lumet</td>
    </tr>
    <tr>
      <th>18</th>
      <td>tt1375666</td>
      <td>Inception</td>
      <td>2010</td>
      <td>8.9</td>
      <td>385149</td>
      <td>8880</td>
      <td>Action|Adventure|Sci-Fi|Thriller</td>
      <td>Christopher Nolan</td>
    </tr>
    <tr>
      <th>215</th>
      <td>tt0073486</td>
      <td>One Flew Over the Cuckoo's Nest</td>
      <td>1975</td>
      <td>8.9</td>
      <td>255503</td>
      <td>7980</td>
      <td>Drama</td>
      <td>Milos Forman</td>
    </tr>
    <tr>
      <th>52</th>
      <td>tt0108052</td>
      <td>Schindler's List</td>
      <td>1993</td>
      <td>8.9</td>
      <td>325888</td>
      <td>11700</td>
      <td>Biography|Drama|History|War</td>
      <td>Steven Spielberg</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 3.
df['duration'].mean() / 60
```




    104.05281541066893




```python
# 4.
df['director'].value_counts().head(10)
```




    Woody Allen         40
    Clint Eastwood      31
    Sidney Lumet        27
    Steven Spielberg    24
    Robert Altman       24
    Brian De Palma      23
    John Huston         23
    Joel Schumacher     22
    Martin Scorsese     21
    Blake Edwards       21
    Name: director, dtype: int64




```python
# 5.
len(df.loc[df['year'] >= 2000])
```




    4283




```python
# 6.
df.loc[df['director'] == 'Akira Kurosawa'].sort_values(by=['year'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>title</th>
      <th>year</th>
      <th>rating</th>
      <th>votes</th>
      <th>duration</th>
      <th>genres</th>
      <th>director</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>854</th>
      <td>tt0042876</td>
      <td>Rashomon</td>
      <td>1950</td>
      <td>8.4</td>
      <td>46250</td>
      <td>5280</td>
      <td>Crime|Drama|Mystery</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>870</th>
      <td>tt0043614</td>
      <td>The Idiot</td>
      <td>1951</td>
      <td>7.5</td>
      <td>1680</td>
      <td>9960</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>857</th>
      <td>tt0044741</td>
      <td>Ikiru</td>
      <td>1952</td>
      <td>8.3</td>
      <td>18948</td>
      <td>8580</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>853</th>
      <td>tt0047478</td>
      <td>Seven Samurai</td>
      <td>1954</td>
      <td>8.8</td>
      <td>111707</td>
      <td>12420</td>
      <td>Adventure|Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>871</th>
      <td>tt0048198</td>
      <td>I Live in Fear</td>
      <td>1955</td>
      <td>7.3</td>
      <td>1360</td>
      <td>6180</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>858</th>
      <td>tt0050613</td>
      <td>Throne of Blood</td>
      <td>1957</td>
      <td>8.1</td>
      <td>13559</td>
      <td>6600</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>869</th>
      <td>tt0050330</td>
      <td>The Lower Depths</td>
      <td>1957</td>
      <td>7.5</td>
      <td>1901</td>
      <td>8220</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>859</th>
      <td>tt0051808</td>
      <td>The Hidden Fortress</td>
      <td>1958</td>
      <td>8.1</td>
      <td>12535</td>
      <td>8340</td>
      <td>Action|Adventure</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>865</th>
      <td>tt0054460</td>
      <td>The Bad Sleep Well</td>
      <td>1960</td>
      <td>8.0</td>
      <td>3356</td>
      <td>9060</td>
      <td>Crime|Drama|Thriller</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>856</th>
      <td>tt0055630</td>
      <td>Yojimbo</td>
      <td>1961</td>
      <td>8.4</td>
      <td>33878</td>
      <td>6600</td>
      <td>Action|Crime|Drama|Thriller</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>861</th>
      <td>tt0056443</td>
      <td>Sanjuro</td>
      <td>1962</td>
      <td>8.1</td>
      <td>9739</td>
      <td>5760</td>
      <td>Action|Drama|Thriller</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>863</th>
      <td>tt0057565</td>
      <td>High and Low</td>
      <td>1963</td>
      <td>8.3</td>
      <td>8603</td>
      <td>8520</td>
      <td>Crime|Drama|Thriller</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>864</th>
      <td>tt0058888</td>
      <td>Red Beard</td>
      <td>1965</td>
      <td>8.1</td>
      <td>5747</td>
      <td>11100</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>867</th>
      <td>tt0065649</td>
      <td>Dodes'ka-den</td>
      <td>1970</td>
      <td>7.6</td>
      <td>2371</td>
      <td>8400</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>862</th>
      <td>tt0071411</td>
      <td>Dersu Uzala</td>
      <td>1975</td>
      <td>8.2</td>
      <td>9180</td>
      <td>8640</td>
      <td>Adventure|Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>860</th>
      <td>tt0080979</td>
      <td>Kagemusha</td>
      <td>1980</td>
      <td>7.9</td>
      <td>12492</td>
      <td>10800</td>
      <td>Drama|History|War</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>855</th>
      <td>tt0089881</td>
      <td>Ran</td>
      <td>1985</td>
      <td>8.3</td>
      <td>39096</td>
      <td>9720</td>
      <td>Action|Drama|War</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>866</th>
      <td>tt0101991</td>
      <td>Rhapsody in August</td>
      <td>1991</td>
      <td>7.2</td>
      <td>2830</td>
      <td>5880</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
    <tr>
      <th>868</th>
      <td>tt0107474</td>
      <td>Madadayo</td>
      <td>1993</td>
      <td>7.4</td>
      <td>1935</td>
      <td>8040</td>
      <td>Drama</td>
      <td>Akira Kurosawa</td>
    </tr>
  </tbody>
</table>
</div>


