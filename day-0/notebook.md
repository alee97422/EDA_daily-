```python
import pandas as pd

```


```python
pip install openpyxl
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: openpyxl in /opt/anaconda/lib/python3.11/site-packages (3.0.10)
    Requirement already satisfied: et_xmlfile in /opt/anaconda/lib/python3.11/site-packages (from openpyxl) (1.1.0)
    Note: you may need to restart the kernel to use updated packages.



```python
df = pd.read_excel('/home/anthony/Desktop/EDAeveryday/day 0/Cola.xlsx')
df
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
      <th>Data provided by SimFin</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Profit &amp; Loss statement</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>in million USD</td>
      <td>FY '09</td>
      <td>FY '10</td>
      <td>FY '11</td>
      <td>FY '12</td>
      <td>FY '13</td>
      <td>FY '14</td>
      <td>FY '15</td>
      <td>FY '16</td>
      <td>FY '17</td>
      <td>FY '18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NET OPERATING REVENUES</td>
      <td>30990</td>
      <td>35119</td>
      <td>46542</td>
      <td>48017</td>
      <td>46854</td>
      <td>45998</td>
      <td>44294</td>
      <td>41863</td>
      <td>35410</td>
      <td>31856</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Cost of goods sold</td>
      <td>11088</td>
      <td>12693</td>
      <td>18215</td>
      <td>19053</td>
      <td>18421</td>
      <td>17889</td>
      <td>17482</td>
      <td>16465</td>
      <td>13255</td>
      <td>11770</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>98</th>
      <td>NaN</td>
      <td>Effect of exchange rate changes on cash and ca...</td>
      <td>576</td>
      <td>-166</td>
      <td>-430</td>
      <td>-255</td>
      <td>-611</td>
      <td>-934</td>
      <td>-878</td>
      <td>-6</td>
      <td>241</td>
      <td>-262</td>
    </tr>
    <tr>
      <th>99</th>
      <td>NaN</td>
      <td>Cash Provided by (Used in) Investing Activitie...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-58</td>
      <td>-421</td>
    </tr>
    <tr>
      <th>100</th>
      <td>NaN</td>
      <td>Cash Provided by (Used in) Financing Activitie...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-38</td>
      <td>205</td>
    </tr>
    <tr>
      <th>101</th>
      <td>NaN</td>
      <td>Net Cash Provided by (Used in) Discontinued Op...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>91</td>
    </tr>
    <tr>
      <th>102</th>
      <td>NaN</td>
      <td>Net increase (decrease) during the year</td>
      <td>2320</td>
      <td>1496</td>
      <td>4286</td>
      <td>-4361</td>
      <td>1972</td>
      <td>-1456</td>
      <td>-1649</td>
      <td>1246</td>
      <td>-2477</td>
      <td>2945</td>
    </tr>
  </tbody>
</table>
<p>103 rows × 12 columns</p>
</div>




