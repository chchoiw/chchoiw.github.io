


## Naive Bayes Algorithm

- Basically, this is my studying from [NTCU open course](http://ocw.nctu.edu.tw/index.php) - [Machine Learning](http://ocw.nctu.edu.tw/course_detail.php?bgid=1&gid=1&nid=563&page=1). I  take the key points for my references.
### Bayes' Rule
Assume that $\{B_i, i=1,\dots,n\}$ is a partition of $S$ such that $P(B_i)>0 \text{ for }  i=1,2,...,k$. Then

$$
\begin{aligned}
P(B_j|A)  &= \frac{P(A|B_j)P(B_j)}{P(A)}\\
&=\frac{P(A|B_j)P(B_j)}{\sum_{i=1}^kP(A|B_i)P(B_i)}
\end{aligned}
$$

### The Bayes' Classifier

$$
P(C_i|x)=max_{k} p(C_k|x)
$$

* For choose $i$ such that $P(C_i|x)$ is maximum is irrelevant with the value of $P(x)$.

### Naive Bayes Algorithm
- Two not reasonalbe assumptions
    * The importance of each of attribute is equal
    * All attributes are conditional probability independent.
$$
\begin{aligned}
P(y=1|x)=\frac{P(y=1)}{P(X=x)} \prod_{i=1}^n
 P(y=1|X_i=x_i)\end{aligned}
$$

### Likelihood Function

- ex. a baised coin flip $N$ times, and we could use **MLE**(Maximum Likelihood Estimates) to estimate the probability $p$ of coin with positive side.

$$
p=\frac{\sum_{i=1}^N x_t}{N}
$$

### Example

![](naive_bayes_alog.JPG)

![](naive_bayes_alog2.JPG)

- The above images are captured from [link](https://youtu.be/ZDFYXjc-j4w)


### python code
- This is from [website](https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn)

```python 
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
```

- Encoding Features

```python
# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
weather_encoded=le.fit_transform(weather)
print weather_encoded
```

```python 
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print "Temp:",temp_encoded
print "Play:",label
features=zip(weather_encoded,temp_encoded)
print features
```
- Perform prediction
```python 
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,label)

#Predict Output
predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print "Predicted Value:", predicted
```