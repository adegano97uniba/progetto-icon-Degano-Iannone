import pandas as pd
from KMeans import KMeans
import output_paths
import seaborn as sns
import matplotlib.pyplot as plt


# dataset paths
alcohol_red = r'datasets\red\alcohol_red.csv'
chlorides_red = r'datasets\red\chlorides_red.csv'
citric_acid_red = r'datasets\red\citric_acid_red.csv'
density_red = r'datasets\red\density_red.csv'
fixed_acid_red = r'datasets\red\fixed_acid_red.csv'
free_sulfur_dioxide_red = r'datasets\red\free_sulfur_dioxide_red.csv'
ph_red = r'datasets\red\ph_red.csv'
residual_sugar_red = r'datasets\red\residual_sugar_red.csv'
sulphates_red = r'datasets\red\sulphates_red.csv'
total_sulfur_dioxide_red = r'datasets\red\total_sulfur_dioxide_red.csv'
volatile_acid_red = r'datasets\red\volatile_acid_red.csv'


# datasets loading
dataset_alcohol_red = pd.read_csv(alcohol_red, sep=',', header=None)
dataset_chlorides_red = pd.read_csv(chlorides_red, sep=',', header=None)
dataset_citric_acid_red = pd.read_csv(citric_acid_red, sep=',', header=None)
dataset_density_red = pd.read_csv(density_red, sep=',', header=None)
dataset_fixed_acid_red = pd.read_csv(fixed_acid_red, sep=',', header=None)
dataset_free_sulfur_dioxide_red = pd.read_csv(free_sulfur_dioxide_red, sep=',', header=None)
dataset_ph_red = pd.read_csv(ph_red, sep=',', header=None)
dataset_residual_sugar_red = pd.read_csv(residual_sugar_red, sep=',', header=None)
dataset_sulphates_red = pd.read_csv(sulphates_red, sep=',', header=None)
dataset_total_sulfur_dioxide_red = pd.read_csv(total_sulfur_dioxide_red, sep=',', header=None)
dataset_volatile_acid_red = pd.read_csv(volatile_acid_red, sep=',', header=None)



# red wine per-trait quality clusters ----------------------------------------------------------------- 
kmeans = KMeans(nCluster=3, randomState=721)
kmeans.fit(dataset_alcohol_red)
kmeans.saveFigures(output_paths.out_alcohol_red)
kmeans.createGif(output_paths.out_alcohol_red)

kmeans = KMeans(nCluster=3, randomState=721)
kmeans.fit(dataset_chlorides_red)
kmeans.saveFigures(output_paths.out_chlorides_red)
kmeans.createGif(output_paths.out_chlorides_red)

kmeans = KMeans(nCluster=3, randomState=721)
kmeans.fit(dataset_citric_acid_red)
kmeans.saveFigures(output_paths.out_citric_acid_red)
kmeans.createGif(output_paths.out_citric_acid_red)

kmeans = KMeans(nCluster=3, randomState=721)
kmeans.fit(dataset_density_red)
kmeans.saveFigures(output_paths.out_density_red)
kmeans.createGif(output_paths.out_density_red)

kmeans = KMeans(nCluster=2, randomState=721)
kmeans.fit(dataset_fixed_acid_red)
kmeans.saveFigures(output_paths.out_fixed_acid_red)
kmeans.createGif(output_paths.out_fixed_acid_red)

kmeans = KMeans(nCluster=2, randomState=721)
kmeans.fit(dataset_free_sulfur_dioxide_red)
kmeans.saveFigures(output_paths.out_free_sulfur_dioxide_red)
kmeans.createGif(output_paths.out_free_sulfur_dioxide_red)

kmeans = KMeans(nCluster=4, randomState=721)
kmeans.fit(dataset_ph_red)
kmeans.saveFigures(output_paths.out_ph_red)
kmeans.createGif(output_paths.out_ph_red)

kmeans = KMeans(nCluster=2, randomState=721)
kmeans.fit(dataset_residual_sugar_red)
kmeans.saveFigures(output_paths.out_residual_sugar_red)
kmeans.createGif(output_paths.out_residual_sugar_red)

kmeans = KMeans(nCluster=5, randomState=721)
kmeans.fit(dataset_sulphates_red)
kmeans.saveFigures(output_paths.out_sulphates_red)
kmeans.createGif(output_paths.out_sulphates_red)

kmeans = KMeans(nCluster=3, randomState=721)
kmeans.fit(dataset_total_sulfur_dioxide_red)
kmeans.saveFigures(output_paths.out_total_sulfur_dioxide_red)
kmeans.createGif(output_paths.out_total_sulfur_dioxide_red)

kmeans = KMeans(nCluster=3, randomState=721)
kmeans.fit(dataset_volatile_acid_red)
kmeans.saveFigures(output_paths.out_volatile_acid_red)
kmeans.createGif(output_paths.out_volatile_acid_red)


# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red.csv')

# Plot
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)

# Decorations
plt.title('Correlogram', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig(output_paths.out_redQualityCorrelations)
plt.show()


# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red.csv')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="quality")
plt.savefig(output_paths.out_redRegQualities)
plt.show()


# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red.csv')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="scatter", hue="quality")
plt.savefig(output_paths.out_redScatterQualities)
plt.show()


# good red pairplots -------------------------------------------------------

colors = ["#FFCCCC", "#FF6666" , "#B30000"]
customPalette = sns.set_palette(sns.color_palette(colors))

# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red-good.csv')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="scatter", hue="quality", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5), palette=customPalette)
plt.savefig(output_paths.out_good_red_wine_correlation_perTrait_scatter)
plt.show()

# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red-good.csv')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="quality", palette=customPalette)
plt.savefig(output_paths.out_good_red_wine_correlation_perTrait_reg)
plt.show()


# simplified red pairplots ------------------------------------------------


# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red-simplified.csv')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="scatter", hue="quality", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
plt.savefig(output_paths.out_good_vs_bad_red_wine_correlation_perTrait_scatter)
plt.show()

# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red-simplified.csv')

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="quality")
plt.savefig(output_paths.out_good_vs_bad_red_wine_correlation_perTrait_reg)
plt.show()


# good red pairplots unified ---------------------------------------------

# Load Dataset
df = pd.read_csv(r'datasets\red\winequality-red-good-simplified.csv')

sns.set(style="ticks", color_codes=True)

# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="quality", plot_kws={'line_kws':{'color':'red'}})
plt.savefig(output_paths.out_good_red_wine_correlation_perTrait_simplified)
plt.show()



# RED REG PER TRAIT ------------------------------------------------------------------------------------------------
color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='alcohol', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_alcohol)
plt.show()


color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='chlorides', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_chlorides)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='citric acid', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_citric_acid)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='density', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_density)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='fixed acidity', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_fixed_acid)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='free sulfur dioxide', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_free_sulfur_dioxide)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='pH', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_ph)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='residual sugar', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_residual_sugar)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='sulphates', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_sulphates)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='total sulfur dioxide', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_total_sulfur_dioxide)
plt.show()

color = ["#ff0000"]
customPalette = sns.set_palette(sns.color_palette(color))

df = pd.read_csv(r'datasets\red\winequality-red.csv')

sns.lmplot(x ='volatile acidity', y ='quality', data = df, palette=customPalette)

plt.savefig(output_paths.out_red_wine_reg_volatile_acid)
plt.show()