```python
df1.head(10)
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
      <th>Data provided by SimFin</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Profit &amp; Loss statement</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>in million USD</td>
      <td>FY '09</td>
      <td>FY '10</td>
      <td>FY '11</td>
      <td>FY '12</td>
      <td>FY '13</td>
      <td>FY '14</td>
      <td>FY '15</td>
      <td>FY '16</td>
      <td>FY '17</td>
      <td>FY '18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NET OPERATING REVENUES</td>
      <td>30990</td>
      <td>35119</td>
      <td>46542</td>
      <td>48017</td>
      <td>46854</td>
      <td>45998</td>
      <td>44294</td>
      <td>41863</td>
      <td>35410</td>
      <td>31856</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Cost of goods sold</td>
      <td>11088</td>
      <td>12693</td>
      <td>18215</td>
      <td>19053</td>
      <td>18421</td>
      <td>17889</td>
      <td>17482</td>
      <td>16465</td>
      <td>13255</td>
      <td>11770</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>Gross Profit</td>
      <td>19902</td>
      <td>22426</td>
      <td>28327</td>
      <td>28964</td>
      <td>28433</td>
      <td>28109</td>
      <td>26812</td>
      <td>25398</td>
      <td>22155</td>
      <td>20086</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>Selling, general and administrative expenses</td>
      <td>11358</td>
      <td>13194</td>
      <td>17422</td>
      <td>17738</td>
      <td>17310</td>
      <td>17218</td>
      <td>16427</td>
      <td>15262</td>
      <td>12654</td>
      <td>10307</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>Other operating charges</td>
      <td>313</td>
      <td>819</td>
      <td>732</td>
      <td>447</td>
      <td>895</td>
      <td>1183</td>
      <td>1657</td>
      <td>1510</td>
      <td>1902</td>
      <td>1079</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>Operating Income</td>
      <td>8231</td>
      <td>8413</td>
      <td>10173</td>
      <td>10779</td>
      <td>10228</td>
      <td>9708</td>
      <td>8728</td>
      <td>8626</td>
      <td>7599</td>
      <td>8700</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>Interest income</td>
      <td>249</td>
      <td>317</td>
      <td>483</td>
      <td>471</td>
      <td>534</td>
      <td>594</td>
      <td>613</td>
      <td>642</td>
      <td>677</td>
      <td>682</td>
    </tr>
  </tbody>
</table>
</div>



## Initial Analysis 
initially we can see that the data set is an absolute hot mess!
the 3rd row seems to be the best header row so lets go ahead and skip the first 3 rows and fix it and then use the first column as Index


```python
df =pd.read_excel("/home/anthony/Desktop/EDAeveryday/day 0/Cola.xlsx",skiprows=3,index_col="in million USD")
```


```python
df
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
      <th>Unnamed: 0</th>
      <th>FY '09</th>
      <th>FY '10</th>
      <th>FY '11</th>
      <th>FY '12</th>
      <th>FY '13</th>
      <th>FY '14</th>
      <th>FY '15</th>
      <th>FY '16</th>
      <th>FY '17</th>
      <th>FY '18</th>
    </tr>
    <tr>
      <th>in million USD</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NET OPERATING REVENUES</th>
      <td>NaN</td>
      <td>30990</td>
      <td>35119</td>
      <td>46542</td>
      <td>48017</td>
      <td>46854</td>
      <td>45998</td>
      <td>44294</td>
      <td>41863</td>
      <td>35410</td>
      <td>31856</td>
    </tr>
    <tr>
      <th>Cost of goods sold</th>
      <td>NaN</td>
      <td>11088</td>
      <td>12693</td>
      <td>18215</td>
      <td>19053</td>
      <td>18421</td>
      <td>17889</td>
      <td>17482</td>
      <td>16465</td>
      <td>13255</td>
      <td>11770</td>
    </tr>
    <tr>
      <th>Gross Profit</th>
      <td>NaN</td>
      <td>19902</td>
      <td>22426</td>
      <td>28327</td>
      <td>28964</td>
      <td>28433</td>
      <td>28109</td>
      <td>26812</td>
      <td>25398</td>
      <td>22155</td>
      <td>20086</td>
    </tr>
    <tr>
      <th>Selling, general and administrative expenses</th>
      <td>NaN</td>
      <td>11358</td>
      <td>13194</td>
      <td>17422</td>
      <td>17738</td>
      <td>17310</td>
      <td>17218</td>
      <td>16427</td>
      <td>15262</td>
      <td>12654</td>
      <td>10307</td>
    </tr>
    <tr>
      <th>Other operating charges</th>
      <td>NaN</td>
      <td>313</td>
      <td>819</td>
      <td>732</td>
      <td>447</td>
      <td>895</td>
      <td>1183</td>
      <td>1657</td>
      <td>1510</td>
      <td>1902</td>
      <td>1079</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Effect of exchange rate changes on cash and cash equivalents</th>
      <td>NaN</td>
      <td>576</td>
      <td>-166</td>
      <td>-430</td>
      <td>-255</td>
      <td>-611</td>
      <td>-934</td>
      <td>-878</td>
      <td>-6</td>
      <td>241</td>
      <td>-262</td>
    </tr>
    <tr>
      <th>Cash Provided by (Used in) Investing Activities, Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-58</td>
      <td>-421</td>
    </tr>
    <tr>
      <th>Cash Provided by (Used in) Financing Activities, Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-38</td>
      <td>205</td>
    </tr>
    <tr>
      <th>Net Cash Provided by (Used in) Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>91</td>
    </tr>
    <tr>
      <th>Net increase (decrease) during the year</th>
      <td>NaN</td>
      <td>2320</td>
      <td>1496</td>
      <td>4286</td>
      <td>-4361</td>
      <td>1972</td>
      <td>-1456</td>
      <td>-1649</td>
      <td>1246</td>
      <td>-2477</td>
      <td>2945</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 11 columns</p>
