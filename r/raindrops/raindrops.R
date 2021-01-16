raindrops <- function(number) {
  f <- c(3, 5, 7)
  words <- c('Pling', 'Plang', 'Plong')

  result <- paste0(words[which(number %% f == 0)], collapse = "")

  if (result == "") {
    result = toString(number)
  }

  return(result)
}
