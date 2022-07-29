# Databricks notebook source
from pyspark.sql import SparkSession

# COMMAND ----------

sc=SparkSession.builder.appName('spark_df').getOrCreate()

# COMMAND ----------

df=spark.read.csv('/FileStore/tables/fifaplayers.csv',sep=',',header=True,inferSchema=True)

# COMMAND ----------

df.show(10)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.show(5)

# COMMAND ----------

#1.Shows the names and height by adding 1 to the height column.
df=df.withColumn('newheight',df['Height']+1)
df.select('FIFA Popular Name','newheight').show(10)

# COMMAND ----------

#2.shows the player name and simultaneously checks whether or not they have height >170
df.select('FIFA Popular Name',df['Height']>170).show(10)

# COMMAND ----------

df.select('FIFA Popular Name').show()

# COMMAND ----------

from pyspark.sql.functions import when,col

# COMMAND ----------

#3.Show FIFA Popular Name and 0 or 1 depending on Height>170
cndn= when(col("Height")>170,"1").when(col("Height")<170,"0")
df1=df.withColumn('more or less',cndn)
df1.select('more or less',"FIFA Popular Name").show(5)

# COMMAND ----------

#4.name of  shortest player
df.select('FIFA Popular Name')
df.orderBy('Height').show(10)

# COMMAND ----------

from pyspark.sql.functions import max

# COMMAND ----------

#5.who is tallest of all. First we find the value of maximum height and then get the details of that player
df.orderBy("Height").select('FIFA Popular Name').tail(10)
df.agg({"Height":'Max'}).show(10)



# COMMAND ----------

#6.average height of the players in Argentina team.
df=df.groupBy("Team").avg()
df.select("avg(Height)").filter(df["Team"] =="Argentina").show()

# COMMAND ----------

sc=SparkSession.builder.appName('SparkSQL').getOrCreate()

# COMMAND ----------

df1=spark.read.csv('/FileStore/tables/movies.csv',sep=',',header=True,inferSchema=True)
df2=spark.read.csv('/FileStore/tables/ratings.csv',sep=',',header=True,inferSchema=True)

# COMMAND ----------

df1.createOrReplaceTempView('movies')
df2.createOrReplaceTempView('ratings')

# COMMAND ----------

df1.show(10)

# COMMAND ----------

from pyspark.sql.functions import year

# COMMAND ----------

sc.sql("select * from movies limit 10").show(10)

# COMMAND ----------

sc1.sql(""select SubString(title,-5,4) as year from movies limit 10"").show(10)

# COMMAND ----------

sc.sql("""select substring(title,-5,4) as year from movies limit 10""").show()

# COMMAND ----------

df2.show(10)

# COMMAND ----------

#5.What is the total rating for each movie?
epresiion=df1['movieId']==df2['MovieId']
join_type='outer'

# COMMAND ----------

#movierat=df2.join(df1,on='movieId',how='inner')
#movierat.show()
movierat.createOrReplaceTempView('data')

# COMMAND ----------

sc.sql("select * from data where genres='Comedy|Drama|Horror|Thriller'").show()


# COMMAND ----------

#5.What is the total rating for each movie?
sc.sql('select genres,sum(rating) as countrat from data group by genres').show()

# COMMAND ----------

#6.What is the average rating for each movie?
sc.sql('select genres,avg(rating) as avgrat from data group by genres').show()

# COMMAND ----------

#3.How many number of movies are there for each rating?
sc.sql('select rating,count(title) as count_title from data group by rating').show()

# COMMAND ----------

#4.How many users have rated each movie?
sc.sql('select title,count(userID)as count_user from data group by title').show(10)

# COMMAND ----------

df1=sc.sql('select *,CAST(substring(right(title,5),1,4)as integer)as year from movies where title like "%(%)"')

# COMMAND ----------

df1.createOrReplaceTempView('movies')

# COMMAND ----------

df.count()

# COMMAND ----------

#2.How many movies are released each year?
sc.sql('select year,count(title)as count_title from movies group by year').show(10)

# COMMAND ----------

#1.Find the list of  oldest released movies.
sc.sql('select * from movies order by year').show(10)

# COMMAND ----------

sc.sql("select year from movies where title='Trip to the Moon, A (Voyage dans la lune, Le) (1902)'").show()

# COMMAND ----------


