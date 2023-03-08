#Library to use xlsx documents
library(readxl)

#Import Document to variable
alumnos_industriales <- read_excel("AlumnosIndustriales.xlsx")

#View table (at least in vscode)
print(alumnos_industriales)

#Frequency table of one categorical varible (residencia) from the file
categorical_abs_table <- table(alumnos_industriales$residencia)
lbls <- c("South of Madrid",
    "Center of Madrid",
    "Madrid-otros",
    "Fuera de Madrid"
)
row.names(categorical_abs_table) <- lbls
print(categorical_abs_table)

#Relative frequency table
rel_table <- prop.table(categorical_abs_table)
print(rel_table)

##Bar chart and pie chart
#barplot(categorical_abs_table)
#pie(categorical_abs_table)

#Frequency table of Discrete Variable
discrete_abs_table <- table(alumnos_industriales$hermanos)
print(discete_abs_table)

#Relative table
discrete_rel_table <- prop.table(discrete_abs_table)
print(discrete_rel_table)

#Charts
#barplot(discrete_abs_table)
#pie(discrete_abs_table)

#Quantitave variables