</div>




```python

#making sure the index name is None
df.index.name=None
```


```python
df
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
      <th>Unnamed: 0</th>
      <th>FY '09</th>
      <th>FY '10</th>
      <th>FY '11</th>
      <th>FY '12</th>
      <th>FY '13</th>
      <th>FY '14</th>
      <th>FY '15</th>
      <th>FY '16</th>
      <th>FY '17</th>
      <th>FY '18</th>
    </tr>
    <tr>
      <th>in million USD</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NET OPERATING REVENUES</th>
      <td>NaN</td>
      <td>30990</td>
      <td>35119</td>
      <td>46542</td>
      <td>48017</td>
      <td>46854</td>
      <td>45998</td>
      <td>44294</td>
      <td>41863</td>
      <td>35410</td>
      <td>31856</td>
    </tr>
    <tr>
      <th>Cost of goods sold</th>
      <td>NaN</td>
      <td>11088</td>
      <td>12693</td>
      <td>18215</td>
      <td>19053</td>
      <td>18421</td>
      <td>17889</td>
      <td>17482</td>
      <td>16465</td>
      <td>13255</td>
      <td>11770</td>
    </tr>
    <tr>
      <th>Gross Profit</th>
      <td>NaN</td>
      <td>19902</td>
      <td>22426</td>
      <td>28327</td>
      <td>28964</td>
      <td>28433</td>
      <td>28109</td>
      <td>26812</td>
      <td>25398</td>
      <td>22155</td>
      <td>20086</td>
    </tr>
    <tr>
      <th>Selling, general and administrative expenses</th>
      <td>NaN</td>
      <td>11358</td>
      <td>13194</td>
      <td>17422</td>
      <td>17738</td>
      <td>17310</td>
      <td>17218</td>
      <td>16427</td>
      <td>15262</td>
      <td>12654</td>
      <td>10307</td>
    </tr>
    <tr>
      <th>Other operating charges</th>
      <td>NaN</td>
      <td>313</td>
      <td>819</td>
      <td>732</td>
      <td>447</td>
      <td>895</td>
      <td>1183</td>
      <td>1657</td>
      <td>1510</td>
      <td>1902</td>
      <td>1079</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Effect of exchange rate changes on cash and cash equivalents</th>
      <td>NaN</td>
      <td>576</td>
      <td>-166</td>
      <td>-430</td>
      <td>-255</td>
      <td>-611</td>
      <td>-934</td>
      <td>-878</td>
      <td>-6</td>
      <td>241</td>
      <td>-262</td>
    </tr>
    <tr>
      <th>Cash Provided by (Used in) Investing Activities, Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-58</td>
      <td>-421</td>
    </tr>
    <tr>
      <th>Cash Provided by (Used in) Financing Activities, Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-38</td>
      <td>205</td>
    </tr>
    <tr>
      <th>Net Cash Provided by (Used in) Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>91</td>
    </tr>
    <tr>
      <th>Net increase (decrease) during the year</th>
      <td>NaN</td>
      <td>2320</td>
      <td>1496</td>
      <td>4286</td>
      <td>-4361</td>
      <td>1972</td>
      <td>-1456</td>
      <td>-1649</td>
      <td>1246</td>
      <td>-2477</td>
      <td>2945</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 11 columns</p>
</div>




```python
#dropping the first column as it contains only NaN values
df.drop("Unnamed: 0",axis=1,inplace=True)
```


```python
df
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
      <th>FY '09</th>
      <th>FY '10</th>
      <th>FY '11</th>
      <th>FY '12</th>
      <th>FY '13</th>
      <th>FY '14</th>
      <th>FY '15</th>
      <th>FY '16</th>
      <th>FY '17</th>
      <th>FY '18</th>
    </tr>
    <tr>
      <th>in million USD</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NET OPERATING REVENUES</th>
      <td>30990</td>
      <td>35119</td>
      <td>46542</td>
      <td>48017</td>
      <td>46854</td>
      <td>45998</td>
      <td>44294</td>
      <td>41863</td>
      <td>35410</td>
      <td>31856</td>
    </tr>
    <tr>
      <th>Cost of goods sold</th>
      <td>11088</td>
      <td>12693</td>
      <td>18215</td>
      <td>19053</td>
      <td>18421</td>
      <td>17889</td>
      <td>17482</td>
      <td>16465</td>
      <td>13255</td>
      <td>11770</td>
    </tr>
    <tr>
      <th>Gross Profit</th>
      <td>19902</td>
      <td>22426</td>
      <td>28327</td>
      <td>28964</td>
      <td>28433</td>
      <td>28109</td>
      <td>26812</td>
      <td>25398</td>
      <td>22155</td>
      <td>20086</td>
    </tr>
    <tr>
      <th>Selling, general and administrative expenses</th>
      <td>11358</td>
      <td>13194</td>
      <td>17422</td>
      <td>17738</td>
      <td>17310</td>
      <td>17218</td>
      <td>16427</td>
      <td>15262</td>
      <td>12654</td>
      <td>10307</td>
    </tr>
    <tr>
      <th>Other operating charges</th>
      <td>313</td>
      <td>819</td>
      <td>732</td>
      <td>447</td>
      <td>895</td>
      <td>1183</td>
      <td>1657</td>
      <td>1510</td>
      <td>1902</td>
      <td>1079</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Effect of exchange rate changes on cash and cash equivalents</th>
      <td>576</td>
      <td>-166</td>
      <td>-430</td>
      <td>-255</td>
      <td>-611</td>
      <td>-934</td>
      <td>-878</td>
      <td>-6</td>
      <td>241</td>
      <td>-262</td>
    </tr>
    <tr>
      <th>Cash Provided by (Used in) Investing Activities, Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-58</td>
      <td>-421</td>
    </tr>
    <tr>
      <th>Cash Provided by (Used in) Financing Activities, Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>-38</td>
      <td>205</td>
    </tr>
    <tr>
      <th>Net Cash Provided by (Used in) Discontinued Operations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>91</td>
    </tr>
    <tr>
      <th>Net increase (decrease) during the year</th>
      <td>2320</td>
      <td>1496</td>
      <td>4286</td>
      <td>-4361</td>
      <td>1972</td>
      <td>-1456</td>
      <td>-1649</td>
      <td>1246</td>
      <td>-2477</td>
      <td>2945</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 10 columns</p>
