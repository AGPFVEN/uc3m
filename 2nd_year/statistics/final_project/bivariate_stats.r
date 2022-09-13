library(readxl)

#Import data
datos_statistics <- read_excel("Datos estadistica.xlsx")

#Choose best second variable
cat("Correlation between percentWeeksOnChart and Danceability\n")
cat(cor(datos_statistics$percentWeeksOnChart, datos_statistics$Danceability))

cat("\n\nCorrelation between percentWeeksOnChart and Duration\n")
cat(cor(datos_statistics$percentWeeksOnChart, datos_statistics$Duration))

cat("\n\nCorrelation between percentWeeksOnChart and Loudness\n")
cat(cor(datos_statistics$percentWeeksOnChart, datos_statistics$Loudness))
cat("\n")

#Histogram/Box-Plot of main variable
hist(datos_statistics$percentWeeksOnChart)
boxplot(datos_statistics$percentWeeksOnChart, horizontal = TRUE)

transformed_ <- (datos_statistics$percentWeeksOnChart)^(.15)

#Scatterplot without linear model of percentWeeksOnChart and Loudness
plot(
    datos_statistics$Loudness,
    transformed_,
    xlab = "Loudness",
    ylab = "Percentage weeks"
)