#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# from myConvexHull import ConvexHull

from scipy.spatial import ConvexHull


#%%
# visualisasi hasil ConvexHull dari iris dataset
# sepal length vs sepal width
data = datasets.load_iris()

# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Target"] = pd.DataFrame(data.target)
print(df.shape)
df.head()

plt.figure(figsize=(10, 6))
colors = ["b", "r", "g"]
x = 0
y = 1
plt.title(data.feature_names[x] + " vs " + data.feature_names[y])
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])
for i in range(len(data.target_names)):
    bucket = df[df["Target"] == i]
    bucket = bucket.iloc[:, [x, y]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()

# %%
# visualisasi hasil ConvexHull dari iris dataset
# petal length vs petal width
data = datasets.load_iris()

# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Target"] = pd.DataFrame(data.target)
print(df.shape)
df.head()

plt.figure(figsize=(10, 6))
colors = ["b", "r", "g"]
x = 2
y = 3
plt.title(data.feature_names[x] + " vs " + data.feature_names[y])
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])
for i in range(len(data.target_names)):
    bucket = df[df["Target"] == i]
    bucket = bucket.iloc[:, [x, y]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()

# %%
# visualisasi hasil ConvexHull dari wine dataset
# flavanoids vs nonflavanoid_phenols
data = datasets.load_wine()

# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Target"] = pd.DataFrame(data.target)
print(df.shape)
df.head()

plt.figure(figsize=(10, 6))
colors = ["b", "r", "g"]
x = 6
y = 7
plt.title(data.feature_names[x] + " vs " + data.feature_names[y])
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])
for i in range(len(data.target_names)):
    bucket = df[df["Target"] == i]
    bucket = bucket.iloc[:, [x, y]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()

# %%
# visualisasi hasil ConvexHull dari breast cancer dataset
# mean radius vs mean texture
data = datasets.load_breast_cancer()

# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Target"] = pd.DataFrame(data.target)
print(df.shape)
df.head()


plt.figure(figsize=(10, 6))
colors = ["b", "r", "g"]
x = 0
y = 1
plt.title(data.feature_names[x] + " vs " + data.feature_names[y])
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])
for i in range(len(data.target_names)):
    bucket = df[df["Target"] == i]
    bucket = bucket.iloc[:, [x, y]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
# %%
