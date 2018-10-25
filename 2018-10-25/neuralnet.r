
library(neuralnet)
set.seed(42)
data(mtcars)

df <- mtcars[c('mpg', 'hp', 'drat', 'vs')]
names(df) <- c('y', 'x1', 'x2', 'x3')

nn <- neuralnet(y ~ x1 + x2 + x3, data=df, hidden=3, linear.output=TRUE)
plot(nn)
dev.copy(png, 'img.png')
dev.off()