</div>



## Data is much cleaner now :)
so after just a few programatic changes this data set is much cleaner now :)



```python
df.isnull().sum()
```




    FY '09    19
    FY '10    19
    FY '11    19
    FY '12    19
    FY '13    19
    FY '14    19
    FY '15    11
    FY '16     9
    FY '17     8
    FY '18     8
    dtype: int64




```python
df.describe()
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
      <th>FY '09</th>
      <th>FY '10</th>
      <th>FY '11</th>
      <th>FY '12</th>
      <th>FY '13</th>
      <th>FY '14</th>
      <th>FY '15</th>
      <th>FY '16</th>
      <th>FY '17</th>
      <th>FY '18</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>89</td>
      <td>91</td>
      <td>92</td>
      <td>92</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>78</td>
      <td>79</td>
      <td>78</td>
      <td>87</td>
      <td>86</td>
    </tr>
    <tr>
      <th>top</th>
      <td>0</td>
      <td>FY '10</td>
      <td>0</td>
      <td>9086</td>
      <td>0</td>
      <td>FY '14</td>
      <td>0</td>
      <td>0</td>
      <td>1283</td>
      <td>6476</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
      <td>8</td>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv('/home/anthony/Desktop/EDAeveryday/day 0/cleaned_data.csv', index=False)
#saving new dataset as a CSV file
```

## Thank you 
Thank you for checking out my first successful EDA/data clean :) 

I plan on finding/creating/making one of these everyday to help carve my data analysis skills 


```python

```
