
# Project Title

A financial planning calculator that roughly projects our future income, expenses and accumulated savings based on a variety of factors such as ***inflation*** & ***wage growth***. 

## Description
To use this calculator, follow the steps below
```bash
1. Input your income and expenses
2. Select your industry, Country & Forecasting length
3. Read the graph!
```

### Additional Features

While the original idea only consisted of the user inputing their own inflation and wage growth, I took the extra step of using my data analyzing and cleaning skills to acquire the datasets for *global inflation rates* and *wage growth for Canadian industries*.

 I did a bit of cleaning up and calculated a average inflation rates and wage growths of each individual country and industry using *pandas*.

 I then used the dataframes as a selectboxes for the user to allow for a more realistic forecasting with this calculator.
## Deployment

### Prerequisite Python Libraries
    1. Streamlit
    2. Plotly
    3. Numpy



**To deploy this project run**

```bash
  streamlit run calculator.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Screenshots

![Input](https://drive.google.com/file/d/1NfZu7fM47ZEdFRn7ioJxai0eX4oP__sF/view?usp=sharing)
![Forecasting](https://drive.google.com/file/d/1TIOt7fBwBgP4j_GsybTfiknc0h2cshCv/view?usp=sharing)
![Graphs](https://drive.google.com/file/d/1TIOt7fBwBgP4j_GsybTfiknc0h2cshCv/view?usp=sharing)
![Selection](https://drive.google.com/file/d/1Zf1EgCXXtUnSDGLHNfkg98DbISCVWMw7/view?usp=sharing)





